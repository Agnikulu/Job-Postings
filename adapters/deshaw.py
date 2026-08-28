"""D. E. Shaw group careers adapter (custom Next.js site, deshaw.com).

The /careers landing page is server-rendered by Next.js and embeds the
FULL job list - including complete description text (intro, HTML
responsibilities, HTML qualifications) - directly in its __NEXT_DATA__
JSON blob (pageProps.regularJobs + pageProps.internships). No pagination
and no separate per-job description fetch are needed: this one page has
everything. pageProps.internalJobs is a mix of hidden placeholder
requisitions and "All Positions in X" category landing stubs, not real
postings, and is deliberately not used.
"""

from __future__ import annotations

import json
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

CAREERS_URL = "https://www.deshaw.com/careers"
BASE_URL = "https://www.deshaw.com/careers/"

_NEXT_DATA = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(.+?)</script>', re.DOTALL
)
_UA = {
    **DEFAULT_HEADERS,
    "Accept": "text/html,application/json,*/*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
}


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_html() -> str:
    resp = requests.get(CAREERS_URL, headers=_UA, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def _extract_jobs(html: str) -> list[dict[str, Any]]:
    match = _NEXT_DATA.search(html)
    if not match:
        raise AdapterError("D. E. Shaw careers page missing __NEXT_DATA__")
    try:
        payload = json.loads(match.group(1))
    except ValueError as e:
        raise AdapterError(f"D. E. Shaw __NEXT_DATA__ invalid JSON: {e}") from e
    page_props = payload.get("props", {}).get("pageProps", {})
    raw = (page_props.get("regularJobs") or []) + (page_props.get("internships") or [])
    return [entry["data"] for entry in raw if isinstance(entry, dict) and "data" in entry]


def _location(data: dict[str, Any]) -> str:
    locs = (data.get("jobMetadata") or {}).get("jobLocations") or []
    names = [loc.get("name") for loc in locs if isinstance(loc, dict) and loc.get("name")]
    return " / ".join(dict.fromkeys(names))


def _description(data: dict[str, Any]) -> str | None:
    jd = data.get("jobDescription") or {}
    parts = [
        jd.get("websiteDescription"),
        jd.get("responsibilitiesHtml"),
        jd.get("peopleWeAreLookingForHtml"),
    ]
    combined = "\n\n".join(p for p in parts if p and str(p).strip())
    return normalize_description(combined, is_html=True)


def fetch(company: dict[str, Any]) -> list[Job]:
    try:
        html = _get_html()
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        raise AdapterError(f"D. E. Shaw HTTP {code}") from e
    except requests.RequestException as e:
        raise AdapterError(f"D. E. Shaw network error: {e}") from e

    raw_jobs = _extract_jobs(html)

    jobs: list[Job] = []
    for data in raw_jobs:
        try:
            if not data.get("activeOnJobsListing"):
                continue
            title = str(data.get("displayName") or "").strip()
            job_url = str(data.get("jobUrl") or "").strip()
            if not title or not job_url or title.startswith("All Positions"):
                continue
            job_id = str(data.get("id") or job_url)
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=title,
                    location=_location(data),
                    url=f"{BASE_URL}{job_url}",
                    posted_at=None,
                    department=(data.get("department") or {}).get("name"),
                    description=_description(data),
                    ats="deshaw",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("D. E. Shaw: skipping malformed job: %s", e)
            continue
    return jobs
