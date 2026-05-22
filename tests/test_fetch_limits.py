import os

from adapters.base import Job
from fetch_limits import cap_job_list, max_list_pages


def test_max_list_pages_default(monkeypatch):
    monkeypatch.delenv("ATS_SNIPER_MAX_LIST_PAGES", raising=False)
    assert max_list_pages(200) == 200


def test_max_list_pages_env(monkeypatch):
    monkeypatch.setenv("ATS_SNIPER_MAX_LIST_PAGES", "60")
    assert max_list_pages(200) == 60
    assert max_list_pages(40) == 40


def test_cap_job_list(monkeypatch):
    monkeypatch.setenv("ATS_SNIPER_MAX_JOBS_PER_COMPANY", "2")
    jobs = [
        Job("1", "Co", "A", "", "http://a", None, None, "gh", "x"),
        Job("2", "Co", "B", "", "http://b", None, None, "gh", "x"),
        Job("3", "Co", "C", "", "http://c", None, None, "gh", "x"),
    ]
    capped = cap_job_list("Co", jobs)
    assert len(capped) == 2
    assert capped[0].id == "1"
