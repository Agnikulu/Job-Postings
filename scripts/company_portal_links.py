"""Emit markdown table of companies + public job board URLs from companies.yaml."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlencode

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def portal_url(entry: dict) -> str:
    ats = entry.get("ats", "")
    if ats == "tier3_todo":
        note = entry.get("note") or ""
        m = re.search(r"https?://[^\s\"']+", note)
        return m.group(0).rstrip(".,)") if m else "— (custom site, no adapter)"

    if ats == "greenhouse":
        slug = entry["slug"]
        return f"https://boards.greenhouse.io/{slug}"
    if ats == "lever":
        return f"https://jobs.lever.co/{entry['slug']}"
    if ats == "ashby":
        return f"https://jobs.ashbyhq.com/{entry['slug']}"
    if ats == "workday":
        if entry.get("workday_public_base"):
            return str(entry["workday_public_base"])
        tenant = entry["tenant"]
        pod = entry.get("wd_pod", "wd5")
        site = entry["site"]
        cxs_host = entry.get("workday_cxs_host") or f"{tenant}.{pod}.myworkdayjobs.com"
        if entry.get("workday_cxs_host"):
            return f"https://{cxs_host}/recruiting/{tenant}/{site}"
        return f"https://{tenant}.{pod}.myworkdayjobs.com/en-US/{site}"
    if ats == "workable":
        return f"https://apply.workable.com/{entry['slug']}"
    if ats == "gem":
        return f"https://jobs.gem.com/{entry['slug']}"
    if ats == "rippling":
        return f"https://ats.rippling.com/{entry['slug']}/jobs"
    if ats == "uber":
        return "https://www.uber.com/careers/list/"
    if ats == "smartrecruiters":
        return f"https://careers.smartrecruiters.com/{entry['slug']}"
    if ats == "recruitee":
        return f"https://{entry['slug']}.recruitee.com"
    if ats == "wiz":
        return "https://www.wiz.io/careers"
    if ats == "coinbase":
        return "https://www.coinbase.com/careers/positions"
    if ats == "snyk":
        return "https://snyk.io/careers/all-jobs/"
    if ats == "amazon_jobs":
        return "https://www.amazon.jobs/en/search"
    if ats == "meta":
        return "https://www.metacareers.com/jobs"
    if ats == "eightfold":
        return f"https://{entry['careers_host']}"
    if ats == "jibe":
        return f"https://{entry['careers_host']}"
    if ats == "microsoft":
        return "https://apply.careers.microsoft.com/careers"
    if ats == "linkedin":
        return "https://www.linkedin.com/jobs/search/"
    if ats == "apple":
        return "https://jobs.apple.com/en-us/search"
    if ats == "google_careers":
        params: list[tuple[str, str]] = []
        if company := entry.get("google_company"):
            params.append(("company", str(company)))
        levels = entry.get("google_target_levels")
        if isinstance(levels, str):
            levels = [levels]
        for level in levels or []:
            params.append(("target_level", str(level)))
        if sort_by := entry.get("google_sort_by"):
            params.append(("sort_by", str(sort_by)))
        base = "https://www.google.com/about/careers/applications/jobs/results"
        return f"{base}?{urlencode(params)}" if params else base + "/"
    return "—"


def main() -> None:
    companies = yaml.safe_load((ROOT / "companies.yaml").read_text(encoding="utf-8"))
    active = [c for c in companies if c.get("ats") != "tier3_todo"]
    todo = [c for c in companies if c.get("ats") == "tier3_todo"]

    print(f"<!-- {len(active)} active, {len(todo)} tier3_todo -->")
    print("| Company | Category | ATS | Job board |")
    print("|---------|----------|-----|-----------|")
    for c in sorted(active, key=lambda x: (x.get("category", ""), x.get("name", ""))):
        url = portal_url(c)
        print(
            f"| {c['name']} | {c.get('category', '')} | `{c['ats']}` | "
            f"[Open board]({url}) |"
        )

    print()
    print("### Tier 3 - tracked, not scraped yet")
    print()
    print("| Company | Category | Notes |")
    print("|---------|----------|-------|")
    for c in sorted(todo, key=lambda x: x.get("name", "")):
        note = (c.get("note") or "").replace("|", "\\|")
        print(f"| {c['name']} | {c.get('category', '')} | {note} |")


if __name__ == "__main__":
    main()
