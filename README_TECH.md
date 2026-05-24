# Serverless ATS Job Sniper — Technical Documentation

> The user-facing [README.md](README.md) is auto-generated each run: open positions,
> stats, and apply links. This document covers architecture, filtering strategy,
> evaluation results, and the full company registry.

Hourly pipeline that queries **public** job-board APIs (no login), filters for
early-career technical roles, deduplicates with git-backed JSON state, notifies
Discord, and commits updated state back to the repo. **Zero servers, zero database.**

---

## Architecture

```mermaid
flowchart TB
  subgraph trigger [GitHub Actions hourly]
    CRON[cron / workflow_dispatch]
  end

  subgraph fetch [Parallel fetch - 4 workers]
    YAML[companies.yaml]
    ADAPT[ATS adapters x18]
    YAML --> ADAPT
    ADAPT --> GH[Greenhouse / Ashby / Lever]
    ADAPT --> WD[Workday / Microsoft / Apple]
    ADAPT --> GC[Google Careers + filters]
    ADAPT --> OTHER[Uber / Gem / Eightfold / ...]
  end

  subgraph classify [Per job]
    PRE[Title pre-filter obvious rejects]
    REGEX[classify_title_confidence]
    DESC[Lazy description fetch when title uncertain]
    US[US location filter]
  end

  subgraph state [Git-backed state]
    SEEN[seen_jobs.json - Discord dedupe]
    ARCH[jobs_archive.json - README table]
    STATS[company_stats.json - slug rot]
  end

  CRON --> fetch
  fetch --> classify
  classify --> SEEN
  classify --> ARCH
  classify --> DISCORD[Discord webhook]
  classify --> README[render README.md]
  SEEN --> COMMIT[git commit + push]
  ARCH --> COMMIT
  STATS --> COMMIT
  README --> COMMIT
```

### Pipeline (one run)

1. **Load** `companies.yaml` (**111 active** companies; no `tier3_todo` entries).
2. **Fetch** all active companies in parallel (`ATS_SNIPER_FETCH_WORKERS`, default 4).
   - Log `Company: fetched N postings` as each company completes.
   - Optional caps: `ATS_SNIPER_MAX_LIST_PAGES`, `ATS_SNIPER_MAX_JOBS_PER_COMPANY` (set in CI).
3. **Classify** every posting: regex on title (+ description when fetched).
4. **US filter** (default on; `ATS_SNIPER_ALL_LOCATIONS=1` disables).
5. **Archive** all matches into `jobs_archive.json` (drives README; tracks closed roles).
6. **Discord** only for URLs not in `seen_jobs.json`; mark seen after notify.
7. **Prune** `seen_jobs.json` entries older than 90 days.
8. **Regenerate** `README.md`, write `latest_jobs.md`, commit state files.

Per-company failures are isolated (logged + skipped); one broken slug does not abort the run.

---

## Strategies

### 1. ATS adapters (breadth)

| ATS | Adapter | Active companies | Fetch pattern |
|-----|---------|------------------|---------------|
| Greenhouse | `greenhouse.py` | 39 | Single JSON list (`?content=true`) |
| Ashby | `ashby.py` | 35 | Single public API |
| Lever | `lever.py` | 5 | Single JSON list |
| Google Careers | `google_careers.py` | 4 | Paginated HTML embedded JSON |
| Workday | `workday.py` | 5 | POST pagination (20/page) |
| LinkedIn | `linkedin.py` | 10 | Guest search API |
| Gem | `gem.py` | 3 | GraphQL job board |
| Recruitee | `recruitee.py` | 1 | Public offers API |
| Wiz | `wiz.py` | 1 | Next.js careers JSON proxy |
| Coinbase | `coinbase.py` | 1 | Careers REST API + GH fallback |
| Microsoft | `microsoft.py` | 1 | PCSX search API (50/page) |
| Apple | `apple.py` | 1 | HTML search pages |
| Uber | `uber.py` | 1 | Careers search API |
| Eightfold | `eightfold.py` | 1 | Batched JSON (Netflix) |
| Workable | `workable.py` | 1 | Widget API |
| Rippling | `rippling.py` | 1 | Public jobs API |
| SmartRecruiters | `smartrecruiters.py` | 1 | Offset pagination |
| Jibe | `jibe.py` | 1 | Paginated JSON |

