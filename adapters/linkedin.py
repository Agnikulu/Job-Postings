"""LinkedIn careers adapter (company jobs via guest search API).

Endpoint: GET https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search
Uses f_C company filter (1337 = LinkedIn) for linkedin.com/careers roles.
"""

from __future__ import annotations

import html
import logging
import re
import time
from dataclasses import replace
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_linkedin_description, map_descriptions_parallel
from fetch_limits import linkedin_page_delay_sec, max_list_pages
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .http_util import http_session

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
PAGE_SIZE = 10
MAX_PAGES = 200
DETAIL_WORKERS = 3
DEFAULT_COMPANY_ID = "1337"


def _normalize_title(title: str) -> str:
    """Strip LinkedIn list-card artifacts (leading #, whitespace)."""
    return title.lstrip("#").strip()


def _browser_headers() -> dict[str, str]:
    return {
        **DEFAULT_HEADERS,
        "Accept": "text/html,application/json,*/*",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    }


def _retryable_request_error(exc: BaseException) -> bool:
    if isinstance(exc, requests.HTTPError):
        return exc.response.status_code in {429, 500, 502, 503}
    return isinstance(exc, requests.RequestException)


def _sleep_for_rate_limit(resp: requests.Response) -> None:
    retry_after = resp.headers.get("Retry-After")
    if retry_after and retry_after.isdigit():
        pause = min(int(retry_after), 120)
    else:
        pause = 30
    log.warning("LinkedIn: HTTP 429, sleeping %ss before retry", pause)
    time.sleep(pause)


@retry(
    reraise=True,
    stop=stop_after_attempt(6),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    retry=retry_if_exception(_retryable_request_error),
)
def _get_page(
    session: requests.Session,
    company_id: str,
    start: int,
    location: str,
) -> str:
    resp = session.get(
        SEARCH_URL,
        params={"f_C": company_id, "location": location, "start": start},
        timeout=DEFAULT_TIMEOUT,
    )
    if resp.status_code == 429:
        _sleep_for_rate_limit(resp)
        resp.raise_for_status()
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
        raw_title = html.unescape(title_match.group(1).strip()) if title_match else ""
        title = _normalize_title(raw_title) if raw_title else ""
        raw_url = html.unescape(link_match.group(1).strip()) if link_match else ""
        # Use a canonical URL (no tracking query params) so the same job
        # posted at different pagination offsets deduplicates correctly.
        url = f"https://www.linkedin.com/jobs/view/{job_id}" if job_id else raw_url
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
    page_delay = linkedin_page_delay_sec()

    all_raw: list[dict[str, str]] = []
    with http_session(_browser_headers()) as session:
        for page in range(max_list_pages(MAX_PAGES)):
            start = page * PAGE_SIZE
            if page and page_delay:
                time.sleep(page_delay)
            try:
                page_jobs = _parse_page(
                    _get_page(session, company_id, start, location)
                )
            except requests.HTTPError as e:
                code = e.response.status_code if e.response is not None else "?"
                if code == 429:
                    log.warning(
                        "LinkedIn HTTP 429 for %s start=%s (retries exhausted)",
                        name,
                        start,
                    )
                # Guest search often returns 400 once start exceeds the index cap
                # (e.g. Intuit/Qualcomm with very large US catalogs).
                if code == 400 and all_raw:
                    log.warning(
                        "LinkedIn HTTP 400 for %s start=%s; stopping pagination at %d jobs",
                        name,
                        start,
                        len(all_raw),
                    )
                    break
                raise AdapterError(f"LinkedIn HTTP {code} for {name} start={start}") from e
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

    fetch_ids = [j.id for j in jobs if should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_ids:
        descs = map_descriptions_parallel(
            fetch_ids,
            fetch_linkedin_description,
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.id)) for j in jobs]
    return jobs
