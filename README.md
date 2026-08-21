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

- **Open positions:** 307
- **All-time tracked:** 736
- **Active companies:** 139
- **Last run (raw / matched):** 29278 postings fetched, 305 passed filters
- **Last updated:** `2026-08-21 04:46 UTC`

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
| Xaira Therapeutics | AI in Residence, Computational Protein Design 🇺🇸 | Seattle, Washington, United States | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5156238007) | Aug 20, 2026 |
| Google | Data Engineer, Google Maps 🇺🇸 | Mountain View, CA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/72704944984990406) | Aug 20, 2026 |
| CrowdStrike | Associate Security Engineer (Remote) 🇺🇸 | USA - Remote, TX | workday | - | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Remote-TX/Security-Engineer--Remote-_R26320) | Aug 20, 2026 |
| Crusoe | Software Engineer I, Network 🇺🇸 | San Francisco, CA - US | ashby | Early Career | [Apply](https://jobs.ashbyhq.com/Crusoe/9a5223c4-9eb7-4fdb-b97c-f43525df35ed) | Aug 20, 2026 |
| Microsoft | Quantum Software Engineer 🇺🇸 | Redmond, WA, US | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556972166) | Aug 19, 2026 |
| SpaceX | New Graduate Engineer, Software (Application Software) 🇺🇸 | Hawthorne, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8730567002?gh_jid=8730567002) | Aug 19, 2026 |
| Skydio | Lead GTM Platform Engineer 🇺🇸 | San Mateo, California, United States | ashby | - | [Apply](https://jobs.ashbyhq.com/skydio/ca13b237-ff5f-4008-977f-ba8c74b7d6da) | Aug 19, 2026 |
| Microsoft | Design Verification Engineer 🇺🇸 | Mountain View, CA, US | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556962661) | Aug 19, 2026 |
| Microsoft | AI for Science Residency - Machine Learning Resident 🇺🇸 | Berlin, BE, DE / Cambridge, England, GB / Amsterdam, NH, NL | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556871066) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Deep Learning Computer Architecture 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Deep-Learning-Computer-Architecture_JR2023491) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Deep Learning 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Deep-Learning_JR2023497-1) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Digital Circuit Design 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Digital-Circuit-Design_JR2023504) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Hardware ASIC Design 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-ASIC-Design_JR2023486) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Hardware Engineering 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Engineering_JR2023508-1) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Hardware Physical Design / VLSI 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Physical-Design---VLSI_JR2023501) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Hardware Verification 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Hardware-Verification_JR2023500) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Autonomous Vehicles 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Autonomous-Vehicles_JR2023838) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Computer Architecture and Systems 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Computer-Architecture-and-Systems_JR2023854) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Computer Vision and Deep Learning 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Computer-Vision-and-Deep-Learning_JR2023833) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Generative AI 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Generative-AI_JR2023475) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Graphics and Simulation 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Graphics-and-Simulation_JR2023835) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Hardware 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Hardware_JR2023855) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Large Language Models 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Large-Language-Models_JR2023837) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Ph.D. Research Robotics 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--PhD-Research-Robotics_JR2023847) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Software Engineering 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Software-Engineering_JR2023495) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Internships: Systems Software Engineering 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Internships--Systems-Software-Engineering_JR2023492) | Aug 19, 2026 |
| Nvidia | NVIDIA 2027 Summer Internships: Ph.D. Engineering 🇺🇸 | US, CA, Santa Clara | workday | PhD | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-2027-Summer-Internships--PhD-Engineering_JR2023856) | Aug 19, 2026 |
| Nvidia | NVIDIA Spring 2027 Internships: Developer and Performance Technology 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/NVIDIA-Spring-2027-Internships--Developer-and-Performance-Technology_JR2023499) | Aug 19, 2026 |
| SpaceX | New Graduate Engineer, Software (Starship) 🇺🇸 | Starbase, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8729121002?gh_jid=8729121002) | Aug 19, 2026 |
| Nvidia | System Software Engineer - Trusted Firmware 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/System-Software-Engineer---Trusted-Firmware_JR2023340) | Aug 18, 2026 |
| Microsoft | Sourcing Engineer 🇺🇸 | Redmond, WA, US | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556972462) | Aug 18, 2026 |
| xAI | OSP Engineer 🇺🇸 | Memphis, Tennessee<br>Southaven, Mississippi | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5215570007) | Aug 18, 2026 |
| SpaceX | Integration & Test Engineer, AI Satellites (Starmind) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8727656002?gh_jid=8727656002) | Aug 18, 2026 |
| SpaceX | Full Stack Software Engineer, Employee Experience 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8726225002?gh_jid=8726225002) | Aug 18, 2026 |
| Roblox | Software Engineer, Foundation AI 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8123004?gh_jid=8123004) | Aug 17, 2026 |
| Nvidia | Verification Engineer - New College Grad 2026 🇺🇸 | 3 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Verification-Engineer---New-College-Grad-2026_JR2021016) | Aug 17, 2026 |
| Qualcomm | Engineering Technician, Intermediate 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4453931235) | Aug 15, 2026 |
| Meta | Data Engineer, Product Analytics 🇺🇸 | New York, NY | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4451724497) | Aug 15, 2026 |
| Lyft | Software Engineer, Fulfillment Core Services 🇺🇸 | Seattle, WA | greenhouse | - | [Apply](https://app.careerpuck.com/job-board/lyft/job/8716222002?gh_jid=8716222002) | Aug 14, 2026 |
| Anduril | Embedded Software Engineer, Manufacturing Test, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5212828007?gh_jid=5212828007) | Aug 14, 2026 |
| Notion | Software Engineer, New Grad (Dec 2026) 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/e32799d2-8ef8-4803-8189-c72514afa816) | Aug 14, 2026 |
| Figma | Product Designer, Design Systems 🇺🇸 | San Francisco, CA • New York, NY • United States | greenhouse | - | [Apply](https://boards.greenhouse.io/figma/jobs/5787576004?gh_jid=5787576004) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software - '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696058002?gh_jid=8696058002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software - '26/'27 (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696080002?gh_jid=8696080002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software  - '26/'27  (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696097002?gh_jid=8696097002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, GNC- '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696105002?gh_jid=8696105002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, GNC- '26/'27 (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696124002?gh_jid=8696124002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696143002?gh_jid=8696143002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696156002?gh_jid=8696156002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Software Security - '26/'27 (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8696158002?gh_jid=8696158002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Palo Alto, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8703552002?gh_jid=8703552002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Irvine, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8706884002?gh_jid=8706884002) | Aug 14, 2026 |
| SpaceX | New Graduate Engineer, Silicon Engineering 🇺🇸 | Redmond, WA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8706885002?gh_jid=8706885002) | Aug 14, 2026 |
| Nvidia | Software Engineer, Infrastructure - DGX Cloud 🇺🇸 | US, CA, Santa Clara | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineer--Infrastructure---DGX-Cloud_JR2022400) | Aug 14, 2026 |
| Microsoft | UK Residency Programme - Optoelectronics Device Engineer 🇺🇸 | Cambridge, England, GB | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556962583) | Aug 14, 2026 |
| Roblox | Software Engineer, Creator Business 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8113334?gh_jid=8113334) | Aug 14, 2026 |
| SpaceX | IT Network Infrastructure Technician 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8707320002?gh_jid=8707320002) | Aug 13, 2026 |
| SpaceX | Full Stack Software Engineer (Components) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8706459002?gh_jid=8706459002) | Aug 13, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing Systems 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8703540002?gh_jid=8703540002) | Aug 12, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2023187) | Aug 12, 2026 |
| Roblox | Software Engineer, Account Authentication 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8097701?gh_jid=8097701) | Aug 12, 2026 |
| Adobe | Photoshop Developer, GPU/Imaging 🇺🇸 | 4 Locations | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Photoshop-Developer--GPU-Imaging_R171014) | Aug 11, 2026 |
| SpaceX | Platform Engineer, Flight Software (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8692268002?gh_jid=8692268002) | Aug 11, 2026 |
| SpaceX | Flight Software Infrastructure Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8692260002?gh_jid=8692260002) | Aug 11, 2026 |
| Mercor | Fullstack Software Engineer, Agent Platform 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/mercor/3750ee8a-64d1-46ac-b4f9-6a823f949034) | Aug 11, 2026 |
| SpaceX | Full Stack Software Engineer, MES (Manufacturing Execution System) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8696897002?gh_jid=8696897002) | Aug 11, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8696154002?gh_jid=8696154002) | Aug 11, 2026 |
| Robinhood | Privacy Engineer 🇺🇸 | New York, NY | greenhouse | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/8109753?t=gh_src=&gh_jid=8109753) | Aug 07, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS Route 53 Global Resolver, AWS Route 53 Global Resolver 🇺🇸 | Herndon, VA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10496060/software-development-engineer-aws-route-53-global-resolver-aws-route-53-global-resolver) | Aug 07, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS Route 53 Global Resolver, AWS Route 53 Global Resolver 🇺🇸 | Herndon, VA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10496059/software-development-engineer-aws-route-53-global-resolver-aws-route-53-global-resolver) | Aug 07, 2026 |
| Google | Data Engineer, gTech Users and Products Engineering 🇺🇸 | Boulder, CO, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/127904573342786246) | Aug 07, 2026 |
| Google | Software Engineer, Early Career, Campus 🇺🇸 | Mountain View, CA, USA / Cambridge, MA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / New York, NY, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Jose, CA, USA / Sunnyvale, CA, USA | google_careers | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/78703249065943750) | Aug 07, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | Massachusetts - Boston | lever | - | [Apply](https://jobs.lever.co/veeva/52ba79af-1086-457d-b5d2-8e184f111ffd) | Aug 06, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | California - Pleasanton | lever | - | [Apply](https://jobs.lever.co/veeva/8fe22df0-02b4-453d-919c-c8998cf913f6) | Aug 06, 2026 |
| Veeva Systems | Associate Software Engineer - 2027 Start Dates 🇺🇸 | Ohio - Columbus | lever | - | [Apply](https://jobs.lever.co/veeva/907dccc7-0052-41e9-920b-28e5ba6aaba9) | Aug 06, 2026 |
| SpaceX | ASIC/SOC DFT Engineer (Silicon Engineering) 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8686199002?gh_jid=8686199002) | Aug 06, 2026 |
| Robinhood | Software Engineer, Wallet 🇺🇸 | Menlo Park, CA<br>New York, NY | greenhouse | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/8088444?t=gh_src=&gh_jid=8088444) | Aug 06, 2026 |
| Nvidia | Technical Product Marketing Engineer, Metropolis - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Technical-Product-Marketing-Engineer--Metropolis---New-College-Grad-2026_JR2022906-1) | Aug 06, 2026 |
| Nvidia | Software Verification Engineer - Networking 🇺🇸 | US, TX, Austin | workday | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Networking-Verification-Engineer_JR2022759) | Aug 06, 2026 |
| Zillow | Machine Learning Engineer, Agentic AI 🇺🇸 | United States | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4449342875) | Aug 06, 2026 |
| Meta | Security Engineer, Investigator - GenAI 🇺🇸 | Seattle, WA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4447394053) | Aug 05, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8686286002?gh_jid=8686286002) | Aug 05, 2026 |
| Apptronik | Software Engineer - Dexterous Manipulation 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/6135687004?gh_jid=6135687004) | Aug 05, 2026 |
| Roblox | [2027] Software Engineer, Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | New Grad | [Apply](https://careers.roblox.com/jobs/8072244?gh_jid=8072244) | Aug 05, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8681167002?gh_jid=8681167002) | Aug 04, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8675909002?gh_jid=8675909002) | Aug 04, 2026 |
| Stripe | Software Engineer, Vulnerability Management 🇺🇸 | US - Remote | greenhouse | - | [Apply](https://stripe.com/jobs/search?gh_jid=8089353) | Aug 04, 2026 |
| SpaceX | GNC Engineer - Embedded Controls, AI Satellites (Starmind) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8677846002?gh_jid=8677846002) | Aug 04, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | Aug 03, 2026 |
| LangChain | Deployed Engineer (Early Career-NYC) 🇺🇸 | New York, NY | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/langchain/dfbba971-a7e2-4feb-a0d9-8e38a1155134) | Aug 03, 2026 |
| Samsara | Software Engineer I - New Grad, SF 🇺🇸 | San Francisco - SF9 | greenhouse | BS Student, New Grad | [Apply](https://www.samsara.com/company/careers/roles/8097343?gh_jid=8097343) | Aug 03, 2026 |
| Meta | Software Engineer, Systems ML - Compilers / Backend 🇺🇸 | New York, NY | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4445800768) | Aug 01, 2026 |
| Roblox | Software Engineer, Communications 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8083944?gh_jid=8083944) | Jul 31, 2026 |
| SpaceX | Full Stack Software Engineer, Internal Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8663562002?gh_jid=8663562002) | Jul 31, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658628002?gh_jid=8658628002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658737002?gh_jid=8658737002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658738002?gh_jid=8658738002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | McGregor, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658740002?gh_jid=8658740002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Vandenberg, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658742002?gh_jid=8658742002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658743002?gh_jid=8658743002) | Jul 30, 2026 |
| SpaceX | Application Software Engineer, Applied AI 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8658744002?gh_jid=8658744002) | Jul 30, 2026 |
| Amazon Web Services (AWS) | SDE - CPLD / FPGA 🇺🇸 | Seattle, WA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10488714/sde-cpld-fpga) | Jul 30, 2026 |
| Roblox | Software Engineer, User Frameworks 🇺🇸 | San Mateo, CA, United States | greenhouse | - | [Apply](https://careers.roblox.com/jobs/8080438?gh_jid=8080438) | Jul 30, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, FSx for Lustre 🇺🇸 | Boston, MA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10488415/software-development-engineer-fsx-for-lustre) | Jul 30, 2026 |
| Qualcomm | Software Engineer - Modem 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4446767992) | Jul 30, 2026 |
| CrowdStrike | CrowdStrike Platform Associate Resident Consultant (Remote) 🇺🇸 | 2 Locations | workday | - | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Remote-TX/CrowdStrike-Platform-Associate-Resident-Consultant--Remote-_R29426) | Jul 29, 2026 |
| SpaceX | Full Stack Software Engineer, Data (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8656465002?gh_jid=8656465002) | Jul 29, 2026 |
| Meta | Data Engineer, Product Analytics 🇺🇸 | Menlo Park, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4444108088) | Jul 29, 2026 |
| Meta | Data Engineer, Product Analytics 🇺🇸 | Los Angeles, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4444109072) | Jul 29, 2026 |
| Meta | Software Engineer, Machine Learning RecSys 🇺🇸 | Burlingame, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4443671415) | Jul 29, 2026 |
| Meta | ASIC Engineer, Design Verification 🇺🇸 | Sunnyvale, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4443253470) | Jul 28, 2026 |
| Broadcom | ASIC Verification Engineer 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://broadcom.wd1.myworkdayjobs.com/en-US/External_Career/job/USA-CA-Irvine-Alton-Parkway-Bldg-2/ASIC-Verification-Engineer_R026559) | Jul 28, 2026 |
| Snowflake | Software Engineer - Database Engineering 🇺🇸 | US-CA-Menlo Park | ashby | PhD | [Apply](https://jobs.ashbyhq.com/snowflake/db1375f0-ea5d-404a-b640-259f94dbc995) | Jul 28, 2026 |
| Qualcomm | Robotics Systems Integration and Test Engineer - Qualcomm Advanced Robotics Team 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4445758870) | Jul 28, 2026 |
| Crusoe | Software Engineer I, Storage 🇺🇸 | San Francisco, CA - US | ashby | Early Career | [Apply](https://jobs.ashbyhq.com/Crusoe/4f5d34ed-0c05-4eec-b8f8-14663e114b02) | Jul 28, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8650988002?gh_jid=8650988002) | Jul 26, 2026 |
| Meta | ASIC Implementation Engineer - Static Verification 🇺🇸 | Austin, TX | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4442313335) | Jul 25, 2026 |
| GitHub | Full-Stack Software Engineer 🇺🇸 | Southlake, TX | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4441822187) | Jul 24, 2026 |
| Nvidia | Research Scientist, Robotics Research -  PhD New College Grad 2026 🇺🇸 | US, WA, Seattle | workday | PhD, New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-WA-Seattle/Research-Scientist--Robotics-Research----PhD-New-College-Grad-2026_JR2011473) | Jul 24, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/33243fb5-6907-40c7-930c-968b25d825d0) | Jul 24, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/5a28f3a5-8655-47f2-ab19-a79b8a319da8) | Jul 24, 2026 |
| Palantir | Forward Deployed Infrastructure Engineer, New Grad - US Government 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/91117724-9389-48dc-912f-98e48d4d45d8) | Jul 24, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | US, MA, Westford | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2022102) | Jul 24, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8648213002?gh_jid=8648213002) | Jul 23, 2026 |
| MongoDB | Technical Services Engineer 🇺🇸 | Palo Alto | greenhouse | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=8065812) | Jul 22, 2026 |
| Nvidia | ASIC Physical Design and Timing Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Timing-Engineer---New-College-Grad-2026_JR2013177) | Jul 22, 2026 |
| Nvidia | Developer Technology Engineer, Public Sector - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Developer-Technology-Engineer--Public-Sector---New-College-Grad-2026_JR2008990) | Jul 22, 2026 |
| OpenAI | Data Center Compute, OpenHouse Savannah 2026 🇺🇸 | US - Remote | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/6ba0ce24-ad32-4c3b-b49c-b373be9a8480) | Jul 22, 2026 |
| Google | Data Engineer, GCS Data Science 🇺🇸 | New York, NY, USA / Mountain View, CA, USA / San Francisco, CA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/139396293603533510) | Jul 22, 2026 |
| SpaceX | Full Stack Software Engineer, Manufacturing Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8645325002?gh_jid=8645325002) | Jul 22, 2026 |
| Discord | Software Engineer, Notifications 🇺🇸 | San Francisco Bay Area | greenhouse | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8642220002) | Jul 22, 2026 |
| Decagon | Research Engineer 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/decagon/9231a1ba-d9f5-4ddd-b398-158297ea7db9) | Jul 22, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Cape Canaveral, FL | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8643772002?gh_jid=8643772002) | Jul 21, 2026 |
| Nvidia | RTL Power Optimization Engineer – New College Grad 2026 🇺🇸 | US, CA, Santa Clara | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/RTL-Power-Optimization-Engineer---New-College-Grad-2026_JR2021841) | Jul 21, 2026 |
| Nvidia | GPU Architecture Engineer - New College Grad 2026 🇺🇸 | 3 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-Architecture-Engineer---New-College-Grad-2026_JR2021615) | Jul 21, 2026 |
| Qualcomm | Data Networking Software Engineer 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4442632896) | Jul 21, 2026 |
| Amazon Web Services (AWS) | Quantum Applied Scientist, AWS Center for Quantum Computing 🇺🇸 | Pasadena, CA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10480477/quantum-applied-scientist-aws-center-for-quantum-computing) | Jul 21, 2026 |
| Nvidia | Deep Learning Software Engineer, TensorRT Performance - New College Grad 2026 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Deep-Learning-Software-Engineer--TensorRT-Performance---New-College-Grad-2026_JR2015071) | Jul 20, 2026 |
| Brex | Systems Analyst II 🇺🇸 | Salt Lake City, Utah, United States | greenhouse | - | [Apply](https://www.brex.com/careers/8641845002?gh_jid=8641845002) | Jul 20, 2026 |
| CrowdStrike | Engineer I, Data Scientist - New Grad (Hybrid) 🇺🇸 | USA - Sunnyvale, CA | workday | New Grad | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Sunnyvale-CA/Engineer-I--Data-Scientist---New-Grad--Hybrid-_R29382-1) | Jul 20, 2026 |
| Brex | Systems Analyst II 🇺🇸 | San Francisco, California, United States | greenhouse | - | [Apply](https://www.brex.com/careers/8641661002?gh_jid=8641661002) | Jul 20, 2026 |
| Brex | Systems Analyst II 🇺🇸 | Seattle, Washington, United States | greenhouse | - | [Apply](https://www.brex.com/careers/8641728002?gh_jid=8641728002) | Jul 20, 2026 |
| Brex | Systems Analyst II 🇺🇸 | New York, New York, United States | greenhouse | - | [Apply](https://www.brex.com/careers/8641732002?gh_jid=8641732002) | Jul 20, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8639573002?gh_jid=8639573002) | Jul 17, 2026 |
| LangChain | Deployed Engineer (Early Career- SF) 🇺🇸 | San Francisco, CA | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/langchain/0f35c8e1-9318-411d-929b-04c60e6d8522) | Jul 16, 2026 |
| Qualcomm | Software Engineer - WLAN 🇺🇸 | Santa Clara, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4440753355) | Jul 16, 2026 |
| Microsoft | Design Verification Engineer 🇺🇸 | Raleigh, NC, US / Hillsboro, OR, US / Austin, TX, US / Mountain View, CA, US / Redmond, WA, US | microsoft | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556937343) | Jul 15, 2026 |
| Google | Security Engineer, Detection 🇺🇸 | Reston, VA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/108836916245209798) | Jul 15, 2026 |
| SpaceX | Power Plant Engineer 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8623199002?gh_jid=8623199002) | Jul 14, 2026 |
| Retool | Support Engineer 🇺🇸 | New York | gem | - | [Apply](https://jobs.gem.com/retool/am9icG9zdDpi-FHplm0tRPk6Y9QGHg95) | Jul 14, 2026 |
| SpaceX | Design Verification Engineer (Silicon Engineering) 🇺🇸 | Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8632967002?gh_jid=8632967002) | Jul 14, 2026 |
| Meta | Software Engineer, Systems ML - Compilers / Backend 🇺🇸 | Sunnyvale, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4437663436) | Jul 14, 2026 |
| SpaceX | Application Software Engineer, Employee Experience 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8632106002?gh_jid=8632106002) | Jul 13, 2026 |
| Anduril | 2026 Early Career Test & Evaluation Systems Integrator 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5185888007?gh_jid=5185888007) | Jul 13, 2026 |
| DRW | Software Developer 🇺🇸 | Chicago | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7980165) | Jul 13, 2026 |
| DRW | FPGA Developer 🇺🇸 | Chicago | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/8039110) | Jul 13, 2026 |
| Veeva Systems | Marketing Analytics - Data Analyst - July 2027 Start Date - ADP 🇺🇸 | New York - New York City | lever | - | [Apply](https://jobs.lever.co/veeva/28c47d34-3ad6-4485-85a9-686b4239b9ea) | Jul 13, 2026 |
| Aurora Innovation | Software Engineer I (Data Eng infra) 🇺🇸 | Mountain View, California | greenhouse | Early Career | [Apply](https://aurora.tech/jobs/8628066002?gh_jid=8628066002) | Jul 13, 2026 |
| Qualcomm | Machine Learning Researcher 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4429652864) | Jul 11, 2026 |
| Anduril | 2026 Early Career Firmware Engineer 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5167865007?gh_jid=5167865007) | Jul 09, 2026 |
| SpaceX | Data Engineer (Starlink) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8626500002?gh_jid=8626500002) | Jul 09, 2026 |
| SpaceX | Data Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8626535002?gh_jid=8626535002) | Jul 09, 2026 |
| SpaceX | Integration & Test Engineer (Fairings) 🇺🇸 | Vandenberg, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8609453002?gh_jid=8609453002) | Jul 08, 2026 |
| Qualcomm | Technician, Engineering 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4437066120) | Jul 08, 2026 |
| Broadcom | Mainframe QA Engineer 🇺🇸 | 2 Locations | workday | - | [Apply](https://broadcom.wd1.myworkdayjobs.com/en-US/External_Career/job/USA-TX-Plano-Legacy-Drive-Suite-700/Mainframe-QA-Engineer_R026439) | Jul 07, 2026 |
| Amazon Web Services (AWS) | Data Center Security Specialist, DC Security, AMER East 🇺🇸 | Frederick, MD, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/10467492/data-center-security-specialist-dc-security-amer-east) | Jul 07, 2026 |
| Tesla | Autonomous Vehicle Robot Engineering Technician, Hardware 🇺🇸 | Sparks, NV | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4437470579) | Jul 06, 2026 |
| Notion | Software Engineer, Early Career (AI) 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/85947779-6b87-466a-98bc-30a640448c28) | Jul 06, 2026 |
| Notion | Software Engineer, Early Career 🇺🇸 | San Francisco, California | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/notion/297b4ece-765f-4eea-b1b8-46057cb6501f) | Jul 06, 2026 |
| xAI | Software Engineer - Network (C++) 🇺🇸 | Palo Alto, California<br>Seattle, Washington | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5179367007) | Jul 02, 2026 |
| Qualcomm | ASIC Design Engineer 🇺🇸 | Santa Clara, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4435252831) | Jul 02, 2026 |
| CoreWeave | Data Center Apprentice Program 🇺🇸 | Ellendale, ND / Dalton, GA | greenhouse | - | [Apply](https://coreweave.com/careers/job?4694103006&board=coreweave&gh_jid=4694103006) | Jul 02, 2026 |
| DoorDash | Software Engineer, Spark Platform 🇺🇸 | San Francisco, CA<br>Seattle, WA<br>Sunnyvale, CA<br>New York, NY | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/8044370) | Jul 02, 2026 |
| Meta | Software Engineer, Machine Learning RecSys 🇺🇸 | Sunnyvale, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4432316470) | Jul 01, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/8027587?gh_jid=8027587) | Jun 30, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer (Systems), Embodied AI/NPCs, ML Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/8027588?gh_jid=8027588) | Jun 30, 2026 |
| Qualcomm | CPU Physical Design Timing Engineer (Austin, TX) 🇺🇸 | Austin, TX | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4434311654) | Jun 30, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/15844944-fb69-4b57-9531-e988650b20c6) | Jun 29, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Commercial 🇺🇸 | Chicago, IL | lever | New Grad | [Apply](https://jobs.lever.co/palantir/e500bcf3-19d8-4d3c-b340-4d76e4a55b40) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/0a838e66-1ab0-4fc4-b4d3-4671c0352278) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/18d901fc-93bb-4d18-9f04-c72031e20d79) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Infrastructure 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/4abf26b4-795c-420a-bf22-1ab98db268b4) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | Seattle, WA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/4d5a144e-87ea-45e2-a68c-3fad590629af) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Infrastructure 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/7d75bed5-45d8-4876-840a-2d92ea79c98d) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/94984771-0704-446c-88c6-91ce748f6d92) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad 🇺🇸 | Denver, CO | lever | New Grad | [Apply](https://jobs.lever.co/palantir/c34b424e-caf2-455a-b104-ae1096ccca29) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Production Infrastructure 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/e1a6c138-98bf-45e2-97f7-2c70371cc38a) | Jun 29, 2026 |
| Palantir | Software Engineer, New Grad - Defense 🇺🇸 | Palo Alto, CA | lever | New Grad | [Apply](https://jobs.lever.co/palantir/f362d7aa-360d-4059-ab38-f482742693b3) | Jun 29, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Commercial 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728) | Jun 29, 2026 |
| Airbnb | Data Scientist - Algorithms, Community Support 🇺🇸 | Remote - USA | greenhouse | - | [Apply](https://careers.airbnb.com/positions/8031901?gh_jid=8031901) | Jun 28, 2026 |
| Airbnb | Data Scientist - Inference, Community Support 🇺🇸 | Remote - USA | greenhouse | - | [Apply](https://careers.airbnb.com/positions/8031907?gh_jid=8031907) | Jun 28, 2026 |
| Palantir | Forward Deployed Software Engineer - Warp Speed 🇺🇸 | New York, NY | lever | - | [Apply](https://jobs.lever.co/palantir/13f99633-43b5-4459-8e84-25073f257c18) | Jun 27, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/cbe90327-3e6e-451c-a54c-1d3cbcef5aeb) | Jun 27, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - US Government 🇺🇸 | New York, NY | lever | New Grad | [Apply](https://jobs.lever.co/palantir/d1ac83d0-e923-42a5-8e6d-58dd0cab25ca) | Jun 27, 2026 |
| Palantir | Forward Deployed Software Engineer 🇺🇸 | New York, NY | lever | - | [Apply](https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0) | Jun 27, 2026 |
| Palantir | Forward Deployed Software Engineer, New Grad - Intel, US Government 🇺🇸 | Washington, D.C. | lever | New Grad | [Apply](https://jobs.lever.co/palantir/fbca0358-083a-4222-bdbb-3bd729b48382) | Jun 27, 2026 |
| Luma AI | Software Engineer - Product 🇺🇸 | SF Bay Area, CA | gem | - | [Apply](https://jobs.gem.com/lumalabs-ai/am9icG9zdDodtsh6pWUJjQgE8lXoaEJi) | Jun 27, 2026 |
| Tesla | Vehicle Cabin Engineering Technician 🇺🇸 | Fremont, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4433886752) | Jun 26, 2026 |
| SpaceX | Full Stack Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8610872002?gh_jid=8610872002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611118002?gh_jid=8611118002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611189002?gh_jid=8611189002) | Jun 26, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Memphis, TN | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8611191002?gh_jid=8611191002) | Jun 26, 2026 |
| Qualcomm | GPU Kernel Development Engineer (Multiple Levels Available) 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4344807525) | Jun 26, 2026 |
| Discord | Software Engineer, Developer Success 🇺🇸 | San Francisco Bay Area | greenhouse | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8609250002) | Jun 26, 2026 |
| Anduril | Mission Engineer, Air Dominance & Strike, Early Career 🇺🇸 | Costa Mesa, California, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5174562007?gh_jid=5174562007) | Jun 25, 2026 |
| Qualcomm | Front-End Design Engineer 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4431839577) | Jun 24, 2026 |
| Marvell | Digital Design Engineer 🇺🇸 | Irvine, CA | workday | - | [Apply](https://marvell.wd1.myworkdayjobs.com/en-US/MarvellCareers/job/Irvine-CA/Digital-Design-Engineer_2602855) | Jun 24, 2026 |
| xAI | Associate Data Center Operations Technician 🇺🇸 | Memphis, Tennessee<br>Southaven, Mississippi | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5168434007) | Jun 23, 2026 |
| SpaceX | Network Software Integration Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8599648002?gh_jid=8599648002) | Jun 23, 2026 |
| SpaceX | Embedded Software Engineer, Satellite Antenna (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8603628002?gh_jid=8603628002) | Jun 23, 2026 |
| Qualcomm | Embedded Systems Software Engineer 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4431419134) | Jun 23, 2026 |
| SpaceX | Integration Engineer, Heatshield (Starship) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8603368002?gh_jid=8603368002) | Jun 22, 2026 |
| Zillow | Applied Scientist, Shopping AI 🇺🇸 | United States | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4370817385) | Jun 19, 2026 |
| Qualcomm | Engineer Technician Intermediate 🇺🇸 | San Diego, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4429655865) | Jun 19, 2026 |
| SpaceX | Application Software Engineer, Manufacturing Systems 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8600012002?gh_jid=8600012002) | Jun 18, 2026 |
| Snowflake | AI Research Scientist, New Grad – Agents & Reinforcement Learning 🇺🇸 | US-WA-Bellevue | ashby | New Grad | [Apply](https://jobs.ashbyhq.com/snowflake/1bad12df-f443-426f-9d09-e96fc780d698) | Jun 16, 2026 |
| Reddit | Software Engineer - Data Movement Platform 🇺🇸 | Remote - United States | greenhouse | - | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7997866) | Jun 12, 2026 |
| Anduril | 2027 Early Career Software Engineer 🇺🇸 | Atlanta, Georgia, United States<br>Boston, Massachusetts, United States<br>Broomfield, Colorado, United States<br>Colorado Springs, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States<br>Irvine, California, United States<br>Reston, Virginia, United States<br>Seattle, Washington, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5162263007?gh_jid=5162263007) | Jun 11, 2026 |
| SpaceX | Embedded Software Engineer, Laser Mesh Routing (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8578934002?gh_jid=8578934002) | Jun 09, 2026 |
| SpaceX | Embedded Software Engineer, Laser Mesh Routing (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8578936002?gh_jid=8578936002) | Jun 09, 2026 |
| SpaceX | Factory Software Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8574053002?gh_jid=8574053002) | Jun 08, 2026 |
| Fireworks AI | Member of Technical Staff- Full Stack Software Engineer 🇺🇸 | San Mateo, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/fireworksai/jobs/4257324009) | Jun 05, 2026 |
| Nvidia | Software R&D Engineer, VLSI Physical Design - New College Grad 2026 🇺🇸 | 2 Locations | workday | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Software-R-D-Engineer--VLSI-Physical-Design---New-College-Grad-2026_JR2019330) | Jun 04, 2026 |
| Arista Networks | Advisory/ Resident Systems Engineer - (Mandarin required) 🇺🇸 | San Jose, CA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000130221863) | Jun 04, 2026 |
| Discord | Software Engineer, Distributed Systems 🇺🇸 | San Francisco Bay Area | greenhouse | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8545663002) | Jun 03, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | New York | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/New-York/Software-Development-Engineer_R168187-1) | Jun 02, 2026 |
| xAI | Software Engineer, Ads Product 🇺🇸 | Palo Alto, California | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5152408007) | Jun 01, 2026 |
| SpaceX | Product Development Engineer (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8545873002?gh_jid=8545873002) | Jun 01, 2026 |
| SpaceX | Financial Systems Analyst 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8571649002?gh_jid=8571649002) | Jun 01, 2026 |
| Tesla | Camera Systems Integration Technician, Reliability & Test 🇺🇸 | Fremont, CA | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4420210980) | May 29, 2026 |
| Tesla | Engineering Technician, Energy 🇺🇸 | Buffalo, NY | linkedin | - | [Apply](https://www.linkedin.com/jobs/view/4420224188) | May 29, 2026 |
| Google | ASIC Design Verification Engineer, Google Cloud 🇺🇸 | Sunnyvale, CA, USA | google_careers | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/77174102632080070) | May 29, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R168026) | May 28, 2026 |
| Adobe | Software Development Engineer - Front End 🇺🇸 | San Francisco | workday | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Software-Development-Engineer---Front-End_R168188) | May 28, 2026 |
| MongoDB | Software Engineer, Data Migration 🇺🇸 | California<br>Oregon<br>Washington | greenhouse | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7523834) | May 27, 2026 |
| Anduril | Robotics Software Engineer, Verification & Validation 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5083521007?gh_jid=5083521007) | May 22, 2026 |
| SpaceX | GNC Software Engineer - Top Secret Clearance 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8560746002?gh_jid=8560746002) | May 21, 2026 |
| SpaceX | OS/Platform Software Engineer (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552882002?gh_jid=8552882002) | May 20, 2026 |
| SpaceX | Flight Software Engineer (Starlink Mobile) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8556909002?gh_jid=8556909002) | May 20, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform  (Starlink) 🇺🇸 | Redmond, WA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552893002?gh_jid=8552893002) | May 20, 2026 |
| SpaceX | AI Software Engineer (Vehicle Engineering) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8559015002?gh_jid=8559015002) | May 20, 2026 |
| Arista Networks | Resident Engineer 🇺🇸 | Austin, TX, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000127345398) | May 20, 2026 |
| SpaceX | Full Stack Software Engineer (Build Reliability) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8555791002?gh_jid=8555791002) | May 19, 2026 |
| Ramp | Software Engineer, Credit 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/5598f7b8-4ae2-4105-a2b4-2d0f55c54c40) | May 13, 2026 |
| Anduril | Robotics Software Engineer, Behaviors 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5121816007?gh_jid=5121816007) | May 11, 2026 |
| SpaceX | Lead Starship Engineer (Ship Vehicle Assembly) 🇺🇸 | Starbase, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533755002?gh_jid=8533755002) | May 06, 2026 |
| OpenAI | Networking Operating System Firmware Engineer 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/f6b9903c-9034-436b-a4ec-4c8643a6d0dd) | May 06, 2026 |
| Apptronik | Robotics Test Engineer 🇺🇸 | Onsite - Austin, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/5988482004?gh_jid=5988482004) | May 05, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starshield) 🇺🇸 | Hawthorne, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530798002?gh_jid=8530798002) | May 05, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | San Francisco HQ | ashby | - | [Apply](https://jobs.ashbyhq.com/plaid/5c5d4414-347c-4caa-be88-384dec2d074b) | May 04, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | New York City Office | ashby | - | [Apply](https://jobs.ashbyhq.com/plaid/7e10c0b5-a09a-4e07-aaa8-899a7f82a0c9) | May 04, 2026 |
| DoorDash | AI Research Fellowship, (Summer and Fall 2026) 🇺🇸 | San Francisco, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7848317) | Apr 29, 2026 |
| Ramp | Software Engineer, Production Engineering 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/be496b52-cfbf-494e-b862-61fb4a188b24) | Apr 27, 2026 |
| Samsara | Associate Sales Engineer, SE Desk - Southeast 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7848351?gh_jid=7848351) | Apr 24, 2026 |
| Samsara | Associate Sales Engineer, SE Desk - TOLA 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7848363?gh_jid=7848363) | Apr 24, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5111318007?gh_jid=5111318007) | Apr 24, 2026 |
| Mercor | Software Engineer, Platform 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/mercor/cb67851b-0269-4cf5-996c-34c3a88a19c8) | Apr 23, 2026 |
| Figma | Data Scientist, Core Data -  PhD (2026) 🇺🇸 | San Francisco, CA • New York, NY | greenhouse | PhD | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) | Apr 22, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starlink) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8511391002?gh_jid=8511391002) | Apr 21, 2026 |
| OpenAI | Performance Modeling Engineer ~2 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/openai/4f6be73e-9a1d-4ec6-8b0e-b2af0b4becfb) | Apr 20, 2026 |
| Point72 | Fundamental Research Fellow, Canvas 🇺🇸 | New York, NY | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/8492784002?gh_jid=8492784002) | Apr 15, 2026 |
| SpaceX | Full Stack Software Engineer (Starlink) 🇺🇸 | Palo Alto, CA | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8501225002?gh_jid=8501225002) | Apr 13, 2026 |
| Figure AI | Reinforcement Learning Engineer – Whole Body Control 🇺🇸 | San Jose, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4671442006) | Apr 08, 2026 |
| Anduril | Robotics Software Engineer, Sensor Integration 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5096506007?gh_jid=5096506007) | Apr 07, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002) | Apr 06, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Bastrop, TX | greenhouse | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002) | Apr 06, 2026 |
| SpaceX | New Graduate Engineer, Software 🇺🇸 | Hawthorne, CA | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8493079002?gh_jid=8493079002) | Apr 03, 2026 |
| Xaira Therapeutics | AI in Residence 🇺🇸 | South San Francisco, California, United States | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5089321007) | Mar 25, 2026 |
| Xaira Therapeutics | AI Research Engineer 🇺🇸 | Seattle, Washington, United States | greenhouse | - | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007) | Mar 20, 2026 |
| Samsara | Associate Specialist Sales Engineer 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7717258?gh_jid=7717258) | Mar 16, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | greenhouse | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080387007?gh_jid=5080387007) | Mar 16, 2026 |
| Anduril | Robotics Software Engineer 🇺🇸 | Atlanta, Georgia, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5078772007?gh_jid=5078772007) | Mar 13, 2026 |
| DRW | Quantitative Researcher 🇺🇸 | New York | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7650182) | Feb 25, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer Apprentice - Military Veterans 🇺🇸 | Seattle, WA, USA | amazon_jobs | - | [Apply](https://www.amazon.jobs/en/jobs/3188438/software-development-engineer-apprentice-military-veterans) | Feb 24, 2026 |
| Samsara | Associate Sales Engineer, SE Desk (French Bilingual) 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7624120?gh_jid=7624120) | Feb 17, 2026 |
| ServiceNow | Associate Software Engineer, Core Infrastructure - Moveworks 🇺🇸 | Mountain View, CALIFORNIA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/ServiceNow/744000107369741) | Feb 04, 2026 |
| Anduril | Flight Software Engineer, Embedded C/C++, Air Dominance & Strike - Advanced Effects 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5035788007?gh_jid=5035788007) | Jan 27, 2026 |
| Ramp | Software Engineer, Core Product 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/5fe4c64e-9336-4384-9e6f-ff32eeb3fdae) | Jan 20, 2026 |
| Arista Networks | Software L1 Test Engineer 🇺🇸 | Santa Clara, CA, United States | smartrecruiters | - | [Apply](https://jobs.smartrecruiters.com/AristaNetworks/744000101072105) | Dec 30, 2025 |
| MongoDB | Software Engineer, Code Generation 🇺🇸 | California<br>Colorado<br>Montana<br>Nevada<br>New Mexico<br>Oregon<br>Utah<br>Washington | greenhouse | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7311666) | Dec 22, 2025 |
| Datadog | Technical Support Engineer 1, Premier - USA 🇺🇸 | Denver, Colorado, USA<br>New York, New York, USA<br>San Francisco, California, USA | greenhouse | Early Career | [Apply](https://careers.datadoghq.com/detail/7449072/?gh_jid=7449072) | Dec 10, 2025 |
| Scale AI | Machine Learning Research Engineer, Agents - Enterprise GenAI 🇺🇸 | San Francisco, CA<br>New York, NY | greenhouse | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4625344005) | Oct 31, 2025 |
| Roblox | [2026] Senior Machine Learning Engineer, Recommendation Systems - PhD Early Career 🇺🇸 | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7350081?gh_jid=7350081) | Oct 27, 2025 |
| CoreWeave | Software Engineer, Inference AI/ML 🇺🇸 | Sunnyvale, CA / Bellevue, WA | greenhouse | - | [Apply](https://coreweave.com/careers/job?4609928006&board=coreweave&gh_jid=4609928006) | Oct 24, 2025 |
| Samsara | Associate Sales Engineer, SE Desk - Northeast 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7311741?gh_jid=7311741) | Oct 17, 2025 |
| Samsara | Associate Sales Engineer, SE Desk - Mid West 🇺🇸 | Remote - US | greenhouse | - | [Apply](https://www.samsara.com/company/careers/roles/7311761?gh_jid=7311761) | Oct 17, 2025 |
| Robinhood | Software Engineer, Backend 🇺🇸 | Menlo Park, CA<br>New York, NY | greenhouse | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/7263592?t=gh_src=&gh_jid=7263592) | Sep 27, 2025 |
| Point72 | Machine Learning Engineer 🇺🇸 | New York | greenhouse | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002) | Sep 15, 2025 |
| Anduril | GNC Engineer, Space 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870847007?gh_jid=4870847007) | Sep 11, 2025 |
| Anduril | GNC Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870871007?gh_jid=4870871007) | Sep 11, 2025 |
| Mercor | Data Scientist 🇺🇸 | San Francisco | ashby | - | [Apply](https://jobs.ashbyhq.com/mercor/982a0751-e9eb-4b96-ac93-a1fd1d2f9152) | Aug 30, 2025 |
| Anduril | 2026 Early Career Software Engineer 🇺🇸 | Atlanta, Georgia, United States<br>Colorado Springs, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States<br>Seattle, Washington, United States | greenhouse | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | Aug 11, 2025 |
| Ramp | Mobile Engineer, Android 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040) | Jul 31, 2025 |
| Ramp | Mobile Engineer, iOS 🇺🇸 | New York, NY (HQ) | ashby | - | [Apply](https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f) | Jul 31, 2025 |
| DRW | Research Engineer 🇺🇸 | New York City | greenhouse | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/6973885) | Jun 16, 2025 |
| Point72 | Data Engineer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002) | Jan 23, 2025 |
| Point72 | Quantitative Software Developer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7825863002?gh_jid=7825863002) | Jan 22, 2025 |
| Point72 | 2027 Cubist Quant Academy – Developers 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7598678002?gh_jid=7598678002) | Sep 09, 2024 |
| Point72 | Quantitative Researcher - Machine Learning 🇺🇸 | New York | greenhouse | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/7297513002?gh_jid=7297513002) | Aug 15, 2024 |
| Point72 | Quantitative Analyst / Software Developer 🇺🇸 | New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7297622002?gh_jid=7297622002) | Aug 15, 2024 |
| Point72 | Quantitative Researcher - Systematic Credit 🇺🇸 | Chicago, New York | greenhouse | - | [Apply](https://boards.greenhouse.io/point72/jobs/7297625002?gh_jid=7297625002) | Aug 15, 2024 |
| DoorDash | Software Engineer, Android (All Teams) 🇺🇸 | Sunnyvale, CA<br>San Francisco, CA<br>Seattle, WA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/5630438) | Jun 10, 2024 |
| DoorDash | Software Engineer, Backend (All Teams) 🇺🇸 | Sunnyvale, CA<br>San Francisco, CA<br>New York, NY<br>Seattle, WA<br>Ann Arbor, MI | greenhouse | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/5630445) | May 22, 2024 |
| Anduril | Flight Software Engineer, Embedded C/C++, Air Dominance & Strike 🇺🇸 | Costa Mesa, California, United States | greenhouse | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4164476007?gh_jid=4164476007) | Dec 07, 2023 |
| Glean | Software Engineer, Frontend 🇺🇸 | Mountain View, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006733005) | Apr 08, 2022 |
| Glean | Software Engineer, Fullstack 🇺🇸 | Mountain View, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006734005) | Apr 08, 2022 |
| Glean | Machine Learning Engineer, Search Quality 🇺🇸 | Mountain View, CA | greenhouse | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006735005) | Apr 08, 2022 |


