"""Greenhouse Job Board API adapter.

Endpoint: GET https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true
Docs:     https://developers.greenhouse.io/job-board.html
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

BASE_URL = "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(slug: str) -> dict[str, Any]:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        params={"content": "true"},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


# Location names that only describe how the job is worked, not where.
_WORK_MODE_LOCATIONS = frozenset({
    "hybrid", "in-office", "in office", "onsite", "on-site", "distributed",
    "hybrid; in-office", "distributed; hybrid", "flexible",
})


def _location(raw: dict[str, Any]) -> str:
    """Board location, or the places from a location custom field when the
    board only names a work mode (Cloudflare posts "Hybrid" and lists the
    cities under a "Job Posting Location" field)."""
    name = ((raw.get("location") or {}).get("name") or "").strip()
    if name and name.lower() not in _WORK_MODE_LOCATIONS:
        return name
    for field in raw.get("metadata") or []:
        if not isinstance(field, dict) or "location" not in str(field.get("name") or "").lower():
            continue
        value = field.get("value")
        places = value if isinstance(value, list) else [value]
        places = [str(p).strip() for p in places if p and str(p).strip()]
        if places:
            return "; ".join(places)
    return name


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Greenhouse adapter requires 'slug' for {company.get('name')}")

    try:
        payload = _get(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Greenhouse HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Greenhouse network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Greenhouse returned invalid JSON for slug='{slug}'") from e

    raw_jobs = payload.get("jobs") or []
    jobs: list[Job] = []
    for raw in raw_jobs:
        try:
            departments = raw.get("departments") or []
            dept = departments[0].get("name") if departments else None
            jobs.append(
                Job(
                    id=str(raw["id"]),
                    company=company["name"],
                    title=raw.get("title", "").strip(),
                    location=_location(raw),
                    url=raw.get("absolute_url", ""),
                    posted_at=raw.get("first_published") or raw.get("updated_at"),
                    department=dept,
                    ats="greenhouse",
                    category=company.get("category", "uncategorized"),
                    description=normalize_description(
                        raw.get("content"), is_html=True
                    ),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Greenhouse: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