**Meta** uses the LinkedIn adapter (`linkedin_company_id: 10667`) because metacareers.com blocks datacenter IPs.

**Wiz** uses a custom adapter against `wiz.io/api/fetch-jobs-data`.

**Coinbase** uses a custom adapter against `coinbase.com/api/v2/careers` (falls back to private Greenhouse slug `cdpjobs`). Both endpoints are currently returning errors from Coinbase's side; the adapter is wired for when they recover.

### 2. Regex classifier (`filters.py` + `classifier.py`)

Pipeline entry point: **`classify_job()`** in `classifier.py` (prefilter → `classify_title_confidence` → education tags → US gate).

Two-stage logic in `filters.py`:

- **`is_obvious_reject(title)`** — conservative title prefilter (`_OBVIOUS_NON_TECH` checked before `_PREFILTER_NEVER_REJECT` so `Junior Clinical…` is not saved by `junior`).
- **`should_fetch_description(title)`** — skip per-job detail HTTP when title-only classification is already decisive (major speed win on Google/Microsoft/Workday).
- **`classify_title_confidence(title, description)`** — include/exclude with reasons (open-level IC, intern, new grad, MTS, HFC fellowships, non-tech intern exclusions, etc.).

**Include signals (examples):** intern, new grad, university graduate, early career, campus, PhD early-career tracks, open-level SWE titles only when description has EC/YOE signals (not bare `2026` in title alone).

**Hard excludes (examples):** senior, staff, principal, director, manager, VP, non-technical intern titles, expert/HFC fellowships, experienced ladder titles (Engineer II/III, Scientist II, Level 4+, P2–P9) even when title also says `Graduate 2026`, safe non-tech prefilter hits (counsel, equipment technician, quant portfolio analyst, operations associate, etc.).

**US locations:** `is_us_location()` + optional description fallback; ambiguous `Remote` / `N Locations` return false in strict mode.

**Education tags (`education.py`):** requirements-first tags (Intern, New Grad, Early Career for Engineer I, degree paths). `is_hard_experienced_ladder(title)` suppresses all tags on mid-level cohort branding (e.g. `Graduate 2026 … Engineer II`).

**Posted dates (`date_parser.py`):** normalizes ATS fields to `YYYY-MM-DD`. LinkedIn list cards: relative (`2 days ago`, `yesterday`) and absolute (`May 24, 2026`). Archive `upsert` overwrites `posted_date` when the ATS provides one (fixes first-run `first_seen` clustering).

### 3. Google Careers sidebar filters

Unfiltered Google search is ~**4,000** jobs (~200 pages). Production uses the same URL params as the careers UI:

```text
target_level=EARLY
target_level=INTERN_AND_APPRENTICE
sort_by=date
```

Configured in `companies.yaml` under `google_target_levels` / `google_sort_by`. Reduces the Google board to ~**440** jobs (~22 pages) while keeping full EC/intern coverage on that filtered catalog.

Other `google_careers` entries use `google_company` (DeepMind, Waymo, Isomorphic Labs).

### 4. GitHub Actions performance

