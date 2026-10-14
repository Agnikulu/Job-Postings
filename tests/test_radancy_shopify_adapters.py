"""Radancy (TalentBrew) and Shopify adapters: list parsing and detail gating."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters import radancy, shopify


def _card(job_id: str, title: str, location: str) -> str:
    return f"""
    <li>
      <a class="job-card__title" href="/job/x/{title.lower().replace(' ', '-')}/33099/{job_id}" data-job-id="{job_id}">{title}</a>
      <span class="location">{location}</span>
      <span class="category">Software Engineering</span>
      <button type="button" class="js-save-job-btn" data-job-id="{job_id}"></button>
    </li>"""


def _results(pages: int, cards: list[str]) -> str:
    return f'<section data-total-pages="{pages}" data-total-results="999"><ul>{"".join(cards)}</ul></section>'


DETAIL = """<html><script type="application/ld+json">{"@type": "JobPosting",
 "datePosted": "2026-08-04", "description": "<p>Build compilers. BS in CS.</p>",
 "jobLocation": [{"@type": "Place", "address": {"addressLocality": "Austin", "addressRegion": "Texas", "addressCountry": "United States"}},
                 {"@type": "Place", "address": {"addressLocality": "Cambridge", "addressRegion": "England", "addressCountry": "United Kingdom"}}]}
</script></html>"""


def test_radancy_parses_pages_and_resolves_multiple_locations() -> None:
    pages = {
        1: _results(2, [_card("1", "Software Engineer", "Multiple locations"),
                        _card("2", "Software Engineer", "Austin, Texas")]),
        2: _results(2, [_card("3", "Senior Principal Architect", "Multiple locations")]),
    }

    class Resp:
        text = DETAIL

    with patch("adapters.radancy._get_page", side_effect=lambda host, p: pages[p]), \
         patch("adapters.radancy._get", return_value=Resp()) as get, \
         patch("adapters.radancy.should_fetch_description", return_value=False):
        jobs = radancy.fetch({"name": "Arm", "careers_host": "careers.arm.com"})

    by_id = {j.id: j for j in jobs}
    assert set(by_id) == {"1", "2", "3"}
    # Decisive title + "Multiple locations" still fetches the detail page.
    assert by_id["1"].location == "Austin, Texas, United States; Cambridge, England, United Kingdom"
    assert by_id["1"].posted_at == "2026-08-04"
    assert "compilers" in (by_id["1"].description or "")
    assert by_id["1"].url == "https://careers.arm.com/job/x/software-engineer/33099/1"
    # Known location + decisive title: no detail fetch. Senior titles: none either.
    assert by_id["2"].description is None and by_id["3"].location == "Multiple locations"
    assert get.call_count == 1


def _turbo(value_root: dict) -> str:
    """Encode a dict as a minimal turbo-stream flat array inside the page."""
    flat: list = []

    def enc(v):
        i = len(flat)
        if isinstance(v, dict):
            flat.append(None)
            obj = {}
            for k, val in v.items():
                ki = len(flat)
                flat.append(k)
                obj[f"_{ki}"] = enc(val)
            flat[i] = obj
        elif isinstance(v, list):
            flat.append(None)
            flat[i] = [enc(x) for x in v]
        else:
            flat.append(v)
        return i

    enc(value_root)
    payload = json.dumps(json.dumps(flat) + "\n")
    return f"<script>window.__reactRouterContext.streamController.enqueue({payload});</script>"


def test_shopify_decodes_postings_and_labels_americas() -> None:
    search = _turbo({"loaderData": {"($locale)/careers": {
        "atsLocations": [
            {"id": "am", "name": "Americas"},
            {"id": "ie", "name": "Ireland"},
            {"id": "uk", "name": "United Kingdom"},
        ],
        "jobPostingsWithJobs": [
            {"jobPosting": {"id": "a1", "title": "Software Engineer", "teamName": "R&D",
                            "publishedDate": "2026-09-01",
                            "locationIds": {"primaryLocationId": "am", "secondaryLocationIds": []}}},
            {"jobPosting": {"id": "b2", "title": "Software Engineer", "teamName": "R&D",
                            "locationIds": {"primaryLocationId": "ie", "secondaryLocationIds": ["uk"]}}},
        ],
    }}})
    detail = _turbo({"loaderData": {"($locale)/careers/$posting": {
        "jobPosting": {"descriptionHtml": "<p>Ship Shopify features.</p>"}}}})

    def fake_get(url: str) -> str:
        return search if url == shopify.SEARCH_URL else detail

    with patch("adapters.shopify._get", side_effect=fake_get):
        jobs = shopify.fetch({"name": "Shopify", "category": "big_tech"})

    by_id = {j.id: j for j in jobs}
    assert by_id["a1"].location == "Americas (Remote: United States, Canada)"
    assert by_id["a1"].url == "https://www.shopify.com/careers?ashby_jid=a1"
    assert by_id["a1"].posted_at == "2026-09-01"
    assert by_id["b2"].location == "Ireland; United Kingdom"
    assert "Ship Shopify" in (by_id["a1"].description or "")
