"""Probe ATS endpoints for missing companies."""
import requests
import time

MISSING = [
    ("Wiz", ["wiz", "wizio", "wiz-io"]),
    ("Magic AI", ["magic", "magicai"]),
    ("Boston Dynamics", ["bostondynamics", "boston-dynamics"]),
    ("Mercor", ["mercor"]),
    ("Coinbase", ["coinbase", "coinbasecareers"]),
    ("1X Technologies", ["1x", "1xtechnologies"]),
    ("Robinhood", ["robinhood"]),
    ("Decagon", ["decagon"]),
    ("Fireworks AI", ["fireworksai", "fireworks-ai"]),
    ("Apptronik", ["apptronik"]),
    ("Replit", ["replit"]),
    ("Modal Labs", ["modal-labs", "modallabs"]),
    ("Anyscale", ["anyscale"]),
    ("Cloudflare", ["cloudflare"]),
    ("Shopify", ["shopify", "shopifyinc"]),
    ("Snap", ["snap", "snapinc"]),
    ("Palo Alto Networks", ["paloaltonetworks", "palo-alto-networks"]),
    ("Lyft", ["lyft"]),
    ("Generate Biomedicines", ["generatebiomedicines", "generate-biomedicines"]),
    ("Amazon", ["amazon", "amazonwebservices", "aws"]),
    ("Spotify", ["spotify", "spotifytechnology"]),
    ("Veeva Systems", ["veeva", "veevasystems"]),
    ("Skydio", ["skydio"]),
    ("Applied Intuition", ["appliedintuition", "applied-intuition"]),
    ("AMD", ["amd", "advancedmicrodevices"]),
    ("Reka AI", ["reka", "rekaai", "reka-ai"]),
    ("World Labs", ["worldlabs", "world-labs"]),
    ("Zillow", ["zillow", "zillowgroup"]),
    ("CrowdStrike", ["crowdstrike", "crowdstrikecareers"]),
    ("Verily", ["verily"]),
    ("Tesla", ["tesla"]),
    ("Tempus AI", ["tempus", "tempusai", "tempus-ai"]),
    ("Shield AI", ["shieldai", "shield-ai"]),
]

GH = "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?per_page=1"
ASH = "https://api.ashbyhq.com/posting-api/job-board/{slug}"
LEV = "https://api.lever.co/v0/postings/{slug}?mode=json&limit=1"
SR = "https://api.smartrecruiters.com/v1/companies/{slug}/postings?limit=1"
EF = "https://explore.jobs.{slug}/api/apply/v2/jobs?domain={slug}&batch=0&limit=1"


def probe(slug: str) -> dict[str, tuple[int, int]]:
    out = {}
    try:
        r = requests.get(GH.format(slug=slug), timeout=8)
        out["gh"] = (r.status_code, len(r.json().get("jobs", [])) if r.ok else 0)
    except Exception as e:
        out["gh"] = (0, str(e)[:30])
    try:
        r = requests.get(ASH.format(slug=slug), timeout=8)
        out["ash"] = (r.status_code, len(r.json().get("jobPostings", [])) if r.ok else 0)
    except Exception as e:
        out["ash"] = (0, str(e)[:30])
    try:
        r = requests.get(LEV.format(slug=slug), timeout=8)
        out["lev"] = (r.status_code, len(r.json()) if r.ok else 0)
    except Exception as e:
        out["lev"] = (0, str(e)[:30])
    try:
        r = requests.get(SR.format(slug=slug), timeout=8)
        out["sr"] = (r.status_code, len(r.json().get("content", [])) if r.ok else 0)
    except Exception as e:
        out["sr"] = (0, str(e)[:30])
    return out


for name, slugs in MISSING:
    print(f"\n=== {name} ===")
    for slug in slugs:
        res = probe(slug)
        hits = {k: v for k, v in res.items() if v[0] == 200 and (isinstance(v[1], int) and v[1] > 0)}
        if hits:
            print(f"  {slug}: HIT {hits}")
        else:
            print(f"  {slug}: {res}")
        time.sleep(0.1)
