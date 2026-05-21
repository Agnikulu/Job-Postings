# Serverless ATS Job Sniper — Technical Documentation

> The user-facing README ([README.md](README.md)) is the auto-generated
> Vansh-style table of open positions. This document covers the
> architecture, setup, and how to customize the pipeline.

A fully automated, zero-cost data pipeline that queries the public JSON APIs
of modern Applicant Tracking Systems (Greenhouse, Lever, Ashby, Workday) to
find early-career engineering roles the second they are posted, then pushes
each new role to a Discord channel via webhook. Runs entirely on a free
GitHub Actions cron — no servers, no databases.

## What it does

1. **Fetches** open postings for ~53 active companies across six categories
   (frontier AI, quant, enterprise, robotics, biotech, big tech).
2. **Filters** them against a regex engine:
   - **Must match** one of: `intern`, `internship`, `co-op`, `coop`,
     `new grad`, `university graduate`, `early career`, `entry level`,
     `campus`, `2026`, `2027`.
   - **Must NOT match** any of: `senior`, `sr.`, `lead`, `manager`,
     `principal`, `director`, `head of`, `staff`, `vp`, `president`.
   - **Technical badge** (informational only) when the title contains
     `software`, `engineer`, `ml`, `data`, `quant`, `research`, `hardware`,
     `firmware`, `chip`, `asic`, `fpga`, `cuda`, etc.
3. **Filters by location** to US-only by default. Set
   `ATS_SNIPER_ALL_LOCATIONS=1` to disable.
4. **Tags by education level** — each role is multi-labelled across
   `{PhD, Masters, Bachelors, New Grad, Intern}`.
