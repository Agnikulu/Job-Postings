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
- Workday lists at most LIST_CAP (2000) postings per query; past that offset
  it wraps back to page 1. Boards at the cap are re-fetched one facet value
  at a time (e.g. per job family) and merged.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_workday_description, map_descriptions_parallel
from fetch_limits import max_list_pages
from filters import should_fetch_description

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .http_util import http_session

log = logging.getLogger(__name__)

DEFAULT_WD_HOST = "myworkdayjobs.com"
BASE_URL = "https://{tenant}.{wd_pod}.{wd_host}/wday/cxs/{tenant}/{site}/jobs"
PAGE_SIZE = 20
# Workday never lists past offset 2000 (it reports total=2000 and wraps).
LIST_CAP = 2000
MAX_PAGES = LIST_CAP // PAGE_SIZE
# Facets tried, in order, to split a board that hits LIST_CAP.
SPLIT_FACETS = ("jobFamilyGroup", "jobFamily", "workerSubType")
DETAIL_WORKERS = 6
DETAIL_DELAY_SEC = 0.02


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.RequestException),
)
def _post_page(
    session: requests.Session,
    url: str,
    offset: int,
    facets: dict[str, list[str]] | None = None,
) -> dict[str, Any]:
    resp = session.post(
        url,
        json={
            "appliedFacets": facets or {},
            "limit": PAGE_SIZE,
            "offset": offset,
            "searchText": "",
        },
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _workday_endpoints(company: dict[str, Any]) -> tuple[str, str, str]:
    """Return (jobs_post_url, public_site_base, cxs_base)."""
    tenant = company["tenant"]
    site = company["site"]
    cxs_host = (company.get("workday_cxs_host") or "").strip()
    if cxs_host:
        jobs_url = f"https://{cxs_host}/wday/cxs/{tenant}/{site}/jobs"
        cxs_base = f"https://{cxs_host}/wday/cxs/{tenant}/{site}"
        public_base = (company.get("workday_public_base") or "").strip()
        site_base = public_base or f"https://{cxs_host}/en-US/{site}"
        return jobs_url, site_base, cxs_base

    wd_pod = company["wd_pod"]
    wd_host = company.get("workday_wd_host") or DEFAULT_WD_HOST
    jobs_url = BASE_URL.format(
        tenant=tenant, wd_pod=wd_pod, site=site, wd_host=wd_host
    )
    site_base = f"https://{tenant}.{wd_pod}.{wd_host}/en-US/{site}"
    cxs_base = f"https://{tenant}.{wd_pod}.{wd_host}/wday/cxs/{tenant}/{site}"
    return jobs_url, site_base, cxs_base


def _list_postings(
    session: requests.Session,
    url: str,
    name: str,
    facets: dict[str, list[str]] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Page through one query; return (postings, first page payload)."""
    all_raw: list[dict[str, Any]] = []
    first: dict[str, Any] = {}
    for page in range(max_list_pages(MAX_PAGES)):
        offset = page * PAGE_SIZE
        try:
            payload = _post_page(session, url, offset, facets)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Workday HTTP {e.response.status_code} for {name} at offset {offset}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Workday network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Workday returned invalid JSON for {name}") from e

        if not page:
            first = payload
        page_jobs = payload.get("jobPostings") or []
        all_raw.extend(page_jobs)
        if len(page_jobs) < PAGE_SIZE:
            break
    return all_raw, first


def _list_split_by_facet(
    session: requests.Session,
    url: str,
    name: str,
    first: dict[str, Any],
    capped: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Re-list a board at LIST_CAP one facet value at a time, merged with the
    capped unfiltered list (which covers postings missing that facet)."""
    by_param = {f.get("facetParameter"): f for f in first.get("facets") or []}
    for param in SPLIT_FACETS:
        values = [
            v for v in (by_param.get(param) or {}).get("values") or []
            if v.get("id") and v.get("count")
        ]
        if values:
            break
    else:
        log.warning("Workday %s: at the %d listing cap and no facet to split on", name, LIST_CAP)
        return capped

    merged: dict[str, dict[str, Any]] = {}
    for raw in capped:
        merged.setdefault(raw.get("externalPath") or raw.get("title", ""), raw)
    for value in values:
        if value["count"] >= LIST_CAP:
            log.warning(
                "Workday %s: %s=%s has %d postings; listing capped at %d",
                name, param, value.get("descriptor"), value["count"], LIST_CAP,
            )
        rows, _ = _list_postings(session, url, name, {param: [value["id"]]})
        for raw in rows:
            merged.setdefault(raw.get("externalPath") or raw.get("title", ""), raw)
    log.info(
        "Workday %s: split by %s into %d queries -> %d postings",
        name, param, len(values), len(merged),
    )
    return list(merged.values())


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    tenant = company.get("tenant")
    wd_pod = company.get("wd_pod")
    site = company.get("site")
    cxs_host = (company.get("workday_cxs_host") or "").strip()
    if not (tenant and site):
        raise AdapterError(
            f"Workday adapter requires 'tenant' and 'site' for {name}"
        )
    if not cxs_host and not wd_pod:
        raise AdapterError(
            f"Workday adapter requires 'wd_pod' for {name} (or set workday_cxs_host)"
        )

    url, site_base, cxs_base = _workday_endpoints(company)

    list_headers = {**DEFAULT_HEADERS, "Content-Type": "application/json"}
    with http_session(list_headers) as session:
        all_raw, first = _list_postings(session, url, name)
        if int(first.get("total") or 0) >= LIST_CAP:
            all_raw = _list_split_by_facet(session, url, name, first, all_raw)

    jobs: list[Job] = []
    descriptions: dict[str, str | None] = {}
    paths_by_id: dict[str, str] = {}
    for raw in all_raw:
        try:
            external_path = raw.get("externalPath", "")
            url_full = f"{site_base}{external_path}" if external_path else ""
            job_id = external_path.rsplit("/", 1)[-1] if external_path else raw.get(
                "title", ""
            )
            job_id = str(job_id)
            if external_path:
                paths_by_id[job_id] = external_path
            jobs.append(
                Job(
                    id=job_id,
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

    paths_to_fetch = [
        paths_by_id[j.id]
        for j in jobs
        if j.id in paths_by_id and should_fetch_description(j.title)
    ]
    if paths_to_fetch:
        def _fetch(path: str) -> str | None:
            if DETAIL_DELAY_SEC:
                time.sleep(DETAIL_DELAY_SEC)
            return fetch_workday_description(cxs_base, path)

        descriptions = map_descriptions_parallel(
            paths_to_fetch,
            _fetch,
            max_workers=DETAIL_WORKERS,
        )

    if descriptions:
        enriched: list[Job] = []
        for job in jobs:
            path = paths_by_id.get(job.id)
            desc = descriptions.get(path) if path else None
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
