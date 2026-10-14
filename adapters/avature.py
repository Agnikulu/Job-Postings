"""Avature careers-portal adapter (server-rendered HTML).

List:   GET https://{avature_host}/{avature_portal}/SearchJobs/?jobRecordsPerPage=12&jobOffset=N
Detail: GET https://{avature_host}/{avature_portal}/JobDetail/{slug}/{id}

The portal ignores larger page sizes, so list pages are fetched in parallel
once the first page reports the total. Detail pages (descriptions) are only
fetched for postings that could be included on title + location.
Used by Bloomberg.
"""

from __future__ import annotations

import html
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

PAGE_SIZE = 12
MAX_PAGES = 200
LIST_WORKERS = 6
DETAIL_WORKERS = 6

_TOTAL_RE = re.compile(r'aria-label="(\d[\d,]*) results?"')
_ARTICLE_RE = re.compile(
    r'<article class="article article--result"(.*?)</article>', re.DOTALL
)
_LINK_RE = re.compile(r'<a class="link" href="([^"]+/JobDetail/[^"]+/(\d+))"\s*>\s*(.*?)\s*</a>', re.DOTALL)
_LOCATION_RE = re.compile(r'<span class="list-item-location">\s*(.*?)\s*</span>', re.DOTALL)
# A details <article> whose header says "Description..." holds the body.
_DESC_ARTICLE_RE = re.compile(
    r'<h2 class="article__header__text__title[^"]*">\s*Description[^<]*</h2>'
    r'(.*?)</article>',
    re.DOTALL,
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
def _get(url: str, params: dict[str, Any] | None = None) -> str:
    resp = requests.get(url, params=params, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def _get_page(base: str, offset: int) -> str:
    return _get(
        f"{base}/SearchJobs/",
        params={"jobRecordsPerPage": PAGE_SIZE, "jobOffset": offset},
    )


def _parse_total(page_html: str) -> int:
    m = _TOTAL_RE.search(page_html)
    return int(m.group(1).replace(",", "")) if m else 0


def _parse_list(page_html: str) -> list[dict[str, str]]:
    rows = []
    for article in _ARTICLE_RE.findall(page_html):
        link = _LINK_RE.search(article)
        if not link:
            continue
        loc = _LOCATION_RE.search(article)
        rows.append(
            {
                "url": html.unescape(link.group(1)),
                "id": link.group(2),
                "title": _text(link.group(3)),
                "location": _text(loc.group(1)) if loc else "",
            }
        )
    return rows


def _parse_description(page_html: str) -> str | None:
    m = _DESC_ARTICLE_RE.search(page_html)
    return normalize_description(m.group(1), is_html=True) if m else None


def _fetch_description(url: str) -> str | None:
    try:
        return _parse_description(_get(url))
    except requests.RequestException:
        return None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    host = company.get("avature_host")
    if not host:
        raise AdapterError(f"Avature adapter requires 'avature_host' for {name}")
    base = f"https://{host}/{company.get('avature_portal', 'careers')}"

    try:
        first = _get_page(base, 0)
        total = _parse_total(first)
        offsets = list(range(PAGE_SIZE, min(total, PAGE_SIZE * MAX_PAGES), PAGE_SIZE))
        with ThreadPoolExecutor(max_workers=LIST_WORKERS) as pool:
            pages = [first, *pool.map(lambda off: _get_page(base, off), offsets)]
    except requests.HTTPError as e:
        raise AdapterError(f"Avature HTTP {e.response.status_code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Avature network error for {name}: {e}") from e

    rows: dict[str, dict[str, str]] = {}
    for page_html in pages:
        for row in _parse_list(page_html):
            rows.setdefault(row["id"], row)
    if not rows:
        raise AdapterError(f"Avature: no postings parsed for {name}")
    if total and len(rows) < total:
        log.warning("Avature %s: parsed %d of %d postings", name, len(rows), total)

    jobs = [
        Job(
            id=row["id"],
            company=company["name"],
            title=row["title"],
            location=row["location"],
            url=row["url"],
            posted_at=None,
            department=None,
            ats="avature",
            category=company.get("category", "uncategorized"),
        )
        for row in rows.values()
    ]

    fetch_urls = [
        j.url
        for j in jobs
        if should_fetch_description(j.title) and could_be_included(j.title, j.location)
    ]
    descs = map_descriptions_parallel(fetch_urls, _fetch_description, max_workers=DETAIL_WORKERS)
    return [replace(j, description=descs.get(j.url)) for j in jobs]
