"""Historical archive of every job posting we've ever observed.

Distinct from `seen_jobs.json`:
  - seen_jobs.json: just URL -> first-seen-timestamp, used to dedupe
    Discord notifications.
  - jobs_archive.json: full posting metadata (title, location, dates,
    education tags, etc.). Used to render the README table.

Schema:
    {
      "<url>": {
        "title": "...",
        "company": "...",
        "location": "...",
        "category": "...",
        "ats": "...",
        "department": "...",
        "education_levels": ["Intern", "PhD"],
        "is_us": true,
        "posted_date": "2026-05-19",     # normalized ATS date
        "first_seen": "2026-05-20T22:55:00+00:00",
        "last_seen":  "2026-05-21T00:23:50+00:00",
        "is_closed": false               # true when the URL stops appearing
      },
      ...
    }
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from adapters import Job

log = logging.getLogger(__name__)


class JobsArchive:
    """Persistent record of every job we've ever seen."""

    def __init__(self, path: str | Path = "jobs_archive.json") -> None:
        self.path = Path(path)
        self._data: dict[str, dict[str, Any]] = {}
        self._touched_this_run: set[str] = set()

    @classmethod
    def load(cls, path: str | Path = "jobs_archive.json") -> "JobsArchive":
        inst = cls(path)
        if not inst.path.exists():
            return inst
        try:
            raw = json.loads(inst.path.read_text(encoding="utf-8")) or {}
        except json.JSONDecodeError as e:
            log.error("jobs_archive.json corrupt (%s); starting fresh", e)
            return inst
        if not isinstance(raw, dict):
            return inst
        inst._data = raw
        return inst

    def upsert(self, job: Job) -> None:
        """Record (or refresh) one observation of `job`."""
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        existing = self._data.get(job.url)
        if existing:
            existing.update(
                title=job.title,
                location=job.location,
                department=job.department,
                category=job.category,
                ats=job.ats,
                education_levels=list(job.education_levels),
                is_us=job.is_us,
                last_seen=now,
                is_closed=False,
            )
            # posted_date should never regress; only fill if missing.
            if job.posted_date and not existing.get("posted_date"):
                existing["posted_date"] = job.posted_date
        else:
            self._data[job.url] = {
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "department": job.department,
                "category": job.category,
                "ats": job.ats,
                "education_levels": list(job.education_levels),
                "is_us": job.is_us,
                "posted_date": job.posted_date,
                "first_seen": now,
                "last_seen": now,
                "is_closed": False,
            }
        self._touched_this_run.add(job.url)

    def close_unseen(self, observed_company_names: set[str]) -> int:
        """Mark URLs as closed if they're from a company we successfully
        scanned this run but their URL didn't reappear.

        Limited to URLs whose company is in `observed_company_names` so we
        don't close everything when a single adapter fails.
        Returns the number of newly-closed entries.
        """
        closed = 0
        for url, entry in self._data.items():
            if entry.get("is_closed"):
                continue
            if entry.get("company") not in observed_company_names:
                continue
            if url not in self._touched_this_run:
                entry["is_closed"] = True
                closed += 1
        return closed

    def save(self) -> None:
        sorted_data = dict(sorted(self._data.items()))
        self.path.write_text(
            json.dumps(sorted_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def entries(self) -> list[dict[str, Any]]:
        """Return [{url, ...}, ...] for rendering."""
        return [
            {"url": url, **entry}
            for url, entry in self._data.items()
        ]

    def __len__(self) -> int:
        return len(self._data)
