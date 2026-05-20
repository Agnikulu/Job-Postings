"""Persistent dedupe state stored in seen_jobs.json.

Schema is a flat dict so lookups are O(1):

    {
      "<job url>": "<ISO8601 first-seen timestamp>",
      ...
    }

The file is committed back to the repo by the GitHub Actions workflow,
giving us a free, durable, version-controlled state store.
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = logging.getLogger(__name__)


class State:
    """Wraps seen_jobs.json with load / is_seen / mark / prune / save."""

    def __init__(self, path: str | os.PathLike[str] = "seen_jobs.json") -> None:
        self.path = Path(path)
        self._data: dict[str, str] = {}

    @classmethod
    def load(cls, path: str | os.PathLike[str] = "seen_jobs.json") -> "State":
        inst = cls(path)
        if not inst.path.exists():
            log.info("State file %s missing; starting fresh", inst.path)
            return inst
        try:
            inst._data = json.loads(inst.path.read_text(encoding="utf-8")) or {}
        except json.JSONDecodeError as e:
            log.error("State file %s is corrupt (%s); starting fresh", inst.path, e)
            inst._data = {}
        if not isinstance(inst._data, dict):
            log.error(
                "State file %s wasn't a dict (was %s); starting fresh",
                inst.path,
                type(inst._data).__name__,
            )
            inst._data = {}
        return inst

    def is_seen(self, url: str) -> bool:
        return url in self._data

    def mark_seen(self, url: str) -> None:
        self._data[url] = datetime.now(timezone.utc).isoformat(timespec="seconds")

    def prune(self, max_age_days: int = 90) -> int:
        """Remove entries older than `max_age_days`. Returns count removed."""
        cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
        before = len(self._data)
        kept: dict[str, str] = {}
        for url, ts in self._data.items():
            try:
                seen_at = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                kept[url] = ts
                continue
            if seen_at >= cutoff:
                kept[url] = ts
        self._data = kept
        removed = before - len(self._data)
        if removed:
            log.info("Pruned %d state entries older than %d days", removed, max_age_days)
        return removed

    def save(self) -> None:
        sorted_data = dict(sorted(self._data.items()))
        self.path.write_text(
            json.dumps(sorted_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def __len__(self) -> int:
        return len(self._data)
