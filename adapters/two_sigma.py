"""Two Sigma careers adapter (Avature-backed careers.twosigma.com).

The OpenRoles page itself is a JS-driven search widget with no discoverable
public JSON API, but the same portal publishes a plain RSS feed of open
roles at /careers/OpenRoles/feed/. That feed caps out at the 20 most
recent postings (pagination params are silently ignored - verified they
return byte-identical output) - acceptable for a smaller-headcount firm,
but means very old/low-turnover postings can fall off the feed before this
scraper sees them.

Job descriptions require a separate per-job HTML page fetch, handled by
adapters.description_fetch.fetch_two_sigma_description.
"""

from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
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
    fetch_two_sigma_description,
    map_descriptions_parallel,
)
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

FEED_URL = "https://careers.twosigma.com/careers/OpenRoles/feed/"
DETAIL_WORKERS = 6

_ID_FROM_URL = re.compile(r"/(\d+)/?$")


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_feed() -> str:
    resp = requests.get(FEED_URL, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def _parse_feed(xml_text: str) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    if channel is None:
        return []
    items: list[dict[str, Any]] = []
    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or item.findtext("guid") or "").strip()
        location = (item.findtext("description") or "").strip()
        pub_date = item.findtext("pubDate")
        if not title or not link:
            continue
        items.append(
            {"title": title, "link": link, "location": location, "posted_at": pub_date}
        )
    return items


def fetch(company: dict[str, Any]) -> list[Job]:
    try:
        xml_text = _get_feed()
    except requests.HTTPError as e:
        code = e.response.status_code if e.response is not None else "?"
        raise AdapterError(f"Two Sigma HTTP {code}") from e
    except requests.RequestException as e:
        raise AdapterError(f"Two Sigma network error: {e}") from e
    except ET.ParseError as e:
        raise AdapterError(f"Two Sigma feed returned invalid XML: {e}") from e

    try:
        raw_jobs = _parse_feed(xml_text)
    except ET.ParseError as e:
        raise AdapterError(f"Two Sigma feed returned invalid XML: {e}") from e

    jobs: list[Job] = []
    for raw in raw_jobs:
        link = raw["link"]
        id_match = _ID_FROM_URL.search(link)
        job_id = id_match.group(1) if id_match else link
        jobs.append(
            Job(
                id=job_id,
                company=company["name"],
                title=raw["title"],
                location=raw["location"],
                url=link,
                posted_at=raw["posted_at"],
                department=None,
                description=None,
                ats="two_sigma",
                category=company.get("category", "uncategorized"),
            )
        )

    fetch_urls = [j.url for j in jobs if j.url and should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_urls:
        descs = map_descriptions_parallel(
            fetch_urls,
            fetch_two_sigma_description,
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.url) or j.description) for j in jobs]
    return jobs
