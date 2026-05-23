"""Probe Meta careers API to find the correct search endpoint/format."""
import re
import requests

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    # 1. Load the jobs page to get cookies + any CSRF tokens
    print("Loading main jobs page...")
    r0 = session.get("https://www.metacareers.com/jobs", timeout=20)
    print(f"  status: {r0.status_code}, cookies: {list(session.cookies.keys())}")

    # Look for fb_dtsg, lsd token (Meta CSRF)
    fb_dtsg = re.search(r'"DTSGInitialData",\[\],\{"token":"([^"]+)"', r0.text)
    lsd = re.search(r'"LSD",\[\],\{"token":"([^"]+)"', r0.text)
    print(f"  fb_dtsg: {fb_dtsg.group(1)[:20] if fb_dtsg else 'NOT FOUND'}")
    print(f"  lsd: {lsd.group(1) if lsd else 'NOT FOUND'}")

    # 2. Try the graphql endpoint with job search doc_id
    # Meta careers uses Relay — look for the graphql endpoint in the HTML
    graphql_urls = re.findall(r'"(https://[^"]*graphql[^"]*)"', r0.text[:20000])
    print(f"  graphql urls found: {graphql_urls[:3]}")

    # 3. Try direct JSON API
    print("\nTrying /jobs/search/ as JSON...")
    api_headers = {
        "Accept": "application/json, text/javascript, */*",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.metacareers.com/jobs",
    }
    params = [
        ("roles[]", "Internship - Engineering, Tech & Design"),
        ("roles[]", "Internship - PhD"),
        ("roles[]", "University Grad - Engineering, Tech & Design"),
        ("roles[]", "University Grad - PhD & Postdoc"),
        ("page", "0"),
    ]
    r1 = session.get(
        "https://www.metacareers.com/jobs/search/",
        params=params,
        headers=api_headers,
        timeout=20,
    )
    print(f"  GET status: {r1.status_code}, content-type: {r1.headers.get('content-type','')}")
    print(f"  body[:300]: {r1.text[:300]}")

    # 4. Try POST with form data
    print("\nTrying POST /jobs/search/...")
    form_data = {
        "q": "",
        "roles[]": [
            "Internship - Engineering, Tech & Design",
            "Internship - PhD",
            "University Grad - Engineering, Tech & Design",
            "University Grad - PhD & Postdoc",
        ],
        "page": "0",
    }
    post_headers = {
        "Accept": "application/json, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.metacareers.com/jobs",
        "X-Requested-With": "XMLHttpRequest",
    }
    if lsd:
        form_data["lsd"] = lsd.group(1)
    r2 = session.post(
        "https://www.metacareers.com/jobs/search/",
        data=form_data,
        headers=post_headers,
        timeout=20,
    )
    print(f"  POST status: {r2.status_code}, content-type: {r2.headers.get('content-type','')}")
    print(f"  body[:400]: {r2.text[:400]}")

    # 5. Try the new metacareers API pattern used by newer versions
    print("\nTrying /api/graphql...")
    r3 = session.post(
        "https://www.metacareers.com/api/graphql",
        json={"q": "", "roles": ["Internship - Engineering, Tech & Design"]},
        headers={"Accept": "application/json"},
        timeout=20,
    )
    print(f"  graphql status: {r3.status_code}, body[:300]: {r3.text[:300]}")


if __name__ == "__main__":
    main()
