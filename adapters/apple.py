"""Apple careers adapter (jobs.apple.com HTML search pages).

Endpoint: GET https://jobs.apple.com/en-us/search?sort=newest&page=N
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

from adapters.description_fetch import fetch_apple_description, map_descriptions_parallel

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SEARCH_URL = "https://jobs.apple.com/en-us/search"
BASE_URL = "https://jobs.apple.com"
_LABEL_RE = re.compile(
    r'aria-label="([^"]+)"[^>]*href="/en-us/details/(\d+)/([^"?]+)',
)
_LOCATION_RE = re.compile(
    r'search-location-search-job-title-PIPE-(\d+)-\d+"[^>]*>.*?'
    r'<span class="table--advanced-search__location-sub"[^>]*>([^<]+)</span>',
    re.DOTALL | re.IGNORECASE,
)
MAX_PAGES = 200
DETAIL_WORKERS = 6


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(page: int) -> str:
    headers = {
        **DEFAULT_HEADERS,
        "Accept": "text/html,application/json,*/*",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    }
    resp = requests.get(
        SEARCH_URL,
        params={"sort": "newest", "page": page},
        headers=headers,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.text


def _parse_page(text: str) -> list[dict[str, str]]:
    locations = {
        job_id: html.unescape(loc.strip())
        for job_id, loc in _LOCATION_RE.findall(text)
    }
    seen: set[str] = set()
    jobs: list[dict[str, str]] = []
    for label, job_id, slug in _LABEL_RE.findall(text):
        if label.startswith("See full") or label.startswith("Where we"):
            continue
        clean_label = html.unescape(label)
        match = re.match(r"^(.+?)\s+(\d{6,})$", clean_label)
        if not match or match.group(2) != job_id or job_id in seen:
            continue
        seen.add(job_id)
        jobs.append(
            {
                "id": job_id,
                "title": match.group(1).strip(),
                "slug": slug,
                "location": locations.get(job_id, ""),
            }
        )
    return jobs


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    all_raw: list[dict[str, str]] = []
    for page in range(1, MAX_PAGES + 1):
        try:
            page_jobs = _parse_page(_get_page(page))
        except requests.HTTPError as e:
            raise AdapterError(
                f"Apple HTTP {e.response.status_code} for {name} page {page}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Apple network error for {name}: {e}") from e

        if not page_jobs:
            break
        all_raw.extend(page_jobs)

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            job_id = raw["id"]
            slug = raw["slug"]
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=raw["title"],
                    location=raw.get("location", "") or "",
                    url=f"{BASE_URL}/en-us/details/{job_id}/{slug}",
                    posted_at=None,
                    department=None,
                    ats="apple",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Apple: skipping malformed job for %s: %s", name, e)
            continue

    if jobs:
        slug_by_id = {raw["id"]: raw["slug"] for raw in all_raw}
        descs = map_descriptions_parallel(
            [j.id for j in jobs],
            lambda job_id: fetch_apple_description(job_id, slug_by_id.get(job_id, "")),
            max_workers=DETAIL_WORKERS,
        )
        jobs = [replace(j, description=descs.get(j.id)) for j in jobs]
    return jobs
