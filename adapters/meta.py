"""Meta careers adapter (metacareers.com job search + detail pages).

One GraphQL request to the careers site's own search (the query behind the
/jobs page) returns every open posting with its current title and locations.
Detail pages — for the real posting date and description — are only fetched
for postings the classifier could still include (see
classifier.could_be_included), so senior, non-software and non-US roles cost
nothing. Detail records are memoized in meta_title_cache.json, so hourly runs
only hit new candidates.

The jobs sitemap is still read as a cross-check: any posting it lists that the
search did not return is handled the old way (detail page for every one). If
the search fails outright (e.g. Meta rotates the query id and rediscovery from
the JS bundles fails too) the whole board falls back to the sitemap path.

metacareers.com sits behind the Facebook edge, which returns HTTP 400 to
requests missing the Sec-Fetch-*/sec-ch-ua client hints a real browser sends —
hence the full header set below. When the edge does block us, the fallback to
LinkedIn expires after _BLOCK_TTL_SEC so a transient block never pins Meta to
LinkedIn permanently.
"""

from __future__ import annotations

import json
import logging
import re
import threading
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

from filters import could_be_included, should_fetch_description
from text_util import normalize_description

from . import linkedin as linkedin_adapter
from .base import DEFAULT_TIMEOUT, AdapterError, Job
from .description_fetch import map_descriptions_parallel

log = logging.getLogger(__name__)

JOBS_URL = "https://www.metacareers.com/jobs"
SITEMAP_URL = "https://www.metacareers.com/jobs/sitemap.xml"
GRAPHQL_URL = "https://www.metacareers.com/graphql"
DETAIL_URL = "https://www.metacareers.com/profile/job_details/{job_id}/"
# Persisted query id of CareersJobSearchResultsV2DataQuery; rediscovered from
# the page's JS bundles when Meta ships a new one.
SEARCH_DOC_ID = "27129360303422352"
_SEARCH_QUERY_NAME = "CareersJobSearchResultsV2DataQuery"
CACHE_PATH = Path(__file__).resolve().parent.parent / "meta_title_cache.json"
STATE_PATH = Path(__file__).resolve().parent.parent / "meta_careers_state.json"

_LD_JSON_RE = re.compile(
    r'<script type="application/ld\+json"[^>]*>(.*?)</script>', re.DOTALL
)
_OG_TITLE_RE = re.compile(r'<meta property="og:title" content="([^"]+)"')
_JOB_ID_RE = re.compile(r"/job_details/(\d+)/?")
_LSD_RE = re.compile(r'"LSD",\[\],\{"token":"([^"]+)"')
_SCRIPT_SRC_RE = re.compile(
    r'<script[^>]+src="(https://static\.xx\.fbcdn\.net/rsrc\.php/[^"]+)"'
)
_DOC_ID_RE = re.compile(
    _SEARCH_QUERY_NAME
    + r'_candidate_portalRelayOperation",\[\],\(function\([^)]*\)\{\w+\.exports="(\d+)"'
)

_DETAIL_WORKERS = 8
_MAX_DETAIL_ATTEMPTS = 4
# A block is retried after this long; without an expiry one bad run would
# leave Meta on the LinkedIn fallback forever.
_BLOCK_TTL_SEC = 6 * 60 * 60

_local = threading.local()


def _browser_headers() -> dict[str, str]:
    # Do not merge DEFAULT_HEADERS — the Facebook edge 400s the bot
    # User-Agent, and 400s any request lacking these client hints.
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,image/apng,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "sec-ch-ua": (
            '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"'
        ),
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }


def _new_session() -> requests.Session:
    session = requests.Session()
    # headers.clear() first: the default python-requests UA/Accept leak through
    # session.headers.update() and are enough to trigger the 400.
    session.headers.clear()
    session.headers.update(_browser_headers())
    return session


def _detail_session() -> requests.Session:
    """One warmed session per worker thread (requests.Session is not thread-safe)."""
    session = getattr(_local, "session", None)
    if session is None:
        session = _new_session()
        try:
            # Warm the datr cookie; the edge is stricter on cold connections.
            session.get(JOBS_URL, timeout=DEFAULT_TIMEOUT)
        except requests.RequestException:
            pass
        _local.session = session
    return session


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


