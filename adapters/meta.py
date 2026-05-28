"""Meta careers adapter (metacareers.com sitemap + job detail pages).

Uses the public jobs sitemap for IDs/URLs and og:title meta tags for titles.
Uncached jobs are fetched slowly with 429 backoff; titles persist in
meta_title_cache.json so hourly runs only hit new postings.
"""

from __future__ import annotations

import json
import logging
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import requests
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from . import linkedin as linkedin_adapter
from .base import DEFAULT_TIMEOUT, AdapterError, Job

log = logging.getLogger(__name__)

SITEMAP_URL = "https://www.metacareers.com/jobs/sitemap.xml"
CACHE_PATH = Path(__file__).resolve().parent.parent / "meta_title_cache.json"
STATE_PATH = Path(__file__).resolve().parent.parent / "meta_careers_state.json"
_OG_TITLE_RE = re.compile(r'<meta property="og:title" content="([^"]+)"')
_DETAIL_DELAY_SEC = 0.85
_BATCH_SIZE = 20
_BATCH_PAUSE_SEC = 8.0
_MAX_DETAIL_ATTEMPTS = 8


def _browser_headers() -> dict[str, str]:
    # Do not merge DEFAULT_HEADERS — metacareers rejects the bot User-Agent.
    return {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        ),
    }


def _detail_headers() -> dict[str, str]:
    return _browser_headers()


def _retryable_request_error(exc: BaseException) -> bool:
    if isinstance(exc, requests.HTTPError):
        return exc.response.status_code in {429, 500, 502, 503}
    return isinstance(exc, requests.RequestException)


def _blocked_status(exc: BaseException) -> int | None:
    if isinstance(exc, requests.HTTPError) and exc.response is not None:
        return exc.response.status_code
    return None


def _fetch_linkedin_fallback(company: dict[str, Any]) -> list[Job]:
    company_id = company.get("linkedin_company_id")
    if not company_id:
        raise AdapterError(
            f"Meta metacareers blocked and no linkedin_company_id for {company.get('name', '?')}"
        )
    log.warning(
        "Meta: metacareers unreachable; using LinkedIn company %s",
        company_id,
    )
    li_company = {**company, "ats": "linkedin"}
    return linkedin_adapter.fetch(li_company)


def _load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}
    try:
        payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def _load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {}
    try:
        payload = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _save_state(state: dict[str, Any]) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def _sitemap_blocked() -> bool:
    return bool(_load_state().get("sitemap_blocked"))


def _mark_sitemap_blocked() -> None:
    state = _load_state()
    if state.get("sitemap_blocked"):
        return
    state["sitemap_blocked"] = True
    _save_state(state)


def _clear_sitemap_blocked() -> None:
    state = _load_state()
    if not state.get("sitemap_blocked"):
        return
    state.pop("sitemap_blocked", None)
    _save_state(state)


@retry(
    reraise=True,
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception(_retryable_request_error),
)
def _get_sitemap_entries() -> list[tuple[str, str | None]]:
    session = requests.Session()
    session.headers.update(_browser_headers())
    # Warm session cookies; some edges require a prior /jobs visit.
    session.get("https://www.metacareers.com/jobs", timeout=DEFAULT_TIMEOUT)
    resp = session.get(SITEMAP_URL, timeout=DEFAULT_TIMEOUT)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries: list[tuple[str, str | None]] = []
    for url_node in root.findall(".//sm:url", ns):
        loc = url_node.find("sm:loc", ns)
        if loc is None or not loc.text:
            continue
        lastmod_node = url_node.find("sm:lastmod", ns)
        lastmod = lastmod_node.text if lastmod_node is not None else None
        entries.append((loc.text.strip(), lastmod))
    return entries


def _extract_job_id(url: str) -> str:
    match = re.search(r"/job_details/(\d+)/?", url)
    return match.group(1) if match else url.rstrip("/").rsplit("/", 1)[-1]