| Setting | Value | Purpose |
|---------|-------|---------|
| `timeout-minutes` | 45 | Avoid 20m kill mid-run (fetch + classify all companies) |
| `ATS_SNIPER_FETCH_WORKERS` | 4 | Parallel company fetch (non-LinkedIn only; LinkedIn is always serial) |
| `ATS_SNIPER_LINKEDIN_DELAY_SEC` | 6 | Pause between LinkedIn company fetches |
| `ATS_SNIPER_LINKEDIN_PAGE_DELAY_SEC` | 0.75 | Pause between LinkedIn search pages |
| `ATS_SNIPER_EVAL_FETCH_WORKERS` | 4 | Parallel workers for eval fetch (non-LinkedIn) |
| `ATS_SNIPER_MAX_LIST_PAGES` | 60 | Cap Google/Microsoft/Workday/Apple list depth in CI |
| `ATS_SNIPER_MAX_JOBS_PER_COMPANY` | 1200 | Cap single-response megaboards (e.g. Anduril ~1.9k) |
| `ATS_SNIPER_RESET_STATE` | — | Set to `1` (or use workflow **reset_state**) to wipe `seen_jobs.json`, `jobs_archive.json`, and `company_stats.json` before the run |

**LinkedIn HTTP 429:** The guest jobs API rate-limits aggressively when many companies are hit at once. The scraper fetches all `linkedin` registry entries **one at a time** with backoff on 429. If you still see warnings, wait 15–30 minutes, re-run, or raise `ATS_SNIPER_LINKEDIN_DELAY_SEC` (e.g. `10`). For eval LinkedIn backfill only: `python testing/scripts/_retry_linkedin_eval.py` (8s between companies).

### 5. State and deduplication

| File | Role |
|------|------|
| `seen_jobs.json` | URL → first-seen time; Discord only fires on new URLs |
| `jobs_archive.json` | All matched jobs ever seen; `is_closed` when URL disappears from a later scrape |
| `company_stats.json` | Per-company posting/match counts; **slug-rot** warning if matches drop to zero |
| `latest_jobs.md` | Human-readable log of the latest Discord batch |

**Archive self-heal:** Each run only `upsert`s URLs that still pass classify. Jobs that no longer match are not touched that run; `close_unseen()` marks them `is_closed` when their company is scraped successfully. README open table drops them on the next render.

**Fresh start:** Run Actions → **ATS Sniper** → **Run workflow** with **reset_state** checked, or locally `ATS_SNIPER_RESET_STATE=1 python scraper.py`. That clears old README rows and re-notifies every current match once (Discord summary if &gt;50).

---

## Results so far

### Production (live scraper)

From the latest committed [README.md](README.md) stats (updates every hourly run):

| Metric | Value |
|--------|-------|
| Open positions (US EC matches in archive) | **251** |
| All-time URLs tracked in archive | **252** |
| Active companies in registry | **102** |
| Last README update | 2026-05-21 17:14 UTC |

Discord alerts only fire for **new** URLs (not already in `seen_jobs.json`). After warm-up, hourly noise drops sharply.

**Operational note:** Early GHA runs hit the 20-minute timeout while processing ~4k Google + ~2k Anduril-class boards. Recent changes (45m timeout, Google EC filters, list/job caps, fetch logging) target a full 102-company pass each hour.

### Manual eval vs regex (`testing/eval/`)

Two modes:

1. **Regression** — per-ATS sample (`fetch --per-ats 200`) with labels in `cursor_eval_labels.jsonl`.
2. **Discovery** — biased sample (`fetch-discovery`) overweighting regex positives, borderline titles, and new adapters; outputs `eval_recommendations.md` with grouped FP/FN fixes.

Track **precision on regex-positive** jobs (not accuracy — most rows are true negatives). Gold regressions: `testing/eval/eval_gold.jsonl` + `pytest tests/test_eval_regression.py`.

```bash
# Full corpus for hand-labeling (all postings, ~8k–25k jobs; 30–90 min)
python testing/scripts/_cursor_manual_eval.py fetch-full

# Regression sample (capped per ATS type — NOT the full corpus)
python testing/scripts/_cursor_manual_eval.py fetch --per-ats 200

# Full local run (deterministic labels, no API key)
set ATS_SNIPER_EVAL_DETERMINISTIC=1
python testing/scripts/_cursor_manual_eval.py run --per-ats 80

# Or step-by-step (sample eval)
python testing/scripts/_cursor_manual_eval.py fetch --per-ats 200
python testing/scripts/_llm_eval_label.py label
python testing/scripts/_cursor_manual_eval.py rescore
python testing/scripts/_cursor_manual_eval.py score
python testing/scripts/_cursor_manual_eval.py sync-gold
python testing/scripts/_eval_metrics.py
pytest tests/test_eval_regression.py -q

# Discovery-only (after fetch)
python testing/scripts/_cursor_manual_eval.py fetch-discovery --max-jobs 600
python testing/scripts/_cursor_manual_eval.py discovery-label
python testing/scripts/_cursor_manual_eval.py discovery-score
```