5. **Normalizes posted dates** from each ATS (Workday's "Posted N Days
   Ago" strings, Lever's epoch ms, Greenhouse/Ashby's ISO8601).
6. **Deduplicates** against `seen_jobs.json` for Discord alerts (committed
   back each run).
7. **Archives** every posting ever observed in `jobs_archive.json` with
   first-seen / last-seen / is-closed tracking. The README's job table is
   rebuilt from this archive every run.
8. **Notifies** Discord with one rich embed per new role (color-coded by
   category, `[TECHNICAL]` prefix where applicable). Falls back to a
   single summary message with a link to `latest_jobs.md` when a run
   produces > 50 new postings.
9. **Detects slug rot** via `company_stats.json`: warns when a previously
   active company suddenly returns 0 matches.

## Coverage

| Tier | ATS | # companies | Status |
|------|-----|-------------|--------|
| 1 | Greenhouse | 44 | live |
| 1 | Ashby | 18 | live |
| 1 | Lever | 1 | live |
| 2 | Workday | 5 | live |
| 3 | Custom careers sites | 26 | stubs in `companies.yaml` (skipped) |

Tier 3 entries (OpenAI, Google, Meta, Apple, Microsoft, LinkedIn,
Netflix, Palantir, SpaceX, xAI, plus the bespoke quant shops like Jane
Street and Jump) all use proprietary careers sites and would each need
their own custom adapter. They're tracked in `companies.yaml` so they
aren't lost, but the orchestrator skips them. Adding a tier-3 adapter is
a one-file change — see `adapters/greenhouse.py` for the pattern.

## Setup

### 1. Fork or push to your own GitHub repo

```bash
cd serverless-ats-sniper
git init
git add .
git commit -m "feat: initial commit"
gh repo create serverless-ats-sniper --private --source=. --push
# or push to an existing remote of your choice
```

### 2. Create a Discord webhook

In your Discord server: **Server Settings → Integrations → Webhooks → New
Webhook**. Pick a channel, copy the webhook URL.

### 3. Add the webhook as a GitHub Actions secret

In the repo: **Settings → Secrets and variables → Actions → New
repository secret**. Name it `DISCORD_WEBHOOK`, paste the URL.

### 4. Enable Actions

In **Settings → Actions → General**, make sure Actions are enabled and
that **Read and write permissions** are granted to `GITHUB_TOKEN` (this
is required so the workflow can commit `seen_jobs.json` back).

### 5. Verify slugs (recommended)

Run `discovery.py` locally to confirm every slug in `companies.yaml`
returns a valid response. Slugs marked tentatively (Citadel,
CoreWeave, etc.) are best guesses and may need updating:

```bash
pip install -r requirements.txt
python discovery.py
```

The script prints `OK` / `BAD` per company and exits non-zero if any
slug is broken. Fix `companies.yaml` and re-run until clean.

### 6. Trigger your first run

Either wait for the next hourly cron, or trigger manually:

```bash
gh workflow run "ATS Sniper"
```

The first run will almost certainly emit more than 50 matches (cold
start), so you'll see one summary message in Discord instead of dozens
of individual alerts. Every subsequent run will only post genuinely
new postings.

## Running locally

```bash
pip install -r requirements.txt
# Dry-run (no webhook env var = prints what it WOULD send)
python scraper.py

# Real run
export DISCORD_WEBHOOK="https://discord.com/api/webhooks/..."
python scraper.py
```

## Running tests

```bash
pip install -r requirements.txt
pytest -q
```

## Project layout

```
serverless-ats-sniper/
├── README.md               # AUTO-GENERATED job table (Vansh-style)
├── README_TECH.md          # This file - architecture and setup
├── scraper.py              # Orchestrator entry point
├── adapters/
│   ├── __init__.py         # ADAPTER_REGISTRY dispatch
│   ├── base.py             # Job dataclass + AdapterError
│   ├── greenhouse.py
│   ├── lever.py
│   ├── ashby.py
│   └── workday.py
├── companies.yaml          # Company registry (single source of truth)
├── filters.py              # Title + US-location regex engine
├── education.py            # Multi-label PhD / MS / BS / NewGrad / Intern tagger
├── date_parser.py          # Normalizes posted dates across ATSes
├── state.py                # seen_jobs.json wrapper (Discord dedupe)
├── jobs_archive.py         # jobs_archive.json wrapper (historical archive)
├── company_stats.py        # company_stats.json wrapper (slug-rot canary)
├── notifier.py             # Discord webhook + rate limiting + summary fallback
├── render_readme.py        # Generates README.md from jobs_archive
├── review.py               # Manual audit tool (--markdown, --diagnose, etc.)
├── discovery.py            # One-time slug verifier
├── seen_jobs.json          # Discord-notification dedupe state
├── jobs_archive.json       # Historical archive (drives README table)
├── company_stats.json      # Per-company match counts & history
├── latest_jobs.md          # Most-recent-run notification log
├── requirements.txt
├── tests/test_filters.py
└── .github/workflows/scraper.yml
```

## Reliability notes

- **Latency.** GitHub Actions cron is best-effort. Expect 5-20 min jitter,
  occasionally up to 30 min during platform peaks. The spec asked for
  "the second they are posted" — that's only possible with a paid VPS or
  a Cloudflare Worker on a 5-min cron. Hourly on Actions is the
  pragmatic free option.
- **Slug rot.** Companies occasionally rename their ATS slug or migrate
  between platforms. `discovery.py` exists specifically to catch this
  drift before it silently breaks coverage.
- **Per-company error isolation.** A single failing company (e.g., 404,
  500, slug change, ATS migration) is logged and skipped — it never
  aborts the run for the other 67.
- **State growth.** `seen_jobs.json` is auto-pruned at 90 days each run.
  At ~50 new postings/day across all companies, the file caps out around
  ~5,000 entries (a few hundred KB). Comfortably within GitHub's file
  size limits.

## Adding a new company

1. Find the company's careers page.
2. Open DevTools → Network tab. Filter for `boards-api`, `jobs.lever.co`,
   `api.ashbyhq.com`, or `myworkdayjobs.com`. The URL gives you the
   slug.
3. Add an entry to `companies.yaml`:
   ```yaml
   - name: New Company
     ats: greenhouse
     slug: newcompany
     category: enterprise
   ```
4. Run `python discovery.py` to confirm the slug works.
5. Commit and push.

## Adding a new ATS

If you find a company on a new ATS (SmartRecruiters, Eightfold, Phenom,
JazzHR, etc.):

1. Create `adapters/<ats>.py` following the pattern in `greenhouse.py`.
2. Export a `fetch(company: dict) -> list[Job]` function.
3. Register it in `adapters/__init__.py`:
   ```python
   ADAPTER_REGISTRY = {
       ...
       "smartrecruiters": fetch_smartrecruiters,
   }
   ```
4. Tag companies with `ats: smartrecruiters` in the registry.

## Roadmap (v2)

- Custom adapters for tier-3 sites (OpenAI, Google careers, Meta GraphQL,
  Apple, Microsoft, Jane Street, Jump, HRT, etc.)
- Location filter (US-only, remote-eligible, or per-country)
- Compensation parsing (extract $XXXk from job description)
- 5-min cadence via Cloudflare Workers cron triggers (paid path to true
  "instant" alerts)