def _load_cache() -> dict[str, dict[str, Any]]:
    if not CACHE_PATH.exists():
        return {}
    try:
        payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    if not isinstance(payload, dict):
        return {}
    cache: dict[str, dict[str, Any]] = {}
    for job_id, value in payload.items():
        # Pre-JSON-LD caches stored a bare title string.
        if isinstance(value, str):
            cache[job_id] = {"title": value}
        elif isinstance(value, dict) and value.get("title"):
            cache[job_id] = value
    return cache


def _save_cache(cache: dict[str, dict[str, Any]]) -> None:
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
    state = _load_state()
    if not state.get("sitemap_blocked"):
        return False
    blocked_at = state.get("blocked_at")
    if not isinstance(blocked_at, (int, float)):
        return True  # Legacy flag with no timestamp; retried once it is rewritten.
    if time.time() - blocked_at >= _BLOCK_TTL_SEC:
        log.info("Meta: sitemap block expired, retrying metacareers")
        return False
    return True


def _mark_sitemap_blocked() -> None:
    state = _load_state()
    state["sitemap_blocked"] = True
    state["blocked_at"] = time.time()
    _save_state(state)


def _clear_sitemap_blocked() -> None:
    state = _load_state()
    if not state.get("sitemap_blocked") and "blocked_at" not in state:
        return
    state.pop("sitemap_blocked", None)
    state.pop("blocked_at", None)
    _save_state(state)


@retry(
    reraise=True,
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception(_retryable_request_error),
)
def _get_sitemap_entries() -> list[tuple[str, str | None]]:
    session = _new_session()
    # Warm session cookies; some edges require a prior /jobs visit.
    session.get(JOBS_URL, timeout=DEFAULT_TIMEOUT)
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


def _search_variables() -> str:
    # Mirrors the /jobs page's default (unfiltered) search; results_per_page
    # null returns every match in one response (paging is client-side).
    search_input = {
        "q": None,
        "divisions": [],
        "offices": [],
        "roles": [],
        "leadership_levels": [],
        "saved_jobs": [],
        "saved_searches": [],
        "sub_teams": [],
        "teams": [],
        "is_leadership": False,
        "is_remote_only": False,
        "sort_by_new": False,
        "results_per_page": None,
    }
    return json.dumps(
        {"search_input": search_input, "isLoggedIn": False, "viewasUserID": None}
    )


def _post_search(
    session: requests.Session, lsd: str, doc_id: str
) -> list[dict[str, Any]] | None:
    """Run the search query; None when the response has no job list (stale doc id)."""
    resp = session.post(
        GRAPHQL_URL,
        data={"lsd": lsd, "doc_id": doc_id, "variables": _search_variables()},
        headers={
            "X-FB-LSD": lsd,
            "Origin": "https://www.metacareers.com",
            "Referer": JOBS_URL,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        },
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    # Body may carry the "for (;;);" XSSI guard and trailing streamed lines.
    first_line = resp.text.lstrip().removeprefix("for (;;);").split("\n", 1)[0]
    try:
        payload = json.loads(first_line)
    except ValueError:
        return None
    data = payload.get("data") if isinstance(payload, dict) else None
    result = (data or {}).get("job_search_with_featured_jobs_v2") or {}
    jobs = result.get("all_jobs")
    return jobs if isinstance(jobs, list) else None


def _discover_doc_id(session: requests.Session, page_html: str) -> str | None:
    for src in dict.fromkeys(_SCRIPT_SRC_RE.findall(page_html)):
        try:
            js = session.get(src.replace("&amp;", "&"), timeout=DEFAULT_TIMEOUT).text
        except requests.RequestException:
            continue
        match = _DOC_ID_RE.search(js)
        if match:
            return match.group(1)
    return None


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=4, max=30),
    retry=retry_if_exception(_retryable_request_error),
)
def _search_jobs() -> list[dict[str, Any]]:
    """Every open posting as {id, title, locations, ...} from the careers search."""
    session = _new_session()
    page = session.get(JOBS_URL, timeout=DEFAULT_TIMEOUT)
    page.raise_for_status()
    lsd_match = _LSD_RE.search(page.text)
    if not lsd_match:
        raise AdapterError("Meta: no LSD token on /jobs page")
    lsd = lsd_match.group(1)

    jobs = _post_search(session, lsd, SEARCH_DOC_ID)
    if jobs is None:
        doc_id = _discover_doc_id(session, page.text)
        if doc_id and doc_id != SEARCH_DOC_ID:
            log.warning(
                "Meta: search doc_id %s is stale, using %s (update SEARCH_DOC_ID)",
                SEARCH_DOC_ID,
                doc_id,
            )
            jobs = _post_search(session, lsd, doc_id)
    if not jobs:
        raise AdapterError("Meta: job search returned no postings")
    return jobs