Reports: `cursor_eval_report.json`, `cursor_eval_discovery_report.json`, `eval_recommendations.md`.

---

## Company registry and job board links

Source of truth: [`companies.yaml`](companies.yaml). Regenerate this table after registry edits:

```bash
python scripts/company_portal_links.py
```

### Active companies (111)

<!-- 111 active, 0 tier3_todo -->
| Company | Category | ATS | Job board |
|---------|----------|-----|-----------|
| AMD | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Adobe | big_tech | `workday` | [Open board](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced) |
| Airbnb | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/airbnb) |
| Amazon Web Services (AWS) | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Apple | big_tech | `apple` | [Open board](https://jobs.apple.com/en-us/search) |
| Atlassian | big_tech | `smartrecruiters` | [Open board](https://careers.smartrecruiters.com/Atlassian) |
| CrowdStrike | big_tech | `workday` | [Open board](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers) |
| Datadog | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/datadog) |
| Discord | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/discord) |
| DoorDash | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/doordashusa) |
| Google | big_tech | `google_careers` | [Open board](https://www.google.com/about/careers/applications/jobs/results?target_level=EARLY&target_level=INTERN_AND_APPRENTICE&sort_by=date) |
| LinkedIn | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Lyft | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/lyft) |
| Meta | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Microsoft | big_tech | `microsoft` | [Open board](https://apply.careers.microsoft.com/careers) |
| MongoDB | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/mongodb) |
| Netflix | big_tech | `eightfold` | [Open board](https://explore.jobs.netflix.net) |
| Palantir | big_tech | `lever` | [Open board](https://jobs.lever.co/palantir) |
| Palo Alto Networks | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Pinterest | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/pinterest) |
| Reddit | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/reddit) |
| Roblox | big_tech | `greenhouse` | [Open board](https://boards.greenhouse.io/roblox) |
| Shopify | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Snap | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Snowflake | big_tech | `ashby` | [Open board](https://jobs.ashbyhq.com/snowflake) |
| Spotify | big_tech | `lever` | [Open board](https://jobs.lever.co/spotify) |
| Tesla | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Uber | big_tech | `uber` | [Open board](https://www.uber.com/careers/list/) |
| Zillow | big_tech | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Benchling | biotech | `ashby` | [Open board](https://jobs.ashbyhq.com/benchling) |
| Click Therapeutics | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/clicktherapeutics) |
| EvolutionaryScale | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/biohub) |
| Flatiron Health | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/flatironhealth) |
| Generate Biomedicines | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/generatebiomedicines) |
| Genesis Therapeutics | biotech | `ashby` | [Open board](https://jobs.ashbyhq.com/genesis) |
| Headway | biotech | `ashby` | [Open board](https://jobs.ashbyhq.com/headway) |
| Inceptive | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/inceptive) |
| Insitro | biotech | `ashby` | [Open board](https://jobs.ashbyhq.com/insitro) |
| Isomorphic Labs | biotech | `google_careers` | [Open board](https://www.google.com/about/careers/applications/jobs/results?company=Isomorphic+Labs) |
| Pathos AI | biotech | `ashby` | [Open board](https://jobs.ashbyhq.com/pathos) |
| Recursion Pharma | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/recursionpharmaceuticals) |
| Tempus AI | biotech | `workday` | [Open board](https://tempus.wd5.myworkdayjobs.com/en-US/Tempus_Careers) |
| Verily | biotech | `workday` | [Open board](https://verily.wd1.myworkdayjobs.com/en-US/Verily_Careers) |
| Xaira Therapeutics | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/xairatherapeutics) |
| Zocdoc | biotech | `greenhouse` | [Open board](https://boards.greenhouse.io/zocdoc) |
| Anyscale | enterprise | `lever` | [Open board](https://jobs.lever.co/anyscale) |
| Clay | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/claylabs) |
| ClickHouse | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/clickhouse) |
| Cloudflare | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/cloudflare) |
| Cognition AI | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/cognition) |
| Coinbase | enterprise | `coinbase` | [Open board](https://www.coinbase.com/careers/positions) |
| Confluent | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/confluent) |
| Databricks | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/databricks) |
| Decagon | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/decagon) |
| ElevenLabs | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/elevenlabs) |
| Etched | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/etched) |
| Figma | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/figma) |
| Hebbia | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/hebbia-ai) |
| Linear | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/linear) |
| Modal Labs | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/modal) |
| Notion | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/notion) |
| Plaid | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/plaid) |
| Ramp | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/ramp) |
| Replit | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/replit) |
| Retool | enterprise | `gem` | [Open board](https://jobs.gem.com/retool) |
| Rippling | enterprise | `rippling` | [Open board](https://ats.rippling.com/rippling/jobs) |
| Robinhood | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/robinhood) |
| Runway ML | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/runway-ml) |
| Sierra | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/sierra) |
| Stripe | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/stripe) |
| Together AI | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/togetherai) |
| Veeva Systems | enterprise | `lever` | [Open board](https://jobs.lever.co/veeva) |
| Vercel | enterprise | `greenhouse` | [Open board](https://boards.greenhouse.io/vercel) |
| Warp | enterprise | `ashby` | [Open board](https://jobs.ashbyhq.com/warp) |
| Anthropic | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/anthropic) |
| Cohere | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/cohere) |
| CoreWeave | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/coreweave) |
| Cursor | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/cursor) |
| Fireworks AI | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/fireworksai) |
| Glean | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/gleanwork) |
| Google DeepMind | frontier_ai | `google_careers` | [Open board](https://www.google.com/about/careers/applications/jobs/results?company=DeepMind) |
| Groq | frontier_ai | `gem` | [Open board](https://jobs.gem.com/groq) |
| Harvey | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/harvey) |
| Hugging Face | frontier_ai | `workable` | [Open board](https://apply.workable.com/huggingface) |
| Lambda Labs | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/lambda) |
| LangChain | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/langchain) |
| Magic AI | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/magic.dev) |
| Mercor | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/mercor) |
| Nvidia | frontier_ai | `workday` | [Open board](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite) |
| OpenAI | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/openai) |
| Perplexity AI | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/perplexity) |
| Pinecone | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/pinecone) |
| Reka AI | frontier_ai | `ashby` | [Open board](https://jobs.ashbyhq.com/reka) |
| Scale AI | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/scaleai) |
| Wiz | frontier_ai | `wiz` | [Open board](https://www.wiz.io/careers) |
| World Labs | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/worldlabs) |
| xAI | frontier_ai | `greenhouse` | [Open board](https://boards.greenhouse.io/xai) |
| DRW | quant | `greenhouse` | [Open board](https://boards.greenhouse.io/drweng) |
| Point72 | quant | `greenhouse` | [Open board](https://boards.greenhouse.io/point72) |
| 1X Technologies | robotics | `recruitee` | [Open board](https://1x.recruitee.com) |
| Anduril | robotics | `greenhouse` | [Open board](https://boards.greenhouse.io/andurilindustries) |
| Applied Intuition | robotics | `greenhouse` | [Open board](https://boards.greenhouse.io/appliedintuition) |
| Apptronik | robotics | `greenhouse` | [Open board](https://boards.greenhouse.io/apptronik) |
| Boston Dynamics | robotics | `linkedin` | [Open board](https://www.linkedin.com/jobs/search/) |
| Figure AI | robotics | `greenhouse` | [Open board](https://boards.greenhouse.io/figureai) |
| Luma AI | robotics | `gem` | [Open board](https://jobs.gem.com/lumalabs-ai) |
| Physical Intelligence | robotics | `ashby` | [Open board](https://jobs.ashbyhq.com/physicalintelligence) |
| Shield AI | robotics | `lever` | [Open board](https://jobs.lever.co/shieldai) |
| Skydio | robotics | `ashby` | [Open board](https://jobs.ashbyhq.com/skydio) |
| SpaceX | robotics | `greenhouse` | [Open board](https://boards.greenhouse.io/spacex) |
| Waymo | robotics | `google_careers` | [Open board](https://www.google.com/about/careers/applications/jobs/results?company=Waymo) |

### Tier 3 - tracked, not scraped yet

| Company | Category | Notes |
|---------|----------|-------|

---

## Project layout

```
serverless-ats-sniper/
├── README.md                 # AUTO-GENERATED open positions table
├── README_TECH.md            # This file
├── scraper.py                # Orchestrator
├── fetch_limits.py           # CI list/job caps
├── companies.yaml            # Company registry
├── filters.py                # Regex + description signals
├── description_signals.py    # Requirement parsing helpers
├── education.py              # Education column tags
├── date_parser.py            # Posted-date normalization
├── classifier.py             # classify_job() wrapper
├── state.py / jobs_archive.py / company_stats.py
├── notifier.py / render_readme.py
├── discovery.py              # Slug verifier
├── review.py                 # Manual audit CLI
├── adapters/                 # Per-ATS fetch modules
├── testing/                  # Eval scripts + reports (see testing/README.md)
├── scripts/company_portal_links.py
└── .github/workflows/scraper.yml
```

---

## Setup

### 1. Fork or clone

```bash
git clone https://github.com/Agnikulu/Job-Postings.git
cd Job-Postings
pip install -r requirements.txt
```

### 2. Discord webhook

Server Settings → Integrations → Webhooks → New Webhook. Add URL as GitHub secret `DISCORD_WEBHOOK`.

### 3. Enable Actions

Repo **Settings → Actions → General**: enable workflows, grant **Read and write** to `GITHUB_TOKEN` (state commit step).

### 4. Verify slugs

```bash
python discovery.py
```

### 5. Run locally

```bash
# Dry-run (no DISCORD_WEBHOOK)
python scraper.py

export DISCORD_WEBHOOK="https://discord.com/api/webhooks/..."
python scraper.py
```

### 6. Tests

```bash
pytest -q
```

---

## Adding a company

1. Find the public careers API (DevTools → Network: `boards-api`, `ashbyhq`, `lever.co`, `myworkdayjobs`, etc.).
2. Add to `companies.yaml` with `ats`, `slug` (or Workday/Google fields).
3. `python discovery.py` → confirm OK.
4. Regenerate portal table: `python scripts/company_portal_links.py`.

### Google Careers optional fields

```yaml
- name: Google
  ats: google_careers
  google_target_levels:
    - EARLY
    - INTERN_AND_APPRENTICE
  google_sort_by: date
  google_location: United States   # optional
  google_q: software engineer      # optional search box
```

---

## Reliability notes

- **Cron jitter:** GitHub Actions hourly cron is best-effort (often +5–20 min).
- **Slug rot:** `company_stats.json` warns when a company goes from N matches to 0 with stable posting count.
- **State size:** `seen_jobs.json` pruned at 90 days; archive grows with open+closed history.
- **First run:** Cold `seen_jobs.json` can produce 50+ Discord matches → single summary embed with link to `latest_jobs.md`.

---

## Roadmap

- Greenhouse list fetch without full `content=true` for every job (Anduril-scale boards)
- Monitor Coinbase careers API (`/api/v2/careers`) recovery; GH slug `cdpjobs` currently 404
- Optional `google_location: United States` on main Google entry
- Safe `_OBVIOUS_NON_TECH` expansions from eval discovery (content moderation, robot teleop ops, etc.)
- LinkedIn `linkedin_company_id` audit when listings look cross-employer
