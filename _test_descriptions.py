"""Comprehensive description + requirements verification across active companies.

Usage:
    python _test_descriptions.py              # full audit
    python _test_descriptions.py --examples 5  # show N examples per ATS
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass, field

from adapters import ADAPTER_REGISTRY, AdapterError
from description_signals import extract_description_signals
from filters import classify_title_confidence
from scraper import load_registry

TECH_TITLE = (
    "engineer", "scientist", "research", "intern", "software",
    "ml", "machine learning", "data", "developer", "firmware",
    "platform", "backend", "frontend", "sre", "devops",
)

REPORT_PATH = "description_audit_report.txt"


@dataclass
class CompanyStats:
    name: str
    ats: str
    jobs: int = 0
    with_desc: int = 0
    with_req: int = 0
    with_strong_ec: int = 0
    with_bachelors: int = 0
    error: str | None = None
    example: dict | None = None
    missing_req_sample: dict | None = None


@dataclass
class AtsRollup:
    companies: int = 0
    jobs: int = 0
    with_desc: int = 0
    with_req: int = 0
    with_strong_ec: int = 0
    with_bachelors: int = 0
    errors: int = 0
    examples: list[dict] = field(default_factory=list)
    missing: list[dict] = field(default_factory=list)


def pct(num: int, den: int) -> str:
    return f"{100 * num / den:.0f}%" if den else "n/a"


def _pick_example(jobs: list, *, prefer_req: bool) -> object | None:
    pool = [j for j in jobs if j.description]
    if not pool:
        return None
    if prefer_req:
        for job in pool:
            if extract_description_signals(job.description).requirements_text:
                title = (job.title or "").lower()
                if any(k in title for k in TECH_TITLE):
                    return job
        for job in pool:
            if extract_description_signals(job.description).requirements_text:
                return job
    for job in pool:
        title = (job.title or "").lower()
        if any(k in title for k in TECH_TITLE):
            return job
    return pool[0]


def _job_snapshot(company: str, job) -> dict:
    sig = extract_description_signals(job.description)
    conf = classify_title_confidence(job.title, job.description)
    req = sig.requirements_text or ""
    return {
        "company": company,
        "title": job.title,
        "url": job.url,
        "desc_len": len(job.description or ""),
        "req_len": len(req),
        "strong_ec": sig.has_strong_ec,
        "bachelors_req": sig.has_bachelors_req,
        "tech_field": sig.has_tech_field,
        "senior_exp": sig.has_senior_exp,
        "classify": conf.level,
        "reason": conf.reason,
        "req_snippet": req[:280],
    }


def audit_company(company: dict) -> CompanyStats:
    name = company["name"]
    ats = company["ats"]
    stats = CompanyStats(name=name, ats=ats)
    if ats == "tier3_todo":
        return stats

    adapter = ADAPTER_REGISTRY.get(ats)
    if not adapter:
        stats.error = f"no adapter for {ats!r}"
        return stats

    try:
        jobs = [j for j in adapter(company) if j.url]
    except AdapterError as e:
        stats.error = str(e)
        return stats
    except Exception as e:
        stats.error = repr(e)
        return stats

    stats.jobs = len(jobs)
    with_desc = [j for j in jobs if j.description]
    stats.with_desc = len(with_desc)

    for job in with_desc:
        sig = extract_description_signals(job.description)
        if sig.requirements_text:
            stats.with_req += 1
        if sig.has_strong_ec:
            stats.with_strong_ec += 1
        if sig.has_bachelors_req:
            stats.with_bachelors += 1

    ex = _pick_example(jobs, prefer_req=True)
    if ex:
        stats.example = _job_snapshot(name, ex)

    no_req = [
        j for j in with_desc
        if not extract_description_signals(j.description).requirements_text
    ]
    miss = _pick_example(no_req, prefer_req=False)
    if miss and stats.with_desc and stats.with_req < stats.with_desc:
        stats.missing_req_sample = _job_snapshot(name, miss)

    return stats


def format_example(label: str, snap: dict) -> list[str]:
    lines = [
        f"  [{label}] {snap['company']}: {snap['title']}",
        f"    desc={snap['desc_len']} req={snap['req_len']} | "
        f"strong_ec={snap['strong_ec']} bach={snap['bachelors_req']} "
        f"tech={snap['tech_field']} senior={snap['senior_exp']}",
        f"    classify={snap['classify']} ({snap['reason']})",
    ]
    if snap["req_snippet"]:
        lines.append(f"    req: {snap['req_snippet']}...")
    else:
        lines.append("    req: (none parsed)")
    lines.append(f"    url: {snap['url']}")
    return lines


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser()
    p.add_argument(
        "--examples", type=int, default=3,
        help="Max example jobs to print per ATS (default 3)",
    )
    args = p.parse_args()

    companies = [c for c in load_registry() if c.get("ats") != "tier3_todo"]
    results: list[CompanyStats] = []
    by_ats: dict[str, AtsRollup] = defaultdict(AtsRollup)

    lines: list[str] = []
    w = lines.append

    w("=" * 88)
    w("DESCRIPTION + REQUIREMENTS AUDIT")
    w("=" * 88)
    w(
        f"{'Company':<22} {'ATS':<16} {'Jobs':>5} {'Desc%':>6} "
        f"{'Req%':>6} {'EC%':>6} {'Bach%':>6}  Notes"
    )
    w("-" * 88)

    for company in sorted(companies, key=lambda c: (c.get("ats", ""), c.get("name", ""))):
        stats = audit_company(company)
        results.append(stats)
        roll = by_ats[stats.ats]
        roll.companies += 1
        if stats.error:
            roll.errors += 1
            w(f"{stats.name:<22} {stats.ats:<16} {'—':>5} {'—':>6} {'—':>6} {'—':>6} {'—':>6}  ERR")
            continue

        roll.jobs += stats.jobs
        roll.with_desc += stats.with_desc
        roll.with_req += stats.with_req
        roll.with_strong_ec += stats.with_strong_ec
        roll.with_bachelors += stats.with_bachelors

        note = ""
        if stats.with_desc == 0:
            note = "no descriptions"
        elif stats.with_req == 0:
            note = "no req parsed"
        elif stats.with_req < stats.with_desc * 0.5:
            note = "low req parse"

        w(
            f"{stats.name:<22} {stats.ats:<16} {stats.jobs:>5} "
            f"{pct(stats.with_desc, stats.jobs):>6} "
            f"{pct(stats.with_req, stats.with_desc):>6} "
            f"{pct(stats.with_strong_ec, stats.with_desc):>6} "
            f"{pct(stats.with_bachelors, stats.with_desc):>6}  {note}"
        )

        if stats.example and stats.example.get("req_len", 0) > 0:
            if len(roll.examples) < args.examples:
                roll.examples.append(stats.example)
        if stats.missing_req_sample and len(roll.missing) < args.examples:
            roll.missing.append(stats.missing_req_sample)

    w("=" * 88)
    w("BY ATS")
    w("-" * 88)
    w(
        f"{'ATS':<16} {'Cos':>4} {'Jobs':>6} {'Desc%':>7} {'Req%':>7} "
        f"{'EC%':>7} {'Bach%':>7} {'Err':>4}"
    )
    w("-" * 88)

    total_jobs = total_desc = total_req = 0
    for ats in sorted(by_ats):
        r = by_ats[ats]
        total_jobs += r.jobs
        total_desc += r.with_desc
        total_req += r.with_req
        w(
            f"{ats:<16} {r.companies:>4} {r.jobs:>6} "
            f"{pct(r.with_desc, r.jobs):>7} "
            f"{pct(r.with_req, r.with_desc):>7} "
            f"{pct(r.with_strong_ec, r.with_desc):>7} "
            f"{pct(r.with_bachelors, r.with_desc):>7} {r.errors:>4}"
        )

    w("-" * 88)
    w(
        f"{'TOTAL':<16} {len(results):>4} {total_jobs:>6} "
        f"{pct(total_desc, total_jobs):>7} "
        f"{pct(total_req, total_desc):>7}"
    )

    w("")
    w("=" * 88)
    w("EXAMPLES BY ATS (parsed requirements)")
    w("=" * 88)
    for ats in sorted(by_ats):
        r = by_ats[ats]
        if not r.examples:
            w(f"\n## {ats} — no examples")
            continue
        w(f"\n## {ats}")
        for i, snap in enumerate(r.examples, 1):
            w("")
            w("\n".join(format_example(f"ok-{i}", snap)))

    w("")
    w("=" * 88)
    w("MISSING REQ PARSE SAMPLES (when desc present but no section)")
    w("=" * 88)
    for ats in sorted(by_ats):
        r = by_ats[ats]
        if not r.missing:
            continue
        w(f"\n## {ats}")
        for i, snap in enumerate(r.missing, 1):
            w("")
            w("\n".join(format_example(f"miss-{i}", snap)))

    w("")
    w("=" * 88)
    w("FLAGGED COMPANIES (Desc>0 but Req<50%)")
    w("=" * 88)
    flagged = [
        s for s in results
        if not s.error and s.with_desc > 0 and s.with_req < s.with_desc * 0.5
    ]
    if not flagged:
        w("  (none)")
    for s in sorted(flagged, key=lambda x: x.with_req / x.with_desc):
        w(
            f"  {s.name} ({s.ats}): req {s.with_req}/{s.with_desc} "
            f"= {pct(s.with_req, s.with_desc)}"
        )

    text = "\n".join(lines) + "\n"
    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    print(f"Report saved to {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
