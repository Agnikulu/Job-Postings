"""Quick check: does LinkedIn company 10667 return Meta jobs?"""
import html
import re
import requests

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"

r = requests.get(
    SEARCH_URL,
    params={"f_C": "10667", "location": "United States", "start": 0},
    headers={
        "User-Agent": UA,
        "Accept": "text/html,application/json,*/*",
    },
    timeout=15,
)
print(f"status: {r.status_code}")
cards = re.split(r"(?=data-entity-urn=\"urn:li:jobPosting:)", r.text)
print(f"cards on page 0: {len(cards) - 1}")
for card in cards[1:6]:
    urn = re.search(r'data-entity-urn="urn:li:jobPosting:(\d+)"', card)
    title_m = re.search(r"base-search-card__title[^>]*>\s*([^<]+)", card)
    if urn and title_m:
        print(f"  [{urn.group(1)}] {html.unescape(title_m.group(1).strip())}")
