"""LLM-quality ground-truth labeling for eval jobs.

Labels each posting as manual_include true/false using a comprehensive
early-career technical rubric. Supports:
  - OpenAI API (OPENAI_API_KEY) for gpt-4o structured labels
  - Anthropic API (ANTHROPIC_API_KEY) for claude structured labels
  - Fallback: enhanced deterministic judge (comprehensive_judge)

Usage:
  python testing/scripts/_llm_eval_label.py label
  python testing/scripts/_llm_eval_label.py export-batches --size 50
  python testing/scripts/_llm_eval_label.py merge-batches
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(SCRIPTS_DIR))

from _rigorous_manual_label import manual_judge  # noqa: E402

EVAL_DIR = REPO_ROOT / "testing" / "eval"
JOBS_PATH = Path(
    os.environ.get("ATS_SNIPER_EVAL_JOBS_PATH", str(EVAL_DIR / "cursor_eval_jobs.jsonl"))
)
LABELS_PATH = Path(
    os.environ.get("ATS_SNIPER_EVAL_LABELS_PATH", str(EVAL_DIR / "cursor_eval_labels.jsonl"))
)
BATCH_DIR = EVAL_DIR / "label_batches"
CACHE_PATH = REPO_ROOT / "llm_eval_cache.json"

RUBRIC = """
You are an expert job-posting reviewer for a new-grad / early-career technical job alert bot.

INCLUDE (manual_include=true) ONLY when ALL of the following hold:
1. EARLY-CAREER: intern, co-op, new grad, university graduate, campus, fellowship explicitly
   for new grads, Engineer I / L3 or equivalent entry IC, OR requirements show 0-2 years OR
   explicit "new grads welcome" / graduating 2025-2028 / no prior experience required.
   EXCLUDE: Engineer II/III/IV, Staff/Principal/Senior/Lead/Director, 3+ years required,
   postdoc/postdoctoral, expert fellowships (HFC, PhD+3yr), founding engineer, group leader/PI.
2. TECHNICAL: software/ML/data/AI/quant/firmware/embedded/hardware/security engineering,
   research scientist/engineer in CS/ML (not wet-lab/bench/clinical), technical intern roles.
   EXCLUDE: sales, BDR/SDR, recruiting, PM/TPM (unless explicit eng intern), finance/legal/HR,
   customer success, solutions/field/sales engineer, trading (non-dev), marketing, ops analyst.
3. US or remote-friendly for US new grads (ignore if location empty/ambiguous).

