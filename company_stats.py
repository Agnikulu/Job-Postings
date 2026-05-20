"""Per-company stats tracking — the slug-rot canary.

Stores per-company counts across runs in `company_stats.json` so we can
detect when a previously-active company suddenly returns 0 matches (likely
slug rot, ATS migration, or a private board). Also catches the opposite:
a quiet company suddenly spiking, which is usually fine but worth noticing.

Schema:
    {
      "Anthropic": {
        "last_postings": 387,
        "last_matches": 0,
        "last_run": "2026-05-20T22:55:00+00:00",
        "history": [
          {"ts": "2026-05-20T22:55:00+00:00", "postings": 387, "matches": 0}
        ]
      },
      ...
    }

History is capped at MAX_HISTORY entries per company.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

MAX_HISTORY = 24  # ~1 day of hourly runs

# Heuristics for slug-rot detection.
ROT_PREV_THRESHOLD = 3      # had at least this many matches last run
ROT_DROP_RATIO = 0.0        # now returning exactly 0
POSTING_PLUNGE_RATIO = 0.5  # postings dropped to half or less


class CompanyStats:
    def __init__(self, path: str | Path = "company_stats.json") -> None:
        self.path = Path(path)
        self._data: dict[str, dict[str, Any]] = {}

    @classmethod
    def load(cls, path: str | Path = "company_stats.json") -> "CompanyStats":
        inst = cls(path)
        if not inst.path.exists():
            return inst
        try:
            inst._data = json.loads(inst.path.read_text(encoding="utf-8")) or {}
        except json.JSONDecodeError as e:
            log.error("company_stats.json corrupt (%s); starting fresh", e)
            inst._data = {}
        if not isinstance(inst._data, dict):
            inst._data = {}
        return inst

    def record(self, name: str, postings: int, matches: int) -> list[str]:
        """Record one run for `name` and return list of warnings (if any)."""
        warnings: list[str] = []
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        prev = self._data.get(name) or {}

        prev_postings = int(prev.get("last_postings") or 0)
        prev_matches = int(prev.get("last_matches") or 0)

        if prev_matches >= ROT_PREV_THRESHOLD and matches == 0:
            warnings.append(
                f"{name}: SLUG-ROT canary — was {prev_matches} matches, now 0 "
                f"(postings: {prev_postings} -> {postings})"
            )
        if (
            prev_postings >= 50
            and postings < prev_postings * POSTING_PLUNGE_RATIO
        ):
            warnings.append(
                f"{name}: posting count plunge — {prev_postings} -> {postings}"
            )

        history = list(prev.get("history") or [])
        history.append({"ts": now, "postings": postings, "matches": matches})
        if len(history) > MAX_HISTORY:
            history = history[-MAX_HISTORY:]

        self._data[name] = {
            "last_postings": postings,
            "last_matches": matches,
            "last_run": now,
            "history": history,
        }
        return warnings

    def save(self) -> None:
        sorted_data = dict(sorted(self._data.items()))
        self.path.write_text(
            json.dumps(sorted_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def __len__(self) -> int:
        return len(self._data)
