"""Amazon Jobs search adapter (amazon.jobs public JSON API).

Endpoint: GET https://www.amazon.jobs/en/search.json
Supports optional base_query (e.g. "Amazon Web Services" for AWS-only listings).
"""

from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from text_util import normalize_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .http_util import http_session

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.amazon.jobs/en/search.json"
JOB_BASE = "https://www.amazon.jobs"
PAGE_SIZE = 100
MAX_PAGES = 100
# Parallel offset fetches (independent pages; merge sorted by offset).
PAGE_WORKERS = 6


def _headers() -> dict[str, str]:
    return {
        "Accept": "application/json",
        "Referer": "https://www.amazon.jobs/en/search",
    }


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(
    session: requests.Session,
    offset: int,
    base_query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {"offset": offset, "result_limit": PAGE_SIZE}
    if base_query:
        params["base_query"] = base_query
    resp = session.get(SEARCH_URL, params=params, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def _page_offsets(first_payload: dict[str, Any]) -> list[int] | None:
    """Offsets for remaining pages after offset 0, or None if total is unknown."""
    first_jobs = first_payload.get("jobs") or []
    if not first_jobs or len(first_jobs) < PAGE_SIZE:
        return []
    hits = first_payload.get("hits")
    try:
        total = int(hits)
    except (TypeError, ValueError):
        return None
    max_offset = min(total, MAX_PAGES * PAGE_SIZE)
    return list(range(PAGE_SIZE, max_offset, PAGE_SIZE))


def _fetch_remaining_serial(
    session: requests.Session,
    base_query: str,
    offset: int,
) -> list[dict[str, Any]]:
    """Same stop rules as the original serial pagination loop."""
    merged: list[dict[str, Any]] = []
    for _ in range(1, MAX_PAGES):
        payload = _get_page(session, offset, base_query)
        page_jobs = payload.get("jobs") or []
        if not page_jobs:
            break
        merged.extend(page_jobs)
        offset += len(page_jobs)
        if len(page_jobs) < PAGE_SIZE:
            break
    return merged


def _fetch_all_raw(session: requests.Session, base_query: str) -> list[dict[str, Any]]:
    first = _get_page(session, 0, base_query)
    first_jobs = list(first.get("jobs") or [])
    if not first_jobs:
        return []
    if len(first_jobs) < PAGE_SIZE:
        return first_jobs

    extra_offsets = _page_offsets(first)
    if extra_offsets is None:
        return first_jobs + _fetch_remaining_serial(
            session, base_query, len(first_jobs)
        )
    if not extra_offsets:
        return first_jobs

    pages: list[tuple[int, list[dict[str, Any]]]] = [(0, first_jobs)]

    def _fetch_offset(offset: int) -> tuple[int, list[dict[str, Any]]]:
        with http_session({**DEFAULT_HEADERS, **_headers()}) as worker_session:
            payload = _get_page(worker_session, offset, base_query)
        return offset, list(payload.get("jobs") or [])

    with ThreadPoolExecutor(max_workers=PAGE_WORKERS) as pool:
        futures = [pool.submit(_fetch_offset, off) for off in extra_offsets]
        for future in as_completed(futures):
            pages.append(future.result())

    merged = _merge_pages(pages)
    # If API total was stale, continue serially from the next offset.
    if merged and len(merged) % PAGE_SIZE == 0 and len(merged) < MAX_PAGES * PAGE_SIZE:
        tail = _fetch_remaining_serial(session, base_query, len(merged))
        if tail:
            merged.extend(tail)
    return merged


def _merge_pages(pages: list[tuple[int, list[dict[str, Any]]]]) -> list[dict[str, Any]]:
    pages.sort(key=lambda item: item[0])
    merged: list[dict[str, Any]] = []
    for _offset, jobs in pages:
        merged.extend(jobs)
    return merged


def _job_url(raw: dict[str, Any]) -> str:
    path = (raw.get("job_path") or "").strip()
    if path.startswith("http"):
        return path
    if path.startswith("/"):
        return f"{JOB_BASE}{path}"
    job_id = raw.get("id_icims")
    if job_id:
        return f"{JOB_BASE}/en/jobs/{job_id}"
    return JOB_BASE


def _location(raw: dict[str, Any]) -> str:
    parts = [raw.get("city"), raw.get("state"), raw.get("country_code")]
    return ", ".join(str(p).strip() for p in parts if p and str(p).strip())


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    base_query = str(
        company.get("amazon_query") or company.get("base_query") or ""
    ).strip()

    try:
        with http_session({**DEFAULT_HEADERS, **_headers()}) as session:
            all_raw = _fetch_all_raw(session, base_query)
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        raise AdapterError(f"Amazon Jobs HTTP {code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Amazon Jobs network error for {name}: {e}") from e
    except ValueError as e:
        raise AdapterError(f"Amazon Jobs invalid JSON for {name}") from e

    jobs: list[Job] = []
    for raw in all_raw:
        if not isinstance(raw, dict):
            continue
        try:
            job_id = str(raw.get("id_icims") or raw.get("id") or "")
            title = str(raw.get("title") or "").strip()
            if not job_id or not title:
                continue
            dept = raw.get("job_category") or raw.get("team")
            if isinstance(dept, dict):
                dept = dept.get("label") or dept.get("title")
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=title,
                    location=_location(raw),
                    url=_job_url(raw),
                    posted_at=raw.get("posted_date") or raw.get("updated_time"),
                    department=str(dept).strip() if dept else None,
                    ats="amazon_jobs",
                    category=company.get("category", "uncategorized"),
                    description=normalize_description(
                        raw.get("description"), is_html=True
                    ),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Amazon Jobs: skipping malformed row for %s: %s", name, e)
            continue
    return jobs
