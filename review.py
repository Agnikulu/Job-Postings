"""Accuracy review tool — parallel + streaming.

Re-runs adapters across all active companies and prints every match grouped
by company. Use it to spot-check whether the regex filters are catching the
right roles and rejecting the wrong ones.

By default applies the same US-only location filter the scraper uses. Pass
--all-locations to bypass and see everything.

Usage:
    python review.py                              # text, US-only
    python review.py --all-locations              # text, all locations
    python review.py --markdown                   # markdown for piping
    python review.py --csv                        # CSV for spreadsheets
    python review.py --misses                     # also list ANTI rejections
    python review.py --diagnose                   # short-experience signals
    python review.py --only "Anthropic,Stripe"    # narrow to companies
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import sys
import time
from collections import Counter, defaultdict
from typing import Iterable

from adapters import ADAPTER_REGISTRY, AdapterError, Job
from filters import ANTI, TARGET, classify, diagnose_weak_signal, is_us_location
from scraper import load_registry


def ascii_only(s: str | None) -> str:
    return (s or "").encode("ascii", errors="replace").decode("ascii")


def fetch_one(company: dict) -> tuple[str, list[Job], str | None]:
    """Returns (company_name, jobs, error_message_or_None)."""
    name = company.get("name", "?")
    adapter = ADAPTER_REGISTRY.get(company["ats"])
    if not adapter:
        return name, [], f"unknown ATS {company['ats']!r}"
    try:
        return name, adapter(company), None
    except AdapterError as e:
        return name, [], str(e)
    except Exception as e:
        return name, [], f"unexpected: {e!r}"


def gather(only: set[str] | None, us_only: bool) -> tuple[
    list[tuple[Job, bool]],
    list[Job],
    list[tuple[str, int, int, int]],
    list[Job],
]:
    """Returns (matches, anti_misses, per_company, weak_signal_hits).

    per_company entries are (name, postings, matches, us_dropped).
    """
    companies = [
        c for c in load_registry()
        if c.get("ats") != "tier3_todo"
        and (only is None or c.get("name") in only)
    ]
    matches: list[tuple[Job, bool]] = []
    anti_misses: list[Job] = []
    weak_hits: list[Job] = []
    per_company: list[tuple[str, int, int, int]] = []

    started = time.time()
    print(f"# Refetching {len(companies)} active companies in parallel "
          f"(us_only={us_only})...", file=sys.stderr)

    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        futures = [ex.submit(fetch_one, c) for c in companies]
        done = 0
        for fut in cf.as_completed(futures):
            name, jobs, err = fut.result()
            done += 1
            if err:
                print(f"# [{done}/{len(companies)}] WARN {name}: {err}",
                      file=sys.stderr)
                continue
            hits = 0
            us_dropped = 0
            for j in jobs:
                passes, is_tech = classify(j.title)
                if passes:
                    if us_only and not is_us_location(j.location):
                        us_dropped += 1
                        continue
                    matches.append((j, is_tech))
                    hits += 1
                elif TARGET.search(j.title or "") and not ANTI.search(j.title or ""):
                    anti_misses.append(j)
                # Weak-signal collection (independent of classify pass/fail)
                if diagnose_weak_signal(j.title) and not passes:
                    weak_hits.append(j)
            per_company.append((name, len(jobs), hits, us_dropped))
            print(f"# [{done}/{len(companies)}] {name}: "
                  f"{hits} matches / {len(jobs)} postings"
                  + (f" ({us_dropped} dropped by US filter)" if us_dropped else ""),
                  file=sys.stderr)

    elapsed = time.time() - started
    print(f"# Gathered in {elapsed:.1f}s", file=sys.stderr)
    return matches, anti_misses, per_company, weak_hits


def print_text(matches: list[tuple[Job, bool]],
               per_company: list[tuple[str, int, int, int]]) -> None:
    by_company: dict[str, list[tuple[Job, bool]]] = defaultdict(list)
    for j, t in matches:
        by_company[j.company].append((j, t))
    for company in sorted(by_company):
        rows = by_company[company]
        tech = sum(1 for _, t in rows if t)
        print(f"\n## {company}  ({len(rows)} matches, {tech} technical)")
        for j, t in sorted(rows, key=lambda r: r[0].title.lower()):
            badge = "[TECH] " if t else "       "
            print(f"  {badge}{ascii_only(j.title)}")
            print(f"            -> {j.url}")
            if j.location:
                print(f"            location: {ascii_only(j.location)}")
    print(f"\n=== TOTAL: {len(matches)} matches across "
          f"{len(by_company)} companies ===")
    print("\n=== Per-company breakdown (hits / total, [US-dropped]) ===")
    for name, total, hits, dropped in sorted(per_company, key=lambda s: -s[2]):
        if hits or dropped:
            tag = f" [{dropped} US-dropped]" if dropped else ""
            print(f"  {name:30} {hits:4d} / {total:5d}{tag}")


def print_markdown(matches: list[tuple[Job, bool]]) -> None:
    by_company: dict[str, list[tuple[Job, bool]]] = defaultdict(list)
    for j, t in matches:
        by_company[j.company].append((j, t))
    print("# Job Sniper Accuracy Review\n")
    print(f"**{len(matches)} matches across {len(by_company)} companies**\n")
    for company in sorted(by_company):
        rows = by_company[company]
        tech = sum(1 for _, t in rows if t)
        print(f"\n## {company}  _( {len(rows)} matches, {tech} technical )_\n")
        for j, t in sorted(rows, key=lambda r: r[0].title.lower()):
            badge = "**[TECH]** " if t else ""
            loc = f" - *{ascii_only(j.location)}*" if j.location else ""
            print(f"- {badge}[{ascii_only(j.title)}]({j.url}){loc}")


def print_csv(matches: list[tuple[Job, bool]]) -> None:
    w = csv.writer(sys.stdout)
    w.writerow(["company", "category", "title", "location",
                "is_technical", "url"])
    for j, t in matches:
        w.writerow([j.company, j.category, ascii_only(j.title),
                    ascii_only(j.location), int(t), j.url])


def print_anti_misses(near: Iterable[Job]) -> None:
    counted: Counter[str] = Counter()
    samples: dict[str, list[Job]] = defaultdict(list)
    for j in near:
        m = ANTI.search(j.title or "")
        if not m:
            continue
        kw = m.group(0).lower()
        counted[kw] += 1
        if len(samples[kw]) < 5:
            samples[kw].append(j)
    print(f"\n=== TARGET-matching roles dropped by ANTI (top keywords) ===")
    for kw, n in counted.most_common():
        print(f"\n* {kw!r}: {n} drops")
        for j in samples[kw]:
            print(f"    - [{j.company}] {ascii_only(j.title)}")


def print_diagnose(weak: list[Job]) -> None:
    """Show titles that hit a weak early-career signal but weren't matched
    by TARGET. These are diagnostic only — they're roles that MIGHT be
    early-career under a non-standard title (Anthropic's "Member of
    Technical Staff", Stripe's "Engineer I", residency programs).
    """
    by_company: dict[str, list[tuple[Job, str]]] = defaultdict(list)
    for j in weak:
        sig = diagnose_weak_signal(j.title) or ""
        by_company[j.company].append((j, sig))

    print(f"\n=== DIAGNOSE: {len(weak)} titles with weak early-career signals "
          f"(across {len(by_company)} companies) ===")
    print("# These were NOT matched by the main filter. Review and decide "
          "if any deserve to be added to TARGET regex.")
    for company in sorted(by_company):
        rows = by_company[company]
        print(f"\n## {company} ({len(rows)} weak hits)")
        # Roll up by signal
        by_signal: dict[str, list[Job]] = defaultdict(list)
        for j, sig in rows:
            by_signal[sig].append(j)
        for sig in sorted(by_signal):
            jobs = by_signal[sig]
            print(f"  * signal {sig!r}: {len(jobs)} titles")
            for j in jobs[:5]:
                print(f"      - {ascii_only(j.title)}")
            if len(jobs) > 5:
                print(f"      ... and {len(jobs) - 5} more")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--markdown", action="store_true")
    p.add_argument("--csv", action="store_true")
    p.add_argument("--misses", action="store_true",
                   help="Also print roles dropped by ANTI keywords")
    p.add_argument("--diagnose", action="store_true",
                   help="Print weak-signal near-misses (Engineer I, MTS, etc)")
    p.add_argument("--all-locations", action="store_true",
                   help="Bypass the US-only location filter")
    p.add_argument("--only", help="Comma-separated company names to limit to")
    args = p.parse_args()

    only = set(s.strip() for s in args.only.split(",")) if args.only else None
    us_only = not args.all_locations

    matches, anti_misses, per_company, weak = gather(only, us_only=us_only)

    if args.csv:
        print_csv(matches)
    elif args.markdown:
        print_markdown(matches)
    else:
        print_text(matches, per_company)

    if args.misses:
        print_anti_misses(anti_misses)
    if args.diagnose:
        print_diagnose(weak)

    return 0


if __name__ == "__main__":
    sys.exit(main())
