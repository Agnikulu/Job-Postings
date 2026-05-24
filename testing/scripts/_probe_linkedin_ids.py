"""Resolve LinkedIn company IDs via guest search."""
import html
import re
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

SEARCH = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
)

CANDIDATES = {
    "Coinbase": ["7795575", "1330979", "2857632"],
    "Wiz": ["85634128", "749LinkedIn"],
    "Amazon": ["1586"],
    "Amazon Web Services (AWS)": ["2382910", "9019"],
    "AMD": ["1495", "7550"],
    "Tesla": ["15564", "3629", "1586"],
    "Verily": ["10686357", "17900701"],
    "Tempus AI": ["314077", "10686357"],
    "Boston Dynamics": ["2680699", "1505"],
    "1X Technologies": ["33246782", "90663159"],
    "Magic AI": ["90630855", "98875656"],
    "Mercor": ["90663159", "98875656"],
    "Shopify": ["784652"],
}


def count_jobs(company_id: str) -> int:
    r = requests.get(
        SEARCH,
        params={"f_C": company_id, "location": "United States", "start": 0},
        headers={"User-Agent": UA, "Accept": "text/html,*/*"},
        timeout=15,
    )
    if not r.ok:
        return -r.status_code
    return len(re.findall(r'data-entity-urn="urn:li:jobPosting:', r.text))


for name, ids in CANDIDATES.items():
  for cid in ids:
    n = count_jobs(cid)
    print(f"{name:25} {cid:10} -> {n}")
    time.sleep(1.5)
