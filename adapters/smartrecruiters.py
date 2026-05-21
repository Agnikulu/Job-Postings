"""SmartRecruiters public posting API adapter.

Endpoint: GET https://api.smartrecruiters.com/v1/companies/{slug}/postings
Used by Atlassian and other companies on jobs.smartrecruiters.com.
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

BASE_URL = "https://api.smartrecruiters.com/v1/companies/{slug}/postings"
PAGE_SIZE = 100
MAX_PAGES = 50


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(slug: str, offset: int) -> dict[str, Any]:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        params={"offset": offset, "limit": PAGE_SIZE},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _format_location(raw: dict[str, Any]) -> str:
    loc = raw.get("location") or {}
    if loc.get("fullLocation"):
        return str(loc["fullLocation"])
    if loc.get("remote"):
        return "Remote"
    bits = [loc.get("city"), loc.get("region"), loc.get("country")]
    return ", ".join(str(b) for b in bits if b)


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(
            f"SmartRecruiters adapter requires 'slug' for {company.get('name')}"
        )

    all_raw: list[dict[str, Any]] = []
    for page in range(MAX_PAGES):
        offset = page * PAGE_SIZE
        try:
            payload = _get_page(slug, offset)
        except requests.HTTPError as e:
            raise AdapterError(
                f"SmartRecruiters HTTP {e.response.status_code} for slug='{slug}'"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"SmartRecruiters network error for slug='{slug}': {e}") from e
        except ValueError as e:
            raise AdapterError(
                f"SmartRecruiters returned invalid JSON for slug='{slug}'"
            ) from e

        page_jobs = payload.get("content") or []
        all_raw.extend(page_jobs)
        total = payload.get("totalFound") or 0
        if not page_jobs or offset + PAGE_SIZE >= total:
            break

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            ref = raw.get("ref") or ""
            job_id = str(raw.get("id") or raw.get("uuid") or "")
            if ref.startswith("https://jobs.smartrecruiters.com/"):
                url = ref
            elif job_id:
                url = f"https://jobs.smartrecruiters.com/{slug}/{job_id}"
            else:
                url = ref
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=str(raw.get("name", "")).strip(),
                    location=_format_location(raw),
                    url=url,
                    posted_at=raw.get("releasedDate"),
                    department=raw.get("department", {}).get("label")
                    if isinstance(raw.get("department"), dict)
                    else raw.get("department"),
                    ats="smartrecruiters",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("SmartRecruiters: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
