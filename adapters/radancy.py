"""Radancy (TalentBrew) careers-site adapter.

List:   GET https://{careers_host}/search-jobs/results?CurrentPage=N&RecordsPerPage=100&...
        (with X-Requested-With: XMLHttpRequest) -> {"results": "<html>"}
Detail: GET https://{careers_host}/job/... -> JSON-LD JobPosting

List cards carry title, a single location (or "Multiple locations") and a
category. Detail pages are fetched only for postings that could be included;
their JSON-LD gives the description, posting date and every location.
Used by Arm.
"""

from __future__ import annotations

import html
import json
import logging
import re
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

from adapters.description_fetch import map_descriptions_parallel
from filters import could_be_included, should_fetch_description
from text_util import normalize_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

PAGE_SIZE = 100
MAX_PAGES = 50
LIST_WORKERS = 4
DETAIL_WORKERS = 6
MULTIPLE_LOCATIONS = "multiple locations"

_TOTAL_PAGES_RE = re.compile(r'data-total-pages="(\d+)"')
_CARD_RE = re.compile(
    r'<a\b[^>]*href="(/job/[^"]+)"[^>]*data-job-id="(\d+)"[^>]*>(.*?)</a>(.*?)(?=<a\b[^>]*data-job-id=|</ul>|$)',
    re.DOTALL,
)
_LOCATION_RE = re.compile(r'<span class="[^"]*\blocation\b[^"]*">(.*?)</span>', re.DOTALL)
_CATEGORY_RE = re.compile(r'<span class="[^"]*\bcategory\b[^"]*">(.*?)</span>', re.DOTALL)
_LD_JSON_RE = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
)
_TAG_RE = re.compile(r"<[^>]+>")


def _text(fragment: str) -> str:
    return " ".join(html.unescape(_TAG_RE.sub(" ", fragment)).split())


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(url: str, params: dict[str, Any] | None = None, *, ajax: bool = False) -> requests.Response:
    headers = {**DEFAULT_HEADERS}
    if ajax:
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Accept"] = "application/json"
    resp = requests.get(url, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp


def _get_page(host: str, page: int) -> str:
    resp = _get(
        f"https://{host}/search-jobs/results",
        params={
            "ActiveFacetID": 0,
            "CurrentPage": page,
            "RecordsPerPage": PAGE_SIZE,
            "SearchResultsModuleName": "Search Results",
            "SearchFiltersModuleName": "Search Filters",
            "SortCriteria": 0,
            "SortDirection": 0,
            "SearchType": 5,
        },
        ajax=True,
    )
    return str(resp.json().get("results") or "")


def _parse_list(page_html: str) -> list[dict[str, str]]:
    rows = []
    for path, job_id, title, rest in _CARD_RE.findall(page_html):
        loc = _LOCATION_RE.search(rest)
        cat = _CATEGORY_RE.search(rest)
        rows.append(
            {
                "path": html.unescape(path),
                "id": job_id,
                "title": _text(title),
                "location": _text(loc.group(1)) if loc else "",
                "category": _text(cat.group(1)) if cat else "",
            }
        )
    return rows


def _place(place: dict[str, Any]) -> str:
    addr = place.get("address") or {}
    bits = [
        str(addr.get(k) or "").strip()
        for k in ("addressLocality", "addressRegion", "addressCountry")
    ]
    return ", ".join(b for b in bits if b)


def parse_detail(page_html: str) -> dict[str, Any] | None:
    """JobPosting JSON-LD -> {description, location, posted_at}."""
    for blob in _LD_JSON_RE.findall(page_html):
        try:
            data = json.loads(blob)
        except ValueError:
            continue
        if not isinstance(data, dict) or data.get("@type") != "JobPosting":
            continue
        places = data.get("jobLocation") or []
        if isinstance(places, dict):
            places = [places]
        locations = [p for p in (_place(pl) for pl in places if isinstance(pl, dict)) if p]
        desc = data.get("description")
        return {
            "description": normalize_description(desc, is_html=True) if desc else None,
            "location": "; ".join(dict.fromkeys(locations)),
            "posted_at": data.get("datePosted"),
        }
    return None


def _fetch_detail(url: str) -> dict[str, Any] | None:
    try:
        return parse_detail(_get(url).text)
    except requests.RequestException:
        return None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    host = company.get("careers_host")
    if not host:
        raise AdapterError(f"Radancy adapter requires 'careers_host' for {name}")

    try:
        first = _get_page(host, 1)
        m = _TOTAL_PAGES_RE.search(first)
        last_page = min(MAX_PAGES, int(m.group(1)) if m else 1)
        with ThreadPoolExecutor(max_workers=LIST_WORKERS) as pool:
            pages = [first, *pool.map(lambda p: _get_page(host, p), range(2, last_page + 1))]
    except requests.HTTPError as e:
        raise AdapterError(f"Radancy HTTP {e.response.status_code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Radancy network error for {name}: {e}") from e
    except ValueError as e:
        raise AdapterError(f"Radancy returned invalid JSON for {name}") from e

    rows: dict[str, dict[str, str]] = {}
    for page_html in pages:
        for row in _parse_list(page_html):
            rows.setdefault(row["id"], row)
    if not rows:
        raise AdapterError(f"Radancy: no postings parsed for {name}")
    # data-total-results counts job x location pairs, so it isn't compared.

    jobs = [
        Job(
            id=row["id"],
            company=company["name"],
            title=row["title"],
            location=row["location"],
            url=f"https://{host}{row['path']}",
            posted_at=None,
            department=row["category"] or None,
            ats="radancy",
            category=company.get("category", "uncategorized"),
        )
        for row in rows.values()
    ]

    def wants_detail(job: Job) -> bool:
        # "Multiple locations" needs the detail page for the real locations,
        # even when the title alone is decisive.
        if job.location.strip().lower() == MULTIPLE_LOCATIONS:
            return could_be_included(job.title)
        return should_fetch_description(job.title) and could_be_included(job.title, job.location)

    details = map_descriptions_parallel(
        [j.url for j in jobs if wants_detail(j)], _fetch_detail, max_workers=DETAIL_WORKERS
    )
    out: list[Job] = []
    for job in jobs:
        detail = details.get(job.url)
        if detail:
            job = replace(
                job,
                location=detail["location"] or job.location,
                posted_at=detail["posted_at"],
                description=detail["description"],
            )
        out.append(job)
    return out
