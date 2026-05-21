"""Ashby Job Board API adapter.

Endpoint: GET https://api.ashbyhq.com/posting-api/job-board/{slug}
Docs:     https://developers.ashbyhq.com/reference/jobpostinginfo
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

BASE_URL = "https://api.ashbyhq.com/posting-api/job-board/{slug}"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(slug: str) -> dict[str, Any]:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        params={"includeCompensation": "false"},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Ashby adapter requires 'slug' for {company.get('name')}")

    try:
        payload = _get(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Ashby HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Ashby network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Ashby returned invalid JSON for slug='{slug}'") from e

    raw_jobs = payload.get("jobs") or []
    jobs: list[Job] = []
    for raw in raw_jobs:
        try:
            jobs.append(
                Job(
                    id=str(raw["id"]),
                    company=company["name"],
                    title=raw.get("title", "").strip(),
                    location=raw.get("location", "") or "",
                    url=raw.get("jobUrl", "") or raw.get("applyUrl", ""),
                    posted_at=raw.get("publishedAt"),
                    department=raw.get("department"),
                    ats="ashby",
                    category=company.get("category", "uncategorized"),
                    description=normalize_description(raw.get("descriptionPlain")),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Ashby: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
