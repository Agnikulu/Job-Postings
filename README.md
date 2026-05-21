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

- **Open positions:** 125
- **All-time tracked:** 125
- **Active companies:** 53
- **Last updated:** `2026-05-21 01:16 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Education** -> Multi-label tag from `{PhD, Masters, Bachelors, New Grad, Intern}`.
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> When the company posted the role (parsed from each ATS).
   Falls back to when our scraper first observed the URL.

## Open positions

| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| Roblox | [2026] Applied Scientist - PhD Intern 🇺🇸 | San Mateo, CA, United States | PhD, Intern | [Apply](https://careers.roblox.com/jobs/7142298?gh_jid=7142298) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Social - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7463634?gh_jid=7463634) | May 20, 2026 |
| Roblox | [2026] Software Engineer, Game Developer 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7557909?gh_jid=7557909) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Foundation AI - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7577436?gh_jid=7577436) | May 20, 2026 |
| Roblox | [2026] Design & Creative Fellowship 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7779304?gh_jid=7779304) | May 20, 2026 |
| Anduril | Early Career Manufacturing Engineer 🇺🇸 | Santa Ana, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5009798007?gh_jid=5009798007) | May 20, 2026 |
| Stripe | PhD Machine Learning Engineer, Intern 🇺🇸 | San Francisco, New York City, Seattle | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7216664) | May 20, 2026 |
| Stripe | PhD Data Scientist, Intern 🇺🇸 | San Francisco, New York City, Seattle, Chicago | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7874965) | May 20, 2026 |
| Nvidia | Quantum Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Research-Scientist-Intern---Fall-2026_JR2018244) | May 20, 2026 |
| Nvidia | AI Software Engineer, Kernel Libraries - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Software-Engineer--Kernel-Libraries---New-College-Grad-2026_JR2018472) | May 20, 2026 |
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
| Nvidia | Technical Marketing Engineering Intern, Robotics - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Technical-Marketing-Engineering-Intern--Robotics---Fall-2026_JR2009105-1) | May 19, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | May 18, 2026 |
| Anduril | Early Career Mechanical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802167007?gh_jid=4802167007) | May 18, 2026 |
| Anduril | Early Career Electrical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802172007?gh_jid=4802172007) | May 18, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Seattle, Washington, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4824364007?gh_jid=4824364007) | May 18, 2026 |
| Nvidia | Circuit Design Engineer, Power Modeling and Simulation - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer--Power-Modeling-and-Simulation---New-College-Grad-2026_JR2018108) | May 15, 2026 |
| Nvidia | Software R&D Engineer, VLSI Physical Design - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Software-R-D-Engineer--VLSI-Physical-Design---New-College-Grad-2026_JR2018183) | May 15, 2026 |
| Pinterest | Master's Fall Machine Learning Internship (ATG - Visual Search) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | Masters, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7253017) | May 14, 2026 |
| Pinterest | PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | PhD, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7255640) | May 14, 2026 |
| Nvidia | PhD Research Intern, Security and Privacy - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Security-and-Privacy---Fall-2026_JR2010492-1) | May 14, 2026 |
| Airbnb | Data Science Intern 🇺🇸 | United States | Intern | [Apply](https://careers.airbnb.com/positions/7839237?gh_jid=7839237) | May 13, 2026 |
| Nvidia | Signal and Power Integrity Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Signal-and-Power-Integrity-Engineer---New-College-Grad-2026_JR2017741) | May 13, 2026 |
| Adobe | 2026 Intern - Data Scientist 🇺🇸 | San Jose | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Data-Scientist_R161453) | May 12, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | May 12, 2026 |
| Nvidia | GPU System and Scheduling Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-System-and-Scheduling-Architect---New-College-Grad-2026_JR2016691-1) | May 11, 2026 |
| Snowflake | Software Engineer Intern (Security) - Fall 2026 🇺🇸 | US-CA-Menlo Park | Intern | [Apply](https://jobs.ashbyhq.com/snowflake/a488959b-6874-4563-acb2-af747c3dc6f7) | May 08, 2026 |
| Nvidia | ASIC Floorplan Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Floorplan-Design-Engineer---New-College-Grad-2026_JR2012971) | May 08, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | US, MA, Westford | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2017593) | May 08, 2026 |
| Scale AI | Software Engineer - New Grad 🇺🇸 | San Francisco, CA | New Grad | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4605996005) | May 08, 2026 |
| Scale AI | Technical Advisor Specialist (Part-Time Internship) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4611533005) | May 08, 2026 |
| Scale AI | National Security Hackathon 2026 - General Interest 🇺🇸 | San Francisco, CA<br>New York, NY<br>Washington, DC | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4687588005) | May 08, 2026 |
| Nvidia | ASIC Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Design-Engineer---New-College-Grad-2026_JR2017581) | May 07, 2026 |
| Nvidia | Applied Deep Learning PhD Research Intern, Reinforcement Learning for LLMs - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Deep-Learning-PhD-Research-Intern--Reinforcement-Learning-for-LLMs---Fall-2026_JR2012398) | May 07, 2026 |
| Nvidia | Software Engineering Intern, AI Tools - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--AI-Tools---Fall-2026_JR2016805) | May 07, 2026 |
| Nvidia | Machine Learning Applications and Compiler Engineer, LPX - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Machine-Learning-Applications-and-Compiler-Engineer--LPX---New-College-Grad-2026_JR2016939) | May 06, 2026 |
| Nvidia | Power Methodology and Modeling Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Power-Methodology-and-Modeling-Engineer---New-College-Grad-2026_JR2017486-1) | May 06, 2026 |
| Inceptive | Internship 🇺🇸 | Palo Alto, CA | Intern | [Apply](https://job-boards.greenhouse.io/inceptive/jobs/5103191007) | May 05, 2026 |
| Nvidia | GPU Power Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-Power-Architect---New-College-Grad-2026_JR2017169) | May 02, 2026 |
| Nvidia | ASIC Clocks Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Clocks-Verification-Engineer---New-College-Grad-2026_JR2013336) | May 01, 2026 |
| Nvidia | Hardware Applications Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Hardware-Applications-Engineer---New-College-Grad-2026_JR2016940) | Apr 29, 2026 |
| Airbnb | iOS Software Engineer, Airbnb - New Grad 🇺🇸 | San Francisco, CA, Seattle, WA | New Grad | [Apply](https://careers.airbnb.com/positions/7859317?gh_jid=7859317) | Apr 28, 2026 |
| Notion | Software Engineer, New Grad (AI) 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9) | Apr 27, 2026 |
| Figure AI | Electrical Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | Apr 25, 2026 |
| Figure AI | Electrical Interconnect Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676468006) | Apr 25, 2026 |
| Nvidia | Low Power ASIC Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Low-Power-ASIC-Engineer---New-College-Grad-2026_JR2017001) | Apr 25, 2026 |
| Nvidia | Software Engineering Intern, JAX - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--JAX---Fall-2026_JR2009745) | Apr 25, 2026 |
| Physical Intelligence | Mechatronics Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/0bcf909e-b38b-4276-91a1-e55c4c56a33a) | Apr 24, 2026 |
| Physical Intelligence | Hardware Systems Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/96bc1142-f406-4df3-aaa0-4bcce85f457f) | Apr 24, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/11aedfd6-8321-45af-b71e-492ea7ed3fff) | Apr 24, 2026 |
| Notion | Software Engineer, New Grad 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555) | Apr 23, 2026 |
| Figma | Inside Sales Representative - Early Career (2026) 🇺🇸 | San Francisco, CA • New York, NY | New Grad | [Apply](https://boards.greenhouse.io/figma/jobs/5977327004?gh_jid=5977327004) | Apr 23, 2026 |
| Nvidia | Deep Learning Architect, LLM Inference - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Deep-Learning-Architect--LLM-Inference---New-College-Grad-2026_JR2016950) | Apr 23, 2026 |
| Figma | Data Scientist, Core Data -  PhD (2026) 🇺🇸 | New York, NY • United States<br>San Francisco, CA • New York, NY | PhD | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) | Apr 22, 2026 |
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
| Etched | DFT Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/5f1f5739-3b58-467c-b351-ff183c94d96d) | Apr 13, 2026 |
| Databricks | PhD GenAI Research Scientist Intern 🇺🇸 | San Francisco, California | PhD, Intern | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002) | Apr 09, 2026 |
| Notion | Software Engineer Intern (Fall 2026) 🇺🇸 | San Francisco, California | Intern | [Apply](https://jobs.ashbyhq.com/notion/5b15697c-fa91-4511-9482-c98a6ff29f90) | Apr 06, 2026 |
| Etched | Technical Recruiter (Entry Level) 🇺🇸 | San Jose | New Grad | [Apply](https://jobs.ashbyhq.com/etched/06398761-0950-4e5c-8590-26f485ba5509) | Apr 02, 2026 |
| Figure AI | Hardware Reliability Intern [Summer 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4613067006) | Mar 31, 2026 |
| Sierra | Intern, Agent Development (Fall 2026) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://jobs.ashbyhq.com/sierra/c74d600c-235c-4d42-8546-b178b7adefc2) | Mar 19, 2026 |
| Etched | RTL Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/157ed4f4-6e3b-4ec9-b93f-3e363e92041e) | Feb 07, 2026 |
| Etched | Infrastructure Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/1b073af4-6764-45ca-a22d-40a4823f0877) | Feb 07, 2026 |
| Etched | Firmware Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/699f3ab2-07e4-466c-9d76-3d4a3abb4ebc) | Feb 07, 2026 |
| Etched | Electrical Platform Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/904ddf46-55fc-4a8f-8b49-f32cfe88116a) | Feb 07, 2026 |
| Etched | Supercomputing Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/982a8ee4-5e1e-43c7-a918-6dac285cdddd) | Feb 07, 2026 |
| Etched | DV Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/dacedaca-c4ca-4964-85a7-8df1738005bb) | Feb 07, 2026 |
| Etched | Mech / Thermal Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f05e3218-5ec7-41d1-bc99-bb7014422229) | Feb 07, 2026 |
| Recursion Pharma | Interested in an internship? 🇺🇸 | Remote Opportunity - United States<br>Salt Lake City, Utah | Intern | [Apply](https://job-boards.greenhouse.io/recursionpharmaceuticals/jobs/7540026) | Jan 20, 2026 |
| Etched | Talent Intern - Summer 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/639fe410-56a4-44aa-ac93-8ee7c10c7d75) | Dec 08, 2025 |
| Etched | Inference Intern - Fall 2026 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/6f23713f-5409-45b7-aae8-adb8710cdbc3) | Dec 08, 2025 |
| Ramp | Software Engineer Internship, Android 🇺🇸 | New York, NY (HQ) | Intern | [Apply](https://jobs.ashbyhq.com/ramp/67fadb77-43d8-4449-954b-d4cf2c6d3b8b) | Aug 07, 2025 |

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

