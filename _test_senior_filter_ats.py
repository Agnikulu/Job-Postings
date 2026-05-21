"""Test description fetch + senior-role filtering on big-tech ATS adapters."""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from unittest.mock import patch

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from adapters import ADAPTER_REGISTRY
from adapters import google_careers, microsoft, workday
from classifier import classify_job_fields
from description_signals import extract_description_signals
from filters import classify_title_confidence
from scraper import load_registry

SENIOR_TITLE = (
    "senior",
    "sr.",
    "sr ",
    "staff",
    "principal",
    "lead ",
    "lead,",
    "manager",
    "director",
    " ii,",
    " iii",
    " iv",
    "level 5",
    "l5",
    "l6",
)

EC_TITLE = (
    "intern",
    "new grad",
    "newgrad",
    "entry",
    "junior",
    "early career",
    "campus",
    " i,",
    " i ",
    "engineer i",
    "engineer 1",
    "2025",
    "2026",
)


@dataclass(frozen=True)
class Bucket:
    name: str
    ats: str
    max_pages: int | None = None


TARGETS = (
    Bucket("Google", "google_careers", max_pages=3),
    Bucket("Microsoft", "microsoft", max_pages=1),
    Bucket("Nvidia", "workday", max_pages=2),
    Bucket("Uber", "uber", max_pages=None),
)


def _title_bucket(title: str) -> str:
    tl = title.lower()
    if any(k in tl for k in EC_TITLE):
        return "ec_title"
    if any(k in tl for k in SENIOR_TITLE):
        return "senior_title"
    if "software engineer" in tl or "software engineering" in tl:
        return "bare_swe"
    if any(
        k in tl
        for k in (
            "engineer",
            "developer",
            "scientist",
            "researcher",
            "machine learning",
            "ml ",
        )
    ):
        return "other_technical"
    return "other"


def _fetch_company(name: str, ats: str, max_pages: int | None) -> list:
    company = next(c for c in load_registry() if c["name"] == name)
    patches = []
    if ats == "google_careers" and max_pages:
        patches.append(patch.object(google_careers, "MAX_PAGES", max_pages))
        patches.append(patch.object(google_careers, "DETAIL_WORKERS", 6))
    if ats == "microsoft" and max_pages:
        patches.append(patch.object(microsoft, "MAX_PAGES", max_pages))
        patches.append(patch.object(microsoft, "DETAIL_WORKERS", 6))
    if ats == "workday" and max_pages:
        patches.append(patch.object(workday, "MAX_PAGES", max_pages))
        patches.append(patch.object(workday, "DETAIL_WORKERS", 6))

    for p in patches:
        p.start()
    try:
        return ADAPTER_REGISTRY[ats](company)
    finally:
        for p in reversed(patches):
            p.stop()


def _analyze_jobs(name: str, ats: str, jobs: list) -> None:
    stats: Counter[str] = Counter()
    desc_stats: Counter[str] = Counter()
    senior_title_outcomes: Counter[str] = Counter()
    bare_swe_outcomes: Counter[str] = Counter()
    false_positives: list[tuple] = []
    false_negatives: list[tuple] = []
    examples: dict[str, list] = defaultdict(list)

    for job in jobs:
        bucket = _title_bucket(job.title or "")
        stats[bucket] += 1
        has_desc = bool(job.description)
        desc_stats["with_desc" if has_desc else "no_desc"] += 1

        conf = classify_title_confidence(job.title, job.description)
        sig = extract_description_signals(job.description)
        regex = classify_job_fields(
            company=job.company,
            title=job.title,
            location=job.location,
            description=job.description,
                us_only=False,
        )

        if bucket == "senior_title":
            senior_title_outcomes[conf.level] += 1
            if conf.level != "high_exclude" or regex.include:
                false_positives.append(
                    (
                        job.title,
                        conf.level,
                        conf.reason,
                        regex.include,
                        sig.has_senior_exp,
                        len(job.description or ""),
                    )
                )
        elif bucket == "bare_swe":
            bare_swe_outcomes[conf.level] += 1
            if regex.include:
                false_positives.append(
                    (
                        job.title,
                        conf.level,
                        conf.reason,
                        True,
                        sig.has_senior_exp,
                        sig.has_ec,
                        len(job.description or ""),
                    )
                )
            if has_desc and sig.has_senior_exp and conf.level != "high_exclude":
                false_negatives.append(
                    (job.title, conf.level, conf.reason, (sig.requirements_text or "")[:120])
                )

        key = f"{bucket}:{conf.level}:{conf.reason}"
        if len(examples[key]) < 2:
            examples[key].append(
                (
                    job.title,
                    conf.reason,
                    sig.has_senior_exp,
                    sig.has_ec,
                    bool(sig.requirements_text),
                    len(job.description or ""),
                )
            )

    tech_jobs = sum(v for k, v in stats.items() if k in ("bare_swe", "senior_title", "ec_title", "other_technical"))
    print("=" * 72)
    print(f"{name} ({ats}) — {len(jobs)} jobs fetched, {tech_jobs} technical-ish")
    print(f"  descriptions: {desc_stats['with_desc']} with / {desc_stats['no_desc']} without")
    print(f"  title buckets: {dict(stats)}")
    print(f"  senior_title confidence: {dict(senior_title_outcomes)}")
    print(f"  bare_swe confidence: {dict(bare_swe_outcomes)}")

    senior_included = sum(
        1
        for job in jobs
        if _title_bucket(job.title or "") == "senior_title"
        and classify_job_fields(
            company=job.company,
            title=job.title,
            location=job.location,
            description=job.description,
                us_only=False,
        ).include
    )
    bare_included = sum(
        1
        for job in jobs
        if _title_bucket(job.title or "") == "bare_swe"
        and classify_job_fields(
            company=job.company,
            title=job.title,
            location=job.location,
            description=job.description,
                us_only=False,
        ).include
    )
    print(f"  regex includes: senior_title={senior_included}, bare_swe={bare_included}")

    if false_positives:
        print(f"  ⚠ false positives / leaks ({len(false_positives)}):")
        for row in false_positives[:8]:
            print(f"    {row}")
    else:
        print("  ✓ no senior_title or bare_swe regex includes that look wrong")

    if false_negatives:
        print(f"  ⚠ senior in req but not excluded ({len(false_negatives)}):")
        for row in false_negatives[:5]:
            print(f"    {row}")

    print("  sample classifications:")
    for key in sorted(examples.keys()):
        if "senior_title" in key or "bare_swe" in key:
            for ex in examples[key]:
                print(f"    [{key}] {ex}")


def main() -> None:
    for target in TARGETS:
        print(f"\nFetching {target.name}...")
        try:
            jobs = _fetch_company(target.name, target.ats, target.max_pages)
        except Exception as exc:
            print(f"FAILED {target.name}: {exc}")
            continue
        _analyze_jobs(target.name, target.ats, jobs)

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("Expected: senior_title → excluded; bare_swe + senior years in req → excluded;")


if __name__ == "__main__":
    main()
