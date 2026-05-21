"""Resolve ambiguous job locations using ATS-specific detail APIs."""

from __future__ import annotations

import logging
import re
from typing import Any

import requests

from adapters.base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, Job
from filters import is_location_ambiguous

log = logging.getLogger(__name__)

_N_LOCATIONS = re.compile(r"^\d+\s+locations?$", re.IGNORECASE)
_WORKDAY_JOB_URL = re.compile(
    r"^https://([^.]+)\.(wd\d+)\.myworkdayjobs\.com/en-US/([^/]+)(/job/.+)$",
    re.IGNORECASE,
)


def _workday_detail_url(job_url: str) -> str | None:
    m = _WORKDAY_JOB_URL.match(job_url.strip())
    if not m:
        return None
    tenant, pod, site, path = m.groups()
    return (
        f"https://{tenant}.{pod}.myworkdayjobs.com/wday/cxs/"
        f"{tenant}/{site}{path}"
    )


def _fetch_workday_locations(job_url: str) -> str | None:
    detail_url = _workday_detail_url(job_url)
    if not detail_url:
        return None
    try:
        resp = requests.get(
            detail_url,
            headers=DEFAULT_HEADERS,
            timeout=DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        info = resp.json().get("jobPostingInfo") or {}
    except Exception as e:
        log.debug("Workday location detail failed for %s: %s", job_url, e)
        return None

    parts: list[str] = []
    for key in ("location", "locationsText"):
        val = info.get(key)
        if isinstance(val, str) and val.strip():
            parts.append(val.strip())
    additional = info.get("additionalLocations") or []
    if isinstance(additional, list):
        parts.extend(str(x).strip() for x in additional if str(x).strip())
    if not parts:
        return None
    # Dedupe while preserving order.
    seen: set[str] = set()
    merged: list[str] = []
    for part in parts:
        if part not in seen:
            seen.add(part)
            merged.append(part)
    return "; ".join(merged)


def resolve_job_location(job: Job) -> str:
    """Return best available location string for classification."""
    location = (job.location or "").strip()
    if not is_location_ambiguous(location):
        return location

    if job.ats == "workday" and job.url and _N_LOCATIONS.match(location):
        enriched = _fetch_workday_locations(job.url)
        if enriched:
            return enriched

    return location
