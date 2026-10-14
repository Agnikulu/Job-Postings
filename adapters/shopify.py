"""Shopify careers adapter (shopify.com/careers, Ashby-backed, no public board).

List:   GET https://www.shopify.com/careers/search
Detail: GET https://www.shopify.com/careers?ashby_jid={id}  (redirects to the posting)

Both pages are React Router apps that inline their loader data as a
"turbo-stream" payload: one flat JSON array where objects are {"_<key index>":
<value index>} and lists hold value indexes. The search page's loader data has
every posting (`jobPostingsWithJobs`) plus the location table; the detail
page's has the description HTML.
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

from adapters.description_fetch import map_descriptions_parallel
from filters import could_be_included, is_location_ambiguous, should_fetch_description
from text_util import normalize_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.shopify.com/careers/search"
POSTING_URL = "https://www.shopify.com/careers?ashby_jid={id}"
DETAIL_WORKERS = 6
# Shopify's remote regions; "Americas" postings are open to the US and
# Canada but their descriptions never say so.
REGION_LABELS = {"Americas": "Americas (Remote: United States, Canada)"}

_ENQUEUE_RE = re.compile(r"streamController\.enqueue\((\".*?\")\);", re.DOTALL)


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get(url: str) -> str:
    resp = requests.get(url, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def decode_turbo_stream(page_html: str) -> dict[str, Any]:
    """Decode the inlined turbo-stream payload's root value (first line)."""
    raw = "".join(json.loads(chunk) for chunk in _ENQUEUE_RE.findall(page_html))
    first_line = next((line for line in raw.split("\n") if line.strip()), "")
    if not first_line:
        return {}
    flat = json.loads(first_line)
    memo: dict[int, Any] = {}

    def resolve(i: Any) -> Any:
        # Negative indexes are sentinels (undefined, null, NaN, ...).
        if not isinstance(i, int) or i < 0 or i >= len(flat):
            return None
        if i in memo:
            return memo[i]
        value = flat[i]
        if isinstance(value, dict):
            obj: dict[str, Any] = {}
            memo[i] = obj
            for key, vi in value.items():
                obj[str(flat[int(key[1:])])] = resolve(vi)
            return obj
        if isinstance(value, list):
            items: list[Any] = []
            memo[i] = items
            items.extend(resolve(x) for x in value)
            return items
        memo[i] = value
        return value

    root = resolve(0)
    return root if isinstance(root, dict) else {}


def _route_data(root: dict[str, Any], suffix: str) -> dict[str, Any]:
    for route, data in (root.get("loaderData") or {}).items():
        if route.endswith(suffix) and isinstance(data, dict):
            return data
    return {}


def _location(posting: dict[str, Any], names: dict[str, str]) -> str:
    ids = posting.get("locationIds") or {}
    order = [ids.get("primaryLocationId"), *(ids.get("secondaryLocationIds") or [])]
    places = [
        REGION_LABELS.get(names[i].strip(), names[i].strip())
        for i in order
        if i in names and names[i].strip()
    ]
    return "; ".join(dict.fromkeys(places)) or str(posting.get("locationName") or "")


def _fetch_description(job_id: str) -> str | None:
    try:
        root = decode_turbo_stream(_get(POSTING_URL.format(id=job_id)))
    except (requests.RequestException, ValueError):
        return None
    posting = _route_data(root, "$posting").get("jobPosting") or {}
    desc = posting.get("descriptionHtml")
    return normalize_description(desc, is_html=True) if desc else None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    try:
        root = decode_turbo_stream(_get(SEARCH_URL))
    except requests.HTTPError as e:
        raise AdapterError(f"Shopify HTTP {e.response.status_code} for {name}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Shopify network error for {name}: {e}") from e
    except ValueError as e:
        raise AdapterError(f"Shopify careers page payload unreadable for {name}") from e

    data = _route_data(root, "/careers")
    postings = data.get("jobPostingsWithJobs")
    if not postings:
        raise AdapterError(f"Shopify: no postings in careers page data for {name}")
    names = {
        loc["id"]: str(loc.get("externalName") or loc.get("name") or "")
        for loc in data.get("atsLocations") or []
        if isinstance(loc, dict) and loc.get("id")
    }

    jobs: list[Job] = []
    for item in postings:
        posting = (item or {}).get("jobPosting") or {}
        job_id = str(posting.get("id") or "")
        title = str(posting.get("title") or "").strip()
        if not job_id or not title:
            continue
        jobs.append(
            Job(
                id=job_id,
                company=company["name"],
                title=title,
                location=_location(posting, names),
                url=POSTING_URL.format(id=job_id),
                posted_at=posting.get("publishedDate"),
                department=posting.get("teamName") or posting.get("departmentName"),
                ats="shopify",
                category=company.get("category", "uncategorized"),
            )
        )

    # Most postings are remote "Americas", which only the description can
    # place in the US, so those are fetched even when the title is decisive.
    fetch_ids = [
        j.id
        for j in jobs
        if (should_fetch_description(j.title) or is_location_ambiguous(j.location))
        and could_be_included(j.title, j.location)
    ]
    descs = map_descriptions_parallel(fetch_ids, _fetch_description, max_workers=DETAIL_WORKERS)
    return [replace(j, description=descs.get(j.id)) for j in jobs]
