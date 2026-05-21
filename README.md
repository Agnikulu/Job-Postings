# Serverless ATS Job Sniper

An auto-updated list of **early-career engineering roles** scraped hourly
from the public ATS APIs of top tech companies (Greenhouse, Lever, Ashby,
Workday). Filtered for entry-level, internship, new-grad, and university
graduate positions. US-only by default.

Built on a free GitHub Actions cron with zero servers and zero ongoing
costs. State (`seen_jobs.json`, `jobs_archive.json`, `company_stats.json`)
is committed back to the repo so the table grows historically.

See [README\_TECH.md](README_TECH.md) for the project architecture,
how to fork, how to add companies, and how filtering works.

## Stats

- **Open positions:** 0
- **All-time tracked:** 0
- **Active companies:** 53
- **Last updated:** `2026-05-21 00:41 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Education** -> Multi-label tag from `{PhD, Masters, Bachelors, New Grad, Intern}`.
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> When the company posted the role (parsed from each ATS).
   Falls back to when our scraper first observed the URL.

## Open positions

_No open positions match the filters right now._

## How it works

1. Hourly GitHub Action queries each company's public ATS API.
2. Titles run through a regex filter (must hit one of:
   `intern, new grad, university graduate, early career, entry level,
   campus, 2026, 2027`; must NOT hit any of:
   `senior, lead, manager, principal, director, head of, staff, vp,
   president`).
3. Locations are filtered to the US by default.
4. New postings ping a Discord webhook in real-time.
5. State is committed back -- this README is regenerated every run.

Want a different scope? See [README\_TECH.md](README_TECH.md) -- you can
toggle the US filter, add tier-3 companies, change the cadence, etc.

