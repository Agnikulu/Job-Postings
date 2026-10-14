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


def test_cap_job_list_override(monkeypatch):
    monkeypatch.setenv("ATS_SNIPER_MAX_JOBS_PER_COMPANY", "1")
    jobs = [
        Job("1", "Co", "A", "", "http://a", None, None, "gh", "x"),
        Job("2", "Co", "B", "", "http://b", None, None, "gh", "x"),
    ]
    assert len(cap_job_list("Co", jobs, 0)) == 2
    assert len(cap_job_list("Co", jobs, 5)) == 2


def test_plunge_vs_recent_peak_blocks_archive_close(tmp_path):
    from company_stats import CompanyStats

    stats = CompanyStats(tmp_path / "stats.json")
    assert not stats.is_plunge("Apple", 0)  # no history yet
    stats.record("Apple", postings=6100, matches=37)
    stats.record("Apple", postings=4354, matches=37)
    assert stats.recent_max_postings("Apple") == 6100
    assert stats.is_plunge("Apple", 0)
    assert stats.is_plunge("Apple", 3000)
    assert not stats.is_plunge("Apple", 4354)
    stats.record("Tiny", postings=10, matches=1)
    assert not stats.is_plunge("Tiny", 0)  # too small to judge
