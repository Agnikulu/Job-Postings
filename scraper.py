"""Orchestrator entry point.

Pipeline per run:
    1. Load companies.yaml.
    2. For each company:
         a. Dispatch to its ATS adapter (skip tier3_todo).
         b. Filter every returned job through filters.classify().
         c. Drop non-US locations (unless ATS_SNIPER_ALL_LOCATIONS=1).
         d. Skip if already in seen_jobs.json.
         e. Otherwise, queue for notification and mark seen.
       One company breaking never aborts the loop.
    3. Notify Discord (single embed per job, or bulk summary if > 50).
    4. Update per-company stats and emit slug-rot warnings.
    5. Prune stale state entries (> 90 days).
    6. Persist seen_jobs.json and company_stats.json.

Environment overrides:
    DISCORD_WEBHOOK           — Webhook URL (dry-run if unset).
    ATS_SNIPER_ALL_LOCATIONS  — "1" to disable US-only location filter.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Any

import yaml

import notifier
from adapters import ADAPTER_REGISTRY, AdapterError, Job
from company_stats import CompanyStats
from filters import classify, is_us_location
from state import State

REGISTRY_PATH = Path(__file__).parent / "companies.yaml"
STATE_PATH = Path(__file__).parent / "seen_jobs.json"
STATS_PATH = Path(__file__).parent / "company_stats.json"


def _setup_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        level=logging.INFO,
        stream=sys.stdout,
    )


def load_registry(path: Path = REGISTRY_PATH) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, list):
        raise ValueError(f"{path} must be a YAML list of company entries")
    return data


def _us_filter_enabled() -> bool:
    return os.environ.get("ATS_SNIPER_ALL_LOCATIONS", "").strip() != "1"


def run() -> int:
    log = logging.getLogger("scraper")
    state = State.load(STATE_PATH)
    stats = CompanyStats.load(STATS_PATH)
    companies = load_registry()
    us_only = _us_filter_enabled()
    log.info("Location filter: %s", "US-only" if us_only else "ALL LOCATIONS")

    skipped_tier3 = 0
    failed = 0
    succeeded = 0
    total_fetched = 0
    total_us_filtered = 0
    new_jobs: list[tuple[Job, bool]] = []

    for company in companies:
        name = company.get("name", "?")
        ats = company.get("ats")

        if ats == "tier3_todo":
            skipped_tier3 += 1
            continue

        adapter = ADAPTER_REGISTRY.get(ats)
        if adapter is None:
            log.warning("%s: unknown ATS %r — skipping", name, ats)
            failed += 1
            continue

        try:
            jobs = adapter(company)
        except AdapterError as e:
            log.warning("%s: %s", name, e)
            failed += 1
            stats.record(name, postings=0, matches=0)
            continue
        except Exception as e:
            log.exception("%s: unexpected error (%s) — skipping", name, e)
            failed += 1
            stats.record(name, postings=0, matches=0)
            continue

        succeeded += 1
        total_fetched += len(jobs)

        company_new = 0
        company_total_matches = 0
        company_us_dropped = 0
        for job in jobs:
            if not job.url:
                continue
            passes, is_tech = classify(job.title)
            if not passes:
                continue
            company_total_matches += 1
            if us_only and not is_us_location(job.location):
                company_us_dropped += 1
                continue
            if state.is_seen(job.url):
                continue
            new_jobs.append((job, is_tech))
            state.mark_seen(job.url)
            company_new += 1

        total_us_filtered += company_us_dropped
        warnings = stats.record(name, postings=len(jobs), matches=company_total_matches)
        for w in warnings:
            log.warning(w)

        if company_new or company_us_dropped:
            log.info(
                "%s: %d new (of %d matches, %d dropped by US filter, %d fetched)",
                name, company_new, company_total_matches,
                company_us_dropped, len(jobs),
            )

    log.info(
        "Scan complete: %d OK, %d failed, %d tier3-skipped, %d postings, "
        "%d new matches (after US filter dropped %d)",
        succeeded, failed, skipped_tier3, total_fetched,
        len(new_jobs), total_us_filtered,
    )

    notifier.send_batch(new_jobs)

    pruned = state.prune(max_age_days=90)
    state.save()
    stats.save()
    log.info(
        "State: %d entries (%d pruned), stats: %d companies tracked",
        len(state), pruned, len(stats),
    )

    return 0


def main() -> int:
    _setup_logging()
    try:
        return run()
    except Exception:
        logging.exception("Fatal error in scraper")
        return 1


if __name__ == "__main__":
    sys.exit(main())
