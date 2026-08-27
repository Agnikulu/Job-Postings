"""Uber careers adapter (Oracle Recruiting Cloud / Fusion HCM).

Uber's careers backend migrated off www.uber.com's old custom
loadSearchJobsResults API onto Oracle Recruiting Cloud. The list endpoint
below is a stateless GET (no CSRF/session dance needed) but doesn't include
description text - that requires a separate per-job detail call, done via
adapters.description_fetch.fetch_uber_description.
"""

from __future__ import annotations

import logging
from dataclasses import replace
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_uber_description, map_descriptions_parallel
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

LIST_URL = (
    "https://iaziqy.fa.ocs.oraclecloud.com/hcmRestApi/resources/latest/"
    "recruitingCEJobRequisitions"
)
JOB_URL = "https://jobs.uber.com/en/jobs/{job_id}"
PAGE_SIZE = 100
MAX_PAGES = 20
DETAIL_WORKERS = 6


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(offset: int) -> dict[str, Any]:
    # Oracle's "finder" mini-language needs literal ; and , separators - if
    # requests' params= percent-encodes them (%3B/%2C) the API silently
    # returns an empty requisitionList instead of erroring, so the query
    # string is built manually here rather than passed via params=.
    finder = (
        f"findReqs;siteNumber=CX_1,limit={PAGE_SIZE},offset={offset},"
        "sortBy=POSTING_DATES_DESC"
    )
    url = (
        f"{LIST_URL}?onlyData=true"
        "&expand=requisitionList.secondaryLocations"
        f"&finder={finder}"
    )
    resp = requests.get(
        url,
        headers={**DEFAULT_HEADERS, "Accept": "application/json"},
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _fetch_all_requisitions() -> list[dict[str, Any]]:
    reqs: list[dict[str, Any]] = []
    offset = 0
    total = None
    for _ in range(MAX_PAGES):
        payload = _get_page(offset)
        items = payload.get("items") or []
        if not items:
            break
        search = items[0]
        page_reqs = search.get("requisitionList") or []
        if not page_reqs:
            break
        reqs.extend(page_reqs)
        total = search.get("TotalJobsCount")
        offset += len(page_reqs)
        if total is not None and offset >= total:
            break
    return reqs


def _format_location(raw: dict[str, Any]) -> str:
    primary = raw.get("PrimaryLocation") or ""
    secondary = raw.get("secondaryLocations") or []
    labels = [primary] if primary else []
    for loc in secondary:
        if isinstance(loc, dict):
            name = loc.get("Name") or loc.get("PrimaryLocation")
            if name:
                labels.append(name)
    return " / ".join(dict.fromkeys(l for l in labels if l))


def fetch(company: dict[str, Any]) -> list[Job]:
    try:
        raw_jobs = _fetch_all_requisitions()
    except requests.HTTPError as e:
        raise AdapterError(f"Uber HTTP {e.response.status_code}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Uber network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Uber returned invalid JSON") from e

    jobs: list[Job] = []
    for raw in raw_jobs:
        try:
            job_id = str(raw["Id"])
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=str(raw.get("Title", "")).strip(),
                    location=_format_location(raw),
                    url=JOB_URL.format(job_id=job_id),
                    posted_at=raw.get("PostedDate"),
                    department=raw.get("Organization") or raw.get("JobFamily"),
                    description=None,
                    ats="uber",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Uber: skipping malformed job: %s", e)
            continue

    fetch_ids = [j.id for j in jobs if j.id and should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_ids:
        descs = map_descriptions_parallel(
            fetch_ids,
            fetch_uber_description,
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.id) or j.description) for j in jobs]
    return jobs
