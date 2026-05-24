"""Wiz careers adapter.

Wiz hosts Greenhouse postings behind a Next.js proxy API:
  GET https://www.wiz.io/api/fetch-jobs-data
  GET https://www.wiz.io/api/fetch-private-jobs-data (optional extra postings)
"""

from __future__ import annotations

import html
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

JOBS_URL = "https://www.wiz.io/api/fetch-jobs-data"
PRIVATE_JOBS_URL = "https://www.wiz.io/api/fetch-private-jobs-data"
_TITLE_SLUG_RE = re.compile(r"[^a-z0-9]+")


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_json(url: str) -> Any:
    resp = requests.get(url, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def _title_slug(title: str) -> str:
    return _TITLE_SLUG_RE.sub("-", title.lower()).strip("-") or "job"


def _job_url(raw: dict[str, Any]) -> str:
    apply_url = str(raw.get("applyUrl") or "").strip()
    title = str(raw.get("title") or "")
    if apply_url and ":title" in apply_url:
        return apply_url.replace(":title", _title_slug(title)).split("#")[0]
    job_id = str(raw.get("id") or "")
    if job_id:
        return (
            f"https://www.wiz.io/careers/job/{job_id}/{_title_slug(title)}"
            f"?gh_jid={job_id}"
        )
    return "https://www.wiz.io/careers"


def _parse_postings(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        postings = payload.get("allJobPostings")
        if isinstance(postings, list):
            return postings
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    return []


def _load_postings() -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for url in (JOBS_URL, PRIVATE_JOBS_URL):
        try:
            payload = _get_json(url)
        except requests.HTTPError as e:
            if url == JOBS_URL:
                raise
            log.warning("Wiz private jobs endpoint failed: %s", e)
            continue
        except requests.RequestException as e:
            if url == JOBS_URL:
                raise AdapterError(f"Wiz network error: {e}") from e
            log.warning("Wiz private jobs network error: %s", e)
            continue
        for raw in _parse_postings(payload):
            job_id = str(raw.get("id") or "")
            if job_id:
                merged[job_id] = raw
    return list(merged.values())


def fetch(company: dict[str, Any]) -> list[Job]:
    try:
        postings = _load_postings()
    except requests.HTTPError as e:
        raise AdapterError(f"Wiz HTTP {e.response.status_code}") from e
    except ValueError as e:
        raise AdapterError("Wiz returned invalid JSON") from e

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
            department = raw.get("team") or raw.get("department")
            jobs.append(
                Job(
                    id=str(raw.get("id") or title),
                    company=company["name"],
                    title=html.unescape(title),
                    location=str(raw.get("location") or "").strip(),
                    url=_job_url(raw),
                    posted_at=None,
                    department=str(department) if department else None,
                    ats="wiz",
                    category=company.get("category", "uncategorized"),
                    description=desc,
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Wiz: skipping malformed job: %s", e)
            continue
    return jobs
