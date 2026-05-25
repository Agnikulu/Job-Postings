"""Fetch job samples + regex scores for evaluation and discovery.

Regression (frozen labels, full per-ATS sample):
    python _cursor_manual_eval.py fetch --per-ats 200
    python _llm_eval_label.py label
    python _cursor_manual_eval.py rescore
    python _cursor_manual_eval.py score

Full corpus (all postings from every company — use before hand-labeling):
    python _cursor_manual_eval.py fetch-full

Discovery (borderline + regex-positive biased sample, actionable report):
    python _cursor_manual_eval.py fetch-discovery --max-jobs 600
    python _cursor_manual_eval.py discovery-label
    python _cursor_manual_eval.py discovery-score

One-shot local run (deterministic labels, no API):
    python _cursor_manual_eval.py run --per-ats 80
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import random
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from adapters import ADAPTER_REGISTRY, AdapterError, Job
from classifier import classify_job_fields
from fetch_limits import linkedin_company_delay_sec
from filters import (
    diagnose_weak_signal,
    is_obvious_reject,
    is_suspicious_prefilter_reject,
    obvious_reject_reason,
)
from scraper import load_registry

EVAL_DIR = Path(__file__).resolve().parents[1] / "eval"
JOBS_PATH = EVAL_DIR / "cursor_eval_jobs.jsonl"
LABELS_PATH = EVAL_DIR / "cursor_eval_labels.jsonl"
REPORT_PATH = EVAL_DIR / "cursor_eval_report.json"
DISCOVERY_JOBS_PATH = EVAL_DIR / "cursor_eval_discovery_jobs.jsonl"
DISCOVERY_LABELS_PATH = EVAL_DIR / "cursor_eval_discovery_labels.jsonl"
DISCOVERY_REPORT_PATH = EVAL_DIR / "cursor_eval_discovery_report.json"
GOLD_PATH = EVAL_DIR / "eval_gold.jsonl"
RECOMMENDATIONS_PATH = EVAL_DIR / "eval_recommendations.md"

PRIORITY_ATS = frozenset(
    {"recruitee", "wiz", "coinbase", "workday", "smartrecruiters", "gem", "jibe", "uber", "google_careers"}
)
DEFAULT_MAX_FP = 6
DEFAULT_MAX_FN = 0


def _eval_fetch_workers() -> int:
    raw = os.environ.get("ATS_SNIPER_EVAL_FETCH_WORKERS", "4").strip()
    try:
        return max(1, min(int(raw), 8))
    except ValueError:
        return 4


def log(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def fetch_company(company: dict, *, limit: int) -> tuple[str, list[Job], str | None]:
    name = company.get("name", "?")
    adapter = ADAPTER_REGISTRY.get(company["ats"])
    if not adapter:
        return name, [], f"unknown ATS {company['ats']!r}"
    try:
        jobs = adapter(company)
    except (AdapterError, Exception) as e:
        return name, [], str(e)
    if len(jobs) > limit:
        rng = random.Random(hash(name) & 0xFFFFFFFF)
        jobs = rng.sample(jobs, limit)
    return name, jobs, None


def _fetch_companies_mixed(
    companies: list[dict],
    *,
    limit: int,
    max_workers: int | None = None,
) -> list[tuple[str, list[Job], str | None]]:
    """Parallel non-LinkedIn; serial LinkedIn with delay (avoids guest API 429)."""
    workers = max_workers if max_workers is not None else _eval_fetch_workers()
    linkedin = [c for c in companies if c.get("ats") == "linkedin"]
    other = [c for c in companies if c.get("ats") != "linkedin"]
    results: list[tuple[str, list[Job], str | None]] = []

    if other:
        with cf.ThreadPoolExecutor(max_workers=workers) as pool:
            futs = {pool.submit(fetch_company, c, limit=limit): c for c in other}
            for fut in cf.as_completed(futs):
                results.append(fut.result())

    delay = linkedin_company_delay_sec()
    for i, company in enumerate(linkedin):
        if i and delay:
            time.sleep(delay)
        results.append(fetch_company(company, limit=limit))
    return results


def _regex_include(
    company: str,
    title: str,
    location: str | None,
    description: str | None,
    url: str | None,
) -> tuple[bool, str, str]:
    if is_obvious_reject(title):
        return False, obvious_reject_reason(title) or "prefilter", "prefilter"
    result = classify_job_fields(
        company=company,
        title=title,
        location=location,
        url=url,
        description=description,
        # Match production: title/description classify + US location gate.
        us_only=True,
    )
    return result.include, result.reason or "", result.source


def _job_row(j: Job, *, regex_inc: bool, regex_reason: str, regex_source: str) -> dict:
    desc = j.description or ""
    return {
        "company": j.company,
        "ats": j.ats,
        "title": j.title,
        "location": j.location,
        "url": j.url,
        "desc_len": len(desc),
        "description": desc[:8000],
        "regex_include": regex_inc,
        "regex_reason": regex_reason,
        "regex_source": regex_source,
    }


def _discovery_priority(job: dict) -> tuple[int, int]:
    """Lower sorts first (higher priority)."""
    title = job.get("title") or ""
    if job.get("regex_include"):
        return (0, 0)
    if (job.get("ats") or "") in PRIORITY_ATS:
        return (1, 0)
    if diagnose_weak_signal(title) or is_suspicious_prefilter_reject(title):
        return (2, 0)
    if not job.get("description"):
        return (3, 0)
    return (4, random.randint(0, 1_000_000))


def _select_discovery_jobs(pool: list[dict], *, max_jobs: int, tn_rate: float) -> list[dict]:
    by_url: dict[str, dict] = {}
    regex_pos: list[dict] = []
    borderline: list[dict] = []
    priority: list[dict] = []
    tn_pool: list[dict] = []

    for job in pool:
        url = job.get("url")
        if not url or url in by_url:
            continue
        by_url[url] = job
        if job.get("regex_include"):
            regex_pos.append(job)
        elif (job.get("ats") or "") in PRIORITY_ATS:
            priority.append(job)
        elif diagnose_weak_signal(job.get("title") or "") or is_suspicious_prefilter_reject(
            job.get("title")
        ):
            borderline.append(job)
        elif not job.get("regex_include"):
            tn_pool.append(job)

    selected: list[dict] = []
    seen: set[str] = set()

    def _take(rows: list[dict]) -> None:
        for row in sorted(rows, key=_discovery_priority):
            if len(selected) >= max_jobs:
                return
            u = row["url"]
            if u in seen:
                continue
            seen.add(u)
            selected.append(row)

    _take(regex_pos)
    _take(borderline)
    _take(priority)

    rng = random.Random(42)
    tn_sample = rng.sample(tn_pool, min(len(tn_pool), max(0, int(max_jobs * tn_rate))))
    _take(tn_sample)

    if len(selected) < max_jobs:
        rest = [j for u, j in by_url.items() if u not in seen]
        rng.shuffle(rest)
        _take(rest)

    return selected[:max_jobs]


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def _append_jsonl(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def cmd_fetch(
    *,
    per_company: int,
    max_companies: int | None,
    per_ats: int | None = None,
) -> None:
    companies = [c for c in load_registry() if c.get("ats") != "tier3_todo"]
    if max_companies:
        companies = companies[:max_companies]

    if per_ats:
        log(f"Fetching up to {per_ats} jobs per ATS type across {len(companies)} companies...")
    else:
        log(f"Fetching {len(companies)} companies, up to {per_company} jobs each...")
    t0 = time.time()
    rows: list[dict] = []
    incremental = bool(os.environ.get("ATS_SNIPER_EVAL_FETCH_INCREMENTAL", "").strip() in {"1", "true", "yes"})
    if incremental:
        JOBS_PATH.parent.mkdir(parents=True, exist_ok=True)
        JOBS_PATH.write_text("", encoding="utf-8")

    if per_ats:
        by_ats: dict[str, list[dict]] = defaultdict(list)
        company_by_name = {c["name"]: c for c in companies}
        done = 0
        for name, jobs, err in _fetch_companies_mixed(companies, limit=per_ats):
            company = company_by_name.get(name, {})
            ats = company.get("ats", "?")
            done += 1
            if err:
                log(f"  [{done}/{len(companies)}] FAIL {name}: {err}")
                continue
            for j in jobs:
                if not j.url:
                    continue
                if len(by_ats[ats]) >= per_ats:
                    continue
                inc, reason, source = _regex_include(
                    j.company, j.title, j.location, j.description, j.url
                )
                by_ats[ats].append(_job_row(j, regex_inc=inc, regex_reason=reason, regex_source=source))
            log(
                f"  [{done}/{len(companies)}] {name}: {len(jobs)} jobs "
                f"({ats} bucket {len(by_ats[ats])}/{per_ats})"
            )
        for ats in sorted(by_ats):
            rows.extend(by_ats[ats][:per_ats])
            log(f"  ATS {ats}: {min(len(by_ats[ats]), per_ats)} jobs collected")
    else:
        done = 0
        for name, jobs, err in _fetch_companies_mixed(companies, limit=per_company):
            done += 1
            if err:
                log(f"  [{done}/{len(companies)}] FAIL {name}: {err}")
                continue
            batch: list[dict] = []
            for j in jobs:
                if not j.url:
                    continue
                inc, reason, source = _regex_include(
                    j.company, j.title, j.location, j.description, j.url
                )
                row = _job_row(j, regex_inc=inc, regex_reason=reason, regex_source=source)
                rows.append(row)
                batch.append(row)
            if incremental and batch:
                _append_jsonl(JOBS_PATH, batch)
            log(
                f"  [{done}/{len(companies)}] {name}: {len(jobs)} jobs "
                f"(corpus {len(rows)} total)"
            )

    if not incremental or not rows:
        _write_jsonl(JOBS_PATH, rows)
    regex_inc = sum(1 for r in rows if r["regex_include"])
    log(
        f"Done in {(time.time()-t0)/60:.1f} min — {len(rows)} jobs "
        f"({regex_inc} regex includes) → {JOBS_PATH.name}"
    )


def cmd_fetch_full(*, max_companies: int | None = None) -> None:
    """Fetch every posting from every active company (no per-ATS cap).

    Typical size: ~8k–25k jobs depending on board sizes. Writes incrementally
  so progress survives long runs (LinkedIn serial + large Greenhouse boards).
    """
    os.environ["ATS_SNIPER_EVAL_FETCH_INCREMENTAL"] = "1"
    cmd_fetch(per_company=1_000_000, max_companies=max_companies, per_ats=None)


def cmd_fetch_discovery(*, max_jobs: int, pool_per_company: int, max_companies: int | None) -> None:
    """Fetch a discovery-biased eval set (regex positives + borderline + ATS priority)."""
    companies = [c for c in load_registry() if c.get("ats") != "tier3_todo"]
    if max_companies:
        companies = companies[:max_companies]
    log(
        f"Discovery fetch: {len(companies)} companies, pool {pool_per_company}/co, "
        f"target {max_jobs} jobs..."
    )
    t0 = time.time()
    pool: list[dict] = []
    done = 0
    for name, jobs, err in _fetch_companies_mixed(companies, limit=pool_per_company):
        done += 1
        if err:
            log(f"  [{done}/{len(companies)}] FAIL {name}: {err}")
            continue
        for j in jobs:
            if not j.url:
                continue
            inc, reason, source = _regex_include(
                j.company, j.title, j.location, j.description, j.url
            )
            pool.append(_job_row(j, regex_inc=inc, regex_reason=reason, regex_source=source))
        log(f"  [{done}/{len(companies)}] {name}: {len(jobs)} jobs (pool {len(pool)})")

    selected = _select_discovery_jobs(pool, max_jobs=max_jobs, tn_rate=0.12)
    _write_jsonl(DISCOVERY_JOBS_PATH, selected)
    _write_jsonl(JOBS_PATH, selected)
    regex_inc = sum(1 for r in selected if r["regex_include"])
    log(
        f"Discovery done in {(time.time()-t0)/60:.1f} min — pool {len(pool)}, "
        f"selected {len(selected)} ({regex_inc} regex+) → {DISCOVERY_JOBS_PATH.name}"
    )


def cmd_discovery_from_corpus(*, max_jobs: int) -> None:
    if not JOBS_PATH.exists():
        log(f"Missing {JOBS_PATH.name} — run fetch or fetch-discovery first")
        sys.exit(1)
    pool = [
        json.loads(line)
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    selected = _select_discovery_jobs(pool, max_jobs=max_jobs, tn_rate=0.12)
    _write_jsonl(DISCOVERY_JOBS_PATH, selected)
    regex_inc = sum(1 for r in selected if r["regex_include"])
    log(f"Discovery sample: {len(selected)} jobs ({regex_inc} regex+) from pool {len(pool)}")


def _load_labels(path: Path) -> dict[str, dict]:
    labels: dict[str, dict] = {}
    if not path.exists():
        return labels
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                if row.get("url"):
                    labels[row["url"]] = row
    return labels


def cmd_rescore(*, jobs_path: Path = JOBS_PATH) -> None:
    if not jobs_path.exists():
        log(f"Missing {jobs_path.name} — run fetch first")
        sys.exit(1)
    rows = [
        json.loads(line)
        for line in jobs_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    regex_inc = 0
    for job in rows:
        inc, reason, source = _regex_include(
            job["company"],
            job["title"],
            job.get("location"),
            job.get("description"),
            job["url"],
        )
        job["regex_include"] = inc
        job["regex_reason"] = reason
        job["regex_source"] = source
        if inc:
            regex_inc += 1
    _write_jsonl(jobs_path, rows)
    log(f"Rescored {len(rows)} jobs — {regex_inc} regex includes")


def _build_score_report(
    rows: list[dict],
    labels: dict[str, dict],
    *,
    max_fp: int,
    max_fn: int,
) -> dict:
    tp = fp = tn = fn = 0
    disagreements: list[dict] = []
    by_company: dict[str, Counter] = defaultdict(Counter)
    by_ats: dict[str, Counter] = defaultdict(Counter)
    fp_by_regex: Counter[str] = Counter()
    fn_by_manual: Counter[str] = Counter()

    for job in rows:
        url = job["url"]
        label = labels.get(url)
        if not label or "manual_include" not in label:
            continue
        regex_inc = job["regex_include"]
        manual_inc = bool(label["manual_include"])
        ats = job.get("ats", "?")

        if manual_inc and regex_inc:
            bucket = "tp"
            tp += 1
        elif not manual_inc and not regex_inc:
            bucket = "tn"
            tn += 1
        elif not manual_inc and regex_inc:
            bucket = "fp"
            fp += 1
            fp_by_regex[job.get("regex_reason") or "?"] += 1
        else:
            bucket = "fn"
            fn += 1
            fn_by_manual[label.get("manual_reason") or "?"] += 1

        by_company[job["company"]][bucket] += 1
        by_ats[ats][bucket] += 1
        if manual_inc != regex_inc:
            disagreements.append(
                {
                    "bucket": bucket,
                    "company": job["company"],
                    "ats": ats,
                    "title": job["title"],
                    "url": url,
                    "regex_include": regex_inc,
                    "regex_reason": job.get("regex_reason"),
                    "manual_include": manual_inc,
                    "manual_reason": label.get("manual_reason", ""),
                    "has_description": bool(job.get("description")),
                }
            )

    total = tp + fp + tn + fn
    regex_positive = tp + fp
    accuracy = (tp + tn) / total if total else 0
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
    precision_on_regex_positive = tp / regex_positive if regex_positive else 0

    recommendations: list[dict] = []
    for reason, count in fp_by_regex.most_common():
        samples = [d for d in disagreements if d["bucket"] == "fp" and d.get("regex_reason") == reason][:3]
        recommendations.append(
            {
                "type": "fix_false_positive",
                "regex_reason": reason,
                "count": count,
                "action": f"Tighten filters for '{reason}' (e.g. senior level, YOE bar, non-dev titles).",
                "samples": samples,
            }
        )
    for reason, count in fn_by_manual.most_common():
        samples = [d for d in disagreements if d["bucket"] == "fn" and d.get("manual_reason") == reason][:3]
        recommendations.append(
            {
                "type": "fix_false_negative",
                "manual_reason": reason,
                "count": count,
                "action": f"Broaden or add signal for cases labeled '{reason}'.",
                "samples": samples,
            }
        )

    return {
        "labeled": total,
        "unlabeled": len(rows) - total,
        "budgets": {
            "max_fp": max_fp,
            "max_fn": max_fn,
            "fp_ok": fp <= max_fp,
            "fn_ok": fn <= max_fn,
        },
        "overall": {
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
            "regex_positive": regex_positive,
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "precision_on_regex_positive": round(precision_on_regex_positive, 4),
        },
        "fp_by_regex_reason": dict(fp_by_regex),
        "fn_by_manual_reason": dict(fn_by_manual),
        "by_ats": {a: dict(c) for a, c in sorted(by_ats.items())},
        "by_company": {c: dict(counts) for c, counts in sorted(by_company.items())},
        "disagreements": disagreements,
        "recommendations": recommendations,
    }


def _write_recommendations_md(report: dict, path: Path) -> None:
    lines = ["# Eval improvement recommendations\n"]
    o = report["overall"]
    lines.append(
        f"**Metrics:** precision {o['precision']:.1%} | recall {o['recall']:.1%} | "
        f"precision on regex+ {o['precision_on_regex_positive']:.1%} | "
        f"FP={o['fp']} FN={o['fn']}\n"
    )
    b = report.get("budgets", {})
    if b:
        status = "PASS" if b.get("fp_ok") and b.get("fn_ok") else "FAIL"
        lines.append(
            f"**Budget ({status}):** FP ≤ {b.get('max_fp')} (got {o['fp']}), "
            f"FN ≤ {b.get('max_fn')} (got {o['fn']})\n"
        )
    recs = report.get("recommendations") or []
    if not recs:
        lines.append("\nNo disagreements — no regex changes suggested from this sample.\n")
    else:
        lines.append("\n## Suggested fixes (by impact)\n")
        for i, rec in enumerate(recs, 1):
            if rec["type"] == "fix_false_positive":
                lines.append(
                    f"\n### {i}. False positives: `{rec['regex_reason']}` ({rec['count']} jobs)\n"
                )
                lines.append(f"{rec['action']}\n")
            else:
                lines.append(
                    f"\n### {i}. False negatives: `{rec.get('manual_reason')}` ({rec['count']} jobs)\n"
                )
                lines.append(f"{rec['action']}\n")
            for s in rec.get("samples") or []:
                lines.append(f"- **{s['company']}** — {s['title']}\n  - {s['url']}\n")
    path.write_text("".join(lines), encoding="utf-8")


def cmd_score(
    *,
    jobs_path: Path = JOBS_PATH,
    labels_path: Path = LABELS_PATH,
    report_path: Path = REPORT_PATH,
    max_fp: int = DEFAULT_MAX_FP,
    max_fn: int = DEFAULT_MAX_FN,
    strict: bool = False,
) -> int:
    if not jobs_path.exists():
        log(f"Missing {jobs_path.name} — run fetch first")
        return 1
    labels = _load_labels(labels_path)
    if not labels:
        log(f"Missing {labels_path.name} — run label first")
        return 1

    rows = [
        json.loads(line)
        for line in jobs_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    report = _build_score_report(rows, labels, max_fp=max_fp, max_fn=max_fn)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _write_recommendations_md(report, RECOMMENDATIONS_PATH)

    o = report["overall"]
    log(
        f"Labeled: {report['labeled']}/{len(rows)} | "
        f"Prec: {o['precision']:.1%} | Recall: {o['recall']:.1%} | "
        f"Prec(regex+): {o['precision_on_regex_positive']:.1%} | "
        f"TP={o['tp']} FP={o['fp']} FN={o['fn']}\n"
        f"Report: {report_path.name} | Recommendations: {RECOMMENDATIONS_PATH.name}"
    )
    for rec in report.get("recommendations") or []:
        key = rec.get("regex_reason") or rec.get("manual_reason")
        log(f"  → {rec['type']}: {key} ({rec['count']})")

    if strict and not (report["budgets"]["fp_ok"] and report["budgets"]["fn_ok"]):
        return 1
    return 0


def cmd_discovery_label() -> int:
    if not DISCOVERY_JOBS_PATH.exists():
        log(f"Missing {DISCOVERY_JOBS_PATH.name}")
        return 1
    os.environ["ATS_SNIPER_EVAL_DETERMINISTIC"] = "1"
    # Reuse labeler on discovery file by temporarily pointing jobs path
    script = REPO_ROOT / "testing" / "scripts" / "_llm_eval_label.py"
    env = {**os.environ, "ATS_SNIPER_EVAL_JOBS_PATH": str(DISCOVERY_JOBS_PATH)}
    env["ATS_SNIPER_EVAL_LABELS_PATH"] = str(DISCOVERY_LABELS_PATH)
    proc = subprocess.run(
        [sys.executable, str(script), "label"],
        cwd=str(REPO_ROOT),
        env=env,
        check=False,
    )
    return proc.returncode


def cmd_sync_gold() -> None:
    """Append disagreement cases from the latest report into eval_gold.jsonl."""
    if not REPORT_PATH.exists():
        log(f"Missing {REPORT_PATH.name} — run score first")
        sys.exit(1)
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    rows = [
        json.loads(line)
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    by_url = {r["url"]: r for r in rows}
    existing = {
        json.loads(line)["url"]
        for line in GOLD_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    } if GOLD_PATH.exists() else set()

    added = 0
    with GOLD_PATH.open("a", encoding="utf-8") as fh:
        for d in report.get("disagreements") or []:
            url = d["url"]
            if url in existing:
                continue
            job = by_url.get(url, d)
            expected = d["bucket"] == "tp" or d["bucket"] == "fn"
            kind = f"{d['bucket']}_regression"
            row = {
                "url": url,
                "company": job.get("company", d.get("company")),
                "title": job.get("title", d.get("title")),
                "location": job.get("location"),
                "description": (job.get("description") or "")[:2000],
                "expected_include": expected,
                "reason": d.get("manual_reason") or d.get("regex_reason"),
                "kind": kind,
            }
            if d["bucket"] == "fp":
                row["xfail"] = True
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            existing.add(url)
            added += 1
    log(f"Synced {added} new gold cases → {GOLD_PATH.name}")


def cmd_run(*, per_ats: int, max_jobs_discovery: int, skip_fetch: bool) -> int:
    """Full local eval: fetch → label → rescore → score → discovery sample → recommendations."""
    env = os.environ.copy()
    env["ATS_SNIPER_EVAL_DETERMINISTIC"] = "1"
    if not skip_fetch:
        cmd_fetch(per_company=50, max_companies=None, per_ats=per_ats)

    label_script = REPO_ROOT / "testing" / "scripts" / "_llm_eval_label.py"
    subprocess.run([sys.executable, str(label_script), "label"], cwd=str(REPO_ROOT), env=env, check=True)
    cmd_rescore()
    code = cmd_score(strict=False)
    cmd_discovery_from_corpus(max_jobs=max_jobs_discovery)
    subprocess.run(
        [sys.executable, str(label_script), "label"],
        cwd=str(REPO_ROOT),
        env={
            **env,
            "ATS_SNIPER_EVAL_JOBS_PATH": str(DISCOVERY_JOBS_PATH),
            "ATS_SNIPER_EVAL_LABELS_PATH": str(DISCOVERY_LABELS_PATH),
        },
        check=True,
    )
    cmd_rescore(jobs_path=DISCOVERY_JOBS_PATH)
    discovery_code = cmd_score(
        jobs_path=DISCOVERY_JOBS_PATH,
        labels_path=DISCOVERY_LABELS_PATH,
        report_path=DISCOVERY_REPORT_PATH,
        max_fp=10,
        max_fn=2,
        strict=False,
    )
    cmd_sync_gold()
    return code or discovery_code


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch")
    f.add_argument("--per-company", type=int, default=50)
    f.add_argument("--per-ats", type=int, default=None)
    f.add_argument("--max-companies", type=int, default=None)

    ff = sub.add_parser(
        "fetch-full",
        help="All jobs from all companies (~8k–25k); incremental write to cursor_eval_jobs.jsonl",
    )
    ff.add_argument("--max-companies", type=int, default=None)

    fd = sub.add_parser("fetch-discovery")
    fd.add_argument("--max-jobs", type=int, default=600)
    fd.add_argument("--pool-per-company", type=int, default=60)
    fd.add_argument("--max-companies", type=int, default=None)

    ds = sub.add_parser("discovery-sample")
    ds.add_argument("--max-jobs", type=int, default=600)

    sub.add_parser("discovery-label")
    dscore = sub.add_parser("discovery-score")
    dscore.add_argument("--strict", action="store_true")

    sc = sub.add_parser("score")
    sc.add_argument("--strict", action="store_true")
    sc.add_argument("--max-fp", type=int, default=DEFAULT_MAX_FP)
    sc.add_argument("--max-fn", type=int, default=DEFAULT_MAX_FN)

    sub.add_parser("rescore")
    sub.add_parser("sync-gold")

    run = sub.add_parser("run")
    run.add_argument("--per-ats", type=int, default=80)
    run.add_argument("--discovery-jobs", type=int, default=500)
    run.add_argument("--skip-fetch", action="store_true")

    args = p.parse_args()
    random.seed(42)

    if args.cmd == "fetch-full":
        cmd_fetch_full(max_companies=getattr(args, "max_companies", None))
        return 0
    if args.cmd == "fetch":
        cmd_fetch(
            per_company=args.per_company,
            max_companies=args.max_companies,
            per_ats=args.per_ats,
        )
        return 0
    if args.cmd == "fetch-discovery":
        cmd_fetch_discovery(
            max_jobs=args.max_jobs,
            pool_per_company=args.pool_per_company,
            max_companies=args.max_companies,
        )
        return 0
    if args.cmd == "discovery-sample":
        cmd_discovery_from_corpus(max_jobs=args.max_jobs)
        return 0
    if args.cmd == "discovery-label":
        return cmd_discovery_label()
    if args.cmd == "discovery-score":
        return cmd_score(
            jobs_path=DISCOVERY_JOBS_PATH,
            labels_path=DISCOVERY_LABELS_PATH,
            report_path=DISCOVERY_REPORT_PATH,
            strict=args.strict,
        )
    if args.cmd == "rescore":
        cmd_rescore()
        return 0
    if args.cmd == "sync-gold":
        cmd_sync_gold()
        return 0
    if args.cmd == "run":
        return cmd_run(
            per_ats=args.per_ats,
            max_jobs_discovery=args.discovery_jobs,
            skip_fetch=args.skip_fetch,
        )
    return cmd_score(
        strict=args.strict,
        max_fp=args.max_fp,
        max_fn=args.max_fn,
    )


if __name__ == "__main__":
    sys.exit(main())
