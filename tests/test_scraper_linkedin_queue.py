"""LinkedIn queue in scraper.run(): runs alongside other ATSes, oldest first,
and skips companies once the time budget is used up."""

from __future__ import annotations

import json
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import scraper


def _setup(tmp_path, monkeypatch, companies, adapters, stats=None):
    for attr, fname in [
        ("STATE_PATH", "seen_jobs.json"),
        ("STATS_PATH", "company_stats.json"),
        ("ARCHIVE_PATH", "jobs_archive.json"),
        ("README_PATH", "README.md"),
    ]:
        monkeypatch.setattr(scraper, attr, tmp_path / fname)
    if stats:
        (tmp_path / "company_stats.json").write_text(json.dumps(stats))
    monkeypatch.setattr(scraper, "load_registry", lambda: companies)
    monkeypatch.setattr(scraper, "ADAPTER_REGISTRY", adapters)
    monkeypatch.setattr(scraper, "write_latest_jobs_md", lambda *a, **k: None)
    monkeypatch.setattr(scraper.notifier, "send_batch", lambda *a, **k: None)
    monkeypatch.setattr(scraper.email_notifier, "send_batch", lambda *a, **k: None)
    monkeypatch.setenv("ATS_SNIPER_LINKEDIN_DELAY_SEC", "0")
    monkeypatch.setenv("ATS_SNIPER_FETCH_WORKERS", "2")


def test_linkedin_runs_alongside_others_oldest_first(tmp_path, monkeypatch) -> None:
    order: list[str] = []
    other_started = threading.Event()
    linkedin_ran_during_other = []

    def other(company):
        other_started.set()
        # Block until LinkedIn has made progress: proves it isn't queued behind us.
        linkedin_ran_during_other.append(bool(order) or _wait_for(order))
        return []

    def linkedin(company):
        order.append(company["name"])
        return []

    companies = [
        {"name": "Slow ATS", "ats": "other"},
        {"name": "Recent", "ats": "linkedin"},
        {"name": "Never", "ats": "linkedin"},
        {"name": "Old", "ats": "linkedin"},
    ]
    stats = {
        "Recent": {"last_run": "2026-10-13T10:00:00+00:00"},
        "Old": {"last_run": "2026-10-12T10:00:00+00:00"},
    }
    _setup(tmp_path, monkeypatch, companies, {"other": other, "linkedin": linkedin}, stats)
    scraper.run()
    assert order == ["Never", "Old", "Recent"]
    assert linkedin_ran_during_other == [True]


def _wait_for(order: list[str], timeout: float = 5.0) -> bool:
    import time

    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if order:
            return True
        time.sleep(0.01)
    return False


def test_linkedin_budget_skips_remaining_companies(tmp_path, monkeypatch) -> None:
    fetched: list[str] = []
    clock = {"now": 0.0}

    def linkedin(company):
        fetched.append(company["name"])
        clock["now"] += 20 * 60  # each company "takes" 20 minutes
        return []

    companies = [
        {"name": "A", "ats": "linkedin"},
        {"name": "B", "ats": "linkedin"},
        {"name": "C", "ats": "linkedin"},
    ]
    _setup(tmp_path, monkeypatch, companies, {"linkedin": linkedin})
    monkeypatch.setenv("ATS_SNIPER_LINKEDIN_BUDGET_MIN", "35")
    monkeypatch.setattr(scraper.time, "monotonic", lambda: clock["now"])
    monkeypatch.setattr(scraper.time, "sleep", lambda s: None)
    scraper.run()
    assert fetched == ["A", "B"]
    saved = json.loads((tmp_path / "company_stats.json").read_text())
    # Skipped company is not recorded, so it leads the queue next run.
    assert "C" not in saved and {"A", "B"} <= saved.keys()
