"""Render README.md from jobs_archive.json.

Produces a Vansh-style table of all open positions:

  | Company | Role | Location | Source | Education | Apply | Date Posted |

Sort order:
  1. Open positions before closed.
  2. Within each, by posted_date DESC, then first_seen DESC.

Open-positions table can hide intern-only and non-software-discipline
postings using `ATS_SNIPER_DROP_INTERNS` and `ATS_SNIPER_SWE_ONLY`
(default ON for both). Archive JSON is preserved either way.

Run standalone for a manual rebuild:

    python render_readme.py
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from filters import is_intern_only, is_software_or_ai_role
from jobs_archive import JobsArchive

ARCHIVE_PATH = Path(__file__).parent / "jobs_archive.json"
README_PATH = Path(__file__).parent / "README.md"
COMPANIES_PATH = Path(__file__).parent / "companies.yaml"
STATS_PATH = Path(__file__).parent / "company_stats.json"

INTRO = """# Serverless ATS Job Sniper

An auto-updated list of **new-grad / entry-level software, AI/ML, and data
roles** scraped hourly from public job boards: Greenhouse, Lever, Ashby,
Workday, SmartRecruiters, Microsoft Careers, Google Careers, Amazon Jobs,
Uber, LinkedIn guest search, and other company-specific APIs.

**Scope (default):** new-grad / university graduate / Engineer I / early
career / MTS-style full-time entry. Internships, co-ops, and non-software
disciplines (mechanical / civil / aero / propulsion / manufacturing /
RF / antenna / facilities / etc.) are filtered out. US-only.

Built on a free GitHub Actions cron with zero servers and zero ongoing
costs. State (`seen_jobs.json`, `jobs_archive.json`, `company_stats.json`)
is committed back to the repo so the table grows historically.

See [README\\_TECH.md](README_TECH.md) for the project architecture,
how to fork, how to add companies, and how filtering works.
"""

LEGEND = """## Legend

- **Role flag** -> Country (currently US-only, `\U0001F1FA\U0001F1F8`).
- **Source** -> Which adapter fetched the row (`greenhouse`, `linkedin`, `workday`, etc.).
- **Education** -> Tags from job requirements (e.g. `{PhD, PhD Student, Masters, Bachelors, New Grad, Early Career, Intern}`).
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> Best-effort publish date from each ATS (`first_published`,
   `publishedAt`, etc.). LinkedIn/Workday relative strings are pinned to the
   earliest date we parsed. If the board provides no date, shows when we first
   saw the URL (`first_seen`).
"""

CONTRIBUTE = """## How it works

1. Hourly GitHub Action queries each company's public ATS API.
2. Titles run through a regex filter (must hit one of:
   `intern, new grad, university graduate, early career, entry level,
   campus, 2026, 2027`; must NOT hit any of:
   `senior, lead, manager, principal, director, head of, staff, vp,
   president`).
3. Locations are filtered to the US by default.
4. New postings ping a Discord webhook in real-time.
5. State is committed back -- this README is regenerated every run.

Want a different scope? See [README\\_TECH.md](README_TECH.md) -- you can
toggle the US filter, add tier-3 companies, change the cadence, etc.
"""


def _row(entry: dict[str, Any]) -> str:
    company = entry.get("company", "?")
    title = (entry.get("title") or "").replace("|", "\\|").strip()
    # Mark US roles with the flag emoji, matching Vansh's convention.
    if entry.get("is_us"):
        title = f"{title} \U0001F1FA\U0001F1F8"
    location = (entry.get("location") or "-").replace("|", "\\|").strip()
    # Vansh wraps multi-location strings to multiple lines using <br>;
    # we'll do the same so the table doesn't get unreadable wide.
    location = location.replace("; ", "<br>").replace(";", "<br>")
    edu = entry.get("education_levels") or []
    education = ", ".join(edu) if edu else "-"
    url = entry.get("url") or ""
    apply_cell = f"[Apply]({url})" if url else "-"

    if entry.get("is_closed"):
        apply_cell = "Closed"
        company = f"~~{company}~~"
        title = f"~~{title}~~"

    posted = entry.get("posted_date") or _date_from_iso(entry.get("first_seen"))
    posted_display = _format_short_date(posted) if posted else "-"
    source = (entry.get("ats") or "-").replace("|", "\\|").strip()

    return (
        f"| {company} | {title} | {location} | {source} | {education} | "
        f"{apply_cell} | {posted_display} |"
    )


def _date_from_iso(s: str | None) -> str | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date().isoformat()
    except (ValueError, AttributeError):
        return None


def _format_short_date(iso_date: str) -> str:
    try:
        d = datetime.fromisoformat(iso_date).date()
        return d.strftime("%b %d, %Y")
    except (ValueError, AttributeError):
        return iso_date


def _sort_key(entry: dict[str, Any]) -> tuple:
    posted = entry.get("posted_date") or _date_from_iso(entry.get("first_seen")) or "0"
    return (
        0 if not entry.get("is_closed") else 1,   # open first
        posted,                                    # then by date desc
        entry.get("first_seen") or "",
    )


def _drop_interns_enabled() -> bool:
    return os.environ.get("ATS_SNIPER_DROP_INTERNS", "1").strip() != "0"


def _swe_only_enabled() -> bool:
    return os.environ.get("ATS_SNIPER_SWE_ONLY", "1").strip() != "0"


def _passes_render_filters(entry: dict[str, Any]) -> bool:
    """Hide archived rows that don't match the current scope toggles."""
    title = entry.get("title") or ""
    if _drop_interns_enabled() and is_intern_only(title):
        return False
    if _swe_only_enabled() and not is_software_or_ai_role(title):
        return False
    return True