<details>
<summary><b>Closed positions (429)</b> &mdash; click to expand</summary>


| Company | Role | Location | Source | Education | Apply | Date Posted |
|---------|------|----------|--------|-----------|-------|-------------|
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | San Francisco, CA | linkedin | - | Closed | Aug 20, 2026 |
| ~~Qualcomm~~ | ~~Computer Vision System Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 19, 2026 |
| ~~Qualcomm~~ | ~~Engineer, Machine Learning (On-Device Software) 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 18, 2026 |
| ~~Qualcomm~~ | ~~Camera Low Power Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 18, 2026 |
| ~~GitHub~~ | ~~Full-Stack Developer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Aug 18, 2026 |
| ~~Google~~ | ~~Software Engineer, Service Networking Engineering Productivity 🇺🇸~~ | Cambridge, MA, USA | google_careers | - | Closed | Aug 17, 2026 |
| ~~SpaceX~~ | ~~Satellite On-Orbit Operations Software Engineer (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Aug 14, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician, Intermediate 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 14, 2026 |
| ~~Nvidia~~ | ~~Software Engineer, Deep Learning Libraries - New College Graduate 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Aug 14, 2026 |
| ~~Qualcomm~~ | ~~System Integration & Test Engineer - Top Secret Clearance Preferred (San Diego CA) 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 12, 2026 |
| ~~SpaceX~~ | ~~RFIC Engineer, AI Satellites (Starmind) 🇺🇸~~ | Bastrop, TX | greenhouse | - | Closed | Aug 11, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer, Core AI Software 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 11, 2026 |
| ~~Microsoft~~ | ~~Software Engineer I/II 🇺🇸~~ | Mountain View, CA, US | microsoft | Early Career | Closed | Aug 10, 2026 |
| ~~Qualcomm~~ | ~~CPU Formal Verification Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Aug 08, 2026 |
| ~~GitHub~~ | ~~Jr. Database Developer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Aug 08, 2026 |
| ~~GitHub~~ | ~~Jr. Database Developer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Aug 08, 2026 |
| ~~Meta~~ | ~~Data Engineer, Product Analytics 🇺🇸~~ | Burlingame, CA | linkedin | - | Closed | Aug 07, 2026 |
| ~~Meta~~ | ~~Software Engineer, Android 🇺🇸~~ | San Francisco, CA | linkedin | - | Closed | Aug 06, 2026 |
| ~~Tesla~~ | ~~Commissioning Turnover Engineer 🇺🇸~~ | Brookshire, TX | linkedin | - | Closed | Aug 06, 2026 |
| ~~Meta~~ | ~~Security Engineer, Investigator - GenAI 🇺🇸~~ | Washington, DC | linkedin | - | Closed | Aug 06, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer - Edge AI/Gen AI 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 06, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | San Francisco, CA | linkedin | - | Closed | Aug 05, 2026 |
| ~~Meta~~ | ~~Security Engineer, Investigator - GenAI 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Aug 05, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer, UEFI Firmware 🇺🇸~~ | 2 Locations | workday | - | Closed | Aug 05, 2026 |
| ~~Snowflake~~ | ~~Software Engineer - Openflow 🇺🇸~~ | US-CA-Menlo Park | ashby | - | Closed | Aug 05, 2026 |
| ~~Qualcomm~~ | ~~Machine Learning Compiler 🇺🇸~~ | New York, NY | linkedin | - | Closed | Aug 05, 2026 |
| ~~Meta~~ | ~~Network Implementation Engineer - Fiber Delivery 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Aug 05, 2026 |
| ~~Meta~~ | ~~Network Implementation Engineer 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Aug 05, 2026 |
| ~~Crusoe~~ | ~~Software Engineer I (DCIE) 🇺🇸~~ | San Francisco, CA - US | ashby | Early Career | Closed | Aug 04, 2026 |
| ~~Qualcomm~~ | ~~Embedded Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Aug 04, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Internal Systems 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 31, 2026 |
| ~~Arm Holdings~~ | ~~Coherent Interconnect Power Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 31, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~SDE - CPLD / FPGA 🇺🇸~~ | Seattle, WA, USA | amazon_jobs | - | Closed | Jul 30, 2026 |
| ~~GitHub~~ | ~~Associate, Software Development & Engineering 🇺🇸~~ | Chicago, IL | linkedin | - | Closed | Jul 30, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Architecture 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Jul 29, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 29, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Architecture 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 29, 2026 |
| ~~Qualcomm~~ | ~~CPU/DSP Performance Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 29, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Design Verification 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 28, 2026 |
| ~~Benchling~~ | ~~Software Engineer, Agents 🇺🇸~~ | San Francisco, CA | ashby | - | Closed | Jul 28, 2026 |
| ~~Benchling~~ | ~~Software Engineer, Registry and Inventory 🇺🇸~~ | San Francisco, CA | ashby | - | Closed | Jul 27, 2026 |
| ~~Meta~~ | ~~Software Engineer, iOS 🇺🇸~~ | San Francisco, CA | linkedin | - | Closed | Jul 26, 2026 |
| ~~Qualcomm~~ | ~~Modem Integration & Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 25, 2026 |
| ~~Stripe~~ | ~~Solutions Architect, Metronome (Startups) 🇺🇸~~ | SF, NYC, Chicago, US-Remote | greenhouse | - | Closed | Jul 24, 2026 |
| ~~Snowflake~~ | ~~Software Engineer- Postgres 🇺🇸~~ | US-WA-Bellevue | ashby | - | Closed | Jul 24, 2026 |
| ~~Qualcomm~~ | ~~AI Infrastructure Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 24, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 - Android 🇺🇸~~ | Mountain View, CA | linkedin | Early Career | Closed | Jul 24, 2026 |
| ~~Benchling~~ | ~~Software Engineer, Backend (Release Engineering) 🇺🇸~~ | San Francisco, CA | ashby | - | Closed | Jul 23, 2026 |
| ~~Qualcomm~~ | ~~CPU Server Physical Design Timing Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 23, 2026 |
| ~~Nvidia~~ | ~~AI and ML Infra Software Engineer, GPU Clusters - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jul 23, 2026 |
| ~~Pure Storage~~ | ~~PCIe Hardware Engineer, Systems 🇺🇸~~ | Santa Clara, California | greenhouse | - | Closed | Jul 23, 2026 |
| ~~Nvidia~~ | ~~Developer Technology Engineer, AI - New College Grad 2026 🇺🇸~~ | 6 Locations | workday | New Grad | Closed | Jul 23, 2026 |
| ~~Nvidia~~ | ~~Software Engineer, Physical Design Infrastructure - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 23, 2026 |
| ~~Intuit~~ | ~~Mid-Market Presales - Associate Digital Sales Engineer 🇺🇸~~ | Sacramento, CA | linkedin | - | Closed | Jul 23, 2026 |
| ~~Meta~~ | ~~Software Engineer, iOS 🇺🇸~~ | Bellevue, WA | linkedin | - | Closed | Jul 22, 2026 |
| ~~Nvidia~~ | ~~Deep Learning Software Engineer, Inference - New College Grad 2026 🇺🇸~~ | 5 Locations | workday | New Grad | Closed | Jul 22, 2026 |
| ~~Qualcomm~~ | ~~Power Management Systems Design and Verification Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 22, 2026 |
| ~~Decagon~~ | ~~Research Engineer 🇺🇸~~ | New York City | ashby | - | Closed | Jul 22, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Manufacturing 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 22, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Safety & Training 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 22, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 22, 2026 |
| ~~Google~~ | ~~Data Engineer, gUP Engineering 🇺🇸~~ | Boulder, CO, USA | google_careers | - | Closed | Jul 22, 2026 |
| ~~Meta~~ | ~~Software Engineer, iOS 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 21, 2026 |
| ~~Qualcomm~~ | ~~Systems SoC Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 21, 2026 |
| ~~GitHub~~ | ~~Associate, Advisor Platform Support 🇺🇸~~ | Westlake, TX | linkedin | - | Closed | Jul 21, 2026 |
| ~~SpaceX~~ | ~~Silicon Photonics Design Engineer (RFIC Engineering) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jul 21, 2026 |
| ~~SpaceX~~ | ~~RFIC Design Engineer (RFIC Engineering) 🇺🇸~~ | Irvine, CA | greenhouse | - | Closed | Jul 21, 2026 |
| ~~SpaceX~~ | ~~RFIC Design Engineer (RFIC Engineering) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jul 21, 2026 |
| ~~Qualcomm~~ | ~~Machine Learning R&D 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 21, 2026 |
| ~~Meta~~ | ~~Software Engineer, iOS 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Jul 20, 2026 |
| ~~Nvidia~~ | ~~Compiler Engineer, Infrastructure  - New College Grad 2026 🇺🇸~~ | 6 Locations | workday | New Grad | Closed | Jul 20, 2026 |
| ~~Tempus AI~~ | ~~Data Abstractor I 🇺🇸~~ | New York City | workday | - | Closed | Jul 20, 2026 |
| ~~Qualcomm~~ | ~~ASIC Design Verification Engineer (Santa Clara, CA) 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 18, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician, Intermediate 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 18, 2026 |
| ~~GitHub~~ | ~~Software Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 18, 2026 |
| ~~GitHub~~ | ~~Software Engineer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Jul 18, 2026 |
| ~~Meta~~ | ~~Software Engineer, iOS 🇺🇸~~ | Seattle, WA | linkedin | - | Closed | Jul 17, 2026 |
| ~~Meta~~ | ~~Software Engineer, Android 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Jul 17, 2026 |
| ~~Meta~~ | ~~Software Engineer, Android 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 17, 2026 |
| ~~Nvidia~~ | ~~ASIC Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 17, 2026 |
| ~~Nvidia~~ | ~~Systems Software Engineer, Accelerated Kubernetes Performance and Scale - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jul 17, 2026 |
| ~~Microsoft~~ | ~~Software Engineer- Manufacturing & Sourcing 🇺🇸~~ | Redmond, WA, US | microsoft | - | Closed | Jul 17, 2026 |
| ~~Intuit~~ | ~~Software Engineer I - Credit Karma 🇺🇸~~ | Charlotte, NC | linkedin | Early Career | Closed | Jul 17, 2026 |
| ~~Qualcomm~~ | ~~Modem HW Design Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 17, 2026 |
| ~~Roblox~~ | ~~Software Engineer, Ads Platform 🇺🇸~~ | San Mateo, CA, United States | greenhouse | - | Closed | Jul 16, 2026 |
| ~~Qualcomm~~ | ~~Associate Attorney, Data 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 16, 2026 |
| ~~Nvidia~~ | ~~Software Engineer - Drive OS 🇺🇸~~ | 2 Locations | workday | - | Closed | Jul 15, 2026 |
| ~~Airbnb~~ | ~~Data Scientist, Trust (ML/Algorithms) 🇺🇸~~ | Remote - USA | greenhouse | - | Closed | Jul 15, 2026 |
| ~~Qualcomm~~ | ~~Embedded Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 15, 2026 |
| ~~Intuit~~ | ~~Software Engineer I - Credit Karma 🇺🇸~~ | Charlotte, NC | linkedin | Early Career | Closed | Jul 15, 2026 |
| ~~Tesla~~ | ~~Autonomous Vehicle Robot Engineering Technician, Hardware 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 14, 2026 |
| ~~Broadcom~~ | ~~Software Engineer VMkernel 🇺🇸~~ | USA-CA - Promontory B | workday | - | Closed | Jul 14, 2026 |
| ~~GitHub~~ | ~~Security Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 14, 2026 |
| ~~GitHub~~ | ~~Security Engineer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Jul 14, 2026 |
| ~~GitHub~~ | ~~Security Engineer 🇺🇸~~ | Omaha, NE | linkedin | - | Closed | Jul 14, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer, Dynamo-Triton Inference Server - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jul 13, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Employee Experience 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 13, 2026 |
| ~~Nvidia~~ | ~~Backend Compiler Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 13, 2026 |
| ~~Nvidia~~ | ~~Compiler Engineer, AI Inference- New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 13, 2026 |
| ~~Nvidia~~ | ~~Security Architect - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 13, 2026 |
| ~~Anduril~~ | ~~Engineering Technical Fellow, Solid Rocket Motors 🇺🇸~~ | Costa Mesa, California, United States | greenhouse | - | Closed | Jul 13, 2026 |
| ~~Pure Storage~~ | ~~AI Transformation Coordinator 🇺🇸~~ | Santa Clara, California | greenhouse | - | Closed | Jul 13, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Jul 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Seattle, WA | linkedin | - | Closed | Jul 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Jul 11, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Bellevue, WA | linkedin | - | Closed | Jul 11, 2026 |
| ~~Intuit~~ | ~~Mid-Market Presales - Associate Digital Sales Engineer 🇺🇸~~ | Sacramento, CA | linkedin | - | Closed | Jul 11, 2026 |
| ~~Google~~ | ~~Hardware Validation Engineer, Cloud Platforms 🇺🇸~~ | Sunnyvale, CA, USA | google_careers | - | Closed | Jul 10, 2026 |
| ~~Nvidia~~ | ~~Formal Verification Engineer - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jul 10, 2026 |
| ~~Nvidia~~ | ~~Systems Software Engineer, Autonomous Systems Mapping - New College Graduate 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 10, 2026 |
| ~~SpaceX~~ | ~~RF Software Engineer (Starlink) 🇺🇸~~ | Bastrop, TX | greenhouse | - | Closed | Jul 09, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Bastrop, TX | greenhouse | - | Closed | Jul 09, 2026 |
| ~~Generate Biomedicines~~ | ~~Data Scientist I 🇺🇸~~ | Somerville, MA | greenhouse | - | Closed | Jul 09, 2026 |
| ~~Nvidia~~ | ~~ASIC Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 09, 2026 |
| ~~Nvidia~~ | ~~Formal Verification Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Components Test (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Components (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 09, 2026 |
| ~~Qualcomm~~ | ~~LLVM/Ripple Compiler Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, CDN  (Starlink) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Jul 08, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Data (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jul 08, 2026 |
| ~~Palo Alto Networks~~ | ~~Early In Career - Software Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 08, 2026 |
| ~~Qualcomm~~ | ~~CPU Server Floorplan and Integration Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 08, 2026 |
| ~~Qualcomm~~ | ~~CPU Verification Engineer 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 08, 2026 |
| ~~Qualcomm~~ | ~~Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 08, 2026 |
| ~~Meta~~ | ~~Linguistic Engineer 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 08, 2026 |
| ~~Meta~~ | ~~Product Design Engineer 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 08, 2026 |
| ~~Nvidia~~ | ~~ASIC Verification Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jul 07, 2026 |
| ~~Meta~~ | ~~Software Engineer, Systems ML - Compilers / Backend 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Jul 07, 2026 |
| ~~Qualcomm~~ | ~~GPU Validation and Emulation Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 07, 2026 |
| ~~Qualcomm~~ | ~~Modem Machine Learning Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 07, 2026 |
| ~~Qualcomm~~ | ~~Video Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 07, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Data Center Security Specialist, DC Security, AMER East 🇺🇸~~ | Leesburg, VA, USA | amazon_jobs | - | Closed | Jul 07, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Design Verification 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Jul 07, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Design Verification 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 07, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starshield) - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 06, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Product Development (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 06, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, High Performance Computing 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jul 06, 2026 |
| ~~Nvidia~~ | ~~Software Engineer - AI Research Clusters 🇺🇸~~ | 6 Locations | workday | - | Closed | Jul 06, 2026 |
| ~~Tesla~~ | ~~Inbound Material Flow Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jul 02, 2026 |
| ~~Zscaler~~ | ~~Software Development Engineer 🇺🇸~~ | San Jose, California, USA | greenhouse | - | Closed | Jul 02, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer, GPU Development Tools 🇺🇸~~ | 2 Locations | workday | - | Closed | Jul 02, 2026 |
| ~~Qualcomm~~ | ~~SOC Design Verification Engineer – Data Center Solutions 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jul 02, 2026 |
| ~~Benchling~~ | ~~Software Engineer, Customer Engineering 🇺🇸~~ | Boston, MA | ashby | - | Closed | Jul 02, 2026 |
| ~~xAI~~ | ~~Software Engineer: Network (C++) 🇺🇸~~ | Palo Alto, CA<br>Seattle, WA | greenhouse | - | Closed | Jul 01, 2026 |
| ~~Qualcomm~~ | ~~ASIC Design Verification Engineer (Santa Clara, CA) 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jul 01, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Menlo Park, CA | linkedin | - | Closed | Jul 01, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | Bellevue, WA | linkedin | - | Closed | Jul 01, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~MLA Design Verification Engineer I, Annapurna Labs 🇺🇸~~ | Austin, TX, USA | amazon_jobs | Early Career | Closed | Jul 01, 2026 |
| ~~GitHub~~ | ~~Associate Software Developer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Jul 01, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning RecSys 🇺🇸~~ | New York, NY | linkedin | - | Closed | Jul 01, 2026 |
| ~~Meta~~ | ~~Linguistic Engineer 🇺🇸~~ | Burlingame, CA | linkedin | - | Closed | Jul 01, 2026 |
| ~~Meta~~ | ~~Linguistic Engineer 🇺🇸~~ | Redmond, WA | linkedin | - | Closed | Jul 01, 2026 |
| ~~Qualcomm~~ | ~~Modem Machine Learning Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 30, 2026 |
| ~~Meta~~ | ~~ASIC Engineer, Physical Design 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 30, 2026 |
| ~~Microsoft~~ | ~~Cambridge Residency Programme: AI Researcher in Interactive Generative AI systems 🇺🇸~~ | Cambridge, England, GB | microsoft | - | Closed | Jun 30, 2026 |
| ~~Meta~~ | ~~Data Engineer, Product Analytics 🇺🇸~~ | Burlingame, CA | linkedin | - | Closed | Jun 30, 2026 |
| ~~Meta~~ | ~~Data Engineer, Product Analytics 🇺🇸~~ | Los Angeles, CA | linkedin | - | Closed | Jun 30, 2026 |
| ~~Nvidia~~ | ~~Compiler Engineer - Smart Network Devices- New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 29, 2026 |
| ~~Nvidia~~ | ~~ASIC Floorplan Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 29, 2026 |
| ~~Qualcomm~~ | ~~Microprocessor Silicon Validation and Optimization Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 27, 2026 |
| ~~Veeva Systems~~ | ~~Associate Software Engineer in Test 🇺🇸~~ | California - Pleasanton | lever | - | Closed | Jun 27, 2026 |
| ~~Veeva Systems~~ | ~~Associate Software Engineer in Test 🇺🇸~~ | Massachusetts - Boston | lever | - | Closed | Jun 27, 2026 |
| ~~Qualcomm~~ | ~~Speech and Audio Systems Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 27, 2026 |
| ~~Qualcomm~~ | ~~Compiler Software Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 27, 2026 |
| ~~Qualcomm~~ | ~~Machine Learning Researcher 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 27, 2026 |
| ~~GitHub~~ | ~~Junior Full Stack .NET Developer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | Jun 27, 2026 |
| ~~AMD~~ | ~~L3 Application Support Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 27, 2026 |
| ~~Qualcomm~~ | ~~Camera DV Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 26, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 26, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Vehicle Operations (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 26, 2026 |
| ~~ServiceNow~~ | ~~Associate Software Engineer, Core Infrastructure - Moveworks 🇺🇸~~ | Mountain View, CALIFORNIA, United States | smartrecruiters | - | Closed | Jun 26, 2026 |
| ~~Nvidia~~ | ~~ASIC Physical Design and Timing Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 26, 2026 |
| ~~Meta~~ | ~~Product Design Engineer 🇺🇸~~ | Sunnyvale, CA | linkedin | - | Closed | Jun 26, 2026 |
| ~~Meta~~ | ~~Product Design Engineer 🇺🇸~~ | Redmond, WA | linkedin | - | Closed | Jun 26, 2026 |
| ~~CrowdStrike~~ | ~~Engineer I - New Grad, Agentic AI (Hybrid) 🇺🇸~~ | USA - Sunnyvale, CA | workday | New Grad | Closed | Jun 26, 2026 |
| ~~Qualcomm~~ | ~~ASIC Design Verification Engineer (Santa Clara, CA) 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 25, 2026 |
| ~~Qualcomm~~ | ~~ASIC Design Verification Engineer (Santa Clara, CA) 🇺🇸~~ | Santa Clara, CA | linkedin | - | Closed | Jun 25, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician, Intermediate 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 25, 2026 |
| ~~Nvidia~~ | ~~DFT Engineer - New College Grad 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 25, 2026 |
| ~~Google~~ | ~~IP DFT Engineer 🇺🇸~~ | Sunnyvale, CA, USA | google_careers | - | Closed | Jun 25, 2026 |
| ~~Qualcomm~~ | ~~SoC Modeling Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 24, 2026 |
| ~~Nvidia~~ | ~~System Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 24, 2026 |
| ~~Broadcom~~ | ~~Software Engineer 🇺🇸~~ | USA-CA San Jose Innovation Drive | workday | - | Closed | Jun 24, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, FSx for Lustre 🇺🇸~~ | Boston, MA, USA | amazon_jobs | - | Closed | Jun 24, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer (C#/ Python), Data 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | Jun 23, 2026 |
| ~~Snap~~ | ~~Embedded Software Engineer, Level 3 🇺🇸~~ | San Diego, California | workday | - | Closed | Jun 23, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer (University Grad) 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 23, 2026 |
| ~~Google~~ | ~~Design Verification Engineer, TPU Cloud Compute 🇺🇸~~ | Sunnyvale, CA, USA | google_careers | - | Closed | Jun 23, 2026 |
| ~~Qualcomm~~ | ~~Engineering Technician 🇺🇸~~ | Boxborough, MA | linkedin | - | Closed | Jun 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ (Simulations) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 22, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Manufacturing 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 22, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer - CUDA Chips 🇺🇸~~ | US, CA, Santa Clara | workday | - | Closed | Jun 22, 2026 |
| ~~Nvidia~~ | ~~CPU Design Engineer - New College Grad 2026 🇺🇸~~ | 6 Locations | workday | New Grad | Closed | Jun 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ (Dragon) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 21, 2026 |
| ~~Uber~~ | ~~Software Engineer I 🇺🇸~~ | Sunnyvale, Santa Clara, United States | uber | Early Career | Closed | Jun 20, 2026 |
| ~~Uber~~ | ~~Software Engineer I 🇺🇸~~ | Seattle, King, United States | uber | Early Career | Closed | Jun 20, 2026 |
| ~~Uber~~ | ~~Software Engineer I 🇺🇸~~ | Seattle, King, United States | uber | Early Career | Closed | Jun 20, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer, AI Tools – Delegate 🇺🇸~~ | Raleigh, NC | linkedin | - | Closed | Jun 20, 2026 |
| ~~Qualcomm~~ | ~~Microprocessor Silicon Validation and Optimization Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 19, 2026 |
| ~~Qualcomm~~ | ~~CI Infrastructure Engineer 🇺🇸~~ | Raleigh, NC | linkedin | - | Closed | Jun 18, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, High Assurance Test (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 18, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, PCBA (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 18, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer (Application Software) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 18, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Inference 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Jun 18, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Manufacturing Systems 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 18, 2026 |
| ~~Marvell~~ | ~~Digital IC Design Engineer - Early Career 🇺🇸~~ | Westborough, MA | workday | New Grad | Closed | Jun 18, 2026 |
| ~~Anduril~~ | ~~Jr People Data Analyst 🇺🇸~~ | Boston, Massachusetts, United States | greenhouse | - | Closed | Jun 17, 2026 |
| ~~Qualcomm~~ | ~~DSP Applications Software Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 17, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ (Raptor) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 17, 2026 |
| ~~Qualcomm~~ | ~~Embedded Software Development Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 17, 2026 |
| ~~Qualcomm~~ | ~~DSP Applications Software Engineer 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 17, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | Atlanta, GA | linkedin | Early Career | Closed | Jun 17, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | New York, NY | linkedin | Early Career | Closed | Jun 17, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | San Diego, CA | linkedin | Early Career | Closed | Jun 17, 2026 |
| ~~Intuit~~ | ~~Software Engineer 1 🇺🇸~~ | Mountain View, CA | linkedin | Early Career | Closed | Jun 17, 2026 |
| ~~Tesla~~ | ~~Engineering Technician, Electrode 🇺🇸~~ | Fremont, CA | linkedin | - | Closed | Jun 16, 2026 |
| ~~Qualcomm~~ | ~~EVA Systems Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 15, 2026 |
| ~~Qualcomm~~ | ~~Camera Firmware Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 15, 2026 |
| ~~Stripe~~ | ~~Software Engineer 🇺🇸~~ | New York, NY | greenhouse | - | Closed | Jun 15, 2026 |
| ~~Stripe~~ | ~~Full-Stack Engineer 🇺🇸~~ | San Francisco | greenhouse | - | Closed | Jun 15, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Flight Software C++ (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 15, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Safety & Training 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 15, 2026 |
| ~~Roblox~~ | ~~Senior Talent Business Partner, Early Career - AI/ML PhD (Short-Term) 🇺🇸~~ | Remote<br>San Mateo, CA, United States | greenhouse | PhD, New Grad | Closed | Jun 15, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer - Camera (Multiple Levels Available) 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 15, 2026 |
| ~~Nvidia~~ | ~~Software Quality Assurance Engineer - 2026 New College Grad 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 15, 2026 |
| ~~Nvidia~~ | ~~High-Performance LLM Training Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 15, 2026 |
| ~~Tesla~~ | ~~Application Support Engineer, Factory Software 🇺🇸~~ | Fremont, CA | linkedin | - | Closed | Jun 14, 2026 |
| ~~Tesla~~ | ~~Engineering Technician, Power Supplies & Electronics 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 14, 2026 |
| ~~Qualcomm~~ | ~~Software Engineer – Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 14, 2026 |
| ~~Qualcomm~~ | ~~GPU Design Implementation Engineer(Synthesis) 🇺🇸~~ | Austin, TX | linkedin | - | Closed | Jun 13, 2026 |
| ~~Qualcomm~~ | ~~System Integration & Test Engineer - Top Secret Clearance Preferred (San Diego CA) 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 13, 2026 |
| ~~Zillow~~ | ~~Machine Learning Engineer, Zillow Shopping AI 🇺🇸~~ | United States | linkedin | - | Closed | Jun 13, 2026 |
| ~~Zillow~~ | ~~Machine Learning Engineer, Agentic AI 🇺🇸~~ | United States | linkedin | - | Closed | Jun 13, 2026 |
| ~~Qualcomm~~ | ~~RFIC Design Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 13, 2026 |
| ~~Tempus AI~~ | ~~Clinical Data Abstractor I 🇺🇸~~ | 2 Locations | workday | - | Closed | Jun 11, 2026 |
| ~~Nvidia~~ | ~~Circuit Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 11, 2026 |
| ~~Nvidia~~ | ~~Research Scientist, Efficient Deep Learning - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 11, 2026 |
| ~~Roblox~~ | ~~Distinguished Engineer, Luau Application 🇺🇸~~ | San Mateo, CA, United States | greenhouse | - | Closed | Jun 10, 2026 |
| ~~Qualcomm~~ | ~~System Performance Modeling Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 10, 2026 |
| ~~DoorDash~~ | ~~Associate, Commerce Platform Logistics 🇺🇸~~ | San Francisco, CA<br>New York, NY<br>United States - Remote | greenhouse | Bachelors | Closed | Jun 10, 2026 |
| ~~Qualcomm~~ | ~~System Level Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 09, 2026 |
| ~~Qualcomm~~ | ~~System Level Test Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 09, 2026 |
| ~~Qualcomm~~ | ~~Embedded Software Engineer – Device Driver Development 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 09, 2026 |
| ~~Tempus AI~~ | ~~Associate IAM Engineer 🇺🇸~~ | Chicago | workday | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Test Infrastructure (Application Software) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Beam Planning (Starlink) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, High Performance Computing (Starlink) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Low Latency Computing (Starlink) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Low Latency Computing (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, High Performance Computing (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Beam Planning (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 09, 2026 |
| ~~Roblox~~ | ~~Software Engineer, Storage 🇺🇸~~ | San Mateo, CA, United States | greenhouse | - | Closed | Jun 09, 2026 |
| ~~Nvidia~~ | ~~ASIC Verification Engineer - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jun 09, 2026 |
| ~~Nvidia~~ | ~~GPU Architect - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 09, 2026 |
| ~~Notion~~ | ~~Software Engineer, Security 🇺🇸~~ | San Francisco, California | ashby | - | Closed | Jun 09, 2026 |
| ~~Google~~ | ~~Chip CAD DevOps Engineer, Google Cloud 🇺🇸~~ | Sunnyvale, CA, USA | google_careers | - | Closed | Jun 09, 2026 |
| ~~Google~~ | ~~Hardware Validation Engineer, Cloud Platforms 🇺🇸~~ | Sunnyvale, CA, USA | google_careers | - | Closed | Jun 09, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, ASIC Design (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | New Grad | Closed | Jun 08, 2026 |
| ~~Qualcomm~~ | ~~Memory Control Design Engineer 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 08, 2026 |
| ~~Nvidia~~ | ~~Formal Verification Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 08, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer - Tegra 🇺🇸~~ | US, CA, Santa Clara | workday | - | Closed | Jun 08, 2026 |
| ~~Qualcomm~~ | ~~Customer Engineer - AI / ML 🇺🇸~~ | San Diego, CA | linkedin | - | Closed | Jun 07, 2026 |
| ~~AMD~~ | ~~L3 Application Support Engineer 🇺🇸~~ | North Carolina, United States | linkedin | - | Closed | Jun 06, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Propulsion Simulation & Data Analysis 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 05, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 05, 2026 |
| ~~Marvell~~ | ~~Validation Engineer - Early Career 🇺🇸~~ | Santa Clara, CA | workday | New Grad | Closed | Jun 05, 2026 |
| ~~Adobe~~ | ~~Machine Learning Engineer 🇺🇸~~ | San Jose | workday | - | Closed | Jun 05, 2026 |
| ~~Benchling~~ | ~~Detection and Response Engineer, New Grad (2026) 🇺🇸~~ | San Francisco, CA | ashby | New Grad | Closed | Jun 04, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, DevOps (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 03, 2026 |
| ~~Nvidia~~ | ~~AI Inference Performance Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 03, 2026 |
| ~~Nvidia~~ | ~~ASIC Clocks Design Engineer - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jun 03, 2026 |
| ~~Nvidia~~ | ~~Research Scientist, Electronic Design Automation - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 03, 2026 |
| ~~Nvidia~~ | ~~Software Engineer, Hardware Tools and Methodology - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 03, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Components (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 02, 2026 |
| ~~Nvidia~~ | ~~Low Power ASIC Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 02, 2026 |
| ~~Nvidia~~ | ~~Software R&D Engineer, Digital Logic Synthesis - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | Jun 02, 2026 |
| ~~Nvidia~~ | ~~Cell Modeling and Verification Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | Jun 02, 2026 |
| ~~Arista Networks~~ | ~~Systems Engineer - Campus (Wired and Wireless) 🇺🇸~~ | Santa Clara, CA, United States | smartrecruiters | New Grad | Closed | Jun 02, 2026 |
| ~~Uber~~ | ~~Software Engineer I 🇺🇸~~ | Sunnyvale, Santa Clara, United States | uber | Early Career | Closed | Jun 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starship) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | Jun 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starship) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Hardware Test & Automation (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~SpaceX~~ | ~~Data Engineer (Starlink Network Analytics, Wi-Fi) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~Robinhood~~ | ~~Software Engineer 🇺🇸~~ | Menlo Park, CA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~Robinhood~~ | ~~Software Engineer 🇺🇸~~ | Menlo Park, CA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~Robinhood~~ | ~~Software Engineer 🇺🇸~~ | Menlo Park, CA | greenhouse | - | Closed | Jun 01, 2026 |
| ~~Marvell~~ | ~~Systems Application Engineer - Early Career 🇺🇸~~ | Santa Clara, CA | workday | New Grad | Closed | Jun 01, 2026 |
| ~~Tesla~~ | ~~Software Engineer, Industrial Energy Products 🇺🇸~~ | Palo Alto, CA | linkedin | - | Closed | May 31, 2026 |
| ~~SpaceX~~ | ~~Software Engineer 🇺🇸~~ | McGregor, TX | greenhouse | - | Closed | May 29, 2026 |
| ~~Nvidia~~ | ~~Software Engineer, TensorRT Specialized Platforms - New College Grad 2025 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | May 29, 2026 |
| ~~Tesla~~ | ~~Frontend Software Engineer, Energy Charging 🇺🇸~~ | Fremont, CA | linkedin | - | Closed | May 28, 2026 |
| ~~Tesla~~ | ~~Frontend Software Engineer, Energy Residential 🇺🇸~~ | Fremont, CA | linkedin | - | Closed | May 28, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starlink Mobile) 🇺🇸~~ | Sunnyvale, CA | greenhouse | - | Closed | May 28, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starlink Mobile) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 28, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Special Projects) - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 28, 2026 |
| ~~Nvidia~~ | ~~ASIC Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | workday | New Grad | Closed | May 28, 2026 |
| ~~Nvidia~~ | ~~Circuit Design Engineer - New College Grad 2026 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Hardware Validation (Test Solutions) Engineer 🇺🇸~~ | Burlington, VT | workday | - | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Design for Test Engineer - Early Career 🇺🇸~~ | Westborough, MA | workday | New Grad | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Design Verification Engineer - Early Career 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Design Verification Engineer - Early Career 🇺🇸~~ | Santa Clara, CA | workday | New Grad | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Advanced Package Technology, Distinguished Engineer 🇺🇸~~ | 3 Locations | workday | PhD | Closed | May 28, 2026 |
| ~~Marvell~~ | ~~Advanced Packaging SI/PI Staff Engineer - Early Career 🇺🇸~~ | 2 Locations | workday | New Grad | Closed | May 28, 2026 |
| ~~Adobe~~ | ~~2026 University Graduate - Machine Learning Engineer 🇺🇸~~ | Seattle | workday | New Grad | Closed | May 28, 2026 |
| ~~Adobe~~ | ~~Software Development Engineer 🇺🇸~~ | San Jose | workday | - | Closed | May 28, 2026 |
| ~~Adobe~~ | ~~Junior Software Development Engineer 🇺🇸~~ | San Jose | workday | - | Closed | May 28, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Hardware Test & Automation (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 27, 2026 |
| ~~GitHub~~ | ~~Specialist, Software Developer 🇺🇸~~ | Southlake, TX | linkedin | - | Closed | May 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Thermal & Fluid Analysis) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | May 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Flight Software (Starship) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | May 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Flight Software (Starship) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 22, 2026 |
| ~~Robinhood~~ | ~~Support Engineer 🇺🇸~~ | Westlake, TX | greenhouse | - | Closed | May 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Bastrop, TX | greenhouse | - | Closed | May 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Flight Software (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Embedded Software (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | May 21, 2026 |
| ~~SpaceX~~ | ~~Design Verification Engineer (Silicon Engineering) 🇺🇸~~ | Austin, TX | greenhouse | - | Closed | May 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 20, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | May 20, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Sunnyvale, CA | greenhouse | - | Closed | May 20, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Engineering Simulation & Automation (Vehicle Engineering) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 20, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Components) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 19, 2026 |
| ~~Plaid~~ | ~~Software Engineer - Product Security 🇺🇸~~ | New York City Office | ashby | - | Closed | May 18, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Data 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | May 15, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 14, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 13, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 13, 2026 |
| ~~Flatiron Health~~ | ~~Data Analyst - Evidence Solutions 🇺🇸~~ | Durham office | greenhouse | - | Closed | May 12, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer 🇺🇸~~ | Costa Mesa, California, United States | greenhouse | - | Closed | May 12, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Hardware Test & Automation (Optical Payloads) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | May 12, 2026 |
| ~~Snowflake~~ | ~~Software Engineer - Snowflake Postgres 🇺🇸~~ | US-WA-Bellevue | ashby | - | Closed | May 12, 2026 |
| ~~MongoDB~~ | ~~Software Engineer, Developer Productivity 🇺🇸~~ | New York City | greenhouse | - | Closed | May 08, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer, Data (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 07, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Telemetry - Top Secret Clearance (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Continuous Integration (Starship) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | May 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Continuous Integration (Starship) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | May 01, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Development Test (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Apr 30, 2026 |
| ~~Google~~ | ~~Security Engineer, Access Security Team 🇺🇸~~ | New York, NY, USA | google_careers | - | Closed | Apr 30, 2026 |
| ~~xAI~~ | ~~Software Engineer - Data Platform 🇺🇸~~ | Palo Alto, California, United States | greenhouse | - | Closed | Apr 29, 2026 |
| ~~Benchling~~ | ~~Software Engineer, Developer Enablement 🇺🇸~~ | San Francisco, CA | ashby | - | Closed | Apr 29, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Apr 28, 2026 |
| ~~Notion~~ | ~~Software Engineer, New Grad (AI) 🇺🇸~~ | San Francisco, California | ashby | New Grad | Closed | Apr 27, 2026 |
| ~~xAI~~ | ~~Software Engineer - Data 🇺🇸~~ | Palo Alto, California, United States | greenhouse | - | Closed | Apr 24, 2026 |
| ~~Notion~~ | ~~Software Engineer, New Grad 🇺🇸~~ | San Francisco, California | ashby | New Grad | Closed | Apr 23, 2026 |
| ~~SpaceX~~ | ~~RF Software Engineer (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Apr 22, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Flight Reliability) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Apr 21, 2026 |
| ~~Google~~ | ~~Security Engineer, Access Risk Intelligence and Security Mitigation 🇺🇸~~ | New York, NY, USA | google_careers | - | Closed | Apr 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starshield) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Apr 10, 2026 |
| ~~Skydio~~ | ~~Product Support Engineer 🇺🇸~~ | San Mateo, California, United States | ashby | - | Closed | Apr 08, 2026 |
| ~~Together AI~~ | ~~Analytics Engineer — Data Warehouse 🇺🇸~~ | San Francisco | greenhouse | - | Closed | Apr 07, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Platform Team) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Apr 06, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer (Application Software) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Apr 06, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Apr 06, 2026 |
| ~~Snowflake~~ | ~~Industry Architect – Advertising & Media 🇺🇸~~ | US-CA-Remote | ashby | - | Closed | Apr 03, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Simulations (Application Software) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 31, 2026 |
| ~~SpaceX~~ | ~~Simulation Software Engineer (Application Software) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 31, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starshield) 🇺🇸~~ | Washington, DC | greenhouse | - | Closed | Mar 27, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starshield) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Mar 27, 2026 |
| ~~SpaceX~~ | ~~AI Security Software Engineer (Starshield) 🇺🇸~~ | Palo Alto, CA | greenhouse | - | Closed | Mar 27, 2026 |
| ~~Roblox~~ | ~~[2026] Senior Machine Learning Engineer, Account Identity - PhD Early Career 🇺🇸~~ | San Mateo, CA, United States | greenhouse | PhD Student, New Grad | Closed | Mar 26, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Starlink Network 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Software Infrastructure Engineer, Flight Software (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starlink) 🇺🇸~~ | Bastrop, TX | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Platform Engineer, Flight Software (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Flight Software Infrastructure Engineer (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 25, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Data (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 24, 2026 |
| ~~Anthropic~~ | ~~Data Scientist, Marketing 🇺🇸~~ | New York City, NY \| Seattle, WA<br>San Francisco, CA | greenhouse | Bachelors | Closed | Mar 23, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Seattle, Washington, United States | greenhouse | - | Closed | Mar 23, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Boston, Massachusetts, United States | greenhouse | - | Closed | Mar 23, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Washington, District of Columbia, United States | greenhouse | - | Closed | Mar 23, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Atlanta, Georgia, United States | greenhouse | - | Closed | Mar 23, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Ashville, Ohio, United States | greenhouse | - | Closed | Mar 23, 2026 |
| ~~OpenAI~~ | ~~Infrastructure Partnership Delivery Lead – Stargate 🇺🇸~~ | Remote - US | ashby | - | Closed | Mar 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Design Software (Starship) 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | Mar 18, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Design Software (Starship) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 18, 2026 |
| ~~DRW~~ | ~~Software Engineer - Prediction Markets (Python) 🇺🇸~~ | New York City | greenhouse | - | Closed | Mar 17, 2026 |
| ~~Aurora Innovation~~ | ~~Software Engineer I 🇺🇸~~ | Mountain View, California | greenhouse | Early Career | Closed | Mar 16, 2026 |
| ~~DRW~~ | ~~Software Engineer - Prediction Markets (Python) 🇺🇸~~ | Chicago | greenhouse | - | Closed | Mar 12, 2026 |
| ~~Together AI~~ | ~~Data Warehouse Engineer 🇺🇸~~ | San Francisco | greenhouse | - | Closed | Mar 11, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Starlink Network 🇺🇸~~ | Sunnyvale, CA | greenhouse | - | Closed | Mar 11, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Embedded Software (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 11, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ (Starlink) 🇺🇸~~ | Sunnyvale, CA | greenhouse | - | Closed | Mar 11, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Telemetry (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 09, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Software (Starlink) 🇺🇸~~ | Sunnyvale, CA | greenhouse | New Grad | Closed | Mar 06, 2026 |
| ~~SpaceX~~ | ~~AI Security Software Engineer (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 06, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, CDN  (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 04, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Data - Top Secret Clearance (Starlink) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 04, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Simulation 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Mar 03, 2026 |
| ~~SpaceX~~ | ~~RF Silicon Software Engineer (RFIC Engineering) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Mar 02, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Software (Starlink) 🇺🇸~~ | Bastrop, TX | greenhouse | New Grad | Closed | Feb 27, 2026 |
| ~~SpaceX~~ | ~~AI Security Software Engineer (Starshield) 🇺🇸~~ | Washington, DC | greenhouse | - | Closed | Feb 27, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Product Development (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 26, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Tracking (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 18, 2026 |
| ~~OpenAI~~ | ~~Research Engineer - Speech & Realtime Models 🇺🇸~~ | San Francisco | ashby | - | Closed | Feb 17, 2026 |
| ~~Apptronik~~ | ~~Simulation Engineer 🇺🇸~~ | Austin, TX | greenhouse | - | Closed | Feb 17, 2026 |
| ~~Anduril~~ | ~~Security Software Engineer - Endpoint Security 🇺🇸~~ | Costa Mesa, California, United States | greenhouse | - | Closed | Feb 13, 2026 |
| ~~SpaceX~~ | ~~Full Stack Software Engineer (Components) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 12, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer, Data 🇺🇸~~ | Starbase, TX | greenhouse | - | Closed | Feb 12, 2026 |
| ~~xAI~~ | ~~Member of Technical Staff 🇺🇸~~ | Memphis, TN | greenhouse | - | Closed | Feb 05, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Quantum Research Scientist, Processor Test & Measurement, AWS Center for Quantum Computing 🇺🇸~~ | Pasadena, CA, USA | amazon_jobs | - | Closed | Feb 05, 2026 |
| ~~SpaceX~~ | ~~Application Software Engineer 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Feb 03, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starshield) - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 02, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, HITL - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 02, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Data - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 02, 2026 |
| ~~SpaceX~~ | ~~Security Software Engineer (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Feb 02, 2026 |
| ~~SpaceX~~ | ~~Backend Software Engineer, GNC (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Feb 02, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Power Systems Controls (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | - | Closed | Jan 29, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Components Test (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jan 28, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, High Performance Computing 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jan 26, 2026 |
| ~~Robinhood~~ | ~~Web Engineer 🇺🇸~~ | Menlo Park, CA | greenhouse | - | Closed | Jan 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Satellite Operations (Starshield) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jan 21, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, C++ - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Jan 19, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Software (Starlink) 🇺🇸~~ | Redmond, WA | greenhouse | New Grad | Closed | Jan 16, 2026 |
| ~~SpaceX~~ | ~~Quality Systems Engineer (Starlink Aviation) 🇺🇸~~ | Woodinville, WA | greenhouse | - | Closed | Jan 15, 2026 |
| ~~Point72~~ | ~~Data Scientist 🇺🇸~~ | Chicago, New York | greenhouse | - | Closed | Jan 13, 2026 |
| ~~Roblox~~ | ~~[2026] Data Scientist, Social 🇺🇸~~ | San Mateo, CA, United States | greenhouse | PhD Student | Closed | Dec 16, 2025 |
| ~~SpaceX~~ | ~~Software Engineer, Additive Manufacturing (Raptor) 🇺🇸~~ | Hawthorne, CA | greenhouse | - | Closed | Dec 11, 2025 |
| ~~Roblox~~ | ~~[2026] Senior Machine Learning Engineer,  Engine Optimization - PhD Early Career 🇺🇸~~ | San Mateo, CA, United States | greenhouse | PhD, New Grad | Closed | Dec 04, 2025 |
| ~~Affirm~~ | ~~Software Engineer, Early Career 🇺🇸~~ | San Francisco, California, United States | greenhouse | New Grad | Closed | Nov 28, 2025 |
| ~~Chime~~ | ~~Product Security Engineer 🇺🇸~~ | San Francisco, CA, USA | greenhouse | - | Closed | Oct 03, 2025 |
| ~~DoorDash~~ | ~~Software Engineer I, Entry-Level (Graduation Date: Fall 2025-Summer 2026) 🇺🇸~~ | New York, NY<br>San Francisco, CA<br>Los Angeles, CA<br>Seattle, WA<br>Sunnyvale, CA | greenhouse | New Grad | Closed | Oct 01, 2025 |
| ~~CoreWeave~~ | ~~Software Engineer, Observability 🇺🇸~~ | New York, NY / Sunnyvale, CA | greenhouse | - | Closed | Jul 25, 2025 |
| ~~Warp~~ | ~~Software Engineer, Growth 🇺🇸~~ | New York | ashby | - | Closed | Jul 22, 2025 |
| ~~Robinhood~~ | ~~Android Engineer 🇺🇸~~ | New York, NY | greenhouse | - | Closed | May 08, 2025 |
| ~~Pinterest~~ | ~~Software Engineer I, Backend 🇺🇸~~ | Seattle, WA, US<br>San Francisco, CA, US | greenhouse | Early Career | Closed | Apr 17, 2025 |
| ~~DoorDash~~ | ~~Software Engineer, Infrastructure - Autonomy & Robotics 🇺🇸~~ | San Francisco, CA | greenhouse | - | Closed | Nov 01, 2024 |
| ~~Stripe~~ | ~~Backend Engineer, Payments and Risk 🇺🇸~~ | US | greenhouse | - | Closed | Aug 08, 2024 |
| ~~Glean~~ | ~~Software Engineer, Product Backend 🇺🇸~~ | Mountain View, CA | greenhouse | - | Closed | Jun 04, 2024 |

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

