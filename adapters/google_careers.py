"""Google Careers adapter (careers.google.com HTML embedded data).

Parses AF_initDataCallback payloads from the public job search results pages.
Supports optional company filter via the `google_company` yaml field.
"""

from __future__ import annotations

import json
import logging
import re
from datetime import datetime, timezone
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_google_description, map_descriptions_parallel
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

RESULTS_URL = "https://www.google.com/about/careers/applications/jobs/results/"
_DATA_RE = re.compile(
    r"AF_initDataCallback\(\{key:\s*'ds:1',\s*hash:\s*'\d+',\s*data:(.*?),\s*sideChannel:",
    re.DOTALL,
)
MAX_PAGES = 200
DETAIL_WORKERS = 8


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_page(page: int, extra_params: dict[str, str]) -> list[list[Any]]:
    params = {"page": page, **extra_params}
    headers = {**DEFAULT_HEADERS, "Accept": "text/html,application/json,*/*"}
    resp = requests.get(RESULTS_URL, params=params, headers=headers, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    match = _DATA_RE.search(resp.text)
    if not match:
        return []
    data = json.loads(match.group(1))
    if not isinstance(data, list) or not data or not data[0]:
        return []
    return data[0]


def _format_locations(raw_locations: Any) -> str:
    if not isinstance(raw_locations, list):
        return ""
    labels: list[str] = []
    for entry in raw_locations:
        if isinstance(entry, list) and entry:
            label = entry[0]
            if isinstance(label, str) and label:
                labels.append(label)
    return " / ".join(labels)


def _epoch_pair_to_iso(value: Any) -> str | None:
    if not isinstance(value, list) or not value:
        return None
    try:
        seconds = int(value[0])
        return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()
    except (ValueError, OSError, TypeError):
        return None


def _normalize_url(job_id: str, raw_url: str) -> str:
    canonical = (
        "https://www.google.com/about/careers/applications/jobs/results/"
        f"{job_id}"
    )
    if raw_url and raw_url.startswith("http") and "signin" not in raw_url.lower():
        return raw_url
    return canonical


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    extra: dict[str, str] = {}
    google_company = company.get("google_company")
    if google_company:
        extra["company"] = google_company

    all_raw: list[list[Any]] = []
    for page in range(1, MAX_PAGES + 1):
        try:
            page_jobs = _get_page(page, extra)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Google Careers HTTP {e.response.status_code} for {name} page {page}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Google Careers network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Google Careers returned invalid JSON for {name}") from e

        if not page_jobs:
            break
        all_raw.extend(page_jobs)

    jobs: list[Job] = []
    job_ids: list[str] = []
    for item in all_raw:
        try:
            if not isinstance(item, list) or len(item) < 3:
                continue
            job_id = str(item[0])
            if not job_id.isdigit():
                continue
            title = str(item[1] or "").strip()
            url = _normalize_url(job_id, str(item[2] or ""))
            location = _format_locations(item[9] if len(item) > 9 else None)
            posted_at = _epoch_pair_to_iso(item[12] if len(item) > 12 else None)
            employer = str(item[7] or "") if len(item) > 7 else ""
            job_ids.append(job_id)
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=title,
                    location=location,
                    url=url,
                    posted_at=posted_at,
                    department=employer or None,
                    ats="google_careers",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError, IndexError) as e:
            log.warning("Google Careers: skipping malformed job for %s: %s", name, e)
            continue

    fetch_ids = [j.id for j in jobs if should_fetch_description(j.title)]
    if fetch_ids:
        descriptions = map_descriptions_parallel(
            fetch_ids,
            fetch_google_description,
            max_workers=DETAIL_WORKERS,
        )
        enriched: list[Job] = []
        for job in jobs:
            desc = descriptions.get(job.id)
            if desc:
                enriched.append(
                    Job(
                        id=job.id,
                        company=job.company,
                        title=job.title,
                        location=job.location,
                        url=job.url,
                        posted_at=job.posted_at,
                        department=job.department,
                        ats=job.ats,
                        category=job.category,
                        description=desc,
                    )
                )
            else:
                enriched.append(job)
        return enriched
    return jobs
