"""One-time slug verifier.

Pings each Greenhouse/Lever/Ashby/Workday endpoint in companies.yaml and
prints whether each returned a usable response. Run this locally before
trusting the registry:

    python discovery.py

Exit code is non-zero if any company failed, so this can be wired into CI
later if desired.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any

import requests

from adapters.base import DEFAULT_HEADERS
from scraper import load_registry

GH = "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
LV = "https://api.lever.co/v0/postings/{slug}?mode=json"
AS = "https://api.ashbyhq.com/posting-api/job-board/{slug}"
WD = "https://{tenant}.{wd_pod}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs"
WK = "https://apply.workable.com/api/v1/widget/accounts/{slug}"
GEM = "https://jobs.gem.com/api/public/graphql"
GEM_QUERY = """
query JobBoardList($boardId: String!) {
  oatsExternalJobPostings(boardId: $boardId) {
    jobPostings { id title }
  }
}
"""
RIP = "https://ats.rippling.com/{slug}/jobs"
UBER_CAREERS = "https://www.uber.com/us/en/careers/list/"
UBER_SEARCH = "https://www.uber.com/api/loadSearchJobsResults"


def _check_get(url: str) -> tuple[int, int]:
    try:
        r = requests.get(url, headers=DEFAULT_HEADERS, timeout=15)
        count = 0
        if r.ok:
            try:
                payload = r.json()
                if isinstance(payload, dict):
                    count = len(payload.get("jobs") or [])
                elif isinstance(payload, list):
                    count = len(payload)
            except ValueError:
                count = -1
        return r.status_code, count
    except requests.RequestException:
        return 0, 0


def _check_workable(slug: str) -> tuple[int, int]:
    return _check_get(WK.format(slug=slug))


def _check_jibe(company: dict[str, Any]) -> tuple[int, int]:
    host = company["careers_host"]
    url = f"https://{host}/api/jobs"
    try:
        r = requests.get(
            url, params={"page": 1, "limit": 1}, headers=DEFAULT_HEADERS, timeout=15
        )
        count = 0
        if r.ok:
            try:
                count = (r.json().get("totalCount") or 0)
            except ValueError:
                count = -1
        return r.status_code, count
    except requests.RequestException:
        return 0, 0


def _check_gem(slug: str) -> tuple[int, int]:
    headers = {
        **DEFAULT_HEADERS,
        "Content-Type": "application/json",
        "Origin": "https://jobs.gem.com",
        "Referer": f"https://jobs.gem.com/{slug}",
    }
    try:
        r = requests.post(
            GEM,
            json={
                "operationName": "JobBoardList",
                "query": GEM_QUERY,
                "variables": {"boardId": slug},
            },
            headers=headers,
            timeout=15,
        )
        count = 0
        if r.ok:
            try:
                payload = r.json()
                postings = (
                    payload.get("data", {})
                    .get("oatsExternalJobPostings", {})
                    .get("jobPostings")
                    or []
                )
                count = len(postings)
            except ValueError:
                count = -1
        return r.status_code, count
    except requests.RequestException:
        return 0, 0


def _check_rippling(slug: str) -> tuple[int, int]:
    try:
        r = requests.get(
            RIP.format(slug=slug), headers=DEFAULT_HEADERS, timeout=15
        )
        count = 0
        if r.ok:
            match = re.search(
                r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>',
                r.text,
                re.DOTALL,
            )
            if match:
                payload = json.loads(match.group(1))
                jobs = payload.get("props", {}).get("pageProps", {}).get("jobs") or {}
                if isinstance(jobs, dict):
                    count = jobs.get("totalItems") or len(jobs.get("items") or [])
                elif isinstance(jobs, list):
                    count = len(jobs)
        return r.status_code, count
    except (requests.RequestException, ValueError):
        return 0, 0


def _check_uber() -> tuple[int, int]:
    try:
        session = requests.Session()
        session.headers.update(DEFAULT_HEADERS)
        page = session.get(UBER_CAREERS, timeout=15)
        csrf = "x"
        match = re.search(r'"csrfToken"\s*:\s*"([^"]+)"', page.text)
        if match:
            csrf = match.group(1)
        r = session.post(
            f"{UBER_SEARCH}?localeCode=en",
            json={},
            headers={
                **DEFAULT_HEADERS,
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Origin": "https://www.uber.com",
                "Referer": UBER_CAREERS,
                "X-Csrf-Token": csrf,
                "x-csrf-token": csrf,
            },
            timeout=15,
        )
        count = 0
        if r.ok:
            try:
                count = len(r.json().get("data", {}).get("results") or [])
            except ValueError:
                count = -1
        return r.status_code, count
    except requests.RequestException:
        return 0, 0


def _check_workday(company: dict[str, Any]) -> tuple[int, int]:
    url = WD.format(
        tenant=company["tenant"], wd_pod=company["wd_pod"], site=company["site"]
    )
    try:
        r = requests.post(
            url,
            json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""},
            headers={**DEFAULT_HEADERS, "Content-Type": "application/json"},
            timeout=15,
        )
        count = 0
        if r.ok:
            try:
                count = (r.json().get("total") or 0)
            except ValueError:
                count = -1
        return r.status_code, count
    except requests.RequestException:
        return 0, 0


def main() -> int:
    companies = load_registry()
    ok = 0
    bad: list[str] = []
    skipped = 0

    print(f"{'Company':35} {'ATS':12} {'Status':8} {'Count'}")
    print("-" * 70)

    for company in companies:
        name = company["name"]
        ats = company["ats"]

        if ats == "tier3_todo":
            print(f"{name:35} {ats:12} SKIP")
            skipped += 1
            continue

        if ats == "greenhouse":
            status, count = _check_get(GH.format(slug=company["slug"]))
        elif ats == "lever":
            status, count = _check_get(LV.format(slug=company["slug"]))
        elif ats == "ashby":
            status, count = _check_get(AS.format(slug=company["slug"]))
        elif ats == "workday":
            status, count = _check_workday(company)
        elif ats == "workable":
            status, count = _check_workable(company["slug"])
        elif ats == "jibe":
            status, count = _check_jibe(company)
        elif ats == "rippling":
            status, count = _check_rippling(company["slug"])
        elif ats == "gem":
            status, count = _check_gem(company["slug"])
        elif ats == "uber":
            status, count = _check_uber()
        else:
            print(f"{name:35} {ats:12} UNKNOWN")
            bad.append(name)
            continue

        flag = "OK " if 200 <= status < 300 else "BAD"
        print(f"{name:35} {ats:12} {status:<5} {flag} {count}")
        if 200 <= status < 300:
            ok += 1
        else:
            bad.append(name)

    print("-" * 70)
    print(f"OK: {ok}   BAD: {len(bad)}   tier3-skipped: {skipped}")
    if bad:
        print("\nBroken slugs to fix in companies.yaml:")
        for n in bad:
            print(f"  - {n}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
