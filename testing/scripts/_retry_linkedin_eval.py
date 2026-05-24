"""Sequential LinkedIn fetch to supplement eval dataset (avoid 429)."""
from __future__ import annotations

import json
import random
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(SCRIPTS))

from scraper import load_registry
from _cursor_manual_eval import _regex_include, JOBS_PATH, log  # noqa: E402
from adapters import ADAPTER_REGISTRY

TARGET = 200
SLEEP_SEC = 8


def main() -> int:
    companies = [c for c in load_registry() if c.get("ats") == "linkedin"]
    existing: dict[str, dict] = {}
    if JOBS_PATH.exists():
        for line in JOBS_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                existing[row["url"]] = row

    existing_urls = set(existing)
    linkedin_rows = [r for r in existing.values() if r.get("ats") == "linkedin"]
    log(f"Existing linkedin jobs: {len(linkedin_rows)}/{TARGET}")

    for company in companies:
        if len(linkedin_rows) >= TARGET:
            break
        name = company["name"]
        adapter = ADAPTER_REGISTRY.get("linkedin")
        if not adapter:
            continue
        log(f"Fetching {name} (linkedin)...")
        time.sleep(SLEEP_SEC)
        try:
            jobs = adapter(company)
        except Exception as e:
            log(f"  FAIL {name}: {e}")
            continue
        rng = random.Random(hash(name) & 0xFFFFFFFF)
        if len(jobs) > 200:
            jobs = rng.sample(jobs, 200)
        added = 0
        for j in jobs:
            if len(linkedin_rows) >= TARGET:
                break
            if not j.url or j.url in existing_urls:
                continue
            regex_inc, regex_reason, regex_source = _regex_include(
                j.company, j.title, j.location, j.description, j.url
            )
            desc = j.description or ""
            row = {
                "company": j.company,
                "ats": j.ats,
                "title": j.title,
                "location": j.location,
                "url": j.url,
                "desc_len": len(desc),
                "description": desc[:8000],
                "regex_include": regex_inc,
                "regex_reason": regex_reason,
                "regex_source": regex_source,
            }
            existing[j.url] = row
            existing_urls.add(j.url)
            linkedin_rows.append(row)
            added += 1
        log(f"  {name}: +{added} (linkedin bucket {len(linkedin_rows)}/{TARGET})")

    # Rebuild file: non-linkedin + linkedin bucket
    non_li = [r for r in existing.values() if r.get("ats") != "linkedin"]
    final = non_li + linkedin_rows[:TARGET]
    with JOBS_PATH.open("w", encoding="utf-8") as fh:
        for row in final:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    log(f"Wrote {len(final)} jobs ({len(linkedin_rows[:TARGET])} linkedin)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
