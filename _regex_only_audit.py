"""Regex-only classification audit — measure pass rate and false-positive risk."""

from __future__ import annotations

import sys
from collections import Counter

from adapters import ADAPTER_REGISTRY, AdapterError
from classifier import ClassifierMode, classify_job
from filters import is_obvious_reject, is_suspicious_prefilter_reject
from scraper import load_registry

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main() -> None:
    companies = [c for c in load_registry() if c.get("ats") != "tier3_todo"]
    stats = Counter()
    examples_fp: list[str] = []
    examples_borderline: list[str] = []

    for company in companies:
        name = company["name"]
        adapter = ADAPTER_REGISTRY.get(company["ats"])
        if not adapter:
            continue
        try:
            jobs = adapter(company)
        except (AdapterError, Exception):
            stats["fetch_errors"] += 1
            continue

        for job in jobs:
            if not job.url:
                continue
            stats["total"] += 1
            if is_obvious_reject(job.title):
                stats["prefilter_drop"] += 1
                if is_suspicious_prefilter_reject(job.title):
                    stats["prefilter_suspicious"] += 1
                continue

            stats["post_prefilter"] += 1
            r = classify_job(job,  us_only=True)
            stats[f"src_{r.source}"] += 1

            if not r.include:
                stats["excluded"] += 1
                if r.source == "regex":
                    stats["regex_exclude"] += 1
                continue

            stats["included"] += 1
            if r.is_us:
                stats["included_us"] += 1
            else:
                stats["us_dropped"] += 1

            if r.source == "regex-borderline":
                stats["borderline_included"] += 1
                if len(examples_borderline) < 15:
                    examples_borderline.append(
                        f"  [{name}] {job.title} | {job.location[:60]}"
                    )
            elif r.source == "regex":
                stats["high_confidence_included"] += 1

            # Likely false positives: included but title looks senior-ish or very generic
            title = (job.title or "").lower()
            if r.include and r.is_us and len(examples_fp) < 20:
                if r.source == "regex-borderline":
                    examples_fp.append(
                        f"  [borderline] [{name}] {job.title} | {job.location[:50]}"
                    )
                elif any(k in title for k in ("senior", "staff", "principal", "lead")):
                    examples_fp.append(
                        f"  [senior leak?] [{name}] {job.title}"
                    )

    total = stats["total"]
    post = stats["post_prefilter"]

    print("=" * 72)
    print("REGEX-ONLY AUDIT (with descriptions where available)")
    print("=" * 72)
    print(f"Total jobs:              {total}")
    print(f"Pre-filter dropped:      {stats['prefilter_drop']} ({100*stats['prefilter_drop']/total:.1f}%)")
    print(f"  suspicious (FN risk):  {stats['prefilter_suspicious']}")
    print(f"Post-pre-filter queue:   {post}")
    print()
    print(f"REGEX INCLUDED:          {stats['included']} ({100*stats['included']/post:.1f}% of queue)")
    print(f"  US matches:            {stats['included_us']}")
    print(f"  high-confidence:       {stats['high_confidence_included']}")
    print(f"  borderline (permissive): {stats['borderline_included']}")
    print()
    print(f"REGEX EXCLUDED:          {stats['excluded']} ({100*stats['excluded']/post:.1f}% of queue)")
    print(f"  regex high_exclude:    {stats['regex_exclude']}")
    print()
    print(f"Included / all jobs:     {100*stats['included']/total:.1f}%")
    print(f"US included / all jobs:  {100*stats['included_us']/total:.1f}%")
    print()
    print("Sources:", {k: v for k, v in stats.items() if k.startswith("src_")})
    print()
    print("=" * 72)
    print("LIKELY FALSE-POSITIVE PATTERN (borderline bare titles passing)")
    print("=" * 72)
    for line in examples_borderline[:12]:
        print(line)
    print()
    print("=" * 72)
    print("OTHER FP SAMPLES")
    print("=" * 72)
    for line in examples_fp[:10]:
        print(line)


if __name__ == "__main__":
    main()
