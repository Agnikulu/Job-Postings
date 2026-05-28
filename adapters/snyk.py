"""Snyk careers adapter (Workday listings via Snyk's Next.js API).

Endpoint: GET https://snyk.io/api/next/jobs
Returns Workday-backed postings with title, location descriptor, and apply URL.
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

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

JOBS_URL = "https://snyk.io/api/next/jobs"
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _headers() -> dict[str, str]:
    return {
        **DEFAULT_HEADERS,
        "User-Agent": BROWSER_UA,
        "Accept": "application/json",
        "Referer": "https://snyk.io/careers/all-jobs/",
    }


def _location_name(raw: dict[str, Any]) -> str:
    loc = raw.get("locations")
    if isinstance(loc, dict):
        desc = loc.get("@_Descriptor") or loc.get("Descriptor")
        if desc:
            return str(desc).strip()
    return ""


def _department_name(raw: dict[str, Any]) -> str | None:
    group = raw.get("Job_Requisition_group")
    if not isinstance(group, dict):
        return None
    dept = group.get("department")
    if isinstance(dept, dict):
        desc = dept.get("@_Descriptor") or dept.get("Descriptor")
        if desc:
            return str(desc).strip()
    dept_id = group.get("departmentID")
    return str(dept_id).strip() if dept_id else None


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_payload() -> list[dict[str, Any]]:
    resp = requests.get(JOBS_URL, headers=_headers(), timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    body = resp.json()
    if not body.get("success"):
        raise AdapterError("Snyk careers API returned success=false")
    data = body.get("data")
    if not isinstance(data, list):
        raise AdapterError("Snyk careers API returned unexpected data shape")
    return data


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "Snyk")
    try:
        raw_jobs = _get_payload()
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        raise AdapterError(f"Snyk HTTP {code}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Snyk network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Snyk returned invalid JSON") from e

    jobs: list[Job] = []
    for raw in raw_jobs:
        if not isinstance(raw, dict):
            continue
        try:
            job_id = str(raw.get("jobRequisitionId") or raw.get("jobPostingID") or "")
            title = str(raw.get("title") or "").strip()
            url = str(raw.get("url") or "").strip()
            if not job_id or not title or not url:
                continue
            jobs.append(
                Job(
                    id=job_id,
                    company=name,
                    title=title,
                    location=_location_name(raw),
                    url=url,
                    posted_at=None,
                    department=_department_name(raw),
                    ats="snyk",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Snyk: skipping malformed job: %s", e)
            continue
    return jobs
