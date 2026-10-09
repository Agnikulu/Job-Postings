"""Apple careers adapter (jobs.apple.com JSON search API).

Endpoint: POST https://jobs.apple.com/api/v1/search
Page size is fixed at 20 server-side; the first page reports totalRecords, so the
remaining pages are fetched in parallel.
"""

from __future__ import annotations

import logging
import math
from concurrent.futures import ThreadPoolExecutor
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
from filters import should_fetch_description
from text_util import normalize_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SEARCH_API = "https://jobs.apple.com/api/v1/search"
BASE_URL = "https://jobs.apple.com"
PAGE_SIZE = 20
# Safety bound only (~6k postings = ~310 pages); not subject to ATS_SNIPER_MAX_LIST_PAGES
# because the whole board is needed to avoid silently dropping postings.
MAX_PAGES = 1000
PAGE_WORKERS = 8
REFETCH_ROUNDS = 5
DETAIL_WORKERS = 6


@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=2, max=15),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(page: int) -> dict[str, Any]:
    headers = {
        **DEFAULT_HEADERS,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": BASE_URL,
        "Referer": f"{BASE_URL}/en-us/search",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    }
    body = {
        "query": "",
        "filters": {},
        "page": page,
        "locale": "en-us",
        "sort": "newest",
        # The API returns no results without a format block.
        "format": {"longDate": "MMMM D, YYYY", "mediumDate": "MMM D, YYYY"},
    }
    resp = requests.post(SEARCH_API, json=body, headers=headers, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    payload = resp.json()
    res = payload.get("res") if isinstance(payload, dict) else None
    if not isinstance(res, dict):
        raise AdapterError(f"Apple search page {page}: unexpected payload")
    return res


def _location(raw: dict[str, Any]) -> str:
    places: list[str] = []
    for loc in raw.get("locations") or []:
        parts: list[str] = []
        for key in ("name", "city", "stateProvince", "countryName"):
            val = str(loc.get(key) or "").strip()
            if val and val not in parts:
                parts.append(val)
        place = ", ".join(parts)
        if place and place not in places:
            places.append(place)
    return "; ".join(places)


def _job_id(raw: dict[str, Any]) -> str:
    # Managed pipeline roles are "PIPE-<req>"; their detail URL uses just <req>.
    # Others are "<req>-<location>" and the URL uses the full id.
    job_id = str(raw.get("id") or raw.get("positionId") or "")
    return job_id.removeprefix("PIPE-")


def _to_job(raw: dict[str, Any], company: dict[str, Any]) -> Job:
    job_id = _job_id(raw)
    title = str(raw["postingTitle"]).strip()
    if not job_id or not title:
        raise KeyError("id/postingTitle")
    slug = raw.get("transformedPostingTitle") or ""
    team = raw.get("team") or {}
    return Job(
        id=job_id,
        company=company["name"],
        title=title,
        location=_location(raw),
        url=f"{BASE_URL}/en-us/details/{job_id}/{slug}",
        posted_at=raw.get("postDateInGMT") or None,
        department=team.get("teamName") or None,
        ats="apple",
        category=company.get("category", "uncategorized"),
    )


def _fetch_all_raw(name: str) -> list[dict[str, Any]]:
    first = _get_page(1)
    results = list(first.get("searchResults") or [])
    if not results:
        return []
    try:
        total = int(first.get("totalRecords") or 0)
    except (TypeError, ValueError):
        total = 0
    last_page = min(MAX_PAGES, max(1, math.ceil(total / PAGE_SIZE)))

    pages: dict[int, list[dict[str, Any]]] = {1: results}
    with ThreadPoolExecutor(max_workers=PAGE_WORKERS) as pool:
        nums = list(range(2, last_page + 1))
        for num, res in zip(nums, pool.map(_get_page, nums)):
            pages[num] = list(res.get("searchResults") or [])

    # Postings added mid-scrape push older ones past the reported last page.
    page = last_page
    while len(pages[page]) == PAGE_SIZE and page < MAX_PAGES:
        page += 1
        pages[page] = list(_get_page(page).get("searchResults") or [])

    seen: set[str] = set()
    merged: list[dict[str, Any]] = []
    first_page: dict[str, int] = {}
    dup_pages: set[int] = set()

    def _merge(page_nums: list[int]) -> None:
        for num in page_nums:
            for raw in pages[num]:
                key = str(raw.get("id") or "")
                if not key:
                    continue
                if key in seen:
                    if first_page[key] != num:
                        dup_pages.update((num, first_page[key]))
                    continue
                seen.add(key)
                first_page[key] = num
                merged.append(raw)

    _merge(sorted(pages))
    # Postings sharing one timestamp (multi-location reqs) are ordered differently on
    # each request, so a tie group straddling a page boundary repeats one sibling and
    # skips another. Re-fetching those pages surfaces the skipped siblings.
    for _ in range(REFETCH_ROUNDS):
        if not dup_pages or (total and len(merged) >= total):
            break
        nums = sorted(dup_pages)
        with ThreadPoolExecutor(max_workers=PAGE_WORKERS) as pool:
            for num, res in zip(nums, pool.map(_get_page, nums)):
                pages[num] = list(res.get("searchResults") or [])
        _merge(nums)
    if total and len(merged) < total:
        log.warning("Apple: got %d of %d reported postings for %s", len(merged), total, name)
    return merged


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    try:
        all_raw = _fetch_all_raw(name)
    except requests.HTTPError as e:
        raise AdapterError(f"Apple HTTP {e.response.status_code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Apple network error for {name}: {e}") from e

    jobs: list[Job] = []
    summaries: dict[str, str] = {}
    for raw in all_raw:
        try:
            job = _to_job(raw, company)
        except (KeyError, TypeError) as e:
            log.warning("Apple: skipping malformed job for %s: %s", name, e)
            continue
        jobs.append(job)
        if raw.get("jobSummary"):
            summaries[job.id] = raw["jobSummary"]

    fetch_ids = [j.id for j in jobs if should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_ids:
        slug_by_id = {j.id: j.url.rsplit("/", 1)[-1] for j in jobs}
        descs = map_descriptions_parallel(
            fetch_ids,
            lambda job_id: fetch_apple_description(job_id, slug_by_id.get(job_id, "")),
            max_workers=DETAIL_WORKERS,
        )
    return [
        replace(
            j,
            description=descs.get(j.id) or normalize_description(summaries.get(j.id)),
        )
        if j.id in descs
        else j
        for j in jobs
    ]
