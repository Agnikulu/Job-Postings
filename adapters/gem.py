"""Gem ATS public job-board GraphQL adapter.

Endpoint: POST https://jobs.gem.com/api/public/graphql
Used by Groq and other companies on jobs.gem.com/{slug}.
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

from adapters.description_fetch import fetch_gem_description, map_descriptions_parallel
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

GRAPHQL_URL = "https://jobs.gem.com/api/public/graphql"
DETAIL_WORKERS = 6
JOB_BOARD_QUERY = """
query JobBoardList($boardId: String!) {
  oatsExternalJobPostings(boardId: $boardId) {
    jobPostings {
      id
      extId
      title
      locations {
        id
        name
        city
        isoCountry
        isRemote
        extId
      }
      job {
        id
        department {
          id
          name
          extId
        }
        locationType
        employmentType
      }
    }
  }
}
"""


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _post(slug: str) -> dict[str, Any]:
    headers = {
        **DEFAULT_HEADERS,
        "Content-Type": "application/json",
        "Origin": "https://jobs.gem.com",
        "Referer": f"https://jobs.gem.com/{slug}",
    }
    resp = requests.post(
        GRAPHQL_URL,
        json={
            "operationName": "JobBoardList",
            "query": JOB_BOARD_QUERY,
            "variables": {"boardId": slug},
        },
        headers=headers,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _format_location(raw: dict[str, Any]) -> str:
    locs = raw.get("locations") or []
    parts: list[str] = []
    for loc in locs:
        if loc.get("isRemote"):
            parts.append("Remote")
            continue
        label = loc.get("name") or loc.get("city") or loc.get("isoCountry")
        if label:
            parts.append(str(label))
    return " / ".join(parts)


def fetch(company: dict[str, Any]) -> list[Job]:
    slug = company.get("slug")
    if not slug:
        raise AdapterError(f"Gem adapter requires 'slug' for {company.get('name')}")

    try:
        payload = _post(slug)
    except requests.HTTPError as e:
        raise AdapterError(
            f"Gem HTTP {e.response.status_code} for slug='{slug}'"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Gem network error for slug='{slug}': {e}") from e
    except ValueError as e:
        raise AdapterError(f"Gem returned invalid JSON for slug='{slug}'") from e

    if payload.get("errors"):
        msg = payload["errors"][0].get("message", "unknown GraphQL error")
        raise AdapterError(f"Gem GraphQL error for slug='{slug}': {msg}")

    postings = (
        payload.get("data", {})
        .get("oatsExternalJobPostings", {})
        .get("jobPostings")
        or []
    )

    jobs: list[Job] = []
    for raw in postings:
        try:
            ext_id = raw.get("extId") or raw.get("id")
            dept = (raw.get("job") or {}).get("department") or {}
            jobs.append(
                Job(
                    id=str(ext_id),
                    company=company["name"],
                    title=str(raw.get("title", "")).strip(),
                    location=_format_location(raw),
                    url=f"https://jobs.gem.com/{slug}/{ext_id}",
                    posted_at=None,
                    department=dept.get("name"),
                    ats="gem",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Gem: skipping malformed job for %s: %s", slug, e)
            continue

    fetch_ids = [j.id for j in jobs if should_fetch_description(j.title)]
    descs: dict[str, str | None] = {}
    if fetch_ids:
        descs = map_descriptions_parallel(
            fetch_ids,
            lambda ext_id: fetch_gem_description(slug, ext_id),
            max_workers=DETAIL_WORKERS,
        )
    jobs = [replace(j, description=descs.get(j.id)) for j in jobs]
    return jobs
