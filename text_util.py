"""Plain-text helpers for job descriptions."""

from __future__ import annotations

import re
from html import unescape

_TAG_RE = re.compile(r"<[^>]+>")


def strip_html(html: str | None) -> str:
    """Convert HTML to normalized plain text."""
    if not html:
        return ""
    text = unescape(html)
    text = _TAG_RE.sub(" ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_description(raw: str | None, *, is_html: bool = False) -> str | None:
    """Return cleaned description text, or None if empty."""
    if not raw or not raw.strip():
        return None
    text = strip_html(raw) if is_html else re.sub(r"\s+", " ", raw).strip()
    return text or None