def _load_fetch_stats() -> tuple[int, int] | None:
    """Sum last-run postings/matches from company_stats.json."""
    if not STATS_PATH.exists():
        return None
    try:
        data = json.loads(STATS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(data, dict):
        return None
    postings = 0
    matches = 0
    for row in data.values():
        if not isinstance(row, dict):
            continue
        postings += int(row.get("last_postings") or 0)
        matches += int(row.get("last_matches") or 0)
    return postings, matches


def _count_active_companies() -> int:
    """Quick read of companies.yaml to count active (non-tier3) companies."""
    if not COMPANIES_PATH.exists():
        return 0
    import yaml  # local import to avoid hard dep at module load
    with COMPANIES_PATH.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or []
    return sum(1 for c in data if c.get("ats") != "tier3_todo")


def render(archive: JobsArchive) -> str:
    entries = archive.entries()
    # Hide archived rows that no longer match the current scope toggles
    # (e.g. intern roles when ATS_SNIPER_DROP_INTERNS=1) without deleting
    # them from jobs_archive.json.
    visible = [e for e in entries if _passes_render_filters(e)]
    open_entries = [e for e in visible if not e.get("is_closed")]
    closed_entries = [e for e in visible if e.get("is_closed")]

    open_entries.sort(key=_sort_key, reverse=True)
    closed_entries.sort(key=_sort_key, reverse=True)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    n_open = len(open_entries)
    n_total = len(visible)
    n_companies = _count_active_companies()

    fetch_stats = _load_fetch_stats()

    out: list[str] = [INTRO]
    stats_lines = [
        f"- **Open positions:** {n_open}",
        f"- **All-time tracked:** {n_total}",
        f"- **Active companies:** {n_companies}",
    ]
    if fetch_stats:
        fetched, matched = fetch_stats
        stats_lines.append(
            f"- **Last run (raw / matched):** {fetched} postings fetched, "
            f"{matched} passed filters"
        )
    stats_lines.append(f"- **Last updated:** `{now}`")
    out.append("## Stats\n\n" + "\n".join(stats_lines) + "\n")
    out.append(LEGEND)

    out.append("## Open positions\n")
    if open_entries:
        out.append(
            "| Company | Role | Location | Source | Education | Apply | Date Posted |"
        )
        out.append(
            "|---------|------|----------|--------|-----------|-------|-------------|"
        )
        out.extend(_row(e) for e in open_entries)
        out.append("")
    else:
        out.append("_No open positions match the filters right now._\n")

    if closed_entries:
        out.append(
            f"\n<details>\n<summary><b>Closed positions ({len(closed_entries)})"
            "</b> &mdash; click to expand</summary>\n"
        )
        out.append(
            "\n| Company | Role | Location | Source | Education | Apply | Date Posted |"
        )
        out.append(
            "|---------|------|----------|--------|-----------|-------|-------------|"
        )
        out.extend(_row(e) for e in closed_entries)
        out.append("\n</details>\n")

    out.append(CONTRIBUTE)
    return "\n".join(out) + "\n"


def main() -> int:
    archive = JobsArchive.load(ARCHIVE_PATH)
    README_PATH.write_text(render(archive), encoding="utf-8")
    print(f"Wrote {README_PATH} with {len(archive)} archive entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
