"""Lever Postings API adapter.

Endpoint: GET https://api.lever.co/v0/postings/{slug}?mode=json
Docs:     https://github.com/lever/postings-api (unofficial but stable)
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
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

BASE_URL = "https://api.lever.co/v0/postings/{slug}"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(slug: str) -> list[dict[str, Any]]:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        params={"mode": "json"},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _ms_to_iso(ms: int | None) -> str | None:
    if not ms:
        return None
    try:
        return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()
    except (ValueError, OSError):
        return None


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Lever adapter requires 'slug' for {company.get('name')}")

    try:
        raw_jobs = _get(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Lever HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Lever network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Lever returned invalid JSON for slug='{slug}'") from e

    jobs: list[Job] = []
    for raw in raw_jobs or []:
        try:
            categories = raw.get("categories") or {}
            jobs.append(
                Job(
                    id=str(raw["id"]),
                    company=company["name"],
                    title=raw.get("text", "").strip(),
                    location=categories.get("location", "") or "",
                    url=raw.get("hostedUrl", "") or raw.get("applyUrl", ""),
                    posted_at=_ms_to_iso(raw.get("createdAt")),
                    department=categories.get("team") or categories.get("department"),
                    ats="lever",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Lever: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
