"""Avature adapter: list parsing, parallel paging, gated description fetches."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adapters import avature

BASE = "https://example.avature.net/careers"


def _article(job_id: str, title: str, location: str) -> str:
    url = f"{BASE}/JobDetail/{title.replace(' ', '-')}/{job_id}"
    return f"""
    <article class="article article--result" id="article--{job_id}">
      <div class="article__header"><div class="article__header__text">
        <h3 class="article__header__text__title title title--04">
          <a class="link" href="{url}">
            {title}
          </a>
        </h3>
        <div class="article__header__text__subtitle">
          <span class="list-item-location">{location}</span>
        </div>
      </div></div>
      <div class="article__footer"><a class="button button--primary" href="{url}">Apply</a></div>
    </article>"""


def _page(total: int, articles: list[str]) -> str:
    return f'<div class="list-controls__text__legend" aria-label="{total} results"></div>' + "".join(articles)


DETAIL = """
<article class="article article--details " >
  <div class="article__content"><div class="article__content__view">
    <div class="article__content__view__field ">
      <div class="article__content__view__field__label">Location</div>
      <div class="article__content__view__field__value">New York</div>
    </div>
  </div></div>
</article>
<article class="article article--details " >
  <div class="article__header "><div class="article__header__text">
    <h2 class="article__header__text__title title title--04">
      Description &amp; Requirements
    </h2>
  </div></div>
  <div class="article__content"><div class="article__content__view">
    <div class="article__content__view__field field--rich-text">
      <div class="article__content__view__field__value"><p>Build things. BS in CS required.</p></div>
    </div>
  </div></div>
</article>
"""

COMPANY = {"name": "Example", "avature_host": "example.avature.net", "category": "big_tech"}


def test_parse_list_and_total() -> None:
    html = _page(2, [_article("1", "Software Engineer", "New York, New York, United States of America"),
                     _article("2", "Sales &amp; Ops", "London, United Kingdom")])
    assert avature._parse_total(html) == 2
    rows = avature._parse_list(html)
    assert [r["id"] for r in rows] == ["1", "2"]
    assert rows[0]["title"] == "Software Engineer"
    assert rows[0]["url"] == f"{BASE}/JobDetail/Software-Engineer/1"
    assert rows[1]["title"] == "Sales & Ops"
    assert rows[1]["location"] == "London, United Kingdom"


def test_parse_description_section_only() -> None:
    desc = avature._parse_description(DETAIL)
    assert desc and "BS in CS required" in desc
    assert "New York" not in desc


def test_fetch_pages_all_offsets_and_gates_details() -> None:
    pages = {
        0: _page(14, [_article(str(i), "Software Engineer", "New York, New York, United States of America") for i in range(12)]),
        12: _page(14, [_article("12", "Senior Staff Software Engineer", "New York, New York, United States of America"),
                       _article("13", "Software Engineer", "London, United Kingdom")]),
    }
    offsets: list[int] = []

    def get_page(base: str, offset: int) -> str:
        assert base == BASE
        offsets.append(offset)
        return pages[offset]

    detail_urls: list[str] = []

    def get(url: str, params=None) -> str:
        detail_urls.append(url)
        return DETAIL

    with patch.object(avature, "_get_page", side_effect=get_page), patch.object(avature, "_get", side_effect=get):
        jobs = avature.fetch(COMPANY)

    assert sorted(offsets) == [0, 12]
    assert len(jobs) == 14
    by_id = {j.id: j for j in jobs}
    assert by_id["0"].description and "BS in CS" in by_id["0"].description
    # Senior title and non-US location are rejected by title/location alone: no detail fetch.
    assert by_id["12"].description is None
    assert by_id["13"].description is None
    assert len(detail_urls) == 12
    assert all(j.ats == "avature" for j in jobs)
