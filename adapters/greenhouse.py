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
                    location=(raw.get("location") or {}).get("name", "") or "",
                    url=raw.get("absolute_url", ""),
                    posted_at=raw.get("updated_at") or raw.get("first_published"),
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
