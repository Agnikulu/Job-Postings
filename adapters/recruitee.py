"""Recruitee Job Board API adapter.

Endpoint: GET https://{slug}.recruitee.com/api/offers
Used by 1X Technologies and other Recruitee-hosted career sites.
"""

from __future__ import annotations

import html
import logging
import re
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


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(slug: str) -> dict[str, Any]:
    resp = requests.get(
        f"https://{slug}.recruitee.com/api/offers",
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _format_location(offer: dict[str, Any]) -> str:
    locs = offer.get("locations") or []
    if locs:
        parts: list[str] = []
        for loc in locs:
            if isinstance(loc, dict):
                bits = [loc.get("city"), loc.get("country")]
                label = ", ".join(b for b in bits if b)
                if label:
                    parts.append(label)
            elif loc:
                parts.append(str(loc))
        if parts:
            return " / ".join(parts)
    if offer.get("location"):
        return str(offer["location"])
    bits = [offer.get("city"), offer.get("country")]
    return ", ".join(b for b in bits if b)


def _offer_url(slug: str, offer: dict[str, Any]) -> str:
    offer_slug = offer.get("slug") or offer.get("id")
    if offer_slug:
        return f"https://{slug}.recruitee.com/o/{offer_slug}"
    return f"https://{slug}.recruitee.com/"


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug") or company.get("recruitee_slug")
    if not slug:
        raise AdapterError(
            f"Recruitee adapter requires 'slug' for {company.get('name')}"
        )

    try:
        payload = _get(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Recruitee HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Recruitee network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Recruitee returned invalid JSON for slug='{slug}'") from e

    jobs: list[Job] = []
    for raw in payload.get("offers") or []:
        try:
            title = str(raw.get("title") or raw.get("position") or "").strip()
            if not title:
                continue
            desc_parts = [
                raw.get("description"),
                raw.get("requirements"),
                raw.get("highlight"),
            ]
            desc_raw = "\n\n".join(
                p for p in desc_parts if p and str(p).strip()
            )
            desc = normalize_description(desc_raw, is_html=True) if desc_raw else None
            job_id = str(raw.get("id") or raw.get("slug") or title)
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=html.unescape(title),
                    location=_format_location(raw),
                    url=_offer_url(slug, raw),
                    posted_at=raw.get("published_at") or raw.get("created_at"),
                    department=raw.get("department"),
                    ats="recruitee",
                    category=company.get("category", "uncategorized"),
                    description=desc,
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Recruitee: skipping malformed job for %s: %s", slug, e)
            continue
    return jobs
