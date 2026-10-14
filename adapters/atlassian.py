"""Atlassian careers adapter.

Endpoint: GET https://www.atlassian.com/endpoint/careers/listings

One JSON array of every posting (iCIMS-backed) with locations and the
overview / responsibilities / qualifications HTML inline, so no detail
fetches are needed.
"""

from __future__ import annotations

import logging
from datetime import datetime
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

LISTINGS_URL = "https://www.atlassian.com/endpoint/careers/listings"
JOB_URL = "https://www.atlassian.com/company/careers/details/{id}"
# Listed alongside a posting's real locations; it adds nothing.
_GENERIC_REMOTE = "Remote - Remote"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_listings() -> Any:
    resp = requests.get(LISTINGS_URL, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def _location(raw: dict[str, Any]) -> str:
    locs = [" ".join(str(x).split()) for x in raw.get("locations") or [] if x]
    specific = [x for x in locs if x != _GENERIC_REMOTE]
    return "; ".join(dict.fromkeys(specific or locs))


def _updated_iso(post: Any) -> str | None:
    """iCIMS "2026-09-24 03:33 PM" -> ISO; the listings carry no posted date."""
    raw = post.get("updatedDate") if isinstance(post, dict) else None
    try:
        return datetime.strptime(str(raw), "%Y-%m-%d %I:%M %p").isoformat()
    except ValueError:
        return None


def _description(raw: dict[str, Any]) -> str | None:
    parts = [raw.get(k) for k in ("overview", "responsibilities", "qualifications")]
    body = "\n\n".join(str(p) for p in parts if p and str(p).strip())
    return normalize_description(body, is_html=True) if body else None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    try:
        listings = _get_listings()
    except requests.HTTPError as e:
        raise AdapterError(f"Atlassian HTTP {e.response.status_code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Atlassian network error for {name}: {e}") from e
    except ValueError as e:
        raise AdapterError(f"Atlassian returned invalid JSON for {name}") from e
    if not isinstance(listings, list) or not listings:
        raise AdapterError(f"Atlassian: no postings in listings for {name}")

    jobs: list[Job] = []
    for raw in listings:
        try:
            job_id = str(raw["id"])
            title = str(raw["title"]).strip()
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=title,
                    location=_location(raw),
                    url=JOB_URL.format(id=job_id),
                    posted_at=_updated_iso(raw.get("portalJobPost")),
                    department=raw.get("category"),
                    ats="atlassian",
                    category=company.get("category", "uncategorized"),
                    description=_description(raw),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Atlassian: skipping malformed job for %s: %s", name, e)
    return jobs
