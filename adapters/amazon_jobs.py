"""Amazon Jobs search adapter (amazon.jobs public JSON API).

Endpoint: GET https://www.amazon.jobs/en/search.json
Supports optional base_query (e.g. "Amazon Web Services" for AWS-only listings).
"""

from __future__ import annotations

import logging
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

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.amazon.jobs/en/search.json"
JOB_BASE = "https://www.amazon.jobs"
PAGE_SIZE = 100
MAX_PAGES = 100


def _headers() -> dict[str, str]:
    return {
        **DEFAULT_HEADERS,
        "Accept": "application/json",
        "Referer": "https://www.amazon.jobs/en/search",
    }


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(offset: int, base_query: str) -> dict[str, Any]:
    params: dict[str, Any] = {"offset": offset, "result_limit": PAGE_SIZE}
    if base_query:
        params["base_query"] = base_query
    resp = requests.get(
        SEARCH_URL, params=params, headers=_headers(), timeout=DEFAULT_TIMEOUT
    )
    resp.raise_for_status()
    return resp.json()


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

    all_raw: list[dict[str, Any]] = []
    offset = 0
    for _ in range(MAX_PAGES):
        try:
            payload = _get_page(offset, base_query)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Amazon Jobs HTTP {e.response.status_code} for {name} offset={offset}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Amazon Jobs network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Amazon Jobs invalid JSON for {name}") from e

        page_jobs = payload.get("jobs") or []
        if not page_jobs:
            break
        all_raw.extend(page_jobs)
        offset += len(page_jobs)
        if len(page_jobs) < PAGE_SIZE:
            break

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
