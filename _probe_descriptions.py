"""Probe job detail pages for description content vs adapter gaps."""

from __future__ import annotations

import json
import re
import sys

import requests

from adapters.base import DEFAULT_HEADERS, DEFAULT_TIMEOUT

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_QUAL_KEYWORDS = (
    "minimum qualifications",
    "preferred qualifications",
    "qualifications",
    "requirements",
    "what you need",
    "what we're looking for",
    "bachelor",
    "years of experience",
    "about the job",
    "about the role",
)


def _keyword_hits(text: str) -> list[str]:
    lower = text.lower()
    return [k for k in _QUAL_KEYWORDS if k in lower]


def probe_google() -> None:
    print("=" * 70)
    print("GOOGLE")
    from adapters.google_careers import _get_page

    page_jobs = _get_page(1, {})
    print(f"  listing jobs page 1: {len(page_jobs)}")
    if not page_jobs:
        return
    item = page_jobs[0]
    job_id = str(item[0])
    title = str(item[1] or "")
    detail_url = (
        f"https://www.google.com/about/careers/applications/jobs/results/{job_id}"
    )
    resp = requests.get(
        detail_url,
        headers={**DEFAULT_HEADERS, "Accept": "text/html"},
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    print(f"  sample: {title!r} id={job_id}")
    print(f"  detail url: {detail_url}")
    print(f"  html length: {len(resp.text)}")
    print(f"  keyword hits: {_keyword_hits(resp.text)}")
    keys = re.findall(r"AF_initDataCallback\(\{key:\s*'([^']+)'", resp.text)
    print(f"  AF_initDataCallback keys: {keys}")
    for key in keys:
        pat = re.compile(
            rf"AF_initDataCallback\(\{{key:\s*'{re.escape(key)}',\s*hash:\s*'\d+',\s*data:(.*?),\s*sideChannel:",
            re.DOTALL,
        )
        match = pat.search(resp.text)
        if not match:
            continue
        blob = match.group(1)
        low = blob.lower()
        if any(x in low for x in ("qualification", "bachelor", "minimum", "about the job")):
            print(f"  key {key}: qualification content, blob len {len(blob)}")
            print(f"    snippet: {blob[:500]}...")


def probe_microsoft() -> None:
    print("=" * 70)
    print("MICROSOFT")
    search = requests.get(
        "https://apply.careers.microsoft.com/api/pcsx/search",
        params={
            "domain": "microsoft.com",
            "query": "software engineer",
            "location": "",
            "start": 0,
            "count": 3,
        },
        headers={
            **DEFAULT_HEADERS,
            "Accept": "application/json",
            "Referer": "https://apply.careers.microsoft.com/careers",
        },
        timeout=DEFAULT_TIMEOUT,
    )
    search.raise_for_status()
    payload = search.json()
    positions = payload.get("data", {}).get("positions") or []
    if not positions:
        print("  No positions in search response")
        return
    raw = positions[0]
    job_id = raw.get("id") or raw.get("displayJobId")
    print(f"  sample job: {raw.get('name')!r} id={job_id}")

    detail_urls = [
        f"https://apply.careers.microsoft.com/api/pcsx/position/{job_id}?domain=microsoft.com",
        f"https://apply.careers.microsoft.com/careers/job/{job_id}",
    ]
    for url in detail_urls:
        try:
            resp = requests.get(
                url,
                headers={
                    **DEFAULT_HEADERS,
                    "Accept": "application/json, text/html",
                    "Referer": "https://apply.careers.microsoft.com/careers",
                },
                timeout=DEFAULT_TIMEOUT,
            )
        except requests.RequestException as exc:
            print(f"  {url} -> error {exc}")
            continue
        ctype = resp.headers.get("content-type", "")
        print(f"  {url}")
        print(f"    status={resp.status_code} type={ctype} len={len(resp.text)}")
        if "json" in ctype:
            try:
                data = resp.json()
                print(f"    json keys: {list(data.keys()) if isinstance(data, dict) else type(data)}")
            except ValueError:
                print("    invalid json")
        else:
            print(f"    keyword hits: {_keyword_hits(resp.text)}")
            next_data = re.search(
                r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
                resp.text,
                re.DOTALL,
            )
            if next_data:
                try:
                    nd = json.loads(next_data.group(1))
                    print(f"    __NEXT_DATA__ keys: {list(nd.keys())}")
                    page_props = nd.get("props", {}).get("pageProps", {})
                    print(f"    pageProps keys: {list(page_props.keys())[:20]}")
                    for k, v in page_props.items():
                        if isinstance(v, str) and len(v) > 200:
                            print(f"    pageProps[{k!r}] len={len(v)} head={v[:200]}...")
                        elif isinstance(v, dict):
                            for sk in ("description", "jobDescription", "qualifications"):
                                if sk in v:
                                    print(f"    pageProps[{k}][{sk}]: {str(v[sk])[:300]}...")
                except ValueError as exc:
                    print(f"    __NEXT_DATA__ parse error: {exc}")
            for needle in ("jobDescription", "qualifications", "minimumQualifications"):
                idx = resp.text.find(needle)
                if idx >= 0:
                    print(f"    found {needle!r} at {idx}: {resp.text[idx:idx+200]}...")


def probe_uber() -> None:
    print("=" * 70)
    print("UBER")
    from adapters.uber import _fetch_results

    results = _fetch_results("en")
    if not results:
        print("  No uber results")
        return
    raw = results[0]
    print(f"  sample job keys: {sorted(raw.keys())}")
    for k in ("description", "descriptionHtml", "summary", "qualifications", "content"):
        if k in raw:
            print(f"  listing field {k}: {str(raw[k])[:300]}...")
    job_id = raw["id"]
    detail_urls = [
        f"https://www.uber.com/api/getJobDetails?localeCode=en",
        f"https://www.uber.com/us/en/careers/list/{job_id}/",
    ]
    for url in detail_urls:
        try:
            if "getJobDetails" in url:
                resp = requests.post(
                    url,
                    json={"jobId": job_id},
                    headers={**DEFAULT_HEADERS, "Content-Type": "application/json"},
                    timeout=DEFAULT_TIMEOUT,
                )
            else:
                resp = requests.get(
                    url,
                    headers={**DEFAULT_HEADERS, "Accept": "text/html"},
                    timeout=DEFAULT_TIMEOUT,
                )
        except requests.RequestException as exc:
            print(f"  {url} -> error {exc}")
            continue
        print(f"  {url} status={resp.status_code} len={len(resp.text)}")
        if resp.headers.get("content-type", "").startswith("application/json"):
            try:
                data = resp.json()
                print(f"    json: {json.dumps(data)[:500]}...")
            except ValueError:
                pass
        else:
            print(f"    keyword hits: {_keyword_hits(resp.text)}")


def probe_workday() -> None:
    print("=" * 70)
    print("WORKDAY (Nvidia sample)")
    # Nvidia workday detail endpoint pattern
    list_url = (
        "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"
    )
    resp = requests.post(
        list_url,
        json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""},
        headers={**DEFAULT_HEADERS, "Content-Type": "application/json"},
        timeout=DEFAULT_TIMEOUT,
    )
    resp.raise_for_status()
    postings = resp.json().get("jobPostings") or []
    if not postings:
        print("  No postings")
        return
    path = postings[0].get("externalPath", "")
    print(f"  sample path: {path}")
    detail_url = f"https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite{path}"
    detail = requests.get(
        detail_url,
        headers={**DEFAULT_HEADERS, "Accept": "application/json"},
        timeout=DEFAULT_TIMEOUT,
    )
    detail.raise_for_status()
    data = detail.json()
    info = data.get("jobPostingInfo") or {}
    print(f"  detail keys: {list(info.keys())[:15]}")
    desc = info.get("jobDescription") or info.get("description") or ""
    print(f"  description length: {len(desc)}")
    if desc:
        print(f"  description head: {desc[:400]}...")


