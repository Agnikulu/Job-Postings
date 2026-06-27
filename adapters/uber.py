"""Uber careers adapter (undocumented public POST API).

Flow:
  1. GET  https://www.uber.com/us/en/careers/list/  (establish session + CSRF)
  2. POST https://www.uber.com/api/loadSearchJobsResults?localeCode={locale}
"""

from __future__ import annotations

import logging
import re
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from text_util import normalize_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

CAREERS_URL = "https://www.uber.com/us/en/careers/list/"
SEARCH_URL = "https://www.uber.com/api/loadSearchJobsResults"
JOB_URL = "https://www.uber.com/careers/list/{job_id}"
_CSRF_RE = re.compile(r'"csrfToken"\s*:\s*"([^"]+)"')


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _fetch_results(locale: str) -> list[dict[str, Any]]:
    session = requests.Session()
    session.headers.update({**DEFAULT_HEADERS, "Accept": "text/html,application/json"})

    page = session.get(CAREERS_URL, timeout=DEFAULT_TIMEOUT)
    page.raise_for_status()

    csrf = "x"
    match = _CSRF_RE.search(page.text)
    if match:
        csrf = match.group(1)

    headers = {
        **DEFAULT_HEADERS,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://www.uber.com",
        "Referer": CAREERS_URL,
        "X-Csrf-Token": csrf,
        "x-csrf-token": csrf,
    }
    resp = session.post(
        f"{SEARCH_URL}?localeCode={locale}",
        json={},
        headers=headers,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("status") != "success":
        raise AdapterError(f"Uber search API returned status={payload.get('status')!r}")
    return payload.get("data", {}).get("results") or []


def _format_location(raw: dict[str, Any]) -> str:
    all_locs = raw.get("allLocations") or []
    if all_locs:
        parts: list[str] = []
        for loc in all_locs:
            if not isinstance(loc, dict):
                continue
            bits = [loc.get("city"), loc.get("region"), loc.get("countryName")]
            label = ", ".join(b for b in bits if b)
            if label:
                parts.append(label)
        if parts:
            return " / ".join(parts)

    loc = raw.get("location") or {}
    if not isinstance(loc, dict):
        return str(loc)
    bits = [loc.get("city"), loc.get("region"), loc.get("countryName")]
    return ", ".join(b for b in bits if b)


def fetch(company: dict[str, Any]) -> list[Job]:
    locale = company.get("locale", "en")

    try:
        raw_jobs = _fetch_results(locale)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Uber HTTP {e.response.status_code} for locale='{locale}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Uber network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Uber returned invalid JSON") from e

    jobs: list[Job] = []
    for raw in raw_jobs:
        try:
            job_id = raw["id"]
            jobs.append(
                Job(
                    id=str(job_id),
                    company=company["name"],
                    title=str(raw.get("title", "")).strip(),
                    location=_format_location(raw),
                    url=JOB_URL.format(job_id=job_id),
                    posted_at=raw.get("creationDate") or raw.get("updatedDate"),
                    department=raw.get("department"),
                    description=normalize_description(raw.get("description")),
                    ats="uber",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Uber: skipping malformed job: %s", e)
            continue
    return jobs
