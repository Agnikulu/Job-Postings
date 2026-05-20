"""ATS adapter dispatch registry.

Each adapter exposes a single `fetch(company: dict) -> list[Job]` function.
Adding a new ATS is just: write a new module, then add it to ADAPTER_REGISTRY.
"""

from .ashby import fetch as fetch_ashby
from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .greenhouse import fetch as fetch_greenhouse
from .lever import fetch as fetch_lever
from .workday import fetch as fetch_workday

ADAPTER_REGISTRY = {
    "greenhouse": fetch_greenhouse,
    "lever": fetch_lever,
    "ashby": fetch_ashby,
    "workday": fetch_workday,
}

__all__ = [
    "ADAPTER_REGISTRY",
    "AdapterError",
    "DEFAULT_HEADERS",
    "DEFAULT_TIMEOUT",
    "Job",
]
