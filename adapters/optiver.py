"""Optiver careers adapter (custom Episerver/Optimizely-backed job API).

Optiver's careers site (optiver.com/join-us/jobs/) is not on any common ATS.
The list is served by a plain JSON endpoint that paginates via a fixed
16-item page size and a `from` offset (no `size`/`limit` override works);
job descriptions require a separate per-job HTML page fetch, since the list
endpoint only returns title/location/experience/domain.
"""

from __future__ import annotations

import logging
from dataclasses import replace
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import (
    fetch_optiver_description,
    map_descriptions_parallel,
)
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

BASE_URL = "https://www.optiver.com"
LIST_URL = f"{BASE_URL}/en/api/v1/jobs"
PAGE_SIZE = 16
MAX_PAGES = 30
DETAIL_WORKERS = 6

_UA = {
    **DEFAULT_HEADERS,
    "Accept": "application/json",
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
def _get_page(offset: int) -> dict[str, Any]:
    resp = requests.get(
        LIST_URL,
        params={"from": offset},
        headers=_UA,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _fetch_all_jobs() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    offset = 0
    total = None
    for _ in range(MAX_PAGES):
        payload = _get_page(offset)
        page_items = payload.get("items") or []
        if not page_items:
            break
        items.extend(page_items)
        total = payload.get("totalCount")
        offset += len(page_items)
        if total is not None and offset >= total:
            break
    return items


def fetch(company: dict[str, Any]) -> list[Job]:
    try:
        raw_jobs = _fetch_all_jobs()
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        raise AdapterError(f"Optiver HTTP {code}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Optiver network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Optiver returned invalid JSON") from e

    jobs: list[Job] = []
    for raw in raw_jobs:
        try:
            href = str(raw.get("href") or "").strip()
            if not href:
                continue
            job_id = str(raw.get("componentID") or href)
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=str(raw.get("title") or "").strip(),
                    location=str(raw.get("location") or "").strip(),
                    url=f"{BASE_URL}{href}" if href.startswith("/") else href,
                    posted_at=None,
                    department=raw.get("domain"),
                    description=None,
                    ats="optiver",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Optiver: skipping malformed job: %s", e)
            continue

    fetch_urls = [j.url for j in jobs if j.url and should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_urls:
        descs = map_descriptions_parallel(
            fetch_urls,
            fetch_optiver_description,
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.url) or j.description) for j in jobs]
    return jobs
