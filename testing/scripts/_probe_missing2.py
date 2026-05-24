"""Extended ATS probe for missing companies."""
import json
import re
import requests

HEADERS = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}


def ashby(slug: str) -> str:
    r = requests.get(
        f"https://api.ashbyhq.com/posting-api/job-board/{slug}", timeout=10
    )
    if not r.ok:
        return f"{r.status_code}"
    data = r.json()
    return f"200 jobs={len(data.get('jobPostings', []))} name={data.get('jobBoardName', '')!r}"


def eightfold(host: str, domain: str) -> str:
    try:
        r = requests.get(
            f"https://{host}/api/apply/v2/jobs",
            params={"domain": domain, "batch": 0, "limit": 1},
            timeout=10,
            headers=HEADERS,
        )
        if not r.ok:
            return str(r.status_code)
        data = r.json()
        return f"200 count={data.get('count', len(data.get('positions', [])))}"
    except Exception as e:
        return f"ERR {e}"


def workday(tenant: str, pod: str, site: str) -> str:
    url = f"https://{tenant}.{pod}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs"
    r = requests.post(
        url,
        json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""},
        timeout=10,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    if not r.ok:
        return str(r.status_code)
    return f"200 total={r.json().get('total', 0)}"


def linkedin(company_id: str) -> str:
    r = requests.get(
        "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search",
        params={"f_C": company_id, "location": "United States", "start": 0},
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,*/*",
        },
        timeout=12,
    )
    if not r.ok:
        return str(r.status_code)
    n = len(re.findall(r'data-entity-urn="urn:li:jobPosting:', r.text))
    return f"200 page0={n}"


ASHBY = [
    "mercor", "decagon", "replit", "skydio", "reka", "modal", "wiz", "1x",
    "magic-dev", "magicdev", "fireworks", "tempus", "shield-ai",
]
print("=== ASHBY ===")
for s in ASHBY:
    print(f"  {s}: {ashby(s)}")

EF = [
    ("explore.jobs.snap.com", "snap.com"),
    ("explore.jobs.shopify.com", "shopify.com"),
    ("explore.jobs.coinbase.com", "coinbase.com"),
    ("explore.jobs.wiz.io", "wiz.io"),
    ("explore.jobs.amd.com", "amd.com"),
    ("explore.jobs.tesla.com", "tesla.com"),
    ("explore.jobs.amazon.com", "amazon.com"),
    ("explore.jobs.verily.com", "verily.com"),
    ("explore.jobs.tempus.com", "tempus.com"),
    ("explore.jobs.paloaltonetworks.com", "paloaltonetworks.com"),
    ("explore.jobs.bostondynamics.com", "bostondynamics.com"),
    ("explore.jobs.zillow.com", "zillow.com"),
    ("explore.jobs.spotify.com", "spotify.com"),
]
print("\n=== EIGHTFOLD ===")
for host, domain in EF:
    print(f"  {host}: {eightfold(host, domain)}")

WD = [
    ("crowdstrike", "wd5", "crowdstrikecareers"),
    ("snap", "wd5", "Snap"),
    ("snap", "wd1", "Snap"),
    ("amd", "wd1", "AMDExternalCareers"),
    ("amd", "wd5", "AMDExternalCareers"),
    ("amd", "wd1", "External"),
    ("shopify", "wd3", "ShopifyCareers"),
    ("zillow", "wd5", "Zillow"),
    ("zillow", "wd1", "Zillow_Group_External"),
    ("tesla", "wd5", "Tesla"),
    ("tesla", "wd1", "Tesla"),
    ("amazon", "wd5", "Amazon"),
    ("amazon", "wd1", "Amazon"),
    ("verily", "wd5", "verily"),
    ("tempus", "wd5", "tempus"),
    ("bostondynamics", "wd5", "bostondynamics"),
]
print("\n=== WORKDAY ===")
for t, pod, site in WD:
    print(f"  {t}/{pod}/{site}: {workday(t, pod, site)}")

# Known LinkedIn company IDs (public knowledge / careers pages)
LI = [
    ("Coinbase", "1330979"),
    ("Wiz", "85634128"),
    ("Shopify", "784652"),
    ("Snap", "15191764"),
    ("Amazon", "1586"),
    ("AWS", "2382910"),
    ("AMD", "1495"),
    ("Tesla", "1586"),  # verify
    ("Verily", "10686357"),
    ("Tempus AI", "10686357"),
    ("Zillow", "13990"),
    ("Boston Dynamics", "2680699"),
    ("Palo Alto Networks", "30086"),
    ("Mercor", "90663159"),
    ("Magic AI", "90663159"),
    ("Modal Labs", "90663159"),
    ("1X Technologies", "90663159"),
    ("Reka AI", "90663159"),
    ("Skydio", "3765672"),
]
print("\n=== LINKEDIN (sample IDs - verify) ===")
for name, cid in LI:
    print(f"  {name} ({cid}): {linkedin(cid)}")
