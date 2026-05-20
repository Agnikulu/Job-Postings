"""Workday CXS adapter (paginated POST).

Endpoint: POST https://{tenant}.{wd_pod}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs
Body:     {"appliedFacets": {}, "limit": 20, "offset": N, "searchText": ""}

Notes
-----
- The 'wd_pod' (e.g. wd1, wd3, wd5) is visible in the public careers URL.
- This is an undocumented but de-facto public endpoint used by every Workday
  career site. It returns JSON when Accept: application/json is sent.
- Stops paginating when the page returns fewer than `limit` postings or
  after MAX_PAGES (a hard safety cap).
"""

from __future__ import annotations

import logging
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

BASE_URL = (
    "https://{tenant}.{wd_pod}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs"
)
PAGE_SIZE = 20
MAX_PAGES = 50  # 1000 postings max per company — generous safety net


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _post_page(url: str, offset: int) -> dict[str, Any]:
    headers = {**DEFAULT_HEADERS, "Content-Type": "application/json"}
    resp = requests.post(
        url,
        json={
            "appliedFacets": {},
            "limit": PAGE_SIZE,
            "offset": offset,
            "searchText": "",
        },
        headers=headers,
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    tenant = company.get("tenant")
    wd_pod = company.get("wd_pod")
    site = company.get("site")
    if not (tenant and wd_pod and site):
        raise AdapterError(
            f"Workday adapter requires 'tenant', 'wd_pod', and 'site' for {name}"
        )

    url = BASE_URL.format(tenant=tenant, wd_pod=wd_pod, site=site)
    site_base = f"https://{tenant}.{wd_pod}.myworkdayjobs.com/en-US/{site}"

    all_raw: list[dict[str, Any]] = []
    for page in range(MAX_PAGES):
        offset = page * PAGE_SIZE
        try:
            payload = _post_page(url, offset)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Workday HTTP {e.response.status_code} for {name} at offset {offset}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Workday network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Workday returned invalid JSON for {name}") from e

        page_jobs = payload.get("jobPostings") or []
        all_raw.extend(page_jobs)
        if len(page_jobs) < PAGE_SIZE:
            break

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            external_path = raw.get("externalPath", "")
            url_full = f"{site_base}{external_path}" if external_path else ""
            # Workday's "externalPath" looks like "/job/.../R-12345" — last
            # component is a usable id; fall back to bulletFields if missing.
            job_id = external_path.rsplit("/", 1)[-1] if external_path else raw.get(
                "title", ""
            )
            jobs.append(
                Job(
                    id=str(job_id),
                    company=company["name"],
                    title=raw.get("title", "").strip(),
                    location=raw.get("locationsText", "") or "",
                    url=url_full,
                    posted_at=raw.get("postedOn"),
                    department=None,  # Workday cxs response doesn't expose dept
                    ats="workday",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Workday: skipping malformed job for %s: %s", name, e)
            continue
    return jobs
