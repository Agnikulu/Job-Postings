"""Verify adapter fetch counts for missing companies."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from adapters.ashby import fetch as fetch_ashby
from adapters.greenhouse import fetch as fetch_gh
from adapters.lever import fetch as fetch_lever
from adapters.workday import fetch as fetch_wd
from adapters.linkedin import fetch as fetch_linkedin

ASHBY = [
    ("Mercor", "mercor"),
    ("Decagon", "decagon"),
    ("Replit", "replit"),
    ("Modal Labs", "modal"),
    ("Skydio", "skydio"),
    ("Reka AI", "reka"),
    ("1X Technologies", "1x"),
    ("Magic AI", "magic"),
    ("Wiz", "wiz"),
]

GH = [
    ("Robinhood", "robinhood"),
    ("Cloudflare", "cloudflare"),
    ("Lyft", "lyft"),
    ("Applied Intuition", "appliedintuition"),
    ("Generate Biomedicines", "generatebiomedicines"),
    ("Apptronik", "apptronik"),
    ("Fireworks AI", "fireworksai"),
    ("World Labs", "worldlabs"),
]

LEVER = [
    ("Spotify", "spotify"),
    ("Veeva Systems", "veeva"),
    ("Shield AI", "shieldai"),
    ("Anyscale", "anyscale"),
]

LINKEDIN = [
    ("Shopify", "784652"),
    ("Snap", "15191764"),
    ("Amazon", "1586"),
    ("Zillow", "13990"),
    ("Palo Alto Networks", "30086"),
    ("Coinbase", "1330979"),
    ("Wiz", "85634128"),
    ("AMD", "1495"),
    ("Boston Dynamics", "2680699"),
    ("Verily", "10686357"),
    ("Tempus AI", "314077"),
    ("Tesla", "15564"),
    ("Mercor", "90663159"),
    ("Skydio", "3765672"),
    ("1X Technologies", "33246782"),
    ("Modal Labs", "79912189"),
    ("Reka AI", "90630855"),
    ("Magic AI", "90630855"),
]

print("=== ASHBY ===")
for name, slug in ASHBY:
    try:
        jobs = fetch_ashby({"name": name, "slug": slug, "category": "enterprise"})
        print(f"  {name} ({slug}): {len(jobs)}")
    except Exception as e:
        print(f"  {name} ({slug}): ERROR {e}")

print("\n=== GREENHOUSE ===")
for name, slug in GH:
    try:
        jobs = fetch_gh({"name": name, "slug": slug, "category": "enterprise"})
        print(f"  {name} ({slug}): {len(jobs)}")
    except Exception as e:
        print(f"  {name} ({slug}): ERROR {e}")

print("\n=== LEVER ===")
for name, slug in LEVER:
    try:
        jobs = fetch_lever({"name": name, "slug": slug, "category": "enterprise"})
        print(f"  {name} ({slug}): {len(jobs)}")
    except Exception as e:
        print(f"  {name} ({slug}): ERROR {e}")

print("\n=== WORKDAY ===")
try:
    jobs = fetch_wd(
        {
            "name": "CrowdStrike",
            "tenant": "crowdstrike",
            "wd_pod": "wd5",
            "site": "crowdstrikecareers",
            "category": "big_tech",
        }
    )
    print(f"  CrowdStrike: {len(jobs)}")
except Exception as e:
    print(f"  CrowdStrike: ERROR {e}")

print("\n=== LINKEDIN ===")
for name, cid in LINKEDIN:
    try:
        jobs = fetch_linkedin(
            {
                "name": name,
                "linkedin_company_id": cid,
                "search_location": "United States",
                "category": "big_tech",
            }
        )
        print(f"  {name} ({cid}): {len(jobs)}")
    except Exception as e:
        print(f"  {name} ({cid}): ERROR {e}")
