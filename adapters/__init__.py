"""ATS adapter dispatch registry.

Each adapter exposes a single `fetch(company: dict) -> list[Job]` function.
Adding a new ATS is just: write a new module, then add it to ADAPTER_REGISTRY.
"""

from .ashby import fetch as fetch_ashby
from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .gem import fetch as fetch_gem
from .greenhouse import fetch as fetch_greenhouse
from .jibe import fetch as fetch_jibe
from .lever import fetch as fetch_lever
from .rippling import fetch as fetch_rippling
from .uber import fetch as fetch_uber
from .workable import fetch as fetch_workable
from .workday import fetch as fetch_workday

ADAPTER_REGISTRY = {
    "greenhouse": fetch_greenhouse,
    "lever": fetch_lever,
    "ashby": fetch_ashby,
    "workday": fetch_workday,
    "workable": fetch_workable,
    "jibe": fetch_jibe,
    "rippling": fetch_rippling,
    "gem": fetch_gem,
    "uber": fetch_uber,
}

__all__ = [
    "ADAPTER_REGISTRY",
    "AdapterError",
    "DEFAULT_HEADERS",
    "DEFAULT_TIMEOUT",
    "Job",
]