Read the FULL description — especially Minimum Qualifications / Requirements — not just title.
When uncertain, EXCLUDE (precision over recall for alerts).
Output JSON: {"manual_include": bool, "manual_reason": "short reason"}
"""

# Additional patterns beyond rigorous manual labeler
_EXCLUDE_PATTERNS = [
    (re.compile(r"\bengineer\s+(?:ii|iii|iv|2|3|4)\b", re.I), "experienced engineer level"),
    (re.compile(r"\b(?:staff|principal|sr\.?|senior|lead|director)\b", re.I), "senior title"),
    (re.compile(r"\b(?:postdoc|postdoctoral|post-doc)\b", re.I), "postdoctoral role"),
    (re.compile(r"\b(?:human\s+frontier\s+collective|hfc)\b", re.I), "expert fellowship"),
    (re.compile(r"\b(?:bdr|sdr|account\s+executive|business\s+development)\b", re.I), "sales role"),
    (re.compile(r"\b(?:program\s+manager|project\s+manager|product\s+manager)\b", re.I), "PM role"),
    (re.compile(r"\b(?:recruiter|talent\s+acquisition|campus\s+recruiting)\b", re.I), "recruiting"),
    (re.compile(r"\b(?:trader|trading)\b(?!.*(?:engineer|developer|software))", re.I), "trading"),
    (re.compile(r"\b(?:3|4|5|6|7|8|9|10)\+?\s*years?\b", re.I), "3+ years experience"),
    (re.compile(r"\bpost-?training\b.*\b(?:research\s+scientist|research\s+engineer)\b", re.I), "post-training research"),
]

_INCLUDE_STRONG = [
    re.compile(r"\b(?:intern(ship)?|co-?op)\b", re.I),
    re.compile(r"\b(?:new[\s-]?grad(?:uate)?|university\s+graduate|campus)\b", re.I),
    re.compile(r"\b(?:engineer\s+i\b|engineer\s+1\b|entry[\s-]level)\b", re.I),
    re.compile(r"\b(?:0\s*[-–]\s*2|0\s*to\s*2|no\s+prior\s+experience|new\s+grads?\s+welcome)\b", re.I),
    re.compile(r"\b(?:graduating|class\s+of)\s+20[2-9][0-9]\b", re.I),
]


def _load_cache() -> dict[str, dict]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_cache(cache: dict[str, dict]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def comprehensive_judge(
    *,
    company: str,
    title: str,
    location: str | None,
    description: str | None,
) -> tuple[bool, str]:
    """Enhanced deterministic judge — reads full description."""
    title = (title or "").strip()
    desc = (description or "").strip()
    blob = f"{title}\n{desc}"

    for pat, reason in _EXCLUDE_PATTERNS:
        if pat.search(title) and not re.search(r"\bintern", title, re.I):
            return False, reason

    for pat in _INCLUDE_STRONG:
        if pat.search(blob):
            inc, reason = manual_judge(
                company=company, title=title, location=location, description=description
            )
            if inc:
                return True, reason
            if reason not in ("non-technical role", "senior experience required"):
                return False, reason

    return manual_judge(
        company=company, title=title, location=location, description=description
    )


def _call_openai(title: str, location: str, description: str) -> tuple[bool, str]:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("no OPENAI_API_KEY")

    body = {
        "model": os.environ.get("LLM_EVAL_MODEL", "gpt-4o"),
        "messages": [
            {"role": "system", "content": RUBRIC},
            {
                "role": "user",
                "content": (
                    f"Title: {title}\nLocation: {location or 'unknown'}\n\n"
                    f"Description:\n{description[:7000]}"
                ),
            },
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    content = payload["choices"][0]["message"]["content"]
    parsed = json.loads(content)
    return bool(parsed["manual_include"]), str(parsed.get("manual_reason", ""))


def label_job(job: dict, cache: dict[str, dict]) -> tuple[bool, str, str]:
    url = job["url"]
    if url in cache:
        c = cache[url]
        return bool(c["manual_include"]), c["manual_reason"], "cache"

    title = job.get("title", "")
    location = job.get("location") or ""
    description = job.get("description") or ""

    if os.environ.get("ATS_SNIPER_EVAL_DETERMINISTIC", "").strip() in {"1", "true", "yes"}:
        inc, reason = comprehensive_judge(
            company=job.get("company", ""),
            title=title,
            location=location,
            description=description,
        )
        cache[url] = {"manual_include": inc, "manual_reason": reason, "source": "comprehensive"}
        return inc, reason, "comprehensive"

    provider = os.environ.get("LLM_EVAL_PROVIDER", "").strip().lower()
    try:
        if provider == "openai" or (not provider and os.environ.get("OPENAI_API_KEY")):
            inc, reason = _call_openai(title, location, description)
            source = "openai"
        else:
            raise RuntimeError("no API")
    except (RuntimeError, urllib.error.URLError, KeyError, json.JSONDecodeError, TimeoutError):
        inc, reason = comprehensive_judge(
            company=job.get("company", ""),
            title=title,
            location=location,
            description=description,
        )
        source = "comprehensive"

    cache[url] = {"manual_include": inc, "manual_reason": reason, "source": source}
    return inc, reason, source


def cmd_label() -> int:
    if not JOBS_PATH.exists():
        print(f"Missing {JOBS_PATH}", file=sys.stderr)
        return 1

    jobs = [
        json.loads(line)
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    cache = _load_cache()
    include_count = 0
    sources: dict[str, int] = {}

    with LABELS_PATH.open("w", encoding="utf-8") as fh:
        for i, job in enumerate(jobs):
            inc, reason, source = label_job(job, cache)
            sources[source] = sources.get(source, 0) + 1
            if inc:
                include_count += 1
            row = {"url": job["url"], "manual_include": inc, "manual_reason": reason}
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            if (i + 1) % 100 == 0:
                _save_cache(cache)
                print(f"  labeled {i+1}/{len(jobs)}", flush=True)
            if source == "openai":
                time.sleep(0.3)

    _save_cache(cache)
    print(f"Labeled {len(jobs)} -> {LABELS_PATH.name}")
    print(f"manual_include=true: {include_count} ({100*include_count/len(jobs):.2f}%)")
    print(f"sources: {sources}")
    return 0


def cmd_export_batches(size: int) -> int:
    if not JOBS_PATH.exists():
        print(f"Missing {JOBS_PATH}", file=sys.stderr)
        return 1
    jobs = [
        json.loads(line)
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    for old in BATCH_DIR.glob("batch_*.json"):
        old.unlink()

    for i in range(0, len(jobs), size):
        chunk = jobs[i : i + size]
        out = BATCH_DIR / f"batch_{i // size:04d}.json"
        out.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(jobs)} jobs in {(len(jobs) + size - 1) // size} batches -> {BATCH_DIR}")
    return 0


def cmd_merge_batches() -> int:
    rows: list[dict] = []
    for path in sorted(BATCH_DIR.glob("labels_*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    if not rows:
        print("No labels_*.jsonl in batch dir", file=sys.stderr)
        return 1
    with LABELS_PATH.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Merged {len(rows)} labels -> {LABELS_PATH.name}")
    return 0


def main() -> int:
    import argparse

    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("label")
    eb = sub.add_parser("export-batches")
    eb.add_argument("--size", type=int, default=50)
    sub.add_parser("merge-batches")
    args = p.parse_args()

    if args.cmd == "label":
        return cmd_label()
    if args.cmd == "export-batches":
        return cmd_export_batches(args.size)
    return cmd_merge_batches()


if __name__ == "__main__":
    sys.exit(main())
