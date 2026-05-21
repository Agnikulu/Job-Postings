# Serverless ATS Job Sniper

An auto-updated list of **early-career engineering roles** scraped hourly
from the public ATS APIs of top tech companies (Greenhouse, Lever, Ashby,
Workday). Filtered for entry-level, internship, new-grad, and university
graduate positions. US-only by default.

Built on a free GitHub Actions cron with zero servers and zero ongoing
costs. State (`seen_jobs.json`, `jobs_archive.json`, `company_stats.json`)
is committed back to the repo so the table grows historically.

See [README\_TECH.md](README_TECH.md) for the project architecture,
how to fork, how to add companies, and how filtering works.

## Stats

- **Open positions:** 250
- **All-time tracked:** 251
- **Active companies:** 79
- **Last updated:** `2026-05-21 11:24 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Education** -> Multi-label tag from `{PhD, Masters, Bachelors, New Grad, Intern}`.
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> When the company posted the role (parsed from each ATS).
   Falls back to when our scraper first observed the URL.

## Open positions

| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| Palantir | Forward Deployed Software Engineer, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/315f695d-04d1-4a9a-848e-cb2bec7a997e) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | Washington, D.C. | Intern | [Apply](https://jobs.lever.co/palantir/5c4c65c5-77da-4d36-856c-4ade87631019) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/5c7bb70c-83ea-43e7-8055-0c8f319f4333) | May 21, 2026 |
| Palantir | Deployment Strategist, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/a49d4181-a289-435a-b581-7f5af0497c8e) | May 21, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - France 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/ac0dc094-2480-43c2-8495-26ade227ff4f) | May 21, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - Poland 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/d582cd84-14fd-4aa3-b413-15982d286bd9) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - Commercial 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/e6789b17-62fb-4226-a079-f8c17ff19e2d) | May 21, 2026 |
| DoorDash | AI Research Fellowship, (Summer and Fall 2026) 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7848317) | May 20, 2026 |
| Microsoft | Data Center Technicians Intern 🇺🇸 | Middenmeer, NH, NL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867635) | May 20, 2026 |
| Google | Network Operations Residency Program, University Graduate, August 2026 Start 🇺🇸 | Atlanta, GA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckW16SkRVgStg44aewUebNozwHc6io0qVgTyBzqrFAF6YEjsACxwdTN2Mxoqd0Pxq2Q8FRyVaKVnp1HIFj40lAjKdBMPXtgfN8YFNurTkzAHGTImKv52Qh34rmkIAZw%3D%3D_V2&loc=US&title=Network+Operations+Residency+Program) | May 20, 2026 |
| Lambda Labs | Field Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Second St) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/e0e555b9-a009-43c4-bd64-57e74cfd67f1) | May 20, 2026 |
| Uber | Graduate 2026 PhD Scientist II (AEA/ASSA Economists Only), Reservations 🇺🇸 | Seattle, Washington, United States | PhD | [Apply](https://www.uber.com/careers/list/158984) | May 20, 2026 |
| Uber | Graduate 2026 PhD Software Engineer II (AV Labs), United States 🇺🇸 | San Francisco, California, United States / Sunnyvale, California, United States | PhD | [Apply](https://www.uber.com/careers/list/159120) | May 20, 2026 |
| Roblox | [2026] Applied Scientist - PhD Intern 🇺🇸 | San Mateo, CA, United States | PhD, Intern | [Apply](https://careers.roblox.com/jobs/7142298?gh_jid=7142298) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Social - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7463634?gh_jid=7463634) | May 20, 2026 |
| Roblox | [2026] Software Engineer, Game Developer 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7557909?gh_jid=7557909) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Foundation AI - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7577436?gh_jid=7577436) | May 20, 2026 |
| Roblox | [2026] Design & Creative Fellowship 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7779304?gh_jid=7779304) | May 20, 2026 |
| Anduril | Early Career Manufacturing Engineer 🇺🇸 | Santa Ana, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5009798007?gh_jid=5009798007) | May 20, 2026 |
| Stripe | PhD Machine Learning Engineer, Intern 🇺🇸 | San Francisco, New York City, Seattle | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7216664) | May 20, 2026 |
| Stripe | PhD Data Scientist, Intern 🇺🇸 | San Francisco, New York City, Seattle, Chicago | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7874965) | May 20, 2026 |
| Microsoft | Critical Environment Ops INTERN 🇺🇸 | ON,CA | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556866710) | May 19, 2026 |
| Microsoft | Research Science PhD Internship Opportunities - Coding Agents 🇺🇸 | Cambridge, England, GB | PhD, Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867906) | May 19, 2026 |
| Etched | GTM Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/0321523b-f0c3-44cd-9c46-cf318a1cad9e) | May 19, 2026 |
| Etched | PD Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/09658f43-69ab-4a98-b4fb-02865a3f9f92) | May 19, 2026 |
| Etched | Firmware Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/0e78a385-c450-4749-9803-0970ce2971a5) | May 19, 2026 |
| Etched | Core Ops Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/0f24f73f-7607-466e-bbc0-de039767e9c0) | May 19, 2026 |
| Etched | DFT Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/15fe0696-ce29-469a-b31e-a206e19302d6) | May 19, 2026 |
| Etched | Firmware Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/1efd9b58-66fe-4798-a877-776857b4e189) | May 19, 2026 |
| Etched | Supercomputing Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/20f77518-1699-4184-ac8e-9fa2f614d6fb) | May 19, 2026 |
| Etched | GTM Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/2369ccf9-2b5b-4355-a0d6-dd6d73317358) | May 19, 2026 |
| Etched | Talent Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/2425e245-6e16-49ca-be54-fb36941af55a) | May 19, 2026 |
| Etched | Chip Simulation Software Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/27e5bd6b-9357-45f0-9e79-cfa2bf4eeba8) | May 19, 2026 |
| Etched | Supercomputing Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/2d7039e2-190e-4039-b5a9-fff9efa7cc8e) | May 19, 2026 |
| Etched | Inference Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/2e4d8727-82f1-4887-9389-df5605783bbd) | May 19, 2026 |
| Etched | Core Ops Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/30514004-7db4-479d-8512-972946b146f4) | May 19, 2026 |
| Etched | DV Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/3ea1610a-3dfd-4b51-aeb8-6317e4d6877f) | May 19, 2026 |
| Etched | PD Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/3ec2bf6a-5ff3-436c-ad3e-6b77ac02ad97) | May 19, 2026 |
| Etched | Talent Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/431a3988-28bb-423b-b526-036b0cfd1963) | May 19, 2026 |
| Etched | DV Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/49009e2e-765a-4c4f-824b-7aea0ade2e8f) | May 19, 2026 |
| Etched | DFT Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/4d12f517-6282-4775-8044-fe2133ad5eff) | May 19, 2026 |
| Etched | Infrastructure Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/65348db2-5658-41d0-a833-af222865d979) | May 19, 2026 |
| Etched | DFT Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/6dca552b-876d-4525-971b-6ee720f267eb) | May 19, 2026 |
| Etched | GTM Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/73ce9d32-26c9-46c0-adaa-dfbe6660a0e1) | May 19, 2026 |
| Etched | Infrastructure Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/80926a71-0a62-4bf8-a877-b6d96df279b7) | May 19, 2026 |
| Etched | Firmware Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/8134a9bf-9624-48dd-98be-0bf1c3cb1f55) | May 19, 2026 |
| Etched | Talent Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/89093845-b572-4f2a-93e5-28e99bcbfa89) | May 19, 2026 |
| Etched | Electrical Platform Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/8c1e7aab-3c6d-49a3-8176-d9158acb181f) | May 19, 2026 |
| Etched | Finance Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/9b060f41-4607-494b-bdcf-57b1e74754ff) | May 19, 2026 |
| Etched | Electrical Platform Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/9e6737f4-394f-43b1-92ef-b9d4a7986f68) | May 19, 2026 |
| Etched | ChipSim Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/a06f95bc-adb5-48a2-b9b5-a77695bbd61b) | May 19, 2026 |
| Etched | Finance Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/a0a1671e-15d4-474c-8227-97fe16ade553) | May 19, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/a63c06e0-ae10-467f-a2d2-f222b7016af1) | May 19, 2026 |
| Etched | Inference Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/aa17bfa2-2922-4aa7-820d-76064f2551a8) | May 19, 2026 |
| Etched | Mech / Thermal Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/b1816ce1-fa42-4855-988b-992556414988) | May 19, 2026 |
| Etched | Supercomputing Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/b45e357c-07ea-4499-9911-1d3cc9b9ac71) | May 19, 2026 |
| Etched | PD Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/bd8c5768-7efa-4a18-9e56-485ccaf4ec77) | May 19, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/d9f7c735-c20c-4c9f-92e5-ae3d598b1643) | May 19, 2026 |
| Etched | ChipSim Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/daa8c6c4-97e3-4df4-b8da-e46fe981da1d) | May 19, 2026 |
| Etched | Infrastructure Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/e56469e3-7398-4d83-9fe3-3f8ab1b10468) | May 19, 2026 |
| Etched | Finance Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/e882eeaf-a34b-4f59-98f3-282cbd444508) | May 19, 2026 |
| Etched | Mech / Thermal Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/ec962944-f7ed-4a3e-a251-9d929295a740) | May 19, 2026 |
| Etched | Core Ops Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f32908bd-8abc-495c-ab69-ac893b6c924d) | May 19, 2026 |
| Etched | RTL Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f33b89ca-ad74-4a4f-8f15-06c64e954f4d) | May 19, 2026 |
| Etched | RTL Intern - Summer 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f66613b6-9942-48ce-a553-c377e44d3118) | May 19, 2026 |
| Etched | Mech / Thermal Intern - Spring 2027 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f77c61ff-da01-42ce-9ad6-ab0facbccd5b) | May 19, 2026 |
| Nvidia | Quantum Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Research-Scientist-Intern---Fall-2026_JR2018244) | May 19, 2026 |
| Nvidia | AI Software Engineer, Kernel Libraries - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Software-Engineer--Kernel-Libraries---New-College-Grad-2026_JR2018472) | May 19, 2026 |
| Microsoft | Research Intern - Self-Improving AI 🇺🇸 | Cambridge, MA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867858) | May 18, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | May 18, 2026 |
| Anduril | Early Career Mechanical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802167007?gh_jid=4802167007) | May 18, 2026 |
| Anduril | Early Career Electrical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802172007?gh_jid=4802172007) | May 18, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Seattle, Washington, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4824364007?gh_jid=4824364007) | May 18, 2026 |
| Nvidia | Technical Marketing Engineering Intern, Robotics - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Technical-Marketing-Engineering-Intern--Robotics---Fall-2026_JR2009105-1) | May 18, 2026 |
| Microsoft | Critical Environment Technician Intern 🇺🇸 | Middenmeer, NH, NL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556866901) | May 14, 2026 |
| Lambda Labs | Security Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Fremont St) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/0663f04c-097d-414f-b0a0-414a7cf153d6) | May 14, 2026 |
| Lambda Labs | Capital Markets & Corporate Development Intern - Summer 2026 🇺🇸 | San Francisco Office (Fremont St) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/4803c790-6e11-4e82-ad5e-f07c79290760) | May 14, 2026 |
| Pinterest | Master's Fall Machine Learning Internship (ATG - Visual Search) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | Masters, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7253017) | May 14, 2026 |
| Pinterest | PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | PhD, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7255640) | May 14, 2026 |
| Nvidia | Circuit Design Engineer, Power Modeling and Simulation - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer--Power-Modeling-and-Simulation---New-College-Grad-2026_JR2018108) | May 14, 2026 |
| Nvidia | Software R&D Engineer, VLSI Physical Design - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Software-R-D-Engineer--VLSI-Physical-Design---New-College-Grad-2026_JR2018183) | May 14, 2026 |
| Microsoft | Cambridge Internship: Novel Light Source Design 🇺🇸 | Cambridge, England, GB | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556866395) | May 13, 2026 |
| Airbnb | Data Science Intern 🇺🇸 | United States | Intern | [Apply](https://careers.airbnb.com/positions/7839237?gh_jid=7839237) | May 13, 2026 |
| Nvidia | PhD Research Intern, Security and Privacy - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Security-and-Privacy---Fall-2026_JR2010492-1) | May 13, 2026 |
| Nvidia | Signal and Power Integrity Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Signal-and-Power-Integrity-Engineer---New-College-Grad-2026_JR2017741) | May 12, 2026 |
| Point72 | Point72 Academy Investment Analyst Program for Upcoming Graduates (2027 – US) 🇺🇸 | Chicago, Florida, New York, San Francisco | - | [Apply](https://boards.greenhouse.io/point72/jobs/8541241002?gh_jid=8541241002) | May 11, 2026 |
| Adobe | 2026 Intern - Data Scientist 🇺🇸 | San Jose | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Data-Scientist_R161453) | May 11, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | May 11, 2026 |
| Nvidia | GPU System and Scheduling Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-System-and-Scheduling-Architect---New-College-Grad-2026_JR2016691-1) | May 10, 2026 |
| Uber | 2026 Fall Software Engineering Internship, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Intern | [Apply](https://www.uber.com/careers/list/159161) | May 08, 2026 |
| Snowflake | Software Engineer Intern (Security) - Fall 2026 🇺🇸 | US-CA-Menlo Park | Intern | [Apply](https://jobs.ashbyhq.com/snowflake/a488959b-6874-4563-acb2-af747c3dc6f7) | May 08, 2026 |
| Scale AI | Software Engineer - New Grad 🇺🇸 | San Francisco, CA | New Grad | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4605996005) | May 08, 2026 |
| Scale AI | Technical Advisor Specialist (Part-Time Internship) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4611533005) | May 08, 2026 |
| Scale AI | National Security Hackathon 2026 - General Interest 🇺🇸 | San Francisco, CA<br>New York, NY<br>Washington, DC | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4687588005) | May 08, 2026 |
| Nvidia | ASIC Floorplan Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Floorplan-Design-Engineer---New-College-Grad-2026_JR2012971) | May 07, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | US, MA, Westford | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2017593) | May 07, 2026 |
| Microsoft | Research Intern - AI Agents & Efficiency 🇺🇸 | Cambridge, England, GB | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556626895) | May 06, 2026 |
| Microsoft | Research Intern - Intelligent Quantum Systems Architecture 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556864482) | May 06, 2026 |
| Microsoft | Research Intern - Fault Tolerant Quantum System Architecture 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556864490) | May 06, 2026 |
| Microsoft | Research Intern - AI Frontiers 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556864498) | May 06, 2026 |
| Nvidia | ASIC Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Design-Engineer---New-College-Grad-2026_JR2017581) | May 06, 2026 |
| Nvidia | Applied Deep Learning PhD Research Intern, Reinforcement Learning for LLMs - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Deep-Learning-PhD-Research-Intern--Reinforcement-Learning-for-LLMs---Fall-2026_JR2012398) | May 06, 2026 |
| Nvidia | Software Engineering Intern, AI Tools - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--AI-Tools---Fall-2026_JR2016805) | May 06, 2026 |
| Inceptive | Internship 🇺🇸 | Palo Alto, CA | Intern | [Apply](https://job-boards.greenhouse.io/inceptive/jobs/5103191007) | May 05, 2026 |
| Nvidia | Machine Learning Applications and Compiler Engineer, LPX - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Machine-Learning-Applications-and-Compiler-Engineer--LPX---New-College-Grad-2026_JR2016939) | May 05, 2026 |
| Nvidia | Power Methodology and Modeling Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Power-Methodology-and-Modeling-Engineer---New-College-Grad-2026_JR2017486-1) | May 05, 2026 |
| Microsoft | Stagiaire Technicien de Centre de Données / Datacenter Technician Intern 🇺🇸 | Québec City, QC, CA | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556859421) | May 01, 2026 |
| Nvidia | GPU Power Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-Power-Architect---New-College-Grad-2026_JR2017169) | May 01, 2026 |
| Nvidia | ASIC Clocks Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Clocks-Verification-Engineer---New-College-Grad-2026_JR2013336) | Apr 30, 2026 |
| Microsoft | Security Research Intern - AI Focus 🇺🇸 | Herzliya, Tel Aviv District, IL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556862170) | Apr 28, 2026 |
| Microsoft | Research Intern - Socio-Technical Workflow Analysis 🇺🇸 | Redmond, WA, US / Cambridge, MA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556862680) | Apr 28, 2026 |
| Airbnb | iOS Software Engineer, Airbnb - New Grad 🇺🇸 | San Francisco, CA, Seattle, WA | New Grad | [Apply](https://careers.airbnb.com/positions/7859317?gh_jid=7859317) | Apr 28, 2026 |
| Nvidia | Hardware Applications Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Hardware-Applications-Engineer---New-College-Grad-2026_JR2016940) | Apr 28, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (iOS) 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158011) | Apr 27, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (Android) 🇺🇸 | Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158037) | Apr 27, 2026 |
| Notion | Software Engineer, New Grad (AI) 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9) | Apr 27, 2026 |
| Figure AI | Electrical Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | Apr 25, 2026 |
| Figure AI | Electrical Interconnect Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676468006) | Apr 25, 2026 |
| Physical Intelligence | Mechatronics Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/0bcf909e-b38b-4276-91a1-e55c4c56a33a) | Apr 24, 2026 |
| Physical Intelligence | Hardware Systems Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/96bc1142-f406-4df3-aaa0-4bcce85f457f) | Apr 24, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/11aedfd6-8321-45af-b71e-492ea7ed3fff) | Apr 24, 2026 |
| Nvidia | Low Power ASIC Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Low-Power-ASIC-Engineer---New-College-Grad-2026_JR2017001) | Apr 24, 2026 |
| Nvidia | Software Engineering Intern, JAX - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--JAX---Fall-2026_JR2009745) | Apr 24, 2026 |
| Microsoft | Research Intern - Audio and Acoustics 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556861664) | Apr 23, 2026 |
| Notion | Software Engineer, New Grad 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555) | Apr 23, 2026 |
| Figma | Inside Sales Representative - Early Career (2026) 🇺🇸 | San Francisco, CA • New York, NY | New Grad | [Apply](https://boards.greenhouse.io/figma/jobs/5977327004?gh_jid=5977327004) | Apr 23, 2026 |
| Figma | Data Scientist, Core Data -  PhD (2026) 🇺🇸 | New York, NY • United States<br>San Francisco, CA • New York, NY | PhD | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) | Apr 22, 2026 |
| Nvidia | Deep Learning Architect, LLM Inference - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Deep-Learning-Architect--LLM-Inference---New-College-Grad-2026_JR2016950) | Apr 22, 2026 |
| Microsoft | Research Intern - Computer Vision and Deep Learning 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621607) | Apr 21, 2026 |
| Adobe | 2026 University Graduate - Research Scientist/Engineer 🇺🇸 | San Francisco | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/XMLNAME-2026-University-Graduate---Research-Scientist-Engineer_R160690) | Apr 21, 2026 |
| Adobe | 2026 University Graduate - Machine Learning Engineer 🇺🇸 | Seattle | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/Seattle/XMLNAME-2026-University-Graduate---Machine-Learning-Engineer_R160133) | Apr 21, 2026 |
| Figure AI | Embedded Software Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4397706006) | Apr 21, 2026 |
| Nvidia | AI Chip Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Chip-Design-Engineer---New-College-Grad-2026_JR2015481) | Apr 21, 2026 |
| Nvidia | AI Chip Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Chip-Design-Engineer---New-College-Grad-2026_JR2015487) | Apr 21, 2026 |
| Nvidia | Cell Modeling and Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Cell-Modelling-and-Verification-Engineer---New-College-Grad-2026_JR2011631) | Apr 21, 2026 |
| Nvidia | Circuit Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer---New-College-Grad-2026_JR2014331) | Apr 21, 2026 |
| Nvidia | Deep Learning Kernel Software Performance Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Deep-Learning-Kernel-Software-Performance-Architect---New-College-Grad-2026_JR2011814) | Apr 21, 2026 |
| Nvidia | Research Scientist, Generative AI for Physical AI - PhD New College Grad 2026 🇺🇸 | US, CA, Santa Clara | PhD, New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Research-Scientist--Generative-AI-for-Physical-AI---PhD-New-College-Grad-2026_JR2016032) | Apr 21, 2026 |
| Nvidia | Signoff Methodology Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Signoff-Methodology-Engineer---New-College-Grad-2026_JR2014110) | Apr 21, 2026 |
| Nvidia | SoC ASIC Verification Engineer – New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/SoC-ASIC-Verification-Engineer---New-College-Grad-2026_JR2015202-1) | Apr 21, 2026 |
| Nvidia | ASIC Hardware Design Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/ASIC-Hardware-Design-Engineer---New-College-Grad-2026_JR2011787) | Apr 21, 2026 |
| Point72 | Summer 2027 Quantitative Developer Internship 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297613002?gh_jid=7297613002) | Apr 13, 2026 |
| Point72 | Summer 2027 Quantitative Research Internship 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297642002?gh_jid=7297642002) | Apr 13, 2026 |
| Etched | DFT Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/5f1f5739-3b58-467c-b351-ff183c94d96d) | Apr 13, 2026 |
| Uber | Graduate 2026 Software Engineer I, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158009) | Apr 09, 2026 |
| Point72 | Point72 Academy 2026-2027 Investment Analyst Program for Experienced Professionals - US 🇺🇸 | Chicago, Florida, New York, San Francisco | - | [Apply](https://boards.greenhouse.io/point72/jobs/8499113002?gh_jid=8499113002) | Apr 09, 2026 |
| Databricks | PhD GenAI Research Scientist Intern 🇺🇸 | San Francisco, California | PhD, Intern | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002) | Apr 09, 2026 |
| Notion | Software Engineer Intern (Fall 2026) 🇺🇸 | San Francisco, California | Intern | [Apply](https://jobs.ashbyhq.com/notion/5b15697c-fa91-4511-9482-c98a6ff29f90) | Apr 06, 2026 |
| Microsoft | Research Intern - Inference Economics and Human Agency 🇺🇸 | Redmond, WA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556856507) | Apr 03, 2026 |
| Microsoft | Research Intern - Applied Power Systems Analysis 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556856536) | Apr 03, 2026 |
| Etched | Technical Recruiter (Entry Level) 🇺🇸 | San Jose | New Grad | [Apply](https://jobs.ashbyhq.com/etched/06398761-0950-4e5c-8590-26f485ba5509) | Apr 02, 2026 |
| Microsoft | Research Intern - Foundation Models and Agentic Systems 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556856002) | Apr 01, 2026 |
| Point72 | Quantitative Software Developer Intern 🇺🇸 | New York, London, or Paris | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297666002?gh_jid=7297666002) | Mar 31, 2026 |
| Point72 | Quantitative Research Intern 🇺🇸 | New York, Seattle | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297667002?gh_jid=7297667002) | Mar 31, 2026 |
| Point72 | Machine Learning Researcher - Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7302611002?gh_jid=7302611002) | Mar 31, 2026 |
| Point72 | Quantitative Researcher Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7586061002?gh_jid=7586061002) | Mar 31, 2026 |
| Point72 | Quantitative Developer Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7609197002?gh_jid=7609197002) | Mar 31, 2026 |
| Point72 | Quantitative Research Intern (NLP) 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/8018862002?gh_jid=8018862002) | Mar 31, 2026 |
| Point72 | Quantitative Portfolio Analyst – 2026 Grad 🇺🇸 | New York, New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/8169967002?gh_jid=8169967002) | Mar 31, 2026 |
| Figure AI | Hardware Reliability Intern [Summer 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4613067006) | Mar 31, 2026 |
| Sierra | Intern, Agent Development (Fall 2026) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://jobs.ashbyhq.com/sierra/c74d600c-235c-4d42-8546-b178b7adefc2) | Mar 19, 2026 |
| Microsoft | Research Intern - AI Safety and Security 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556826707) | Mar 05, 2026 |
| Microsoft | Research Intern - Cryptography and Applications 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556768703) | Feb 20, 2026 |
| Etched | RTL Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/157ed4f4-6e3b-4ec9-b93f-3e363e92041e) | Feb 07, 2026 |
| Etched | Infrastructure Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/1b073af4-6764-45ca-a22d-40a4823f0877) | Feb 07, 2026 |
| Etched | Firmware Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/699f3ab2-07e4-466c-9d76-3d4a3abb4ebc) | Feb 07, 2026 |
| Etched | Electrical Platform Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/904ddf46-55fc-4a8f-8b49-f32cfe88116a) | Feb 07, 2026 |
| Etched | Supercomputing Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/982a8ee4-5e1e-43c7-a918-6dac285cdddd) | Feb 07, 2026 |
| Etched | DV Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/dacedaca-c4ca-4964-85a7-8df1738005bb) | Feb 07, 2026 |
| Etched | Mech / Thermal Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f05e3218-5ec7-41d1-bc99-bb7014422229) | Feb 07, 2026 |
| Microsoft | Research Intern - Azure Storage 🇺🇸 | Redmond, WA, US / Mountain View, CA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556752793) | Feb 06, 2026 |
| Microsoft | Research Intern - Applied Speech Research 🇺🇸 | Berkeley, CA, US / Burlington, MA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556751423) | Feb 04, 2026 |
| Microsoft | Research Intern - Agentic Programming 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556750506) | Feb 03, 2026 |
| Microsoft | Research Intern - Applied Sciences Group 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556748770) | Jan 28, 2026 |
| Microsoft | Research Intern - AI Systems and Tools 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556748177) | Jan 27, 2026 |
| Google | Hardware Test Engineer, University Graduate, Platforms Infrastructure 🇺🇸 | Sunnyvale, CA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckSMqGPLNoC0z-o9KDjKRQL8btCSBfKiIjyXJLaCsfbVVEjsAvkGZm-hoLAAK8ODGn5xR249xfB3Mxn4pNpWWUO7IQ2Q0bGoM3eLZHZpe0_EmxKOVbiSSP_9wKFz-yw%3D%3D_V2&loc=US&title=Hardware+Test+Engineer) | Jan 27, 2026 |
| Google | Hardware Validation Engineer, ML Products, University Graduate 🇺🇸 | Sunnyvale, CA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckaqA3xjX5aX_4s4uZOS0XJoGi0vDfnYn-b2cHivq6fg3EjsAvkGZm-QIEAKdEuPLcs1MNcBuxew0kt0Iv8GfbY65FO_Y7RN9nAXy2NWcrfgUeyRzQTzlv1d8bIVyKQ%3D%3D_V2&loc=US&title=Hardware+Validation+Engineer) | Jan 27, 2026 |
| Microsoft | Research Intern - Multi-Modal Sensing & Secure AI Devices 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556745603) | Jan 22, 2026 |
| Google | Silicon CAD Engineer, University Graduate, PhD 🇺🇸 | Sunnyvale, CA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckXQEUI9XfOeK_3XYuXygggJ1a_miLVttYmMwabnENaQXEjsAvkGZm0RQKdLFnO2Ito9mFe48LB3Cgc6u1G-ovNbiOY28Hj0OLQ_BDRsxHklfEw1eaAGVmVZ00EMthw%3D%3D_V2&loc=US&title=Silicon+CAD+Engineer) | Jan 22, 2026 |
| Microsoft | Research Intern - Bayesian Methods in Geometric Computer Vision 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556745482) | Jan 21, 2026 |
| Microsoft | Research Intern - Office of the Chief Scientific Officer 🇺🇸 | Mountain View, CA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556744903) | Jan 20, 2026 |
| Recursion Pharma | Interested in an internship? 🇺🇸 | Remote Opportunity - United States<br>Salt Lake City, Utah | Intern | [Apply](https://job-boards.greenhouse.io/recursionpharmaceuticals/jobs/7540026) | Jan 20, 2026 |
| Microsoft | Research Intern - AI Evaluation and Alignment 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556735254) | Jan 16, 2026 |
| Microsoft | Research Intern - Foundations of GenAI 🇺🇸 | New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556659148) | Jan 13, 2026 |
| Microsoft | Research Intern - Security, Privacy and AI 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556659072) | Jan 12, 2026 |
| Microsoft | Research Intern - Machine Learning and Optimization 🇺🇸 | Cambridge, MA, US / Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556655958) | Dec 31, 2025 |
| Microsoft | Research Intern - Quantum Error Correction 🇺🇸 | Redmond, WA, US / Santa Barbara, CA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556650810) | Dec 18, 2025 |
| Microsoft | Research Intern - Human-AI Interaction Research and Design (Health AI) 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556643556) | Dec 17, 2025 |
| Microsoft | Research Intern - LLM Performance Optimization 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556643548) | Dec 16, 2025 |
| Google | Hardware Architecture Modeling Engineer, PhD, University Graduate 🇺🇸 | Sunnyvale, CA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckQDRg7-SWg1ii1hE2JH0AjNahNZa2Lxngk6WCaS9Wb8YEjkAvkGZm16Ks30-FCkCI58yNIyB9h_JxPr0l7B6rnrG-W27DcMWw7EvjYc9e7x7-aypAecWmyLNHT0%3D_V2&loc=US&title=Hardware+Architecture+Modeling+Engineer) | Dec 15, 2025 |
| Microsoft | Research Intern - AI System Architecture Modeling and Performance 🇺🇸 | Hillsboro, OR, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556641879) | Dec 11, 2025 |
| Microsoft | Research Intern - Microsoft Teams (PhD) 🇺🇸 | Redmond, WA, US | PhD, Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556640715) | Dec 09, 2025 |
| Microsoft | Research Intern - OneDrive and SharePoint (Summer 2026) 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556640732) | Dec 09, 2025 |
| Microsoft | Research Intern - Office of the Chief Scientific Officer 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556640817) | Dec 09, 2025 |
| Microsoft | Research Intern - Diagnostic Imaging AI, Imaging Computing, Reconstruction and Inverse Problem 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556640831) | Dec 09, 2025 |
| Microsoft | Research Intern - AI Hardware 🇺🇸 | Vancouver, BC, CA | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621661) | Dec 08, 2025 |
| Etched | Talent Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/639fe410-56a4-44aa-ac93-8ee7c10c7d75) | Dec 08, 2025 |
| Etched | Inference Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/6f23713f-5409-45b7-aae8-adb8710cdbc3) | Dec 08, 2025 |
| Microsoft | Research Intern - AI Frameworks (Network Systems and Tools) 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556639524) | Dec 05, 2025 |
| Microsoft | Research Intern - AI Network Observability 🇺🇸 | Mountain View, CA, US / Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556639544) | Dec 05, 2025 |
| Microsoft | Research Intern - Computational Social Science 🇺🇸 | New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556639564) | Dec 05, 2025 |
| Microsoft | Research Intern - Deep Learning Group 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556637090) | Dec 02, 2025 |
| Microsoft | Research Intern - AI/ML Numerics & Efficiency 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556637096) | Dec 02, 2025 |
| Microsoft | Research Intern - AIP AI Knowledge Multimodal AI 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556637119) | Dec 02, 2025 |
| Microsoft | Research Intern - Office of Applied Research 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556636970) | Dec 01, 2025 |
| Microsoft | Research Intern - Data Center and AI Networking 🇺🇸 | Mountain View, CA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556636994) | Dec 01, 2025 |
| Microsoft | Research Intern - Technology for Religious Empowerment 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631718) | Nov 26, 2025 |
| Microsoft | Research Intern - Memory & Orchestration in Large Language Models 🇺🇸 | Redmond, WA, US / Silverdale, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631728) | Nov 26, 2025 |
| Microsoft | Research Intern - AI Systems & Architecture 🇺🇸 | Mountain View, CA, US / Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631742) | Nov 26, 2025 |
| Microsoft | Research Intern - Data Center and AI Networking 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631744) | Nov 26, 2025 |
| Microsoft | Research Intern - MSR Inclusive Futures Team 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631751) | Nov 26, 2025 |
| Microsoft | Research Intern - Medical Image Reconstruction 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631289) | Nov 25, 2025 |
| Microsoft | Research Intern - MSR Montreal / ML Team 🇺🇸 | Montreal, QC, CA | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556631315) | Nov 25, 2025 |
| Microsoft | Research Intern - Multimodal Language Models 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628867) | Nov 21, 2025 |
| Microsoft | Research Intern - Model Optimization and HW Acceleration 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628875) | Nov 21, 2025 |
| Microsoft | Research Intern - Training Methods for LLM Efficiency 🇺🇸 | Mountain View, CA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628881) | Nov 21, 2025 |
| Microsoft | Research Intern - Machine Learning and Optimization - Redmond 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628908) | Nov 21, 2025 |
| Microsoft | Research Intern - Economics and Computation 🇺🇸 | Cambridge, MA, US / New York, NY, US / Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628919) | Nov 21, 2025 |
| Microsoft | Research Intern - Microsoft Research Special Projects 🇺🇸 | Redmond, WA, US / Cambridge, MA, US / Silverdale, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628925) | Nov 21, 2025 |
| Google | Network Operations Residency Program, University Graduate, 2026 Start 🇺🇸 | Thornton, CO, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckfHzHMV0yE_g87eg2EqQSIPJ3NlB1unM6TRiOER0wNluEjsAbDj5iC6kYe5OQewD-cXoTVqnAQfMTIt0JKgL-rc9dRQoUFAgRJkV9oTDYB2TXU1UJSzGYPFyWQwFIg%3D%3D_V2&loc=US&title=Network+Operations+Residency+Program) | Nov 21, 2025 |
| Microsoft | Research Intern - LLM Acceleration 🇺🇸 | Mountain View, CA, US / Cambridge, MA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556627833) | Nov 20, 2025 |
| Microsoft | Research Intern - STAC, NYC (Sociotechnical Alignment Center) 🇺🇸 | New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556628319) | Nov 20, 2025 |
| Microsoft | Research Intern - Artificial Intelligence 🇺🇸 | Vancouver, BC, CA | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621503) | Nov 19, 2025 |
| Microsoft | Research Intern - ML and Computational Biology for the Immune System 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621559) | Nov 19, 2025 |
| Microsoft | Research Intern - Machine Learning at MSR NYC 🇺🇸 | New York, NY, US / Cambridge, MA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621563) | Nov 19, 2025 |
| Microsoft | Research Intern - RiSE group 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621565) | Nov 19, 2025 |
| Microsoft | Research Intern - Data Systems 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621612) | Nov 19, 2025 |
| Microsoft | Research Intern - Gray Systems Lab (GSL) 🇺🇸 | Redmond, WA, US / Mountain View, CA, US / Madison, WI, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621621) | Nov 19, 2025 |
| Microsoft | Research Intern - Fundamentals of AI: Security, Agents, Systems & Control 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621658) | Nov 19, 2025 |
| Microsoft | Research Intern - AI Hardware 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621664) | Nov 19, 2025 |
| Microsoft | Research Intern - MSR AI Interaction and Learning 🇺🇸 | Redmond, WA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621727) | Nov 19, 2025 |
| Microsoft | Research Intern - MSR Software-Hardware Co-design 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621730) | Nov 19, 2025 |
| Microsoft | Research Intern - MSR Systems Research Group - Redmond 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621732) | Nov 19, 2025 |
| Microsoft | Research Intern - Computer Vision and Deep Learning 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621779) | Nov 19, 2025 |
| Microsoft | Research Intern - Systems For Efficient AI 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621783) | Nov 19, 2025 |
| Microsoft | Research Intern - Reliability of Cloud and AI Systems 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621789) | Nov 19, 2025 |
| Microsoft | Research Intern - AI Frontiers - Reasoning & Agentic Models 🇺🇸 | Redmond, WA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621824) | Nov 19, 2025 |
| Microsoft | Research Intern - Hardware/Software Codesign 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621833) | Nov 19, 2025 |
| Microsoft | Research Intern - Machine Learning and Statistics 🇺🇸 | Cambridge, MA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621837) | Nov 19, 2025 |
| Microsoft | Research Intern - Systems for Reliable and Scalable AI Agents 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621908) | Nov 19, 2025 |
| Microsoft | Research Intern - Artificial Intelligence 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556622017) | Nov 19, 2025 |
| Microsoft | Research Intern - Azure Research - Systems 🇺🇸 | Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556622018) | Nov 19, 2025 |
| Microsoft | Research Intern - Foundations of Generative AI 🇺🇸 | New York, NY, US / Redmond, WA, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556621454) | Nov 18, 2025 |
| Google | Student Researcher, PhD, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / Goleta, CA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA | PhD | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckdDBszOwAboL1irYc5xQuYyKqC3h2okBoNLk3COfTIvnEjsAbDj5iFcTaZqyNkN9jNNd5HHI8cIk1Ag8eQCdAohcear60mczr-Sinm0tegTidLDm40kDJ-TGNZYA1Q%3D%3D_V2&loc=US&title=Student+Researcher) | Sep 29, 2025 |
| Google | Student Researcher, BS/MS, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA / Princeton, NJ, USA | Masters | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckTl3i0Kg9bm5-cwU_unEJ4immCkcmZEzsgvd7IwvbipLEjsAbDj5iIwSGTQMJEawk9aCtA9M1kBY7mUyJ58Qj5QSMtYgdTolThXSMDFsvF1G1pKNBvg-0csRwwwkTQ%3D%3D_V2&loc=US&title=Student+Researcher) | Sep 29, 2025 |
| Google | Software Engineer, PhD, Early Career, Embedded Systems and Firmware, 2026 Start 🇺🇸 | Sunnyvale, CA, USA / Atlanta, GA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / Seattle, WA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckQvzerP2JPvVejlhnKXNFmO6FM-Dw0Ro__woxbxSyl41EjsASXckS4TLFL_nNo4UurLUPHnKmiEd8vI4gduX5o5pnvi98j6E16OUhyheSxHmTWyU-qptk6K2EQFIPA%3D%3D_V2&loc=US&title=Software+Engineer) | Aug 26, 2025 |
| Google | Software Engineer, PhD, Early Career, Infrastructure, 2026 Start 🇺🇸 | Sunnyvale, CA, USA / Atlanta, GA, USA / Austin, TX, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / San Bruno, CA, USA / Seattle, WA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckVc-hqc8Mfy8TEjImPUHx0VmQ9kQ9CTDN8PM-_fdBJMnEjsASXckS-JBAexAvjEFm9McCTVJZ-NYL1N-ki1ogeKscLhYagOnaWypLCuEAPMZsM1Xbi9WsHjLrGuCJg%3D%3D_V2&loc=US&title=Software+Engineer) | Aug 26, 2025 |
| Google | Software Engineer, PhD, Early Career, AI/Machine Learning, 2026 Start 🇺🇸 | Sunnyvale, CA, USA / Atlanta, GA, USA / Kirkland, WA, USA / Madison, WI, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / San Bruno, CA, USA / Seattle, WA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckeYz1B-u5NbhAHYeBKz8za-fw00UT4XUcBVn_yPGzicDEjsASXckS88W464drpXUZRWh39KLsIpEiJTUx6Xu3ayH8bw_QxrWmpyTUGOn7EyCIsdhfuw-KtPc3YAjuQ%3D%3D_V2&loc=US&title=Software+Engineer) | Aug 26, 2025 |
| Ramp | Software Engineer Internship, Android 🇺🇸 | New York, NY (HQ) | Intern | [Apply](https://jobs.ashbyhq.com/ramp/67fadb77-43d8-4449-954b-d4cf2c6d3b8b) | Aug 07, 2025 |
| Google | Software Engineer, Systems Research, PhD, Early Career 🇺🇸 | Sunnyvale, CA, USA / Seattle, WA, USA | PhD, New Grad | [Apply](https://www.google.com/about/careers/applications/signin?jobId=CiUAL2FckcfynwY9n55CWFUO9YSo68R9PHMiQAr1nx-Z7xoo3Pf5EjsA7mFcrIEl4LMHm_mldhWYr9hod5CuVWsDE_q6FPfcbNw1_MoNvzI3asvAz1S9FloeLdqksv5vD3ECgw%3D%3D_V2&loc=US&title=Software+Engineer) | Jan 29, 2025 |


<details>
<summary><b>Closed positions (1)</b> &mdash; click to expand</summary>


| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| ~~Microsoft~~ | ~~Research Intern - Networking Research Group 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |

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

