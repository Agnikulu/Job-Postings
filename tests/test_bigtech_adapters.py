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


def test_google_careers_builds_sidebar_filter_params() -> None:
    from adapters.google_careers import _build_query_params

    company = {
        "google_company": "Google",
        "google_target_levels": ["EARLY", "INTERN_AND_APPRENTICE"],
        "google_sort_by": "date",
        "google_location": "United States",
    }
    params = _build_query_params(company, page=3)
    assert ("page", "3") in params
    assert ("company", "Google") in params
    assert ("location", "United States") in params
    assert params.count(("target_level", "EARLY")) == 1
    assert params.count(("target_level", "INTERN_AND_APPRENTICE")) == 1
    assert ("sort_by", "date") in params


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
    with patch(
        "adapters.google_careers._get_page", side_effect=[page_jobs, []]
    ) as mock_get:
        jobs = fetch_google_careers(company)
    assert mock_get.call_args_list[0][0][0][0] == ("page", "1")
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


def _apple_raw(job_id: str, title: str, slug: str, locations: list[dict]) -> dict:
    return {
        "id": job_id,
        "postingTitle": title,
        "transformedPostingTitle": slug,
        "locations": locations,
        "postDateInGMT": "2026-10-01T05:57:40.072Z",
        "team": {"teamName": "Hardware", "teamCode": "HRDWR"},
    }


def test_apple_fetch_maps_fields() -> None:
    page = {
        "totalRecords": 2,
        "searchResults": [
            _apple_raw(
                "PIPE-200314033",
                "Software Engineer",
                "software-engineer",
                [{"name": "Cupertino", "stateProvince": "California",
                  "countryName": "United States of America"}],
            ),
            _apple_raw(
                "200687074-3543",
                "Software Engineer, Satellite Operations",
                "software-engineer-satellite-operations",
                [{"name": "Austin", "countryName": "United States of America"},
                 {"name": "Shanghai", "countryName": "China"}],
            ),
        ],
    }
    company = {"name": "Apple", "category": "big_tech"}
    with patch("adapters.apple._get_page", return_value=page):
        jobs = fetch_apple(company)
    assert len(jobs) == 2
    assert jobs[0].id == "200314033"
    assert jobs[0].title == "Software Engineer"
    assert jobs[0].location == "Cupertino, California, United States of America"
    assert jobs[0].url.endswith("/details/200314033/software-engineer")
    assert jobs[0].posted_at == "2026-10-01T05:57:40.072Z"
    assert jobs[0].department == "Hardware"
    assert jobs[1].id == "200687074-3543"
    assert jobs[1].location == "Austin, United States of America; Shanghai, China"
    assert jobs[1].url.endswith("/details/200687074-3543/software-engineer-satellite-operations")


def test_apple_fetches_every_page_and_dedupes() -> None:
    def page(n: int) -> dict:
        # 45 reported -> 3 pages; page 3 repeats a job shifted by a new posting.
        ids = {1: range(0, 20), 2: range(20, 40), 3: range(39, 45)}[n]
        return {
            "totalRecords": 45,
            "searchResults": [
                _apple_raw(f"{i}-1", f"Role {i}", f"role-{i}", []) for i in ids
            ],
        }

    company = {"name": "Apple", "category": "big_tech"}
    with patch("adapters.apple._get_page", side_effect=page) as get:
        jobs = fetch_apple(company)
    assert sorted(c.args[0] for c in get.call_args_list) == [1, 2, 3]
    assert len(jobs) == 45
    assert len({j.id for j in jobs}) == 45


def test_apple_refetches_pages_with_shuffled_ties() -> None:
    # Page 2's first slot repeats job 19 instead of job 20 on the first request only.
    calls = {2: 0}

    def page(n: int) -> dict:
        ids = list(range(0, 20)) if n == 1 else list(range(20, 25))
        if n == 2:
            calls[2] += 1
            if calls[2] == 1:
                ids[0] = 19
        return {
            "totalRecords": 25,
            "searchResults": [
                _apple_raw(f"{i}-1", f"Role {i}", f"role-{i}", []) for i in ids
            ],
        }

    company = {"name": "Apple", "category": "big_tech"}
    with patch("adapters.apple._get_page", side_effect=page):
        jobs = fetch_apple(company)
    assert len(jobs) == 25
    assert "20-1" in {j.id for j in jobs}


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


def test_linkedin_strips_leading_hash_from_title() -> None:
    html = """
    <div data-entity-urn="urn:li:jobPosting:99999">
      <a class="base-card__full-link" href="https://www.linkedin.com/jobs/view/99999">link</a>
      <h3 class="base-search-card__title">#Product Software Engineer</h3>
      <span class="job-search-card__location">San Diego, CA</span>
    </div>
    """
    company = {"name": "Qualcomm", "linkedin_company_id": "2017", "category": "big_tech"}
    with patch("adapters.linkedin._get_page", side_effect=[html, ""]):
        jobs = fetch_linkedin(company)
    assert len(jobs) == 1
    assert jobs[0].title == "Product Software Engineer"
