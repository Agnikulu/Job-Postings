"""Helpers for fetching job descriptions from detail endpoints."""

from __future__ import annotations

import json
import logging
import re
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
def _get_json(url: str, *, referer: str | None = None) -> dict[str, Any]:
    headers = {**DEFAULT_HEADERS, "Accept": "application/json"}
    if referer:
        headers["Referer"] = referer
    resp = requests.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
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
    headers = {**DEFAULT_HEADERS, "Accept": "text/html,application/json,*/*"}
    if referer:
        headers["Referer"] = referer
    resp = requests.get(url, headers=headers, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def fetch_workday_description(cxs_base: str, external_path: str) -> str | None:
    if not external_path:
        return None
    payload = _get_json(f"{cxs_base}{external_path}")
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
