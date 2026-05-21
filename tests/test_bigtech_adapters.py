"""Unit tests for big-tech ATS adapters."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters.apple import fetch as fetch_apple
from adapters.eightfold import fetch as fetch_eightfold
from adapters.google_careers import fetch as fetch_google_careers
from adapters.linkedin import fetch as fetch_linkedin
from adapters.microsoft import fetch as fetch_microsoft


def test_eightfold_fetch_maps_fields() -> None:
    payload = {
        "count": 1,
        "positions": [
            {
                "id": 123,
                "name": "Software Engineer",
                "location": "USA - Remote",
                "department": "Engineering",
                "t_update": 1779148800,
                "canonicalPositionUrl": "https://explore.jobs.netflix.net/careers/job/123",
            }
        ],
    }
    company = {
        "name": "Netflix",
        "careers_host": "explore.jobs.netflix.net",
        "domain": "netflix.com",
        "category": "big_tech",
    }
    with patch("adapters.eightfold._get_batch", return_value=payload):
        jobs = fetch_eightfold(company)
    assert len(jobs) == 1
    assert jobs[0].title == "Software Engineer"
    assert jobs[0].ats == "eightfold"


def test_google_careers_fetch_maps_fields() -> None:
    page_jobs = [
        [
            "102644388273758918",
            "Software Engineer",
            "https://www.google.com/about/careers/applications/jobs/results/102644388273758918",
            None,
            None,
            None,
            None,
            "Google",
            None,
            [["Sunnyvale, CA, USA"]],
            None,
            None,
            [1779336019, 585000000],
        ]
    ]
    company = {"name": "Google", "category": "big_tech"}
    with patch("adapters.google_careers._get_page", side_effect=[page_jobs, []]):
        jobs = fetch_google_careers(company)
    assert len(jobs) == 1
    assert jobs[0].location == "Sunnyvale, CA, USA"
    assert jobs[0].ats == "google_careers"


def test_microsoft_fetch_maps_fields() -> None:
    company = {"name": "Microsoft", "domain": "microsoft.com", "category": "big_tech"}
    with patch(
        "adapters.microsoft._get_page",
        side_effect=[
            {"data": {"positions": [{"id": 1, "name": "Software Engineer II", "standardizedLocations": ["Redmond, WA, US"], "postedTs": 1779315378, "department": "Software Engineering", "positionUrl": "/careers/job/1"}], "count": 1}},
            {"data": {"positions": [], "count": 1}},
        ],
    ):
        jobs = fetch_microsoft(company)
    assert jobs[0].location == "Redmond, WA, US"
    assert jobs[0].url.endswith("/careers/job/1")


def test_apple_fetch_maps_fields() -> None:
    html = """
    <a aria-label="Software Engineer 200314033"
       href="/en-us/details/200314033/software-engineer?team=HRDWR">
       Software Engineer
    </a>
    <div id="search-location-search-job-title-PIPE-200314033-1"
         class="column large-4 small-12 text-align-start job-title-location">
      <span class="table--advanced-search__location-sub">Cupertino, CA, US</span>
    </div>
    """
    company = {"name": "Apple", "category": "big_tech"}
    with patch("adapters.apple._get_page", side_effect=[html, ""]):
        jobs = fetch_apple(company)
    assert len(jobs) == 1
    assert jobs[0].title == "Software Engineer"
    assert jobs[0].id == "200314033"
    assert jobs[0].location == "Cupertino, CA, US"


def test_linkedin_fetch_maps_fields() -> None:
    html = """
    <div data-entity-urn="urn:li:jobPosting:12345">
      <a class="base-card__full-link" href="https://www.linkedin.com/jobs/view/12345">link</a>
      <h3 class="base-search-card__title">Software Engineer</h3>
      <span class="job-search-card__location">Sunnyvale, CA</span>
      <time class="job-search-card__listdate">2 days ago</time>
    </div>
    """
    company = {"name": "LinkedIn", "linkedin_company_id": "1337", "category": "big_tech"}
    with patch("adapters.linkedin._get_page", side_effect=[html, ""]):
        jobs = fetch_linkedin(company)
    assert len(jobs) == 1
    assert jobs[0].title == "Software Engineer"
    assert jobs[0].location == "Sunnyvale, CA"
