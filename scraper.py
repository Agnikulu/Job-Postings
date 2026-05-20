"""Orchestrator entry point.

Pipeline per run:
    1. Load companies.yaml.
    2. For each company:
         a. Dispatch to its ATS adapter (skip tier3_todo).
         b. Filter every returned job through filters.classify().
         c. Skip if already in seen_jobs.json.
         d. Otherwise, queue for notification and mark seen.
       One company breaking never aborts the loop.
    3. Notify Discord (single embed per job, or bulk summary if > 50).
    4. Prune stale state entries (> 90 days).
    5. Persist seen_jobs.json.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

import yaml

import notifier
from adapters import ADAPTER_REGISTRY, AdapterError, Job
from filters import classify
from state import State

REGISTRY_PATH = Path(__file__).parent / "companies.yaml"
STATE_PATH = Path(__file__).parent / "seen_jobs.json"


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


def run() -> int:
    log = logging.getLogger("scraper")
    state = State.load(STATE_PATH)
    companies = load_registry()

    skipped_tier3 = 0
    failed = 0
    succeeded = 0
    total_fetched = 0
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
            continue
        except Exception as e:
            log.exception("%s: unexpected error (%s) — skipping", name, e)
            failed += 1
            continue

        succeeded += 1
        total_fetched += len(jobs)

        company_new = 0
        for job in jobs:
            if not job.url:
                continue
            passes, is_tech = classify(job.title)
            if not passes:
                continue
            if state.is_seen(job.url):
                continue
            new_jobs.append((job, is_tech))
            state.mark_seen(job.url)
            company_new += 1

        if company_new:
            log.info("%s: %d new early-career roles (of %d fetched)",
                     name, company_new, len(jobs))

    log.info(
        "Scan complete: %d companies OK, %d failed, %d tier3-skipped, "
        "%d total postings fetched, %d new matches",
        succeeded, failed, skipped_tier3, total_fetched, len(new_jobs),
    )

    notifier.send_batch(new_jobs)

    pruned = state.prune(max_age_days=90)
    state.save()
    log.info("State: %d entries (%d pruned this run)", len(state), pruned)

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
