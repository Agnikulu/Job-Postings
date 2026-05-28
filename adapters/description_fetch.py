"""Helpers for fetching job descriptions from detail endpoints."""

from __future__ import annotations

import json
import logging
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, TypeVar

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from adapters.base import DEFAULT_HEADERS, DEFAULT_TIMEOUT
from text_util import normalize_description

log = logging.getLogger(__name__)

K = TypeVar("K")
V = TypeVar("V")

_thread_local = threading.local()


def _json_session() -> requests.Session:
    session = getattr(_thread_local, "json_session", None)
    if session is None:
        session = requests.Session()
        session.headers.update({**DEFAULT_HEADERS, "Accept": "application/json"})
        _thread_local.json_session = session
    return session


def _html_session() -> requests.Session:
    session = getattr(_thread_local, "html_session", None)
    if session is None:
        session = requests.Session()
        session.headers.update({**DEFAULT_HEADERS, "Accept": "text/html,application/json,*/*"})
        _thread_local.html_session = session
    return session

_GOOGLE_DETAIL_DS0 = re.compile(
    r"AF_initDataCallback\(\{key:\s*'ds:0',\s*hash:\s*'\d+',\s*data:(.*?),\s*sideChannel:",
    re.DOTALL,
)
_MS_DESCRIPTION = re.compile(r'"description"\s*:\s*"((?:\\.|[^"\\])*)"', re.DOTALL)


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_json(
    url: str,
    *,
    referer: str | None = None,
    timeout: float = DEFAULT_TIMEOUT,
) -> dict[str, Any]:
    session = _json_session()
    headers: dict[str, str] = {}
    if referer:
        headers["Referer"] = referer
    resp = session.get(url, headers=headers or None, timeout=timeout)
    resp.raise_for_status()
    payload = resp.json()
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object from {url}")
    return payload


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type(requests.RequestException),
)
def _get_html(url: str, *, referer: str | None = None) -> str:
    session = _html_session()
    headers: dict[str, str] = {}
    if referer:
        headers["Referer"] = referer
    resp = session.get(url, headers=headers or None, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


WORKDAY_DETAIL_TIMEOUT = 35


def fetch_workday_description(cxs_base: str, external_path: str) -> str | None:
    if not external_path:
        return None
    payload = _get_json(
        f"{cxs_base}{external_path}",
        timeout=WORKDAY_DETAIL_TIMEOUT,
    )
    raw = (payload.get("jobPostingInfo") or {}).get("jobDescription")
    return normalize_description(raw, is_html=True)


def extract_google_description(html: str) -> str | None:
    match = _GOOGLE_DETAIL_DS0.search(html)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except ValueError:
        return None
    return _collect_google_html(data)


def fetch_google_description(job_id: str) -> str | None:
    url = (
        "https://www.google.com/about/careers/applications/jobs/results/"
        f"{job_id}"
    )
    html = _get_html(url)
    raw = extract_google_description(html)
    return normalize_description(raw, is_html=True)


def extract_microsoft_description(html: str) -> str | None:
    decoded: list[str] = []
    for match in _MS_DESCRIPTION.findall(html):
        try:
            text = json.loads(f'"{match}"')
        except ValueError:
            continue
        if len(text) > 80:
            decoded.append(text)
    if not decoded:
        return None
    return max(decoded, key=len)


def fetch_microsoft_description(job_id: str, *, base_url: str) -> str | None:
    url = f"{base_url}/careers/job/{job_id}"
    html = _get_html(url, referer=f"{base_url}/careers")
    raw = extract_microsoft_description(html)
    return normalize_description(raw)


def fetch_gem_description(slug: str, ext_id: str) -> str | None:
    """Gem detail page is a SPA; description comes from ExternalJobPostingQuery."""
    headers = {
        **DEFAULT_HEADERS,
        "Content-Type": "application/json",
        "Origin": "https://jobs.gem.com",
        "Referer": f"https://jobs.gem.com/{slug}/{ext_id}",
    }
    query = """
    query ExternalJobPostingQuery($boardId: String!, $extId: String!) {
      oatsExternalJobPosting(boardId: $boardId, extId: $extId) {
        descriptionHtml
      }
    }
    """
    try:
        resp = requests.post(
            "https://jobs.gem.com/api/public/graphql",
            json={
                "operationName": "ExternalJobPostingQuery",
                "query": query,
                "variables": {"boardId": slug, "extId": ext_id},
            },
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        payload = resp.json()
    except Exception:
        return None
    if payload.get("errors"):
        return None
    raw = (
        payload.get("data", {})
        .get("oatsExternalJobPosting", {})
        .get("descriptionHtml")
    )
    return normalize_description(raw, is_html=True)


def fetch_workable_description(slug: str, shortcode: str) -> str | None:
    url = f"https://apply.workable.com/api/v2/accounts/{slug}/jobs/{shortcode}"
    try:
        payload = _get_json(url, referer=f"https://apply.workable.com/{slug}/")
    except Exception:
        # Legacy v1 fallback for older boards.
        try:
            payload = _get_json(
                f"https://apply.workable.com/api/v1/jobs/{shortcode}",
                referer=f"https://apply.workable.com/{slug}/",
            )
        except Exception:
            return None
    parts = [
        payload.get("description") or payload.get("full_description"),
        payload.get("requirements"),
    ]
    raw = "\n\n".join(p for p in parts if p and str(p).strip())
    return normalize_description(raw, is_html=True)


def fetch_linkedin_description(job_id: str) -> str | None:
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
    try:
        html = _get_html(url)
    except Exception:
        return None
    match = re.search(
        r"<div class=\"show-more-less-html__markup[^\"]*\"[^>]*>(.*?)</div>",
        html,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return None
    return normalize_description(match.group(1), is_html=True)


def fetch_eightfold_description(host: str, domain: str, job_id: str) -> str | None:
    url = f"https://{host}/api/apply/v2/jobs/{job_id}?domain={domain}"
    try:
        payload = _get_json(url, referer=f"https://{host}/careers")
    except Exception:
        return None
    raw = payload.get("job_description") or payload.get("description")
    return normalize_description(raw, is_html=True)


def fetch_jibe_description(host: str, req_id: str) -> str | None:
    url = f"https://{host}/api/jobs/{req_id}"
    try:
        payload = _get_json(url)
    except Exception:
        return None
    data = payload.get("data") or payload
    raw = data.get("description") or data.get("job_description")
    return normalize_description(raw, is_html=True)


def fetch_apple_description(job_id: str, slug: str) -> str | None:
    url = f"https://jobs.apple.com/api/v1/jobDetails/{job_id}"
    headers = {
        **DEFAULT_HEADERS,
        "Accept": "application/json",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    }
    try:
        resp = requests.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
        resp.raise_for_status()
        payload = resp.json()
    except Exception:
        return None
    detail = payload.get("res") or payload
    if not isinstance(detail, dict):
        return None
    parts = [
        detail.get("jobSummary"),
        detail.get("description"),
        detail.get("minimumQualifications"),
        detail.get("preferredQualifications"),
    ]
    raw = "\n\n".join(p for p in parts if p and str(p).strip())
    return normalize_description(raw)


def fetch_rippling_description(job_url: str) -> str | None:
    if not job_url:
        return None
    try:
        html = _get_html(job_url)
    except Exception:
        return None
    match = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>',
        html,
        re.DOTALL,
    )
    if not match:
        return None
    try:
        payload = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    api_data = payload.get("props", {}).get("pageProps", {}).get("apiData") or {}
    job_post = api_data.get("jobPost") or {}
    raw = job_post.get("description") or job_post.get("descriptionHtml")
    if isinstance(raw, dict):
        raw = "\n\n".join(
            str(v) for v in (raw.get("role"), raw.get("company")) if v and str(v).strip()
        )
    if not raw:
        job = payload.get("props", {}).get("pageProps", {}).get("job") or {}
        raw = job.get("description") or job.get("descriptionHtml")
    return normalize_description(raw, is_html=True)


def _collect_google_html(data: Any) -> str | None:
    parts: list[str] = []
    seen: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, str):
            if len(obj) < 40:
                return
            low = obj.lower()
            if "<" in obj or any(
                token in low
                for token in (
                    "minimum qualification",
                    "preferred qualification",
                    "about the job",
                    "qualification",
                )
            ):
                if obj not in seen:
                    seen.add(obj)
                    parts.append(obj)
        elif isinstance(obj, list):
            for entry in obj:
                walk(entry)
        elif isinstance(obj, dict):
            for entry in obj.values():
                walk(entry)

    walk(data)
    if not parts:
        return None
    return "\n\n".join(parts)


def map_descriptions_parallel(
    keys: list[K],
    fetch_one: Callable[[K], V | None],
    *,
    max_workers: int = 8,
    delay_sec: float = 0.0,
) -> dict[K, V | None]:
    """Fetch descriptions concurrently; failures become None."""
    if not keys:
        return {}
    if max_workers <= 1:
        return {key: fetch_one(key) for key in keys}

    out: dict[K, V | None] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fetch_one, key): key for key in keys}
        for future in as_completed(futures):
            key = futures[future]
            try:
                out[key] = future.result()
            except Exception as exc:
                log.debug("Description fetch failed for %r: %s", key, exc)
                out[key] = None
            if delay_sec:
                time.sleep(delay_sec)
    return out