def _extract_job_id(url: str) -> str:
    match = _JOB_ID_RE.search(url)
    return match.group(1) if match else url.rstrip("/").rsplit("/", 1)[-1]


def _ld_locations(payload: dict[str, Any]) -> str:
    raw = payload.get("jobLocation")
    if isinstance(raw, dict):
        raw = [raw]
    if not isinstance(raw, list):
        return ""
    names: list[str] = []
    for place in raw:
        if not isinstance(place, dict):
            continue
        name = place.get("name")
        if not isinstance(name, str):
            address = place.get("address")
            if isinstance(address, dict):
                parts = [
                    address.get("addressLocality"),
                    address.get("addressRegion"),
                ]
                name = ", ".join(p for p in parts if isinstance(p, str) and p)
        if isinstance(name, str) and name.strip() and name not in names:
            names.append(name.strip())
    return "; ".join(names)


def _ld_description(payload: dict[str, Any]) -> str | None:
    sections = [
        payload.get("description"),
        payload.get("responsibilities"),
        payload.get("qualifications"),
    ]
    joined = "\n".join(s for s in sections if isinstance(s, str) and s.strip())
    return normalize_description(joined, is_html=True)


def _parse_detail(html: str) -> dict[str, Any] | None:
    """Extract a cache record from a job detail page."""
    for match in _LD_JSON_RE.finditer(html):
        try:
            payload = json.loads(match.group(1))
        except ValueError:
            continue
        if not isinstance(payload, dict) or payload.get("@type") != "JobPosting":
            continue
        title = payload.get("title")
        if not isinstance(title, str) or not title.strip():
            continue
        record: dict[str, Any] = {
            "title": title.strip(),
            "location": _ld_locations(payload),
            "posted_at": payload.get("datePosted"),
        }
        # Descriptions are only consulted for ambiguous titles; skipping the
        # rest keeps the on-disk cache small.
        if should_fetch_description(record["title"]):
            description = _ld_description(payload)
            if description:
                record["description"] = description
        return record

    # No JSON-LD (rare) — fall back to the og:title meta tag.
    og = _OG_TITLE_RE.search(html)
    if og and og.group(1).strip():
        return {"title": og.group(1).strip(), "location": "", "posted_at": None}
    return None


def _fetch_detail(url: str) -> dict[str, Any] | None:
    last_error: requests.RequestException | None = None
    for attempt in range(_MAX_DETAIL_ATTEMPTS):
        if attempt:
            time.sleep(min(5 * attempt, 30))
        try:
            resp = _detail_session().get(url, timeout=DEFAULT_TIMEOUT)
        except requests.RequestException as exc:
            last_error = exc
            continue
        if resp.status_code == 429:
            retry_after = resp.headers.get("Retry-After")
            pause = int(retry_after) if retry_after and retry_after.isdigit() else 30
            log.warning("Meta: 429 for %s, sleeping %ss", url, pause)
            time.sleep(pause)
            last_error = requests.HTTPError("429 Too Many Requests", response=resp)
            continue
        if resp.status_code in {400, 500, 502, 503}:
            last_error = requests.HTTPError(str(resp.status_code), response=resp)
            continue
        resp.raise_for_status()
        return _parse_detail(resp.text)
    if last_error:
        log.debug("Meta: giving up on %s: %s", url, last_error)
    return None


def _fetch_missing(
    missing: list[tuple[str, str]],
    cache: dict[str, dict[str, Any]],
    listed: dict[str, tuple[str, str]],
) -> None:
    log.info("Meta: fetching details for %s jobs", len(missing))
    results = map_descriptions_parallel(
        [url for _job_id, url in missing],
        _fetch_detail,
        max_workers=_DETAIL_WORKERS,
    )
    for job_id, url in missing:
        record = results.get(url)
        if record:
            if job_id in listed:
                # Search and JSON-LD titles can differ; remember which search
                # title this record belongs to so it is not re-fetched hourly.
                record["listed_title"] = listed[job_id][0]
            cache[job_id] = record
    _save_cache(cache)


