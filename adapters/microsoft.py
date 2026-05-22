"""Microsoft careers adapter (apply.careers.microsoft.com PCSX API).

Endpoint: GET https://apply.careers.microsoft.com/api/pcsx/search
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_microsoft_description, map_descriptions_parallel
from fetch_limits import max_list_pages
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SEARCH_URL = "https://apply.careers.microsoft.com/api/pcsx/search"
BASE_URL = "https://apply.careers.microsoft.com"
PAGE_SIZE = 50
MAX_PAGES = 200
PAGE_DELAY_SEC = 0.35
DETAIL_WORKERS = 8


def _retryable_request_error(exc: BaseException) -> bool:
    if isinstance(exc, requests.HTTPError):
        return exc.response.status_code in {429, 500, 502, 503}
    return isinstance(exc, requests.RequestException)


@retry(
    reraise=True,
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception(_retryable_request_error),
)
def _get_page(domain: str, start: int) -> dict[str, Any]:
    headers = {
        **DEFAULT_HEADERS,
        "Accept": "application/json, text/plain, */*",
        "Referer": f"{BASE_URL}/careers",
    }
    resp = requests.get(
        SEARCH_URL,
        params={
            "domain": domain,
            "query": "",
            "location": "",
            "start": start,
            "count": PAGE_SIZE,
        },
        headers=headers,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _extract_positions(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], int | None]:
    data = payload.get("data")
    if isinstance(data, list):
        return data, None
    if isinstance(data, dict):
        positions = data.get("positions") or []
        total = data.get("count")
        if isinstance(total, int):
            return positions, total
        return positions, None
    return [], None


def _epoch_to_iso(value: int | None) -> str | None:
    if not value:
        return None
    try:
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
    except (ValueError, OSError):
        return None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    domain = company.get("domain") or company.get("slug") or "microsoft.com"

    all_raw: list[dict[str, Any]] = []
    start = 0
    total: int | None = None
    for page_num in range(max_list_pages(MAX_PAGES)):
        if page_num:
            time.sleep(PAGE_DELAY_SEC)
        try:
            payload = _get_page(domain, start)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Microsoft HTTP {e.response.status_code} for {name} start={start}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Microsoft network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Microsoft returned invalid JSON for {name}") from e

        page_jobs, page_total = _extract_positions(payload)
        if page_total is not None:
            total = page_total
        if not page_jobs:
            break
        all_raw.extend(page_jobs)
        start += len(page_jobs)
        if total is not None and start >= total:
            break

    jobs: list[Job] = []
    job_ids: list[str] = []
    for raw in all_raw:
        if not isinstance(raw, dict):
            continue
        try:
            job_id = str(raw.get("id") or raw.get("displayJobId") or "")
            locs = raw.get("standardizedLocations") or raw.get("locations") or []
            location = " / ".join(str(x) for x in locs if x)
            path = raw.get("positionUrl") or f"/careers/job/{job_id}"
            url = path if str(path).startswith("http") else f"{BASE_URL}{path}"
            job_ids.append(job_id)
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=str(raw.get("name") or "").strip(),
                    location=location,
                    url=url,
                    posted_at=_epoch_to_iso(raw.get("postedTs") or raw.get("creationTs")),
                    department=raw.get("department"),
                    ats="microsoft",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Microsoft: skipping malformed job for %s: %s", name, e)
            continue

    fetch_ids = [j.id for j in jobs if should_fetch_description(j.title)]
    if fetch_ids:
        descriptions = map_descriptions_parallel(
            fetch_ids,
            lambda job_id: fetch_microsoft_description(job_id, base_url=BASE_URL),
            max_workers=DETAIL_WORKERS,
        )
        enriched: list[Job] = []
        for job in jobs:
            desc = descriptions.get(job.id)
            if desc:
                enriched.append(
                    Job(
                        id=job.id,
                        company=job.company,
                        title=job.title,
                        location=job.location,
                        url=job.url,
                        posted_at=job.posted_at,
                        department=job.department,
                        ats=job.ats,
                        category=job.category,
                        description=desc,
                    )
                )
            else:
                enriched.append(job)
        return enriched
    return jobs
