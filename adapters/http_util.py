"""Shared HTTP session helpers (connection reuse, same request semantics)."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import requests

from .base import DEFAULT_HEADERS


@contextmanager
def http_session(
    extra_headers: dict[str, str] | None = None,
) -> Iterator[requests.Session]:
    """Yield a requests.Session with default headers; closes on exit."""
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    if extra_headers:
        session.headers.update(extra_headers)
    try:
        yield session
    finally:
        session.close()
