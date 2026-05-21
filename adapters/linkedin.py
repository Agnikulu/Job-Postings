"""LinkedIn careers adapter (company jobs via guest search API).

Endpoint: GET https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search
Uses f_C company filter (1337 = LinkedIn) for linkedin.com/careers roles.
"""

from __future__ import annotations

import html
import logging
import re
from dataclasses import replace
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_linkedin_description, map_descriptions_parallel

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
PAGE_SIZE = 10
MAX_PAGES = 200
DETAIL_WORKERS = 6
DEFAULT_COMPANY_ID = "1337"


def _browser_headers() -> dict[str, str]:
    return {
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
def _get_page(company_id: str, start: int, location: str) -> str:
    resp = requests.get(
        SEARCH_URL,
        params={"f_C": company_id, "location": location, "start": start},
        headers=_browser_headers(),
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.text


def _parse_page(text: str) -> list[dict[str, str]]:
    jobs: list[dict[str, str]] = []
    cards = re.split(r"(?=data-entity-urn=\"urn:li:jobPosting:)", text)
    for card in cards:
        urn = re.search(r'data-entity-urn="urn:li:jobPosting:(\d+)"', card)
        if not urn:
            continue
        job_id = urn.group(1)
        title_match = re.search(r"base-search-card__title[^>]*>\s*([^<]+)", card)
        link_match = re.search(r'base-card__full-link[^>]*href="([^"]+)"', card)
        loc_match = re.search(r"job-search-card__location[^>]*>\s*([^<]+)", card)
        time_match = re.search(r"job-search-card__listdate[^>]*>\s*([^<]+)", card)
        title = html.unescape(title_match.group(1).strip()) if title_match else ""
        url = html.unescape(link_match.group(1).strip()) if link_match else ""
        location = html.unescape(loc_match.group(1).strip()) if loc_match else ""
        posted_at = html.unescape(time_match.group(1).strip()) if time_match else None
        if title and url:
            jobs.append(
                {
                    "id": job_id,
                    "title": title,
                    "url": url,
                    "location": location,
                    "posted_at": posted_at,
                }
            )
    return jobs


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    company_id = str(company.get("linkedin_company_id") or DEFAULT_COMPANY_ID)
    location = company.get("search_location") or "United States"

    all_raw: list[dict[str, str]] = []
    for page in range(MAX_PAGES):
        start = page * PAGE_SIZE
        try:
            page_jobs = _parse_page(_get_page(company_id, start, location))
        except requests.HTTPError as e:
            raise AdapterError(
                f"LinkedIn HTTP {e.response.status_code} for {name} start={start}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"LinkedIn network error for {name}: {e}") from e

        if not page_jobs:
            break
        all_raw.extend(page_jobs)

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            jobs.append(
                Job(
                    id=raw["id"],
                    company=company["name"],
                    title=raw["title"],
                    location=raw.get("location") or "",
                    url=raw["url"],
                    posted_at=raw.get("posted_at"),
                    department=None,
                    ats="linkedin",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("LinkedIn: skipping malformed job for %s: %s", name, e)
            continue

    if jobs:
        descs = map_descriptions_parallel(
            [j.id for j in jobs],
            fetch_linkedin_description,
            max_workers=DETAIL_WORKERS,
        )
        jobs = [replace(j, description=descs.get(j.id)) for j in jobs]
    return jobs
