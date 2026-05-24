"""Orchestrator entry point.

Pipeline per run:
    1. Load companies.yaml.
    2. For each company:
         a. Dispatch to its ATS adapter (skip tier3_todo).
         b. Pre-filter obvious non-targets, then regex classify.
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
    ATS_SNIPER_RESET_STATE    — "1" to wipe seen_jobs, jobs_archive, and
                                company_stats before this run (fresh README).
"""

from __future__ import annotations

import logging
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

import notifier
import render_readme
from adapters import ADAPTER_REGISTRY, AdapterError, Job
from fetch_limits import cap_job_list, linkedin_company_delay_sec
from company_stats import CompanyStats
from date_parser import parse_posted_date
from classifier import classify_job
from jobs_archive import JobsArchive
from state import State

REGISTRY_PATH = Path(__file__).parent / "companies.yaml"
STATE_PATH = Path(__file__).parent / "seen_jobs.json"
STATS_PATH = Path(__file__).parent / "company_stats.json"
LATEST_JOBS_PATH = Path(__file__).parent / "latest_jobs.md"
ARCHIVE_PATH = Path(__file__).parent / "jobs_archive.json"
README_PATH = Path(__file__).parent / "README.md"


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


def _reset_state_requested() -> bool:
    return os.environ.get("ATS_SNIPER_RESET_STATE", "").strip() == "1"


def _reset_persisted_state(log: logging.Logger) -> None:
    """Clear dedupe, archive, and stats so the next run rebuilds from scratch."""
    log.warning(
        "ATS_SNIPER_RESET_STATE=1 — clearing seen_jobs, jobs_archive, company_stats"
    )
    for path in (STATE_PATH, ARCHIVE_PATH, STATS_PATH):
        path.write_text("{}\n", encoding="utf-8")
    LATEST_JOBS_PATH.write_text(
        "# Latest Job Sniper Run\n\n_State reset; awaiting first scrape._\n",
        encoding="utf-8",
    )
    README_PATH.write_text(
        render_readme.render(JobsArchive.load(ARCHIVE_PATH)),
        encoding="utf-8",
    )


def _fetch_workers() -> int:
    raw = os.environ.get("ATS_SNIPER_FETCH_WORKERS", "4").strip()
    try:
        n = int(raw)
    except ValueError:
        return 1
    return max(1, min(n, 12))


def _fetch_company_jobs(company: dict[str, Any]) -> tuple[str, list[Job] | None, str | None]:
    """Return (name, jobs, error_message)."""
    name = company.get("name", "?")
    ats = company.get("ats")
    if ats == "tier3_todo":
        return name, None, "tier3"
    adapter = ADAPTER_REGISTRY.get(ats)
    if adapter is None:
        return name, None, f"unknown ATS {ats!r}"
    try:
        jobs = cap_job_list(name, adapter(company))
        return name, jobs, None
    except AdapterError as e:
        return name, None, str(e)
    except Exception as e:
        return name, None, f"unexpected: {e}"


def _ascii(s: str | None) -> str:
    return (s or "").encode("ascii", errors="replace").decode("ascii")


