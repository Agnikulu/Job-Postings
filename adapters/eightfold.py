"""Eightfold AI careers adapter (Netflix and similar explore.jobs.* sites).

Endpoint: GET https://{host}/api/apply/v2/jobs?domain={domain}&batch=N&limit=10
"""

from __future__ import annotations

import logging
import time
from dataclasses import replace
from datetime import datetime, timezone
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.description_fetch import fetch_eightfold_description, map_descriptions_parallel

from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

DEFAULT_HOST = "explore.jobs.netflix.net"
DEFAULT_DOMAIN = "netflix.com"
BATCH_SIZE = 10
MAX_BATCHES = 200
BATCH_DELAY_SEC = 0.35
DETAIL_WORKERS = 6


@retry(
    reraise=True,
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_batch(host: str, domain: str, batch: int) -> dict[str, Any]:
    resp = requests.get(
        f"https://{host}/api/apply/v2/jobs",
        params={"domain": domain, "batch": batch, "limit": BATCH_SIZE},
        headers=DEFAULT_HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )
    if resp.status_code == 429:
        resp.raise_for_status()
    resp.raise_for_status()
    return resp.json()


def _epoch_to_iso(value: int | None) -> str | None:
    if not value:
        return None
    try:
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
    except (ValueError, OSError):
        return None


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    host = company.get("careers_host") or DEFAULT_HOST
    domain = company.get("domain") or company.get("slug") or DEFAULT_DOMAIN

    all_raw: list[dict[str, Any]] = []
    for batch in range(MAX_BATCHES):
        try:
            payload = _get_batch(host, domain, batch)
        except requests.HTTPError as e:
            raise AdapterError(
                f"Eightfold HTTP {e.response.status_code} for {name} batch {batch}"
            ) from e
        except requests.RequestException as e:
            raise AdapterError(f"Eightfold network error for {name}: {e}") from e
        except ValueError as e:
            raise AdapterError(f"Eightfold returned invalid JSON for {name}") from e

        page_jobs = payload.get("positions") or []
        all_raw.extend(page_jobs)
        total = payload.get("count") or 0
        if batch:
            time.sleep(BATCH_DELAY_SEC)
        if not page_jobs or (total and len(all_raw) >= total):
            break

    jobs: list[Job] = []
    for raw in all_raw:
        try:
            job_id = str(raw.get("id") or raw.get("display_job_id") or "")
            locs = raw.get("locations") or []
            location = raw.get("location") or " / ".join(str(x) for x in locs if x)
            url = raw.get("canonicalPositionUrl") or f"https://{host}/careers/job/{job_id}"
            jobs.append(
                Job(
                    id=job_id,
                    company=company["name"],
                    title=str(raw.get("name") or raw.get("posting_name") or "").strip(),
                    location=str(location or ""),
                    url=str(url),
                    posted_at=_epoch_to_iso(raw.get("t_update") or raw.get("t_create")),
                    department=raw.get("department"),
                    ats="eightfold",
                    category=company.get("category", "uncategorized"),
                )
            )
        except (KeyError, TypeError) as e:
            log.warning("Eightfold: skipping malformed job for %s: %s", name, e)
            continue

    if jobs:
        descs = map_descriptions_parallel(
            [j.id for j in jobs],
            lambda job_id: fetch_eightfold_description(host, domain, job_id),
            max_workers=DETAIL_WORKERS,
        )
        jobs = [replace(j, description=descs.get(j.id)) for j in jobs]
    return jobs
