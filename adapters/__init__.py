"""ATS adapter dispatch registry.

Each adapter exposes a single `fetch(company: dict) -> list[Job]` function.
Adding a new ATS is just: write a new module, then add it to ADAPTER_REGISTRY.
"""

from .apple import fetch as fetch_apple
from .ashby import fetch as fetch_ashby
from .base import DEFAULT_HEADERS, DEFAULT_TIMEOUT, AdapterError, Job
from .eightfold import fetch as fetch_eightfold
from .gem import fetch as fetch_gem
from .google_careers import fetch as fetch_google_careers
from .greenhouse import fetch as fetch_greenhouse
from .jibe import fetch as fetch_jibe
from .lever import fetch as fetch_lever
from .linkedin import fetch as fetch_linkedin
from .meta import fetch as fetch_meta
from .microsoft import fetch as fetch_microsoft
from .rippling import fetch as fetch_rippling
from .smartrecruiters import fetch as fetch_smartrecruiters
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
    "smartrecruiters": fetch_smartrecruiters,
    "eightfold": fetch_eightfold,
    "google_careers": fetch_google_careers,
    "microsoft": fetch_microsoft,
    "apple": fetch_apple,
    "meta": fetch_meta,
    "linkedin": fetch_linkedin,
}

__all__ = [
    "ADAPTER_REGISTRY",
    "AdapterError",
    "DEFAULT_HEADERS",
    "DEFAULT_TIMEOUT",
    "Job",
]