def write_latest_jobs_md(
    new_jobs: list[tuple[Job, bool]],
    us_only: bool,
    path: Path = LATEST_JOBS_PATH,
) -> None:
    """Write a clickable markdown report of this run's new matches.

    Overwrites the file each run so it always reflects the most recent
    notification batch. Committed back to the repo by the workflow so it
    can be linked from the Discord bulk-summary message.
    """
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = []
    lines.append("# Latest Job Sniper Run\n")
    lines.append(f"**Run timestamp:** {now}  ")
    lines.append(f"**New matches this run:** {len(new_jobs)}  ")
    lines.append(f"**Location filter:** {'US-only' if us_only else 'ALL LOCATIONS'}\n")

    if not new_jobs:
        lines.append("\n_No new early-career roles since the last run._\n")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    by_company: dict[str, list[tuple[Job, bool]]] = defaultdict(list)
    for j, t in new_jobs:
        by_company[j.company].append((j, t))

    lines.append(f"\nGrouped by company (sorted by match count):\n")

    ordered = sorted(by_company.items(), key=lambda kv: -len(kv[1]))
    for company, rows in ordered:
        tech = sum(1 for _, t in rows if t)
        lines.append(f"\n## {company} - {len(rows)} new ({tech} technical)\n")
        for j, t in sorted(rows, key=lambda r: r[0].title.lower()):
            badge = "**[TECH]** " if t else ""
            loc = f" - *{_ascii(j.location)}*" if j.location else ""
            lines.append(f"- {badge}[{_ascii(j.title)}]({j.url}){loc}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run() -> int:
    log = logging.getLogger("scraper")
    if _reset_state_requested():
        _reset_persisted_state(log)
    state = State.load(STATE_PATH)
    stats = CompanyStats.load(STATS_PATH)
    archive = JobsArchive.load(ARCHIVE_PATH)
    companies = load_registry()
    us_only = _us_filter_enabled()
    log.info("Location filter: %s", "US-only" if us_only else "ALL LOCATIONS")
    log.info("Classifier: regex")

    skipped_tier3 = 0
    failed = 0
    succeeded = 0
    total_fetched = 0
    total_us_filtered = 0
    new_jobs: list[tuple[Job, bool]] = []
    observed_companies: set[str] = set()

    active = [c for c in companies if c.get("ats") != "tier3_todo"]
    skipped_tier3 = len(companies) - len(active)
    linkedin_active = [c for c in active if c.get("ats") == "linkedin"]
    other_active = [c for c in active if c.get("ats") != "linkedin"]
    workers = _fetch_workers()
    log.info(
        "Fetching %d companies (%d parallel workers; %d LinkedIn serial)",
        len(active),
        workers,
        len(linkedin_active),
    )

    def _record_fetch(name: str, jobs: list[Job] | None, err: str | None) -> None:
        nonlocal failed
        if err or jobs is None:
            log.warning("%s: %s", name, err)
            failed += 1
            stats.record(name, postings=0, matches=0)
            return
        log.info("%s: fetched %d postings", name, len(jobs))
        fetched.append((name, jobs))

    fetched: list[tuple[str, list[Job]]] = []
    if workers <= 1:
        for company in other_active:
            name, jobs, err = _fetch_company_jobs(company)
            if err == "tier3":
                continue
            _record_fetch(name, jobs, err)
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = {pool.submit(_fetch_company_jobs, c): c for c in other_active}
            for fut in as_completed(futs):
                name, jobs, err = fut.result()
                _record_fetch(name, jobs, err)

    li_delay = linkedin_company_delay_sec()
    for i, company in enumerate(linkedin_active):
        if i and li_delay:
            time.sleep(li_delay)
        name, jobs, err = _fetch_company_jobs(company)
        _record_fetch(name, jobs, err)

    for name, jobs in sorted(fetched, key=lambda x: x[0].lower()):
        succeeded += 1
        observed_companies.add(name)
        total_fetched += len(jobs)

        company_new = 0
        company_total_matches = 0
        company_us_dropped = 0
        for job in jobs:
            if not job.url:
                continue
            result = classify_job(job, us_only=us_only)
            if not result.include:
                continue
            company_total_matches += 1

            # Enrich Job with normalized fields used by the archive + README.
            enriched = replace(
                job,
                posted_date=parse_posted_date(job.posted_at, job.ats),
                education_levels=result.education_levels,
                is_us=result.is_us,
            )

            if us_only and not enriched.is_us:
                company_us_dropped += 1
                continue

            # Archive update happens for every matched job, regardless of
            # whether we've notified about it yet. This way the README
            # captures all currently-open positions, not just new ones.
            archive.upsert(enriched)

            if state.is_seen(enriched.url):
                continue
            new_jobs.append((enriched, result.is_technical))
            state.mark_seen(enriched.url)
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

    # Mark archive entries as closed if their company was successfully
    # scanned this run but the URL no longer appears in the ATS response.
    closed = archive.close_unseen(observed_companies)
    if closed:
        log.info("Archive: marked %d previously-open URLs as closed", closed)

    log.info(
        "Scan complete: %d OK, %d failed, %d tier3-skipped, %d postings, "
        "%d new matches (after US filter dropped %d)",
        succeeded, failed, skipped_tier3, total_fetched,
        len(new_jobs), total_us_filtered,
    )

    write_latest_jobs_md(new_jobs, us_only=us_only)
    notifier.send_batch(new_jobs)

    pruned = state.prune(max_age_days=90)
    state.save()
    stats.save()
    archive.save()

    # Rebuild the README's open-positions table.
    README_PATH.write_text(render_readme.render(archive), encoding="utf-8")
    log.info(
        "State: %d entries (%d pruned), stats: %d companies, archive: %d entries",
        len(state), pruned, len(stats), len(archive),
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
