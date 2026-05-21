"""Sample jobs per ATS, run regex classifier, emit review packet."""

from __future__ import annotations

import json
import random
import sys
from unittest.mock import patch

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from adapters import ADAPTER_REGISTRY
from adapters import google_careers, microsoft, workday
from classifier import classify_job_fields
from description_signals import extract_description_signals
from filters import classify_title_confidence, is_obvious_reject
from scraper import load_registry

random.seed(42)

SAMPLES_PER_SOURCE = 12
OUTPUT = "_regex_eval_sample.json"

SOURCES = [
    ("Google", "google_careers", 2),
    ("Microsoft", "microsoft", 1),
    ("Nvidia", "workday", 1),
    ("Uber", "uber", None),
    ("Stripe", "greenhouse", None),
    ("Anthropic", "ashby", None),
]


def _bucket(title: str) -> str:
    tl = (title or "").lower()
    if any(k in tl for k in ("intern", "new grad", "newgrad", "early career", "campus", "2025", "2026")):
        return "ec_title"
    if any(k in tl for k in ("senior", "staff", "principal", "lead", "manager", "director", " ii", " iii", " iv")):
        return "senior_title"
    if "software engineer" in tl or "software engineering" in tl:
        return "bare_swe"
    if any(k in tl for k in ("engineer", "developer", "scientist", "researcher", "machine learning")):
        return "other_technical"
    return "other"


def _fetch(name: str, ats: str, max_pages: int | None) -> list:
    company = next(c for c in load_registry() if c["name"] == name)
    patches = []
    if ats == "google_careers" and max_pages:
        patches += [
            patch.object(google_careers, "MAX_PAGES", max_pages),
            patch.object(google_careers, "DETAIL_WORKERS", 6),
        ]
    if ats == "microsoft" and max_pages:
        patches += [
            patch.object(microsoft, "MAX_PAGES", max_pages),
            patch.object(microsoft, "DETAIL_WORKERS", 6),
        ]
    if ats == "workday" and max_pages:
        patches += [
            patch.object(workday, "MAX_PAGES", max_pages),
            patch.object(workday, "DETAIL_WORKERS", 6),
        ]
    for p in patches:
        p.start()
    try:
        return ADAPTER_REGISTRY[ats](company)
    finally:
        for p in reversed(patches):
            p.stop()


def _stratified_sample(jobs: list, n: int) -> list:
    by_bucket: dict[str, list] = {}
    for j in jobs:
        if not j.title:
            continue
        by_bucket.setdefault(_bucket(j.title), []).append(j)
    order = ("ec_title", "bare_swe", "senior_title", "other_technical", "other")
    picked: list = []
    per = max(2, n // len(order))
    for b in order:
        pool = by_bucket.get(b, [])
        random.shuffle(pool)
        picked.extend(pool[:per])
    if len(picked) < n:
        rest = [j for j in jobs if j not in picked and j.title]
        random.shuffle(rest)
        picked.extend(rest[: n - len(picked)])
    return picked[:n]


def _job_record(job) -> dict:
    conf = classify_title_confidence(job.title, job.description)
    sig = extract_description_signals(job.description)
    regex = classify_job_fields(
        company=job.company,
        title=job.title,
        location=job.location,
        description=job.description,
        us_only=False,
    )
    desc = job.description or ""
    req = sig.requirements_text or ""
    return {
        "company": job.company,
        "ats": job.ats,
        "title": job.title,
        "location": job.location,
        "bucket": _bucket(job.title),
        "desc_len": len(desc),
        "req_len": len(req),
        "prefilter_reject": is_obvious_reject(job.title),
        "conf_level": conf.level,
        "conf_reason": conf.reason,
        "regex_include": regex.include,
        "regex_reason": regex.reason,
        "regex_source": regex.source,
        "has_senior_exp": sig.has_senior_exp,
        "has_ec": sig.has_ec,
        "has_strong_ec": sig.has_strong_ec,
        "description": desc,
        "description_head": desc[:1200],
        "requirements_head": req[:800],
    }


def main() -> None:
    all_rows: list[dict] = []
    for name, ats, max_pages in SOURCES:
        print(f"Fetching {name}...", flush=True)
        try:
            jobs = _fetch(name, ats, max_pages)
        except Exception as exc:
            print(f"  FAILED: {exc}")
            continue
        sample = _stratified_sample(jobs, SAMPLES_PER_SOURCE)
        print(f"  {len(sample)} sampled from {len(jobs)}")
        for job in sample:
            all_rows.append(_job_record(job))

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(all_rows, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(all_rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
