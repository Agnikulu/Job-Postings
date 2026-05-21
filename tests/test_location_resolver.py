"""Tests for location enrichment."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters.base import Job
from location_resolver import resolve_job_location


def test_resolve_workday_n_locations() -> None:
    job = Job(
        id="JR1",
        company="Nvidia",
        title="Software Engineer Intern",
        location="3 Locations",
        url=(
            "https://nvidia.wd5.myworkdayjobs.com/en-US/"
            "NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/"
            "Software-Engineer-Intern_JR1"
        ),
        posted_at=None,
        department=None,
        ats="workday",
        category="big_tech",
    )
    detail = {
        "jobPostingInfo": {
            "location": "US, CA, Santa Clara",
            "additionalLocations": ["Remote, US"],
        }
    }
    with patch("location_resolver._fetch_workday_locations", return_value="US, CA, Santa Clara; Remote, US"):
        assert "Santa Clara" in resolve_job_location(job)
