"""Workable public widget API adapter.

Endpoint: GET https://apply.workable.com/api/v1/widget/accounts/{slug}
Used by Hugging Face and other companies on apply.workable.com.
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

BASE_URL = "https://apply.workable.com/api/v1/widget/accounts/{slug}"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(slug: str) -> dict[str, Any]:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _format_location(raw: dict[str, Any]) -> str:
    locs = raw.get("locations") or []
    if locs:
        parts: list[str] = []
        for loc in locs:
            bits = [loc.get("city"), loc.get("region"), loc.get("country")]
            label = ", ".join(b for b in bits if b)
            if label:
                parts.append(label)
        if parts:
            return " / ".join(parts)
    bits = [raw.get("city"), raw.get("state"), raw.get("country")]
    return ", ".join(b for b in bits if b)


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Workable adapter requires 'slug' for {company.get('name')}")

    try:
        payload = _get(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Workable HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Workable network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Workable returned invalid JSON for slug='{slug}'") from e

    jobs: list[Job] = []
    for raw in payload.get("jobs") or []:
        try:
            jobs.append(
                Job(
                    id=str(raw.get("shortcode") or raw.get("id") or raw.get("title")),
                    company=company["name"],
                    title=raw.get("title", "").strip(),
                    location=_format_location(raw),
                    url=raw.get("url") or raw.get("shortlink") or "",
                    posted_at=raw.get("published_on") or raw.get("created_at"),
                    department=raw.get("department"),
                    ats="workable",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Workable: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
