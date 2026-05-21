"""Tests for detail-page description fetching."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters.description_fetch import (
    extract_google_description,
    extract_microsoft_description,
    fetch_workday_description,
)
from adapters.google_careers import fetch as fetch_google
from adapters.microsoft import fetch as fetch_microsoft
from adapters.workday import fetch as fetch_workday


GOOGLE_DS0 = """
AF_initDataCallback({key: 'ds:0', hash: '1', data:[["123","Software Engineer",null,[null,
"<ul><li>Build systems</li></ul>"],null,"Minimum qualifications: Bachelor's degree required."]],
sideChannel: {}});
"""

MICROSOFT_HTML = (
    'window.__app={"description":"As a Software Engineer you will build services. '
    'You have 6+ years of professional experience."}'
)


def test_extract_google_description_from_ds0() -> None:
    desc = extract_google_description(GOOGLE_DS0)
    assert desc is not None
    assert "Minimum qualifications" in desc
    assert "Bachelor's degree required" in desc


def test_extract_microsoft_description_from_html() -> None:
    desc = extract_microsoft_description(MICROSOFT_HTML)
    assert desc is not None
    assert "6+ years" in desc


def test_workday_fetch_description() -> None:
    payload = {
        "jobPostingInfo": {
            "jobDescription": "<p>Bachelor's degree required. 2+ years experience.</p>",
        }
    }
    with patch("adapters.description_fetch._get_json", return_value=payload):
        desc = fetch_workday_description(
            "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite",
            "/job/US-CA-Santa-Clara/Engineer_JR123",
        )
    assert desc is not None
    assert "Bachelor's degree required" in desc


def test_google_adapter_attaches_description() -> None:
    page_jobs = [
        [
            "102644388273758918",
            "Software Engineer",
            "https://www.google.com/about/careers/applications/signin?jobId=abc",
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
    with patch("adapters.google_careers._get_page", side_effect=[page_jobs, []]), patch(
        "adapters.google_careers.map_descriptions_parallel",
        return_value={"102644388273758918": "Minimum qualifications: Bachelor's degree."},
    ):
        jobs = fetch_google(company)
    assert jobs[0].description == "Minimum qualifications: Bachelor's degree."
    assert "signin" not in jobs[0].url


def test_microsoft_adapter_attaches_description() -> None:
    company = {"name": "Microsoft", "domain": "microsoft.com", "category": "big_tech"}
    with patch(
        "adapters.microsoft._get_page",
        side_effect=[
            {
                "data": {
                    "positions": [
                        {
                            "id": 1,
                            "name": "Software Engineer",
                            "standardizedLocations": ["Redmond, WA, US"],
                            "postedTs": 1779315378,
                            "positionUrl": "/careers/job/1",
                        }
                    ],
                    "count": 1,
                }
            },
            {"data": {"positions": [], "count": 1}},
        ],
    ), patch(
        "adapters.microsoft.map_descriptions_parallel",
        return_value={"1": "You have 6+ years of professional experience."},
    ):
        jobs = fetch_microsoft(company)
    assert jobs[0].description == "You have 6+ years of professional experience."


def test_workday_adapter_attaches_description() -> None:
    company = {
        "name": "Nvidia",
        "tenant": "nvidia",
        "wd_pod": "wd5",
        "site": "NVIDIAExternalCareerSite",
        "category": "big_tech",
    }
    listing = {
        "jobPostings": [
            {
                "title": "Software Engineer",
                "externalPath": "/job/US-CA-Santa-Clara/Engineer_JR123",
                "locationsText": "Santa Clara, CA",
                "postedOn": "Posted Today",
            }
        ]
    }
    with patch("adapters.workday._post_page", side_effect=[listing, {"jobPostings": []}]), patch(
        "adapters.workday.map_descriptions_parallel",
        return_value={
            "/job/US-CA-Santa-Clara/Engineer_JR123": "Bachelor's degree required."
        },
    ):
        jobs = fetch_workday(company)
    assert jobs[0].description == "Bachelor's degree required."
