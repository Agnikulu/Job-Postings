"""Coinbase careers adapter.

Coinbase's careers site loads listings from:
  GET https://www.coinbase.com/api/v2/careers
with CoinbaseWeb client headers (see c_CzZwNKtm.js). Individual roles:
  GET https://www.coinbase.com/api/v2/careers/{offerId}

The developer-platform board still references Greenhouse slug ``cdpjobs`` as a
fallback when the careers API is unavailable.
"""

from __future__ import annotations

import html
import logging
import uuid
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from text_util import normalize_description

from .base import DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

CAREERS_URL = "https://www.coinbase.com/api/v2/careers"
GH_LIST_URL = "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true"
DEFAULT_GH_SLUG = "cdpjobs"
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _coinbase_headers() -> dict[str, str]:
    return {
        "User-Agent": BROWSER_UA,
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "CB-CLIENT": "CoinbaseWeb",
        "cb-version": "2021-01-11",
        "Referer": "https://www.coinbase.com/careers/positions",
        "Origin": "https://www.coinbase.com",
        "X-Device-TimeZone": "America/Los_Angeles",
        "x-timezone-offset": "420",
        "cf-ipcountry": "US",
        "X-CB-Device-ID": str(uuid.uuid4()),
        "X-CB-User-ID": "unknown",
        "X-CB-Is-Logged-In": "false",
        "X-CB-Pagekey": "careers_positions",
        "X-CB-Platform": "web",
        "X-CB-Project-Name": "consumer",
        "X-CB-Session-UUID": str(uuid.uuid4()),
        "X-CB-Version-Name": "unknown",
    }


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_json(url: str, headers: dict[str, str]) -> Any:
    resp = requests.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def _location_name(raw: dict[str, Any]) -> str:
    location = raw.get("location")
    if isinstance(location, dict):
        return str(location.get("name") or "").strip()
    if location:
        return str(location).strip()
    offices = raw.get("offices") or []
    if offices and isinstance(offices[0], dict):
        return str(offices[0].get("name") or "").strip()
    return ""


def _department_name(raw: dict[str, Any], fallback: str | None = None) -> str | None:
    departments = raw.get("departments") or []
    if departments and isinstance(departments[0], dict):
        name = departments[0].get("name")
        if name:
            return str(name)
    if raw.get("department"):
        return str(raw["department"])
    return fallback


def _job_url(raw: dict[str, Any]) -> str:
    absolute = str(raw.get("absolute_url") or "").strip()
    if absolute:
        return absolute
    job_id = str(raw.get("id") or "").strip()
    if job_id:
        return f"https://www.coinbase.com/careers/positions/{job_id}"
    return "https://www.coinbase.com/careers/positions"


def _parse_careers_api(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict):
        return []
    data = payload.get("data")
    if not isinstance(data, dict):
        return []
    departments = data.get("departments")
    if not isinstance(departments, list):
        return []
    postings: list[dict[str, Any]] = []
    for dept in departments:
        if not isinstance(dept, dict):
            continue
        dept_name = str(dept.get("name") or "")
        jobs = dept.get("jobs")
        if not isinstance(jobs, list):
            continue
        for raw in jobs:
            if isinstance(raw, dict):
                if dept_name and not _department_name(raw):
                    raw = {**raw, "department": dept_name}
                postings.append(raw)
    return postings


def _parse_greenhouse(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        jobs = payload.get("jobs")
        if isinstance(jobs, list):
            return [j for j in jobs if isinstance(j, dict)]
    return []


def _load_postings(gh_slug: str) -> list[dict[str, Any]]:
    headers = _coinbase_headers()
    try:
        payload = _get_json(CAREERS_URL, headers)
        postings = _parse_careers_api(payload)
        if postings:
            return postings
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code not in (400, 404):
            raise AdapterError(f"Coinbase careers HTTP {e.response.status_code}") from e
        log.warning("Coinbase careers API unavailable (%s); trying Greenhouse", e)
    except requests.RequestException as e:
        raise AdapterError(f"Coinbase network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Coinbase careers API returned invalid JSON") from e

    gh_url = GH_LIST_URL.format(slug=gh_slug)
    try:
        gh_payload = _get_json(gh_url, headers)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Coinbase careers and Greenhouse both failed (GH {e.response.status_code})"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Coinbase Greenhouse network error: {e}") from e
    except ValueError as e:
        raise AdapterError("Coinbase Greenhouse returned invalid JSON") from e

    postings = _parse_greenhouse(gh_payload)
    if not postings:
        raise AdapterError(
            "Coinbase careers API returned no jobs and Greenhouse board is empty"
        )
    return postings


def fetch(company: dict[str, Any]) -> list[Job]:
    gh_slug = str(
        company.get("greenhouse_slug")
        or company.get("slug")
        or DEFAULT_GH_SLUG
    )
    postings = _load_postings(gh_slug)

    jobs: list[Job] = []
    for raw in postings:
        try:
            title = str(raw.get("title") or "").strip()
            if not title:
                continue
            content = raw.get("content")
            desc = (
                normalize_description(str(content), is_html=True)
                if content and str(content).strip()
                else None
            )
            jobs.append(
                Job(
                    id=str(raw.get("id") or title),
                    company=company["name"],
                    title=html.unescape(title),
                    location=_location_name(raw),
                    url=_job_url(raw),
                    posted_at=raw.get("updated_at") or raw.get("first_published"),
                    department=_department_name(raw),
                    ats="coinbase",
                    category=company.get("category", "uncategorized"),
                    description=desc,
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Coinbase: skipping malformed job: %s", e)
            continue
    return jobs
