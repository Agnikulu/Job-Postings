"""Discord webhook notifier.

Behavior
--------
- Sends one Discord embed per new job.
- Color-codes the embed by job category.
- Adds a [TECHNICAL] badge to the title when `is_technical=True`.
- Rate-limits to ~25 messages / minute (Discord allows 30; we leave headroom).
- If a single run would emit > BULK_THRESHOLD jobs (likely a first run or a
  major batch dump), falls back to one summary message instead of spamming.

Environment
-----------
- DISCORD_WEBHOOK: Required for actual delivery. If unset, the notifier logs
  what it *would* have sent and returns — useful for local dry runs.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Iterable

import requests

from adapters import Job

log = logging.getLogger(__name__)

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK", "").strip()
BULK_THRESHOLD = 50
MAX_PER_MINUTE = 25  # Discord webhook quota is 30/min; leave a buffer.
SLEEP_BETWEEN = 60.0 / MAX_PER_MINUTE  # ~2.4s

CATEGORY_COLORS = {
    "frontier_ai": 0x9B59B6,  # purple
    "quant": 0x2ECC71,        # green
    "enterprise": 0xF1C40F,   # yellow
    "robotics": 0xE67E22,     # orange
    "biotech": 0x1ABC9C,      # teal
    "big_tech": 0x3498DB,     # blue
    "uncategorized": 0x95A5A6,
}


def _embed_for_job(job: Job, is_technical: bool) -> dict:
    title = job.title or "(no title)"
    if is_technical:
        title = f"[TECHNICAL] {title}"

    fields = [
        {"name": "Company", "value": job.company, "inline": True},
        {"name": "Category", "value": job.category, "inline": True},
        {"name": "Location", "value": job.location or "—", "inline": False},
    ]
    if job.department:
        fields.append({"name": "Department", "value": job.department, "inline": True})

    embed: dict = {
        "title": title[:256],
        "url": job.url,
        "color": CATEGORY_COLORS.get(job.category, CATEGORY_COLORS["uncategorized"]),
        "fields": fields,
        "footer": {"text": f"ATS: {job.ats}"},
    }
    if job.posted_at:
        embed["timestamp"] = job.posted_at
    return embed


def _post(payload: dict) -> bool:
    if not WEBHOOK_URL:
        log.info("DRY RUN (no DISCORD_WEBHOOK): %s", payload.get("embeds", payload))
        return True
    try:
        resp = requests.post(WEBHOOK_URL, json=payload, timeout=15)
        if resp.status_code == 429:
            retry_after = float(resp.headers.get("retry-after", "2"))
            log.warning("Discord 429; sleeping %.1fs", retry_after)
            time.sleep(retry_after + 0.5)
            resp = requests.post(WEBHOOK_URL, json=payload, timeout=15)
        resp.raise_for_status()
        return True
    except requests.RequestException as e:
        log.error("Discord webhook failed: %s", e)
        return False


def send_batch(new_jobs: Iterable[tuple[Job, bool]]) -> int:
    """Send notifications for each (job, is_technical) tuple.

    Returns the number of messages actually sent (or that would have been
    sent in dry-run mode).
    """
    jobs = list(new_jobs)
    if not jobs:
        log.info("No new jobs to notify.")
        return 0

    if len(jobs) > BULK_THRESHOLD:
        log.info(
            "Run produced %d jobs (> %d). Sending summary instead of individual alerts.",
            len(jobs),
            BULK_THRESHOLD,
        )
        return 1 if _send_summary(jobs) else 0

    sent = 0
    for i, (job, is_tech) in enumerate(jobs):
        ok = _post({"embeds": [_embed_for_job(job, is_tech)]})
        if ok:
            sent += 1
        if i + 1 < len(jobs):
            time.sleep(SLEEP_BETWEEN)
    log.info("Notifier sent %d / %d messages.", sent, len(jobs))
    return sent


def _latest_jobs_url() -> str | None:
    """Construct the GitHub URL of latest_jobs.md for the current repo.

    Uses env vars set automatically by GitHub Actions:
      GITHUB_SERVER_URL   (e.g. https://github.com)
      GITHUB_REPOSITORY   (e.g. Agnikulu/Job-Postings)
      GITHUB_REF_NAME     (e.g. main)
    Returns None when not running inside Actions (local dry-run).
    """
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo = os.environ.get("GITHUB_REPOSITORY")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    if not repo:
        return None
    return f"{server}/{repo}/blob/{branch}/latest_jobs.md"


def _send_summary(jobs: list[tuple[Job, bool]]) -> bool:
    by_company: dict[str, int] = {}
    for job, _ in jobs:
        by_company[job.company] = by_company.get(job.company, 0) + 1
    top = sorted(by_company.items(), key=lambda kv: -kv[1])[:15]
    breakdown = "\n".join(f"- **{c}**: {n}" for c, n in top)

    description_parts = ["Too many new postings for individual alerts."]
    link = _latest_jobs_url()
    if link:
        description_parts.append(
            f"**[View all {len(jobs)} jobs with apply links \u2192]({link})**"
        )
    description_parts.append("**Top companies:**\n" + breakdown)
    description = "\n\n".join(description_parts)

    payload = {
        "embeds": [
            {
                "title": f"{len(jobs)} new early-career roles detected",
                "description": description,
                "color": 0xE74C3C,
            }
        ]
    }
    return _post(payload)
