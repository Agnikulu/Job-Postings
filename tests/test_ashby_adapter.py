"""Unit tests for Ashby adapter."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters.ashby import fetch


def test_fetch_uses_published_at() -> None:
    payload = {
        "jobs": [
            {
                "id": "abc-123",
                "title": "Software Engineer Intern",
                "location": "San Francisco",
                "jobUrl": "https://jobs.ashbyhq.com/example/abc-123",
                "publishedAt": "2026-04-02T21:00:55.755+00:00",
                "department": "Engineering",
            }
        ]
    }
    company = {"name": "Example Co", "slug": "example", "category": "enterprise"}

    with patch("adapters.ashby._get", return_value=payload):
        jobs = fetch(company)

    assert len(jobs) == 1
    assert jobs[0].posted_at == "2026-04-02T21:00:55.755+00:00"
