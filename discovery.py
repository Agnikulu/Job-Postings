"""One-time slug verifier.

Pings each Greenhouse/Lever/Ashby/Workday endpoint in companies.yaml and
prints whether each returned a usable response. Run this locally before
trusting the registry:

    python discovery.py

Exit code is non-zero if any company failed, so this can be wired into CI
later if desired.
"""

from __future__ import annotations

import sys
from typing import Any

import requests

from adapters.base import DEFAULT_HEADERS
from scraper import load_registry

GH = "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
LV = "https://api.lever.co/v0/postings/{slug}?mode=json"
AS = "https://api.ashbyhq.com/posting-api/job-board/{slug}"
WD = "https://{tenant}.{wd_pod}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs"


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
