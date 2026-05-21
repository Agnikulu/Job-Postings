"""Jibe/iCIMS careers-site adapter (paginated JSON).

Endpoint: GET https://{careers_host}/api/jobs?page=N&limit=100
Used by BlackLine and other Jibe-powered career portals.
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

PAGE_SIZE = 100
MAX_PAGES = 50


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(host: str, page: int) -> dict[str, Any]:
    resp = requests.get(
        f"https://{host}/api/jobs",
        params={"page": page, "limit": PAGE_SIZE},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _format_location(data: dict[str, Any]) -> str:
    if data.get("location_name"):
        return str(data["location_name"])
    bits = [data.get("city"), data.get("state"), data.get("country")]
    return ", ".join(b for b in bits if b)


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    host = company.get("careers_host")
    if not host:
        raise AdapterError(f"Jibe adapter requires 'careers_host' for {name}")

    jobs_path = company.get("jobs_path", "careers-home/jobs")
    all_raw: list[dict[str, Any]] = []
    for page in range(1, MAX_PAGES + 1):
        try:
            payload = _get_page(host, page)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Jibe HTTP {e.response.status_code} for {name} page {page}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Jibe network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Jibe returned invalid JSON for {name}") from e

        page_jobs = payload.get("jobs") or []
        all_raw.extend(page_jobs)
        total = payload.get("totalCount") or payload.get("count") or 0
        if not page_jobs or page * PAGE_SIZE >= total:
            break

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            data = raw.get("data") or raw
            req_id = str(data.get("req_id") or data.get("slug") or "")
            jobs.append(
                Job(
                    id=req_id,
                    company=company["name"],
                    title=str(data.get("title", "")).strip(),
                    location=_format_location(data),
                    url=f"https://{host}/{jobs_path}/{req_id}",
                    posted_at=data.get("posted_date"),
                    department=data.get("department"),
                    ats="jibe",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Jibe: skipping malformed job for %s: %s", name, e)
            continue
    return jobs
