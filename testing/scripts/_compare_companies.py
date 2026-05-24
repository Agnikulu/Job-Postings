"""Compare user list against companies.yaml."""
import yaml

USER_LIST = [
    "Google", "Nvidia", "Stripe", "Databricks", "Figma", "OpenAI", "Anthropic",
    "Meta", "Snowflake", "Datadog", "Google DeepMind", "Cursor (Anysphere)",
    "Ramp", "xAI", "Notion", "Anduril", "Waymo", "Palantir", "LinkedIn", "Apple",
    "Plaid", "Scale AI", "Bloomberg LP", "Adobe", "DRW", "Point72", "Wiz",
    "Cognition AI", "Magic AI (Magic.dev)", "Sierra", "Boston Dynamics", "Mercor",
    "Roblox", "Netflix", "Coinbase", "1X Technologies", "Robinhood", "CoreWeave",
    "Figure AI", "Linear", "Decagon", "Fireworks AI", "Apptronik", "Replit",
    "Modal Labs", "Anyscale", "Cloudflare", "Physical Intelligence (Pi)",
    "Airbnb", "Shopify", "Snap", "Palo Alto Networks", "Lyft",
    "Generate Biomedicines", "Insitro", "Flatiron Health", "Hugging Face",
    "Amazon AWS", "Atlassian", "Confluent", "Vercel", "Rippling", "Perplexity AI",
    "Harvey", "Pinterest", "Lambda Labs", "Spotify", "Luma AI", "Etched",
    "Genesis Therapeutics", "Veeva Systems", "ElevenLabs", "Skydio",
    "Applied Intuition", "AMD", "Groq", "Microsoft", "Reka AI", "World Labs",
    "SpaceX", "Retool", "Zillow", "CrowdStrike", "Together AI", "Verily",
    "Tesla", "Glean", "Uber", "DoorDash", "EvolutionaryScale", "Xaira Therapeutics",
    "ClickHouse", "MongoDB", "Tempus AI", "Headway", "Pinecone", "Pathos AI",
    "Inceptive", "Zocdoc", "Isomorphic Labs", "Click Therapeutics", "Hebbia",
    "Cohere", "Shield AI", "Warp", "LangChain", "Discord", "Clay",
    "Recursion Pharma", "Runway ML", "Reddit",
]

ALIASES = {
    "cursor (anysphere)": "cursor",
    "physical intelligence (pi)": "physical intelligence",
    "magic ai (magic.dev)": "magic ai",
    "bloomberg lp": "bloomberg",
    "amazon aws": "amazon",
    "recursion pharma": "recursion pharma",
}

with open("companies.yaml") as f:
    companies = yaml.safe_load(f)

existing_names = {c["name"].lower(): c for c in companies}

def normalize(name: str) -> str:
    n = name.lower().strip()
    return ALIASES.get(n, n)

def matches(user_name: str) -> tuple[bool, str | None]:
    key = normalize(user_name)
    for en, cfg in existing_names.items():
        if key == en:
            return True, en
        if key.replace(" ", "") == en.replace(" ", ""):
            return True, en
        if key in en or en in key:
            if len(key) > 3 and len(en) > 3:
                return True, en
    return False, None

missing = []
present = []
for u in USER_LIST:
    ok, matched = matches(u)
    if ok:
        present.append((u, matched))
    else:
        missing.append(u)

print(f"Present: {len(present)}/{len(USER_LIST)}")
print(f"Missing: {len(missing)}")
for m in missing:
    print(f"  - {m}")
