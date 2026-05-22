"""Optional caps for production scrape runs (e.g. GitHub Actions time budget)."""

from __future__ import annotations

import logging
import os

from adapters.base import Job

log = logging.getLogger(__name__)


def max_list_pages(default: int) -> int:
    """Upper bound on paginated list requests; never exceeds adapter hard cap."""
    raw = os.environ.get("ATS_SNIPER_MAX_LIST_PAGES", "").strip()
    if not raw:
        return default
    try:
        n = int(raw)
    except ValueError:
        return default
    return max(1, min(n, default))


def cap_job_list(company: str, jobs: list[Job]) -> list[Job]:
    """Truncate oversized single-response boards (e.g. huge Greenhouse lists)."""
    raw = os.environ.get("ATS_SNIPER_MAX_JOBS_PER_COMPANY", "").strip()
    if not raw:
        return jobs
    try:
        cap = int(raw)
    except ValueError:
        return jobs
    if cap <= 0 or len(jobs) <= cap:
        return jobs
    log.warning(
        "%s: truncating job list %d -> %d (ATS_SNIPER_MAX_JOBS_PER_COMPANY)",
        company,
        len(jobs),
        cap,
    )
    return jobs[:cap]