def _listed_job(raw: dict[str, Any]) -> tuple[str, str, str] | None:
    job_id = str(raw.get("id") or "").strip()
    title = str(raw.get("title") or "").strip()
    if not job_id or not title:
        return None
    locations = [
        str(loc).strip() for loc in raw.get("locations") or [] if str(loc).strip()
    ]
    return job_id, title, "; ".join(dict.fromkeys(locations))


def fetch(company: dict[str, Any]) -> list[Job]:
    name = company.get("name", "?")
    if _sitemap_blocked() and company.get("linkedin_company_id"):
        return _fetch_linkedin_fallback(company)

    listed: dict[str, tuple[str, str]] = {}
    try:
        for raw in _search_jobs():
            parsed = _listed_job(raw) if isinstance(raw, dict) else None
            if parsed:
                listed[parsed[0]] = (parsed[1], parsed[2])
    except (requests.RequestException, AdapterError) as e:
        log.warning("Meta: job search failed (%s); using sitemap only", e)

    try:
        entries = _get_sitemap_entries()
    except (requests.RequestException, ET.ParseError) as e:
        if listed:
            log.warning("Meta: sitemap unavailable (%s); using job search only", e)
            entries = []
        elif isinstance(e, requests.HTTPError):
            if _blocked_status(e) in {400, 403} and company.get("linkedin_company_id"):
                _mark_sitemap_blocked()
                return _fetch_linkedin_fallback(company)
            raise AdapterError(
                f"Meta HTTP {e.response.status_code} fetching sitemap for {name}"
            ) from e
        elif isinstance(e, ET.ParseError):
            raise AdapterError(f"Meta sitemap parse error for {name}: {e}") from e
        else:
            raise AdapterError(f"Meta network error for {name}: {e}") from e
    _clear_sitemap_blocked()

    url_by_id: dict[str, str] = {}
    lastmod_by_id: dict[str, str | None] = {}
    for url, lastmod in entries:
        job_id = _extract_job_id(url)
        url_by_id.setdefault(job_id, url)
        lastmod_by_id.setdefault(job_id, lastmod)
    unlisted = [job_id for job_id in url_by_id if job_id not in listed]

    cache = _load_cache()
    # Detail pages only for listed postings that could still be included
    # (re-fetched when the title changed since caching), plus every posting
    # the search missed, whose title is only known from its detail page.
    missing: list[tuple[str, str]] = []
    for job_id, (title, location) in listed.items():
        if not could_be_included(title, location):
            continue
        record = cache.get(job_id)
        if not record or record.get("listed_title", record["title"]) != title:
            url = url_by_id.get(job_id) or DETAIL_URL.format(job_id=job_id)
            missing.append((job_id, url))
    missing.extend(
        (job_id, url_by_id[job_id]) for job_id in unlisted if job_id not in cache
    )
    if missing:
        _fetch_missing(missing, cache, listed)
    # Drop records for postings that have closed.
    live = listed.keys() | url_by_id.keys()
    if live and not live >= cache.keys():
        cache = {job_id: rec for job_id, rec in cache.items() if job_id in live}
        _save_cache(cache)

    def to_job(job_id: str, title: str, location: str) -> Job:
        record = cache.get(job_id) or {}
        return Job(
            id=job_id,
            company=company["name"],
            title=title,
            location=location or record.get("location") or "",
            url=url_by_id.get(job_id) or DETAIL_URL.format(job_id=job_id),
            # Sitemap lastmod is the crawl time (identical for every entry),
            # so only use it when JSON-LD has no real datePosted.
            posted_at=record.get("posted_at") or lastmod_by_id.get(job_id),
            department=None,
            ats="meta",
            category=company.get("category", "uncategorized"),
            description=record.get("description"),
        )

    jobs = [to_job(job_id, title, loc) for job_id, (title, loc) in listed.items()]
    for job_id in unlisted:
        record = cache.get(job_id)
        if record:
            jobs.append(to_job(job_id, record["title"], record.get("location") or ""))

    if url_by_id and not jobs:
        raise AdapterError(
            f"Meta returned 0 parsed jobs for {name} "
            f"({len(entries)} in sitemap, {len(cache)} cached)"
        )
    unresolved = sum(1 for job_id, _url in missing if job_id not in cache)
    if unresolved:
        log.warning(
            "Meta: missing details for %s/%s fetched jobs for %s",
            unresolved,
            len(missing),
            name,
        )
    return jobs