def probe_google_swe_structure() -> None:
    print("=" * 70)
    print("GOOGLE SWE DETAIL STRUCTURE")
    from adapters.google_careers import _get_page
    from text_util import strip_html

    for page in range(1, 8):
        for item in _get_page(page, {}):
            title = str(item[1] or "")
            tl = title.lower()
            if "software engineer" not in tl or "senior" in tl:
                continue
            job_id = str(item[0])
            detail_url = (
                f"https://www.google.com/about/careers/applications/jobs/results/{job_id}"
            )
            resp = requests.get(
                detail_url,
                headers={**DEFAULT_HEADERS, "Accept": "text/html"},
                timeout=DEFAULT_TIMEOUT,
            )
            resp.raise_for_status()
            pat = re.compile(
                r"AF_initDataCallback\(\{key:\s*'ds:0',\s*hash:\s*'\d+',\s*data:(.*?),\s*sideChannel:",
                re.DOTALL,
            )
            match = pat.search(resp.text)
            if not match:
                print(f"  {title}: no ds:0 payload")
                return
            data = json.loads(match.group(1))
            print(f"  title: {title}")
            print(f"  id: {job_id}")

            def collect_strings(obj: object, out: list[str], depth: int = 0) -> None:
                if depth > 10:
                    return
                if isinstance(obj, str) and len(obj) > 40:
                    low = obj.lower()
                    if any(
                        k in low
                        for k in (
                            "minimum qualification",
                            "preferred qualification",
                            "bachelor",
                            "years of experience",
                            "about the job",
                        )
                    ):
                        out.append(strip_html(obj))
                elif isinstance(obj, list):
                    for entry in obj:
                        collect_strings(entry, out, depth + 1)
                elif isinstance(obj, dict):
                    for entry in obj.values():
                        collect_strings(entry, out, depth + 1)

            hits: list[str] = []
            collect_strings(data, hits)
            for hit in hits[:4]:
                print(f"  chunk: {hit[:350]}...")
            return
    print("  No bare software engineer found in first 7 pages")


def main() -> None:
    probe_google()
    probe_google_swe_structure()
    probe_microsoft()
    probe_uber()
    probe_workday()


if __name__ == "__main__":
    main()
