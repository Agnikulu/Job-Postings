"""Rippling ATS public job-board adapter.

Endpoint: GET https://ats.rippling.com/{slug}/jobs
Jobs are embedded in the page's __NEXT_DATA__ JSON (SSR).
"""

from __future__ import annotations

import json
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

from adapters.description_fetch import fetch_rippling_description, map_descriptions_parallel
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

BASE_URL = "https://ats.rippling.com/{slug}/jobs"
_NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>',
    re.DOTALL,
)
DETAIL_WORKERS = 6


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_html(slug: str) -> str:
    resp = requests.get(
        BASE_URL.format(slug=slug),
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.text


def _merge_items(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse duplicate job IDs (one row per location) into one posting."""
    merged: dict[str, dict[str, Any]] = {}
    for item in items:
        jid = str(item.get("id") or "")
        if not jid:
            continue
        if jid not in merged:
            merged[jid] = dict(item)
            continue
        seen = {
            loc.get("name")
            for loc in merged[jid].get("locations") or []
            if loc.get("name")
        }
        for loc in item.get("locations") or []:
            name = loc.get("name")
            if name and name not in seen:
                merged[jid].setdefault("locations", []).append(loc)
                seen.add(name)
    return list(merged.values())


def _format_location(raw: dict[str, Any]) -> str:
    locs = raw.get("locations") or []
    names = [loc.get("name", "") for loc in locs if loc.get("name")]
    return " / ".join(names)


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Rippling adapter requires 'slug' for {company.get('name')}")

    try:
        html = _get_html(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Rippling HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Rippling network error for slug='{slug}': {e}") from e

    match = _NEXT_DATA_RE.search(html)
    if not match:
        raise AdapterError(f"Rippling: no __NEXT_DATA__ found for slug='{slug}'")

    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        raise AdapterError(f"Rippling returned invalid __NEXT_DATA__ for '{slug}'") from e

    jobs_blob = payload.get("props", {}).get("pageProps", {}).get("jobs") or {}
    items = jobs_blob.get("items") if isinstance(jobs_blob, dict) else jobs_blob
    if not isinstance(items, list):
        raise AdapterError(f"Rippling: unexpected jobs payload for slug='{slug}'")

    jobs: list[Job] = []
    for raw in _merge_items(items):
        try:
            dept = raw.get("department") or {}
            jobs.append(
                Job(
                    id=str(raw["id"]),
                    company=company["name"],
                    title=str(raw.get("name", "")).strip(),
                    location=_format_location(raw),
                    url=raw.get("url") or "",
                    posted_at=None,
                    department=dept.get("name") if isinstance(dept, dict) else dept,
                    ats="rippling",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Rippling: skipping malformed job for %s: %s", slug, e)
            continue

    fetch_urls = [
        j.url for j in jobs if j.url and should_fetch_description(j.title)
    ]
    descs: dict[str, str | None] = {}
    if fetch_urls:
        descs = map_descriptions_parallel(
            fetch_urls,
            fetch_rippling_description,
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.url)) for j in jobs]
    return jobs
