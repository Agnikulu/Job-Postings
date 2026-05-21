"""Unit tests for new bespoke ATS adapters."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters.gem import fetch as fetch_gem
from adapters.jibe import fetch as fetch_jibe
from adapters.rippling import fetch as fetch_rippling
from adapters.smartrecruiters import fetch as fetch_smartrecruiters
from adapters.uber import fetch as fetch_uber
from adapters.workable import fetch as fetch_workable


def test_workable_fetch_maps_fields() -> None:
    payload = {
        "jobs": [
            {
                "title": "ML Engineer",
                "shortcode": "ABC123",
                "department": "Engineering",
                "url": "https://apply.workable.com/j/ABC123",
                "published_on": "2026-02-12",
                "city": "Paris",
                "country": "France",
            }
        ]
    }
    company = {"name": "Hugging Face", "slug": "huggingface", "category": "frontier_ai"}
    with patch("adapters.workable._get", return_value=payload):
        jobs = fetch_workable(company)
    assert len(jobs) == 1
    assert jobs[0].title == "ML Engineer"
    assert jobs[0].posted_at == "2026-02-12"
    assert jobs[0].ats == "workable"


def test_jibe_fetch_maps_fields() -> None:
    payload = {
        "jobs": [{
            "data": {
                "req_id": "7433",
                "title": "Director",
                "city": "LA",
                "state": "CA",
                "country": "US",
                "posted_date": "2026-05-20T20:27:00+0000",
                "department": "Ops",
                "description": "<p>Build systems.</p>",
                "qualifications": "<ul><li>Bachelor's degree</li></ul>",
            },
        }],
        "totalCount": 1,
    }
    company = {"name": "BlackLine", "careers_host": "careers.blackline.com", "category": "big_tech"}
    with patch("adapters.jibe._get_page", return_value=payload):
        jobs = fetch_jibe(company)
    assert jobs[0].url == "https://careers.blackline.com/careers-home/jobs/7433"
    assert jobs[0].location == "LA, CA, US"
    assert jobs[0].description is not None
    assert "Bachelor's degree" in jobs[0].description


def test_rippling_fetch_dedupes_locations() -> None:
    html = """
    <script id="__NEXT_DATA__" type="application/json">
    {"props":{"pageProps":{"jobs":{"items":[
      {"id":"1","name":"Engineer","url":"https://ats.rippling.com/x/jobs/1","department":{"name":"Eng"},"locations":[{"name":"SF"}]},
      {"id":"1","name":"Engineer","url":"https://ats.rippling.com/x/jobs/1","department":{"name":"Eng"},"locations":[{"name":"NY"}]}
    ],"totalItems":1}}}}
    </script>
    """
    company = {"name": "Rippling", "slug": "rippling", "category": "enterprise"}
    with patch("adapters.rippling._get_html", return_value=html):
        jobs = fetch_rippling(company)
    assert len(jobs) == 1
    assert jobs[0].location == "SF / NY"


def test_gem_fetch_maps_fields() -> None:
    payload = {
        "data": {
            "oatsExternalJobPostings": {
                "jobPostings": [
                    {
                        "extId": "ext-1",
                        "title": "Software Engineer",
                        "locations": [{"name": "Remote", "isRemote": True}],
                        "job": {"department": {"name": "Engineering"}},
                    }
                ]
            }
        }
    }
    company = {"name": "Groq", "slug": "groq", "category": "frontier_ai"}
    with patch("adapters.gem._post", return_value=payload):
        jobs = fetch_gem(company)
    assert jobs[0].url == "https://jobs.gem.com/groq/ext-1"
    assert jobs[0].location == "Remote"


def test_uber_fetch_maps_fields() -> None:
    api_payload = {
        "status": "success",
        "data": {
            "results": [
                {
                    "id": 123,
                    "title": "Software Engineer Intern",
                    "department": "Engineering",
                    "creationDate": "2026-03-18T06:01:00.000Z",
                    "description": "**About the Role**\n\nBuild backend systems.",
                    "location": {"city": "San Francisco", "region": "CA", "countryName": "United States"},
                }
            ]
        },
    }
    company = {"name": "Uber", "locale": "en", "category": "big_tech"}
    with patch("adapters.uber._fetch_results", return_value=api_payload["data"]["results"]):
        jobs = fetch_uber(company)
    assert jobs[0].url == "https://www.uber.com/careers/list/123"
    assert "San Francisco" in jobs[0].location
    assert jobs[0].description == "**About the Role** Build backend systems."


def test_smartrecruiters_fetch_maps_fields() -> None:
    payload = {
        "totalFound": 1,
        "content": [
            {
                "id": "744000122509268",
                "name": "Sr. SW Engineer",
                "releasedDate": "2026-04-23T16:54:54.835Z",
                "location": {"fullLocation": "Austin, TX, United States", "remote": False},
                "department": {"label": "Engineering"},
                "ref": "https://api.smartrecruiters.com/v1/companies/Visa/postings/744000122509268",
            }
        ],
    }
    company = {"name": "Atlassian", "slug": "Atlassian", "category": "big_tech"}
    with patch("adapters.smartrecruiters._get_page", return_value=payload):
        jobs = fetch_smartrecruiters(company)
    assert jobs[0].title == "Sr. SW Engineer"
    assert jobs[0].posted_at == "2026-04-23T16:54:54.835Z"
    assert "744000122509268" in jobs[0].url
