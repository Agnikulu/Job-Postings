"""Fetch job samples + regex scores for manual (Cursor) evaluation.

Phase 1 — export jobs with descriptions and regex classification:
    python _cursor_manual_eval.py fetch --per-company 50

Phase 2 — after adding manual_include to each row (or separate labels file), score:
    python _cursor_manual_eval.py score

Labels file format (cursor_eval_labels.jsonl): one JSON object per line with at least:
    url, manual_include (bool), manual_reason (str)
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from adapters import ADAPTER_REGISTRY, AdapterError, Job
from classifier import classify_job_fields
from filters import is_obvious_reject, obvious_reject_reason
from scraper import load_registry

ROOT = Path(__file__).parent
JOBS_PATH = ROOT / "cursor_eval_jobs.jsonl"
LABELS_PATH = ROOT / "cursor_eval_labels.jsonl"
REPORT_PATH = ROOT / "cursor_eval_report.json"


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
        us_only=False,
    )
    return result.include, result.reason or "", result.source


def cmd_fetch(*, per_company: int, max_companies: int | None) -> None:
    companies = [c for c in load_registry() if c.get("ats") != "tier3_todo"]
    if max_companies:
        companies = companies[:max_companies]

    log(f"Fetching {len(companies)} companies, up to {per_company} jobs each...")
    t0 = time.time()
    rows: list[dict] = []
    ok = fail = 0

    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(fetch_company, c, limit=per_company): c for c in companies}
        done = 0
        for fut in cf.as_completed(futs):
            name, jobs, err = fut.result()
            done += 1
            if err:
                fail += 1
                log(f"  [{done}/{len(companies)}] FAIL {name}: {err}")
                continue
            ok += 1
            for j in jobs:
                if not j.url:
                    continue
                regex_inc, regex_reason, regex_source = _regex_include(
                    j.company, j.title, j.location, j.description, j.url
                )
                desc = j.description or ""
                rows.append(
                    {
                        "company": j.company,
                        "ats": j.ats,
                        "title": j.title,
                        "location": j.location,
                        "url": j.url,
                        "desc_len": len(desc),
                        "description": desc[:4500],
                        "regex_include": regex_inc,
                        "regex_reason": regex_reason,
                        "regex_source": regex_source,
                    }
                )
            log(f"  [{done}/{len(companies)}] {name}: {len(jobs)} jobs")

    with JOBS_PATH.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    regex_inc = sum(1 for r in rows if r["regex_include"])
    log(
        f"Done in {(time.time()-t0)/60:.1f} min — {len(rows)} jobs "
        f"({regex_inc} regex includes) → {JOBS_PATH.name}"
    )


def _load_labels() -> dict[str, dict]:
    labels: dict[str, dict] = {}
    if not LABELS_PATH.exists():
        return labels
    with LABELS_PATH.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("url"):
                labels[row["url"]] = row
    return labels


def cmd_rescore() -> None:
    """Re-apply regex classification to existing cursor_eval_jobs.jsonl."""
    if not JOBS_PATH.exists():
        log(f"Missing {JOBS_PATH.name} — run fetch first")
        sys.exit(1)

    rows: list[dict] = []
    with JOBS_PATH.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))

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

    with JOBS_PATH.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    log(f"Rescored {len(rows)} jobs — {regex_inc} regex includes")


def cmd_score() -> None:
    if not JOBS_PATH.exists():
        log(f"Missing {JOBS_PATH.name} — run fetch first")
        sys.exit(1)
    labels = _load_labels()
    if not labels:
        log(f"Missing {LABELS_PATH.name} — add manual labels first")
        sys.exit(1)

    rows: list[dict] = []
    with JOBS_PATH.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))

    tp = fp = tn = fn = 0
    disagreements: list[dict] = []
    by_company: dict[str, Counter] = defaultdict(Counter)

    for job in rows:
        url = job["url"]
        label = labels.get(url)
        if not label or "manual_include" not in label:
            continue
        regex_inc = job["regex_include"]
        manual_inc = bool(label["manual_include"])
        if manual_inc and regex_inc:
            bucket = "tp"
            tp += 1
        elif not manual_inc and not regex_inc:
            bucket = "tn"
            tn += 1
        elif not manual_inc and regex_inc:
            bucket = "fp"
            fp += 1
        else:
            bucket = "fn"
            fn += 1
        by_company[job["company"]][bucket] += 1
        if manual_inc != regex_inc:
            disagreements.append(
                {
                    "bucket": bucket,
                    "company": job["company"],
                    "title": job["title"],
                    "url": url,
                    "regex_include": regex_inc,
                    "regex_reason": job["regex_reason"],
                    "manual_include": manual_inc,
                    "manual_reason": label.get("manual_reason", ""),
                }
            )

    total = tp + fp + tn + fn
    accuracy = (tp + tn) / total if total else 0
    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    report = {
        "labeled": total,
        "unlabeled": len(rows) - total,
        "overall": {
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
        },
        "by_company": {
            c: dict(counts) for c, counts in sorted(by_company.items())
        },
        "disagreements": disagreements,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    o = report["overall"]
    log(
        f"Labeled: {total}/{len(rows)} | Acc: {o['accuracy']:.1%} | "
        f"Prec: {o['precision']:.1%} | Recall: {o['recall']:.1%} | "
        f"TP={tp} FP={fp} TN={tn} FN={fn}\nReport: {REPORT_PATH.name}"
    )


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch")
    f.add_argument("--per-company", type=int, default=50)
    f.add_argument("--max-companies", type=int, default=None)
    sub.add_parser("score")
    sub.add_parser("rescore")
    args = p.parse_args()
    random.seed(42)
    if args.cmd == "fetch":
        cmd_fetch(per_company=args.per_company, max_companies=args.max_companies)
    elif args.cmd == "rescore":
        cmd_rescore()
    else:
        cmd_score()
    return 0


if __name__ == "__main__":
    sys.exit(main())