def _fetch_title(session: requests.Session, url: str) -> str:
    last_error: requests.RequestException | None = None
    for attempt in range(_MAX_DETAIL_ATTEMPTS):
        if attempt:
            wait = min(30 * attempt, 120)
            log.info("Meta: retrying %s after %ss (attempt %s)", url, wait, attempt + 1)
            time.sleep(wait)
        try:
            resp = session.get(url, timeout=DEFAULT_TIMEOUT)
        except requests.RequestException as exc:
            last_error = exc
            continue
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            pause = int(retry_after) if retry_after and retry_after.isdigit() else 60
            log.warning("Meta: 429 for %s, sleeping %ss", url, pause)
            time.sleep(pause)
            last_error = requests.HTTPError("429 Too Many Requests", response=resp)
            continue
        try:
            resp.raise_for_status()
        except requests.HTTPError as exc:
            last_error = exc
            if resp.status_code in {400, 500, 502, 503}:
                continue
            raise
        match = _OG_TITLE_RE.search(resp.text)
        return match.group(1).strip() if match else ""
    if last_error:
        raise last_error
    return ""


def _fetch_missing_titles(
    session: requests.Session,
    missing: list[tuple[str, str]],
    cache: dict[str, str],
) -> None:
    if not missing:
        return
    log.info("Meta: fetching titles for %s uncached jobs", len(missing))
    for index, (job_id, url) in enumerate(missing):
        if index and index % _BATCH_SIZE == 0:
            time.sleep(_BATCH_PAUSE_SEC)
        elif index:
            time.sleep(_DETAIL_DELAY_SEC)
        try:
            title = _fetch_title(session, url)
        except requests.RequestException as e:
            log.warning("Meta: failed to fetch %s: %s", url, e)
            continue
        if title:
            cache[job_id] = title
            if len(cache) % 25 == 0:
                _save_cache(cache)
    _save_cache(cache)


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    if _sitemap_blocked() and company.get("linkedin_company_id"):
        return _fetch_linkedin_fallback(company)
    try:
        entries = _get_sitemap_entries()
        _clear_sitemap_blocked()
    except requests.HTTPError as e:
        if _blocked_status(e) in {400, 403} and company.get("linkedin_company_id"):
            _mark_sitemap_blocked()
            return _fetch_linkedin_fallback(company)
        raise AdapterError(
            f"Meta HTTP {e.response.status_code} fetching sitemap for {name}"
        ) from e
    except requests.RequestException as e:
        raise AdapterError(f"Meta network error for {name}: {e}") from e
    except ET.ParseError as e:
        raise AdapterError(f"Meta sitemap parse error for {name}: {e}") from e

    cache = _load_cache()
    session = requests.Session()
    session.headers.update(_detail_headers())

    missing: list[tuple[str, str]] = []
    for url, _lastmod in entries:
        job_id = _extract_job_id(url)
        if job_id not in cache:
            missing.append((job_id, url))

    if len(missing) > 50:
        log.info("Meta: cooldown before bulk title fetch (%s jobs)", len(missing))
        time.sleep(90)

    _fetch_missing_titles(session, missing, cache)
    _save_cache(cache)

    jobs: list[Job] = []
    for url, lastmod in entries:
        job_id = _extract_job_id(url)
        title = cache.get(job_id)
        if not title:
            continue
        jobs.append(
            Job(
                id=job_id,
                company=company["name"],
                title=title,
                location="",
                url=url,
                posted_at=lastmod,
                department=None,
                ats="meta",
                category=company.get("category", "uncategorized"),
            )
        )

    if entries and not jobs:
        raise AdapterError(
            f"Meta returned 0 titled jobs for {name} "
            f"({len(entries)} in sitemap, {len(cache)} cached titles)"
        )
    if len(jobs) < len(entries):
        log.warning(
            "Meta: missing titles for %s/%s jobs for %s",
            len(entries) - len(jobs),
            len(entries),
            name,
        )
    return jobs
