# Serverless ATS Job Sniper

An auto-updated list of **new-grad / entry-level software, AI/ML, and data
roles** scraped hourly from public job boards: Greenhouse, Lever, Ashby,
Workday, SmartRecruiters, Microsoft Careers, Google Careers, Amazon Jobs,
Uber, LinkedIn guest search, and other company-specific APIs.

**Scope (default):** new-grad / university graduate / Engineer I / early
career / MTS-style full-time entry. Internships, co-ops, and non-software
disciplines (mechanical / civil / aero / propulsion / manufacturing /
RF / antenna / facilities / etc.) are filtered out. US-only.

Built on a free GitHub Actions cron with zero servers and zero ongoing
costs. State (`seen_jobs.json`, `jobs_archive.json`, `company_stats.json`)
is committed back to the repo so the table grows historically.

See [README\_TECH.md](README_TECH.md) for the project architecture,
how to fork, how to add companies, and how filtering works.

## Stats

- **Open positions:** 308
- **All-time tracked:** 331
- **Active companies:** 150
- **Last run (raw / matched):** 32058 postings fetched, 308 passed filters
- **Last updated:** `2026-08-30 03:51 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Source** -> Which adapter fetched the row (`greenhouse`, `linkedin`, `workday`, etc.).
- **Education** -> Tags from job requirements (e.g. `{PhD, PhD Student, Masters, Bachelors, New Grad, Early Career, Intern}`).
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> Best-effort publish date from each ATS (`first_published`,
   `publishedAt`, etc.). LinkedIn/Workday relative strings are pinned to the
   earliest date we parsed. If the board provides no date, shows when we first
   saw the URL (`first_seen`).

## Open positions

| Company | Role | Location | Source | Education | Apply | Date Posted |
|---------|------|----------|--------|-----------|-------|-------------|
| Qualcomm | Software Engineer - Edge AI/Gen AI 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4449756259) | Aug 28, 2026 |
| Together AI | GTM Data Analytics Engineer 🇺🇸 | San Francisco | greenhouse | - | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5223190007) | Aug 28, 2026 |
| Crusoe | Enablement Engineer 🇺🇸 | Denver, CO - US | ashby | - | [Apply](https://jobs.ashbyhq.com/Crusoe/1eb50f41-8a4b-4db0-953e-1bee91e3f40e) | Aug 28, 2026 |
| Crusoe | Enablement Engineer 🇺🇸 | San Francisco, CA - US | ashby | - | [Apply](https://jobs.ashbyhq.com/Crusoe/91b8d1dd-2368-4509-bcce-d1a528dac9a2) | Aug 28, 2026 |
| Roblox | Software Engineer, Economy Platform 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8060254?gh_jid=8060254) | Aug 28, 2026 |
| Broadcom | ASIC Verification Engineer 🇺🇸 | USA-CA Irvine Alton Parkway Bldg 2 | workday | New Grad | [Apply](https://broadcom.wd1.myworkdayjobs.com/en-US/External_Career/job/USA-CA-Irvine-Alton-Parkway-Bldg-2/R-D-IC-Design-Engineer_R024631) | Aug 28, 2026 |
| Anduril | Embedded Firmware Engineer, Connected Warfare 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5225618007?gh_jid=5225618007) | Aug 28, 2026 |
| Veeva Systems | Marketing Analytics - Data Analyst - July 2027 Start Date - ADP 🇺🇸 | New York - New York City | lever | - | [Apply](https://jobs.lever.co/veeva/28c47d34-3ad6-4485-85a9-686b4239b9ea) | Aug 28, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | Massachusetts - Boston | lever | - | [Apply](https://jobs.lever.co/veeva/52ba79af-1086-457d-b5d2-8e184f111ffd) | Aug 28, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | California - Pleasanton | lever | - | [Apply](https://jobs.lever.co/veeva/8fe22df0-02b4-453d-919c-c8998cf913f6) | Aug 28, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | Ohio - Columbus | lever | - | [Apply](https://jobs.lever.co/veeva/907dccc7-0052-41e9-920b-28e5ba6aaba9) | Aug 28, 2026 |
| Two Sigma | Quantitative Software Engineer: Techniques Engineering 🇺🇸 | United States New York City | two_sigma | - | [Apply](https://careers.twosigma.com/careers/JobDetail/New-York-City-United-States-Quantitative-Software-Engineer-Techniques-Engineering/13080) | Aug 28, 2026 |
| Two Sigma | AI Research Scientist - Campus Full-Time 🇺🇸 | United States New York New York | two_sigma | New Grad | [Apply](https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-AI-Research-Scientist-Campus-Full-Time/13671) | Aug 28, 2026 |
| Two Sigma | Software Engineer, Enterprise Platform Engineering 🇺🇸 | United States New York New York | two_sigma | - | [Apply](https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-Software-Engineer-Enterprise-Platform-Engineering/13516) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/0a838e66-1ab0-4fc4-b4d3-4671c0352278) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/15844944-fb69-4b57-9531-e988650b20c6) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/18d901fc-93bb-4d18-9f04-c72031e20d79) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Infrastructure 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/4abf26b4-795c-420a-bf22-1ab98db268b4) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | Seattle, WA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/4d5a144e-87ea-45e2-a68c-3fad590629af) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Infrastructure 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/7d75bed5-45d8-4876-840a-2d92ea79c98d) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/94984771-0704-446c-88c6-91ce748f6d92) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad 🇺🇸 | Denver, CO | lever | New Grad | [Apply](https://jobs.lever.co/palantir/c34b424e-caf2-455a-b104-ae1096ccca29) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/e1a6c138-98bf-45e2-97f7-2c70371cc38a) | Aug 28, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/f362d7aa-360d-4059-ab38-f482742693b3) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer - Warp Speed 🇺🇸 | New York, NY | lever | - | [Apply](https://jobs.lever.co/palantir/13f99633-43b5-4459-8e84-25073f257c18) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Commercial 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728) | Aug 28, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/33243fb5-6907-40c7-930c-968b25d825d0) | Aug 28, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/5a28f3a5-8655-47f2-ab19-a79b8a319da8) | Aug 28, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/91117724-9389-48dc-912f-98e48d4d45d8) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/cbe90327-3e6e-451c-a54c-1d3cbcef5aeb) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - US Government 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/d1ac83d0-e923-42a5-8e6d-58dd0cab25ca) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer 🇺🇸 | New York, NY | lever | - | [Apply](https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Commercial 🇺🇸 | Chicago, IL | lever | New Grad | [Apply](https://jobs.lever.co/palantir/e500bcf3-19d8-4d3c-b340-4d76e4a55b40) | Aug 28, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Intel, US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/fbca0358-083a-4222-bdbb-3bd729b48382) | Aug 28, 2026 |
| Optiver | Graduate Software Engineer (2027 Start) 🇺🇸 | Austin | optiver | - | [Apply](https://www.optiver.com/join-us/jobs/technology/austin/graduate-software-engineer-2027-start/) | Aug 28, 2026 |
| Optiver | Graduate FPGA Engineer (2027 Start - Chicago) 🇺🇸 | Chicago | optiver | - | [Apply](https://www.optiver.com/join-us/jobs/technology/chicago/graduate-fpga-engineer-2027-start-chicago/) | Aug 28, 2026 |
| Optiver | Graduate Software Engineer (2027 Start) 🇺🇸 | Chicago | optiver | - | [Apply](https://www.optiver.com/join-us/jobs/technology/chicago/graduate-software-engineer-2027-start/) | Aug 28, 2026 |
| Nvidia | GPU PCIe and Boot Architect - New College Grad 2026 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-PCIe-and-Boot-Architect---New-College-Grad-2026_JR2021768) | Aug 28, 2026 |
| Marvell | Application Engineer - Early Career 🇺🇸 | Santa Clara, CA | workday | New Grad | [Apply](https://marvell.wd1.myworkdayjobs.com/en-US/MarvellCareers/job/Santa-Clara-CA/Application-Engineer---Early-Career_2503703) | Aug 28, 2026 |
| Luma AI | Software Engineer - Product 🇺🇸 | SF Bay Area, CA | gem | - | [Apply](https://jobs.gem.com/lumalabs-ai/am9icG9zdDodtsh6pWUJjQgE8lXoaEJi) | Aug 28, 2026 |
| CrowdStrike | Software Engineer – Sensor, Sensor Performance and Stability (Hybrid) 🇺🇸 | 2 Locations | workday | - | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Redmond-WA/Software-Engineer---Sensor--SaO--Hybrid-_R29874) | Aug 28, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS Route 53 Global Resolver, AWS Route 53 Global Resolver 🇺🇸 | Herndon, VA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10520075/software-development-engineer-aws-route-53-global-resolver-aws-route-53-global-resolver) | Aug 28, 2026 |
| SpaceX | OS/Platform Software Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8752620002?gh_jid=8752620002) | Aug 27, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform  (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8752935002?gh_jid=8752935002) | Aug 27, 2026 |
| Nvidia | Compiler Engineer, Backend- New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Compiler-Engineer--Backend--New-College-Grad-2026_JR2017290) | Aug 27, 2026 |
| Uber | Software Engineer I 🇺🇸 | New York City, NY, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/301277) | Aug 26, 2026 |
| Roblox | Software Engineer, Creator 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8115917?gh_jid=8115917) | Aug 26, 2026 |
| Broadcom | ASIC Verification Engineer 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://broadcom.wd1.myworkdayjobs.com/en-US/External_Career/job/USA-CA-Irvine-Alton-Parkway-Bldg-2/ASIC-Verification-Engineer_R026559) | Aug 26, 2026 |
| Vercel | Software Engineer, Data Platform 🇺🇸 | Hybrid - San Francisco, New York City | greenhouse | - | [Apply](https://job-boards.greenhouse.io/vercel/jobs/6161129004) | Aug 25, 2026 |
| Uber | Software Engineer I 🇺🇸 | San Francisco, CA, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/301203) | Aug 25, 2026 |
| SpaceX | Full Stack Software Engineer, Data Platform (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8746439002?gh_jid=8746439002) | Aug 25, 2026 |
| Nvidia | Cell Modeling and Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Cell-Modelling-and-Verification-Engineer---New-College-Grad-2026_JR2011631) | Aug 25, 2026 |
| CrowdStrike | Associate Security Engineer (Remote) 🇺🇸 | USA - Remote, TX | workday | - | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Remote-TX/Security-Engineer--Remote-_R26320) | Aug 25, 2026 |
| Applied Intuition | Build & Release Engineer - New Grad (December 2026) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/9534b49a-9feb-4063-ac33-a9c4d94a1352) | Aug 25, 2026 |
| Applied Intuition | UX Test Engineer - New Grad (December 2026) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/c222bb2f-893d-455b-8dd2-f585205632e4) | Aug 25, 2026 |
| Applied Intuition | OTA/Cloud Validation Engineer - New Grad (December 2026) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/e5ec6599-5ae4-4f0f-b0fd-cd6f4cad8d95) | Aug 25, 2026 |
| Anduril | OT Support Operator (Second Shift) - Factory Systems 🇺🇸 | Ashville, Ohio, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5221532007?gh_jid=5221532007) | Aug 25, 2026 |
| Nvidia | Technical Product Marketing Engineer, Metropolis - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Technical-Product-Marketing-Engineer--Metropolis---New-College-Grad-2026_JR2022906-1) | Aug 24, 2026 |
| Jump Trading | Campus Quantitative Researcher, PhD (Full-Time) 🇺🇸 | Chicago<br>New York | greenhouse | PhD, New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=8125888) | Aug 24, 2026 |
| Broadcom | PCIe QA Engineer 🇺🇸 | USA-California-San Jose-1320 Ridder Park Drive | workday | - | [Apply](https://broadcom.wd1.myworkdayjobs.com/en-US/External_Career/job/USA-California-San-Jose-1320-Ridder-Park-Drive/PCIe-QA-Engineer_R026923) | Aug 24, 2026 |
| Qualcomm | Machine Learning Researcher 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4429652864) | Aug 23, 2026 |
| Zillow | Applied Scientist, Shopping AI 🇺🇸 | United States | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4370817385) | Aug 23, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8741940002?gh_jid=8741940002) | Aug 23, 2026 |
| SIG | Sell Side Research Associate, Technology 🇺🇸 | New York, NY | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4445525476) | Aug 22, 2026 |
| Meta | Enterprise Systems Engineer 🇺🇸 | Menlo Park, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4455030849) | Aug 22, 2026 |
| SIG | Associate Linux/Window Engineer \| Platform Services \| Experienced Hire 🇺🇸 | Bala-Cynwyd, PA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4409221256) | Aug 22, 2026 |
| SIG | Associate Linux/Windows Engineer  - New Grad 🇺🇸 | Bala-Cynwyd, PA | linkedin | New Grad | [Apply](https://www.linkedin.com/jobs/view/4409629420) | Aug 22, 2026 |
| Applied Intuition | Research Scientist - Humanoid Robotics 🇺🇸 | Sunnyvale | ashby | PhD | [Apply](https://jobs.ashbyhq.com/applied/4cd7cf1d-717c-4887-93b4-520a40a906b1) | Aug 22, 2026 |
| Qualcomm | Video Software Engineer 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4436814013) | Aug 21, 2026 |
| SIG | Equity Research Sales Associate 🇺🇸 | New York, NY | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4414021921) | Aug 21, 2026 |
| Qualcomm | Software Engineer - Modem 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4446767992) | Aug 21, 2026 |
| Uber | Software Engineer I 🇺🇸 | Sunnyvale, CA, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/301056) | Aug 21, 2026 |
| SpaceX | Electromagnetic Effects Engineer (Starlink Aviation) 🇺🇸 | Woodinville, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8731514002?gh_jid=8731514002) | Aug 21, 2026 |
| Snowflake | Developer Advocate - AI & Developer Experiences 🇺🇸 | US-CA-Menlo Park | ashby | - | [Apply](https://jobs.ashbyhq.com/snowflake/267d8514-2580-4ade-b5d1-0ea41d11cf62) | Aug 21, 2026 |
| SIG | Sell Side Research Associate, Freight Transportation & Rail Equipment 🇺🇸 | New York, NY | linkedin | Bachelors | [Apply](https://www.linkedin.com/jobs/view/4406722221) | Aug 21, 2026 |
| SIG | Quantitative Strategy Developer - New Grad 🇺🇸 | Bala-Cynwyd, PA | linkedin | New Grad | [Apply](https://www.linkedin.com/jobs/view/4453487626) | Aug 21, 2026 |
| SIG | Trading System Engineer - New Grad 🇺🇸 | Bala-Cynwyd, PA | linkedin | New Grad | [Apply](https://www.linkedin.com/jobs/view/4454660119) | Aug 21, 2026 |
| Nvidia | Research Engineer, Interactive World Models - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Research-Engineer--Interactive-World-Models---New-College-Grad-2026_JR2023950) | Aug 21, 2026 |
| Nvidia | Architecture Energy Modeling Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Architecture-Energy-Modeling-Engineer---New-College-Grad-2026_JR2023398) | Aug 21, 2026 |
| Uber | Software Engineer I 🇺🇸 | Seattle, WA, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/301001) | Aug 20, 2026 |
| SpaceX | Electromagnetic Effects Test Engineer (Automotive/Satellite EMC) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8721179002?gh_jid=8721179002) | Aug 20, 2026 |
| Google | Data Engineer, Google Maps 🇺🇸 | Mountain View, CA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/72704944984990406) | Aug 20, 2026 |
| Crusoe | Software Engineer I, Network 🇺🇸 | San Francisco, CA - US | ashby | Early Career | [Apply](https://jobs.ashbyhq.com/Crusoe/9a5223c4-9eb7-4fdb-b97c-f43525df35ed) | Aug 20, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Hawthorne, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8724316002?gh_jid=8724316002) | Aug 19, 2026 |
| SpaceX | New Graduate Engineer, Software (Starship) 🇺🇸 | Starbase, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8729121002?gh_jid=8729121002) | Aug 19, 2026 |
| SpaceX | New Graduate Engineer, Software (Application Software) 🇺🇸 | Hawthorne, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8730567002?gh_jid=8730567002) | Aug 19, 2026 |
| Skydio | Lead GTM Platform Engineer 🇺🇸 | San Mateo, California, United States | ashby | - | [Apply](https://jobs.ashbyhq.com/skydio/ca13b237-ff5f-4008-977f-ba8c74b7d6da) | Aug 19, 2026 |
| xAI | OSP Engineer 🇺🇸 | Memphis, Tennessee<br>Southaven, Mississippi | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5215570007) | Aug 18, 2026 |
| Uber | Software Engineer I 🇺🇸 | San Francisco, CA, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/300883) | Aug 18, 2026 |
| SpaceX | Integration & Test Engineer, AI Satellites (Starmind) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8727656002?gh_jid=8727656002) | Aug 18, 2026 |
| SpaceX | Full Stack Software Engineer, Employee Experience 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8726225002?gh_jid=8726225002) | Aug 18, 2026 |
| Five Rings | LINK 2027: Software Development Intensive Program 🇺🇸 | New York | greenhouse | - | [Apply](https://job-boards.greenhouse.io/fiveringsllc/jobs/5394515008) | Aug 18, 2026 |
| Uber | Software Engineer I 🇺🇸 | San Francisco, CA, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/300814) | Aug 17, 2026 |
| Uber | Software Engineer I 🇺🇸 | New York City, NY, United States | uber | Early Career | [Apply](https://jobs.uber.com/en/jobs/300823) | Aug 17, 2026 |
| Roblox | Software Engineer, Foundation AI 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8123004?gh_jid=8123004) | Aug 17, 2026 |
| LangChain | Deployed Engineer (Early Career- SF) 🇺🇸 | San Francisco, CA | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/langchain/0f35c8e1-9318-411d-929b-04c60e6d8522) | Aug 17, 2026 |
| LangChain | Deployed Engineer (Early Career-NYC) 🇺🇸 | New York, NY | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/langchain/dfbba971-a7e2-4feb-a0d9-8e38a1155134) | Aug 17, 2026 |
| Qualcomm | Embedded Software Engineer – Device Driver Development 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4425829354) | Aug 15, 2026 |
| Qualcomm | Data Networking Software Engineer 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4442632896) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software - '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696058002?gh_jid=8696058002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software - '26/'27 (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696080002?gh_jid=8696080002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software  - '26/'27  (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696097002?gh_jid=8696097002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696143002?gh_jid=8696143002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696156002?gh_jid=8696156002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696158002?gh_jid=8696158002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8703552002?gh_jid=8703552002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Irvine, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8706884002?gh_jid=8706884002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8706885002?gh_jid=8706885002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, GNC- '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696105002?gh_jid=8696105002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, GNC- '26/'27 (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696124002?gh_jid=8696124002) | Aug 14, 2026 |
| SIG | Quantitative Researcher – Master's: 2027 🇺🇸 | Bala-Cynwyd, PA | linkedin | Masters | [Apply](https://www.linkedin.com/jobs/view/4431533759) | Aug 14, 2026 |
| SIG | Quantitative Researcher – Master's: 2027 🇺🇸 | New York, NY | linkedin | Masters | [Apply](https://www.linkedin.com/jobs/view/4431540631) | Aug 14, 2026 |
| Roblox | Software Engineer, Creator Business 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8113334?gh_jid=8113334) | Aug 14, 2026 |
| Notion | Software Engineer, New Grad (Dec 2026) 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/e32799d2-8ef8-4803-8189-c72514afa816) | Aug 14, 2026 |
| Applied Intuition | Embedded Test Engineer - New Grad (December 2026) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/0695a5b7-6823-4da5-b918-3b580d49662c) | Aug 14, 2026 |
| Applied Intuition | Software Integration Engineer - New Grad (2027) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/250080bd-10a8-4e5f-82b8-506029292d19) | Aug 14, 2026 |
| Applied Intuition | Research Engineer - New Grad (2027) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/45fc41cd-8280-4010-ba1f-def6114b3e39) | Aug 14, 2026 |
| Applied Intuition | Embedded Software Engineer - New Grad (2027) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/6971d533-1536-448b-96b8-544ad5383f44) | Aug 14, 2026 |
| Applied Intuition | Software Engineer - New Grad (December 2026) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/a837cbd6-9fe4-4d74-a2dc-84f602c40694) | Aug 14, 2026 |
| Applied Intuition | Scenario Engineer - New Grad (2027) 🇺🇸 | Sunnyvale | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/applied/f382de9d-d5e4-4dc8-85a0-0bae7125f8cf) | Aug 14, 2026 |
| Anduril | Embedded Software Engineer, Manufacturing Test, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5212828007?gh_jid=5212828007) | Aug 14, 2026 |
| SpaceX | IT Network Infrastructure Technician 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8707320002?gh_jid=8707320002) | Aug 13, 2026 |
| SpaceX | Full Stack Software Engineer (Components) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8706459002?gh_jid=8706459002) | Aug 13, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing Systems 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8703540002?gh_jid=8703540002) | Aug 12, 2026 |
| Roblox | Software Engineer, Account Authentication 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8097701?gh_jid=8097701) | Aug 12, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2023187) | Aug 12, 2026 |
| Nvidia | Software Verification Engineer - Networking 🇺🇸 | US, TX, Austin | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Networking-Verification-Engineer_JR2022759) | Aug 12, 2026 |
| SpaceX | Platform Engineer, Flight Software (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8692268002?gh_jid=8692268002) | Aug 11, 2026 |
| SpaceX | Flight Software Infrastructure Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8692260002?gh_jid=8692260002) | Aug 11, 2026 |
| SpaceX | Full Stack Software Engineer, MES (Manufacturing Execution System) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8696897002?gh_jid=8696897002) | Aug 11, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8696154002?gh_jid=8696154002) | Aug 11, 2026 |
| Adobe | Photoshop Developer, GPU/Imaging 🇺🇸 | 4 Locations | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Photoshop-Developer--GPU-Imaging_R171014) | Aug 11, 2026 |
| Qualcomm | Software Engineer - WLAN 🇺🇸 | Santa Clara, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4440753355) | Aug 08, 2026 |
| Google | Data Engineer, gTech Users and Products Engineering 🇺🇸 | Boulder, CO, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/127904573342786246) | Aug 07, 2026 |
| Google | Software Engineer, Early Career, Campus 🇺🇸 | Mountain View, CA, USA / Cambridge, MA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / New York, NY, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Jose, CA, USA / Sunnyvale, CA, USA | google_careers | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/78703249065943750) | Aug 07, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS Route 53 Global Resolver, AWS Route 53 Global Resolver 🇺🇸 | Herndon, VA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10496059/software-development-engineer-aws-route-53-global-resolver-aws-route-53-global-resolver) | Aug 07, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS Route 53 Global Resolver, AWS Route 53 Global Resolver 🇺🇸 | Herndon, VA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10496060/software-development-engineer-aws-route-53-global-resolver-aws-route-53-global-resolver) | Aug 07, 2026 |
| SpaceX | ASIC/SOC DFT Engineer (Silicon Engineering) 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8686199002?gh_jid=8686199002) | Aug 06, 2026 |
| CrowdStrike | CrowdStrike Platform Associate Resident Consultant (Remote) 🇺🇸 | 2 Locations | workday | - | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Remote-TX/CrowdStrike-Platform-Associate-Resident-Consultant--Remote-_R29426) | Aug 06, 2026 |
| CrowdStrike | Engineer I, Data Scientist - New Grad (Hybrid) 🇺🇸 | USA - Sunnyvale, CA | workday | New Grad | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Sunnyvale-CA/Engineer-I--Data-Scientist---New-Grad--Hybrid-_R29382-1) | Aug 06, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8686286002?gh_jid=8686286002) | Aug 05, 2026 |
| Roblox | [2027] Software Engineer, Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | New Grad | [Apply](https://careers.roblox.com/jobs/8072244?gh_jid=8072244) | Aug 05, 2026 |
| Apptronik | Software Engineer - Dexterous Manipulation 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/6135687004?gh_jid=6135687004) | Aug 05, 2026 |
| Applied Intuition | Android Software Engineer - Applications 🇺🇸 | Sunnyvale | ashby | - | [Apply](https://jobs.ashbyhq.com/applied/ffd8635d-43d5-4298-a29c-67eaa45c5a4a) | Aug 05, 2026 |
| SpaceX | GNC Engineer - Embedded Controls, AI Satellites (Starmind) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8677846002?gh_jid=8677846002) | Aug 04, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8681167002?gh_jid=8681167002) | Aug 04, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8675909002?gh_jid=8675909002) | Aug 04, 2026 |
| IMC Trading | Equity Research Analyst 🇺🇸 | Chicago, United States | greenhouse | - | [Apply](https://job-boards.eu.greenhouse.io/imc/jobs/4696380101) | Aug 04, 2026 |
| Fireworks AI | Member of Technical Staff, Research 🇺🇸 | San Mateo | ashby | - | [Apply](https://jobs.ashbyhq.com/fireworks/ee35bd97-43f9-4574-8ab7-81debd5d3d1a) | Aug 04, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | Aug 03, 2026 |
| Aurora Innovation | Software Engineer I (Data Eng infra) 🇺🇸 | Mountain View, CA | ashby | Early Career | [Apply](https://jobs.ashbyhq.com/aurora-operations-inc/8624caf6-91c7-4f27-a979-c3cab7877bca) | Aug 03, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8663562002?gh_jid=8663562002) | Jul 31, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658628002?gh_jid=8658628002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658737002?gh_jid=8658737002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658738002?gh_jid=8658738002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | McGregor, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658740002?gh_jid=8658740002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Vandenberg, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658742002?gh_jid=8658742002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658743002?gh_jid=8658743002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658744002?gh_jid=8658744002) | Jul 30, 2026 |
| Roblox | Software Engineer, User Frameworks 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8080438?gh_jid=8080438) | Jul 30, 2026 |
| Chime | Full-Stack Engineer, Human Agent Tooling 🇺🇸 | San Francisco, CA, USA | greenhouse | - | [Apply](https://boards.greenhouse.io/chime/jobs/8606649002?gh_jid=8606649002) | Jul 30, 2026 |
| Amazon Web Services (AWS) | SDE - CPLD / FPGA 🇺🇸 | Seattle, WA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10488714/sde-cpld-fpga) | Jul 30, 2026 |
| SpaceX | Full Stack Software Engineer, Data (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8656465002?gh_jid=8656465002) | Jul 29, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R168026) | Jul 29, 2026 |
| Adobe | Software Development Engineer - Front End 🇺🇸 | San Francisco | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Software-Development-Engineer---Front-End_R168188) | Jul 29, 2026 |
| Crusoe | Software Engineer I, Storage 🇺🇸 | San Francisco, CA - US | ashby | Early Career | [Apply](https://jobs.ashbyhq.com/Crusoe/4f5d34ed-0c05-4eec-b8f8-14663e114b02) | Jul 28, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8650988002?gh_jid=8650988002) | Jul 26, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8648213002?gh_jid=8648213002) | Jul 23, 2026 |
| Cerebras | Kernel Engineer - New Grad 🇺🇸 | Sunnyvale, CA | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/cerebras/9c7da4b8-446b-4bf2-8d07-23241590bf2e) | Jul 23, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8645325002?gh_jid=8645325002) | Jul 22, 2026 |
| OpenAI | Data Center Compute, OpenHouse Savannah 2026 🇺🇸 | US - Remote | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/6ba0ce24-ad32-4c3b-b49c-b373be9a8480) | Jul 22, 2026 |
| MongoDB | Technical Services Engineer 🇺🇸 | Palo Alto | greenhouse | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=8065812) | Jul 22, 2026 |
| Jane Street | Linux Engineer 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/8635672002?gh_jid=8635672002) | Jul 22, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8643772002?gh_jid=8643772002) | Jul 21, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8639573002?gh_jid=8639573002) | Jul 17, 2026 |
| Cerebras | Full Stack Engineer - Console Team 🇺🇸 | Sunnyvale, CA | ashby | - | [Apply](https://jobs.ashbyhq.com/cerebras/79eec4ee-8c02-407a-899c-3848f7c2a8b8) | Jul 17, 2026 |
| Jane Street | Linux Engineer 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/8626260002?gh_jid=8626260002) | Jul 15, 2026 |
| Google | Security Engineer, Detection 🇺🇸 | Reston, VA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/108836916245209798) | Jul 15, 2026 |
| SpaceX | Power Plant Engineer 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8623199002?gh_jid=8623199002) | Jul 14, 2026 |
| SpaceX | Integration & Test Engineer (Starlink Aviation) 🇺🇸 | Woodinville, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8629248002?gh_jid=8629248002) | Jul 14, 2026 |
| SpaceX | Design Verification Engineer (Silicon Engineering) 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8632967002?gh_jid=8632967002) | Jul 14, 2026 |
| Five Rings | Campus Full Time 2027 - Software Developer 🇺🇸 | New York | greenhouse | New Grad | [Apply](https://job-boards.greenhouse.io/fiveringsllc/jobs/5349839008) | Jul 14, 2026 |
| SpaceX | Application Software Engineer, Employee Experience 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8632106002?gh_jid=8632106002) | Jul 13, 2026 |
| Hudson River Trading | Software Engineer (C++ or Python) – 2027 Grads 🇺🇸 | Austin, TX, United States<br>Chicago, Illinois, United States<br>London, United Kingdom<br>New York, NY, United States<br>Singapore | greenhouse | MS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=8052122) | Jul 13, 2026 |
| Hudson River Trading | Algorithm Developer (Quant Research & Trading) – 2027 Grads 🇺🇸 | London, United Kingdom<br>New York, NY, United States<br>Singapore | greenhouse | MS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=8052050) | Jul 13, 2026 |
| Hudson River Trading | Algorithm Developer (Quant Research & Trading) – 2027 PhDs 🇺🇸 | London, United Kingdom<br>New York, NY, United States<br>Singapore | greenhouse | PhD Student | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=8059845) | Jul 13, 2026 |
| DRW | Software Developer 🇺🇸 | Chicago | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7980165) | Jul 13, 2026 |
| DRW | FPGA Developer 🇺🇸 | Chicago | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/8039110) | Jul 13, 2026 |
| Anduril | 2026 Early Career Test & Evaluation Systems Integrator 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5185888007?gh_jid=5185888007) | Jul 13, 2026 |
| Akuna Capital | Software Engineer (Entry-Level) - C++ 🇺🇸 | Chicago, IL | greenhouse | New Grad | [Apply](https://www.akunacapital.com/careers/job/8013085/?gh_jid=8013085) | Jul 13, 2026 |
| Akuna Capital | Software Engineer (Entry-Level) - Python 🇺🇸 | Chicago, IL | greenhouse | New Grad | [Apply](https://www.akunacapital.com/careers/job/8013230/?gh_jid=8013230) | Jul 13, 2026 |
| Akuna Capital | Junior Quantitative Developer & Strategist 🇺🇸 | Chicago, IL | greenhouse | - | [Apply](https://www.akunacapital.com/careers/job/8016687/?gh_jid=8016687) | Jul 13, 2026 |
| Akuna Capital | Junior Quantitative Researcher 🇺🇸 | Chicago, IL | greenhouse | - | [Apply](https://www.akunacapital.com/careers/job/8036541/?gh_jid=8036541) | Jul 13, 2026 |
| Jane Street | Hardware Engineer (FPGA/ASIC) 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/8624440002?gh_jid=8624440002) | Jul 10, 2026 |
| SpaceX | Data Engineer (Starlink) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8626500002?gh_jid=8626500002) | Jul 09, 2026 |
| SpaceX | Data Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8626535002?gh_jid=8626535002) | Jul 09, 2026 |
| Applied Intuition | OTA Validation Engineer 🇺🇸 | Sunnyvale | ashby | - | [Apply](https://jobs.ashbyhq.com/applied/567062a4-578e-4d05-a175-4fff84dd07b5) | Jul 09, 2026 |
| Anduril | 2026 Early Career Firmware Engineer 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5167865007?gh_jid=5167865007) | Jul 09, 2026 |
| SpaceX | Mission Integration Engineer (Starshield) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8624678002?gh_jid=8624678002) | Jul 08, 2026 |
| SpaceX | Integration & Test Engineer (Fairings) 🇺🇸 | Vandenberg, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8609453002?gh_jid=8609453002) | Jul 08, 2026 |
| Jump Trading | Campus Quantitative Researcher, UG/MS (Full-Time) 🇺🇸 | Chicago<br>New York | greenhouse | Masters, New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=7728630) | Jul 08, 2026 |
| Jump Trading | Campus Software Engineer (Full-Time) 🇺🇸 | Chicago | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=8000835) | Jul 08, 2026 |
| Jump Trading | Campus Systems Engineer (Full-Time) 🇺🇸 | Chicago | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=8008112) | Jul 08, 2026 |
| Jump Trading | Campus AI Research Engineer (Full-Time) 🇺🇸 | Chicago<br>New York | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=8052313) | Jul 08, 2026 |
| Jump Trading | Campus AI Research Engineer – Deep Learning (Full-Time) 🇺🇸 | Chicago<br>New York | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=8052343) | Jul 08, 2026 |
| Notion | Software Engineer, Early Career 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/297b4ece-765f-4eea-b1b8-46057cb6501f) | Jul 06, 2026 |
| Notion | Software Engineer, Early Career (AI) 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/85947779-6b87-466a-98bc-30a640448c28) | Jul 06, 2026 |
| Jane Street | Machine Learning Researcher 🇺🇸 | New York, New York, United States | greenhouse | PhD Student | [Apply](https://www.janestreet.com/join-jane-street/apply/8384490002?gh_jid=8384490002) | Jul 06, 2026 |
| Jane Street | Software Engineer 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/8419303002?gh_jid=8419303002) | Jul 06, 2026 |
| Jane Street | Quantitative Researcher 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/8498547002?gh_jid=8498547002) | Jul 06, 2026 |
| Hudson River Trading | Junior Trading Systems Engineer 🇺🇸 | Chicago, Illinois, United States<br>London, United Kingdom<br>New York, NY, United States | greenhouse | - | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=8046074) | Jul 06, 2026 |
| Akuna Capital | Junior Quantitative Risk Analyst 🇺🇸 | Chicago | greenhouse | - | [Apply](https://www.akunacapital.com/careers/job/8035515/?gh_jid=8035515) | Jul 06, 2026 |
| xAI | Software Engineer - Network (C++) 🇺🇸 | Palo Alto, California<br>Seattle, Washington | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5179367007) | Jul 02, 2026 |
| DoorDash | Software Engineer, Spark Platform 🇺🇸 | San Francisco, CA<br>Seattle, WA<br>Sunnyvale, CA<br>New York, NY | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/8044370) | Jul 02, 2026 |
| Anduril | Mission Software Engineer, EW 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5161108007?gh_jid=5161108007) | Jul 01, 2026 |
| Tesla | Vehicle Cabin Engineering Technician 🇺🇸 | Fremont, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4433886752) | Jun 30, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/8027587?gh_jid=8027587) | Jun 30, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/8027588?gh_jid=8027588) | Jun 30, 2026 |
| SpaceX | Full Stack Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8610872002?gh_jid=8610872002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611118002?gh_jid=8611118002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611189002?gh_jid=8611189002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611191002?gh_jid=8611191002) | Jun 26, 2026 |
| Discord | Software Engineer, Developer Success 🇺🇸 | San Francisco Bay Area | greenhouse | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8609250002) | Jun 26, 2026 |
| Anduril | Mission Engineer, Air Dominance & Strike, Early Career 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5174562007?gh_jid=5174562007) | Jun 25, 2026 |
| Hudson River Trading | Junior Treasury Quant Researcher 🇺🇸 | New York, NY, United States | greenhouse | - | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7364943) | Jun 24, 2026 |
| xAI | Associate Data Center Operations Technician 🇺🇸 | Memphis, Tennessee<br>Southaven, Mississippi | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5168434007) | Jun 23, 2026 |
| SpaceX | Network Software Integration Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8599648002?gh_jid=8599648002) | Jun 23, 2026 |
| SpaceX | Embedded Software Engineer, Satellite Antenna (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8603628002?gh_jid=8603628002) | Jun 23, 2026 |
| SpaceX | Integration Engineer, Heatshield (Starship) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8603368002?gh_jid=8603368002) | Jun 22, 2026 |
| SpaceX | Application Software Engineer, Manufacturing Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8600012002?gh_jid=8600012002) | Jun 18, 2026 |
| Snowflake | AI Research Scientist, New Grad – Agents & Reinforcement Learning 🇺🇸 | US-WA-Bellevue | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/snowflake/1bad12df-f443-426f-9d09-e96fc780d698) | Jun 16, 2026 |
| Anduril | 2027 Early Career Software Engineer 🇺🇸 | Atlanta, Georgia, United States<br>Boston, Massachusetts, United States<br>Broomfield, Colorado, United States<br>Colorado Springs, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States<br>Irvine, California, United States<br>Reston, Virginia, United States<br>Seattle, Washington, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5162263007?gh_jid=5162263007) | Jun 11, 2026 |
| SpaceX | Electromagnetic Effects Test Engineer 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8586528002?gh_jid=8586528002) | Jun 10, 2026 |
| SpaceX | Embedded Software Engineer, Laser Mesh Routing (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8578934002?gh_jid=8578934002) | Jun 09, 2026 |
| SpaceX | Embedded Software Engineer, Laser Mesh Routing (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8578936002?gh_jid=8578936002) | Jun 09, 2026 |
| SpaceX | Factory Software Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8574053002?gh_jid=8574053002) | Jun 08, 2026 |
| Arista Networks | Advisory/ Resident Systems Engineer - (Mandarin required) 🇺🇸 | San Jose, CA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000130221863) | Jun 04, 2026 |
| SpaceX | Integration Engineer (Starship) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8576029002?gh_jid=8576029002) | Jun 02, 2026 |
| xAI | Software Engineer, Ads Product 🇺🇸 | Palo Alto, California | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5152408007) | Jun 01, 2026 |
| SpaceX | Product Development Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8545873002?gh_jid=8545873002) | Jun 01, 2026 |
| SpaceX | Integration & Test Engineer (Bus & Payload Sub-Assemblies) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8571994002?gh_jid=8571994002) | Jun 01, 2026 |
| SpaceX | Financial Systems Analyst 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8571649002?gh_jid=8571649002) | Jun 01, 2026 |
| SpaceX | Data Engineer (Starship) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8569186002?gh_jid=8569186002) | Jun 01, 2026 |
| Tesla | Camera Systems Integration Technician, Reliability & Test 🇺🇸 | Fremont, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4420210980) | May 31, 2026 |
| Google | ASIC Design Verification Engineer, Google Cloud 🇺🇸 | Sunnyvale, CA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/77174102632080070) | May 29, 2026 |
| SpaceX | Integration Engineer (Super Heavy Booster) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8567325002?gh_jid=8567325002) | May 27, 2026 |
| Jump Trading | Digital Modem Engineer 🇺🇸 | Chicago, New York, London or Bristol | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=7951911) | May 27, 2026 |
| SpaceX | Integration & Test Engineer (Starship) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8553658002?gh_jid=8553658002) | May 26, 2026 |
| SpaceX | Flight Software Engineer (Starlink Mobile) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8556909002?gh_jid=8556909002) | May 20, 2026 |
| SpaceX | AI Software Engineer (Vehicle Engineering) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8559015002?gh_jid=8559015002) | May 20, 2026 |
| Arista Networks | Resident Engineer 🇺🇸 | Austin, TX, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000127345398) | May 20, 2026 |
| SpaceX | Full Stack Software Engineer (Build Reliability) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8555791002?gh_jid=8555791002) | May 19, 2026 |
| Cerebras | Member of Technical Staff (Software Engineer) 🇺🇸 | Sunnyvale, CA | ashby | - | [Apply](https://jobs.ashbyhq.com/cerebras/24e42002-7f6d-4769-9ce0-0d844757cc0e) | May 08, 2026 |
| SpaceX | Lead Starship Engineer (Ship Vehicle Assembly) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533755002?gh_jid=8533755002) | May 06, 2026 |
| OpenAI | Networking Operating System Firmware Engineer 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/f6b9903c-9034-436b-a4ec-4c8643a6d0dd) | May 06, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starshield) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530798002?gh_jid=8530798002) | May 05, 2026 |
| Apptronik | Robotics Test Engineer 🇺🇸 | Onsite - Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/5988482004?gh_jid=5988482004) | May 05, 2026 |
| SpaceX | Integration Engineer (Starship) - Night Shift 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8527462002?gh_jid=8527462002) | Apr 29, 2026 |
| DoorDash | AI Research Fellowship, (Summer and Fall 2026) 🇺🇸 | San Francisco, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7848317) | Apr 29, 2026 |
| SpaceX | Integration & Test Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8527331002?gh_jid=8527331002) | Apr 28, 2026 |
| Akuna Capital | Quantitative Researcher - Prediction Markets 🇺🇸 | Chicago, IL | greenhouse | - | [Apply](https://www.akunacapital.com/careers/job/7846695/?gh_jid=7846695) | Apr 28, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5111318007?gh_jid=5111318007) | Apr 24, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8511391002?gh_jid=8511391002) | Apr 21, 2026 |
| OpenAI | Performance Modeling Engineer ~2 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/4f6be73e-9a1d-4ec6-8b0e-b2af0b4becfb) | Apr 20, 2026 |
| Point72 | Fundamental Research Fellow, Canvas 🇺🇸 | New York, NY | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/8492784002?gh_jid=8492784002) | Apr 15, 2026 |
| SpaceX | Full Stack Software Engineer (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8501225002?gh_jid=8501225002) | Apr 13, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002) | Apr 06, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002) | Apr 06, 2026 |
| SpaceX | New Graduate Engineer, Software 🇺🇸 | Hawthorne, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8493079002?gh_jid=8493079002) | Apr 03, 2026 |
| Applied Intuition | Software Engineer - Python 🇺🇸 | Sunnyvale | ashby | - | [Apply](https://jobs.ashbyhq.com/applied/32e39ce9-9c09-4dd9-9ad1-4ee0b0cf7907) | Mar 18, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080387007?gh_jid=5080387007) | Mar 16, 2026 |
| Applied Intuition | Software Engineer - C++ 🇺🇸 | Sunnyvale | ashby | - | [Apply](https://jobs.ashbyhq.com/applied/c9473dcb-f651-47bb-9a59-4150bddcdaa8) | Mar 04, 2026 |
| OpenAI | Hardware Tools Engineer 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/467cbfac-3e7d-4cc6-a131-2b26617afa02) | Mar 02, 2026 |
| DRW | Quantitative Researcher 🇺🇸 | New York | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7650182) | Feb 25, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer Apprentice - Military Veterans 🇺🇸 | Seattle, WA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/3188438/software-development-engineer-apprentice-military-veterans) | Feb 24, 2026 |
| Cerebras | AI Inference Core - Software Integration Engineer 🇺🇸 | United States and Canada | ashby | - | [Apply](https://jobs.ashbyhq.com/cerebras/90879967-1071-4d05-9180-6e18023ed887) | Feb 05, 2026 |
| ServiceNow | Associate Software Engineer, Core Infrastructure - Moveworks 🇺🇸 | Mountain View, CALIFORNIA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/ServiceNow/744000107369741) | Feb 04, 2026 |
| Hudson River Trading | Software Engineer - Python 🇺🇸 | Chicago, Illinois, United States<br>London, United Kingdom<br>New York, NY, United States | greenhouse | BS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7398013) | Feb 02, 2026 |
| Hudson River Trading | Research Engineer 🇺🇸 | London, United Kingdom<br>New York, NY, United States | greenhouse | BS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7583922) | Feb 02, 2026 |
| Hudson River Trading | Software Engineer - Treasury Infrastructure 🇺🇸 | New York, NY, United States | greenhouse | BS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7583953) | Feb 02, 2026 |
| Hudson River Trading | Software Engineer - AI Tools 🇺🇸 | Chicago, Illinois, United States<br>New York, NY, United States | greenhouse | BS Student, New Grad | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7583957) | Feb 02, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016001007?gh_jid=5016001007) | Jan 06, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016334007?gh_jid=5016334007) | Jan 06, 2026 |
| Akuna Capital | Software Engineer - C++ 🇺🇸 | Chicago, IL | greenhouse | New Grad | [Apply](https://www.akunacapital.com/careers/job/7496397/?gh_jid=7496397) | Jan 02, 2026 |
| Arista Networks | Software L1 Test Engineer 🇺🇸 | Santa Clara, CA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000101072105) | Dec 30, 2025 |
| Five Rings | Experienced/Lateral - Quantitative Researcher 🇺🇸 | New York | greenhouse | - | [Apply](https://job-boards.greenhouse.io/fiveringsllc/jobs/5046298008) | Dec 23, 2025 |
| Datadog | Technical Support Engineer 1, Premier - USA 🇺🇸 | Denver, Colorado, USA<br>New York, New York, USA<br>San Francisco, California, USA | greenhouse | Early Career | [Apply](https://careers.datadoghq.com/detail/7449072/?gh_jid=7449072) | Dec 10, 2025 |
| Scale AI | Machine Learning Research Engineer, Agents - Enterprise GenAI 🇺🇸 | San Francisco, CA<br>New York, NY | greenhouse | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4625344005) | Oct 31, 2025 |
| Roblox | [2026] Senior Machine Learning Engineer, Recommendation Systems - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7350081?gh_jid=7350081) | Oct 27, 2025 |
| CoreWeave | Software Engineer, Inference AI/ML 🇺🇸 | Sunnyvale, CA / Bellevue, WA | greenhouse | - | [Apply](https://coreweave.com/careers/job?4609928006&board=coreweave&gh_jid=4609928006) | Oct 24, 2025 |
| Point72 | Machine Learning Engineer 🇺🇸 | New York | greenhouse | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002) | Sep 15, 2025 |
| Anduril | GNC Engineer, Space 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870847007?gh_jid=4870847007) | Sep 11, 2025 |
| Anduril | GNC Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870871007?gh_jid=4870871007) | Sep 11, 2025 |
| Mercor | Data Scientist 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/mercor/982a0751-e9eb-4b96-ac93-a1fd1d2f9152) | Aug 30, 2025 |
| Anduril | 2026 Early Career Software Engineer 🇺🇸 | Atlanta, Georgia, United States<br>Colorado Springs, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States<br>Seattle, Washington, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | Aug 11, 2025 |
| Ramp | Mobile Engineer, iOS 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f) | Jul 31, 2025 |
| Ramp | Mobile Engineer, Android 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040) | Jul 31, 2025 |
| DRW | Research Engineer 🇺🇸 | New York City | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/6973885) | Jun 16, 2025 |
| IMC Trading | Software Engineer, Early Career 🇺🇸 | Chicago, United States | greenhouse | New Grad | [Apply](https://job-boards.eu.greenhouse.io/imc/jobs/4577504101) | Apr 17, 2025 |
| Point72 | Data Engineer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002) | Jan 23, 2025 |
| Point72 | Quantitative Software Developer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7825863002?gh_jid=7825863002) | Jan 22, 2025 |
| Point72 | 2027 Cubist Quant Academy – Developers 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7598678002?gh_jid=7598678002) | Sep 09, 2024 |
| Point72 | Quantitative Researcher - Machine Learning 🇺🇸 | New York | greenhouse | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/7297513002?gh_jid=7297513002) | Aug 15, 2024 |
| Point72 | Quantitative Analyst / Software Developer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7297622002?gh_jid=7297622002) | Aug 15, 2024 |
| Jane Street | Machine Learning Performance Engineer 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/7449077002?gh_jid=7449077002) | May 20, 2024 |
| Jane Street | Machine Learning Performance Engineer 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.janestreet.com/join-jane-street/apply/7449190002?gh_jid=7449190002) | May 20, 2024 |
| Jump Trading | HPC Systems Engineer 🇺🇸 | Chicago | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=5752845) | Mar 08, 2024 |
| Jump Trading | UI Developer 🇺🇸 | Chicago | greenhouse | New Grad | [Apply](https://www.jumptrading.com/hr/job?gh_jid=5500453) | Dec 05, 2023 |


<details>
<summary><b>Closed positions (23)</b> &mdash; click to expand</summary>


| Company | Role | Location | Source | Education | Apply | Date Posted |
|---------|------|----------|--------|-----------|-------|-------------|
| ~~Qualcomm~~ | ~~Embedded Systems Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 28, 2026 |
| ~~Intuit~~ | ~~Distinguished Engineer - Distinguished Engineer, Data Foundation 🇺🇸~~ | Mountain View, CA | linkedin | - | Closed | Aug 28, 2026 |
| ~~Qualcomm~~ | ~~Machine Learning Compiler 🇺🇸~~ | New York, NY | linkedin | - | Closed | Aug 27, 2026 |
| ~~Qualcomm~~ | ~~Video DV Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 27, 2026 |
| ~~GitHub~~ | ~~Java Software Engineer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Aug 27, 2026 |
| ~~GitHub~~ | ~~Java Software Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Aug 27, 2026 |
| ~~Meta~~ | ~~Software Engineer, Systems ML - Compilers / Backend 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Aug 26, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician 🇺🇸~~ | Boxborough, MA | linkedin | - | Closed | Aug 26, 2026 |
| ~~GitHub~~ | ~~Software Developer 🇺🇸~~ | Phoenix, AZ | linkedin | - | Closed | Aug 26, 2026 |
| ~~GitHub~~ | ~~Software Developer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Aug 26, 2026 |
| ~~Qualcomm~~ | ~~Modem Integration & Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 22, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | New York, NY | linkedin | Early Career | Closed | Aug 22, 2026 |
| ~~SIG~~ | ~~Compensation Systems Coordinator 🇺🇸~~ | Bala-Cynwyd, PA | linkedin | - | Closed | Aug 21, 2026 |
| ~~Qualcomm~~ | ~~System Level Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 21, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | Atlanta, GA | linkedin | Early Career | Closed | Aug 21, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | San Diego, CA | linkedin | Early Career | Closed | Aug 21, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | Mountain View, CA | linkedin | Early Career | Closed | Aug 21, 2026 |
| ~~GitHub~~ | ~~QA Engineer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Aug 21, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician, Intermediate 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 15, 2026 |
| ~~SIG~~ | ~~Software Developer \| Core Order Management System \| C++ \| Experienced Hire 🇺🇸~~ | Chicago, IL | linkedin | - | Closed | Aug 14, 2026 |
| ~~Qualcomm~~ | ~~Systems SoC Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 14, 2026 |
| ~~Nvidia~~ | ~~GPU Verification Engineer - New College Grad 2026 🇺🇸~~ | US, MA, Westford | workday | New Grad | Closed | Jul 29, 2026 |
| ~~Marvell~~ | ~~Digital Design Engineer 🇺🇸~~ | Irvine, CA | workday | - | Closed | Jul 29, 2026 |

</details>

## How it works

1. Hourly GitHub Action queries each company's public ATS API.
2. Titles run through a regex filter (must hit one of:
   `intern, new grad, university graduate, early career, entry level,
   campus, 2026, 2027`; must NOT hit any of:
   `senior, lead, manager, principal, director, head of, staff, vp,
   president`).
3. Locations are filtered to the US by default.
4. New postings ping a Discord webhook in real-time.
5. State is committed back -- this README is regenerated every run.

Want a different scope? See [README\_TECH.md](README_TECH.md) -- you can
toggle the US filter, add tier-3 companies, change the cadence, etc.

