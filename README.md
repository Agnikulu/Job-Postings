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

- **Open positions:** 623
- **All-time tracked:** 774
- **Active companies:** 111
- **Last updated:** `2026-05-27 22:14 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Education** -> Tags from job requirements (e.g. `{PhD, PhD Student, Masters, Bachelors, New Grad, Early Career, Intern}`).
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> When the company posted the role (parsed from each ATS).
   Falls back to when our scraper first observed the URL.

## Open positions

| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| Shield AI | PCB Engineer I (R4974) 🇺🇸 | Dallas, Texas | Early Career | [Apply](https://jobs.lever.co/shieldai/2f182d07-d8bb-4e52-b5ab-d6c4b54cc286) | May 27, 2026 |
| Nvidia | Data Analysis Intern, Applied System Engineering - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Data-Analysis-Intern--Applied-System-Engineering---Fall-2026_JR2018687-1) | May 27, 2026 |
| Nvidia | Software Performance at Scale Intern - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Performance-at-Scale-Intern---Fall-2026_JR2018701) | May 27, 2026 |
| MongoDB | Software Engineer, Data Migration 🇺🇸 | California<br>Oregon<br>Washington | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7523834) | May 27, 2026 |
| SpaceX | Software Engineer, Hardware Test & Automation (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8565155002?gh_jid=8565155002) | May 27, 2026 |
| SpaceX | Hardware Test Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8565090002?gh_jid=8565090002) | May 27, 2026 |
| Nvidia | AI and Systems Software Intern, At Scale AI - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-and-Systems-Software-Intern--At-Scale-AI---Fall-2026_JR2018652) | May 27, 2026 |
| Glean | Software Engineer, University Grad 🇺🇸 | Mountain View, CA | New Grad | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4592324005) | May 27, 2026 |
| Glean | Product Management Intern, Admin Console 🇺🇸 | Mountain View, CA | Intern | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4699772005) | May 27, 2026 |
| Boston Dynamics | Raytheon Full-time RF/Microwave Antenna Electrical Engineer I (Onsite) 🇺🇸 | El Segundo, CA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4419831048) | May 27, 2026 |
| Amazon Web Services (AWS) | Data Center Engineering Operations Technician Internship 🇺🇸 | Herndon, VA | Intern | [Apply](https://www.linkedin.com/jobs/view/4390366476) | May 27, 2026 |
| Amazon Web Services (AWS) | C/C++ Hardware / Software Co-Design SDE, Machine Learning Acceleration Systems 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4410903491) | May 27, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Carle Place, NY | - | [Apply](https://www.linkedin.com/jobs/view/4419840869) | May 27, 2026 |
| Microsoft | AI for Science Internship - Machine Learning Intern 🇺🇸 | Berlin, BE, DE | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556869781) | May 27, 2026 |
| Boston Dynamics | Raytheon Full-time Digital Design Hardware Electrical Engineer I (Onsite) 🇺🇸 | El Segundo, CA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4419827546) | May 27, 2026 |
| Boston Dynamics | 2026 Radar Systems Engineer I– Onsite 🇺🇸 | El Segundo, CA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4419816852) | May 27, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Arlington, VA | - | [Apply](https://www.linkedin.com/jobs/view/4419846777) | May 27, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, NY | - | [Apply](https://www.linkedin.com/jobs/view/4419835928) | May 27, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4419844805) | May 27, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, United States | - | [Apply](https://www.linkedin.com/jobs/view/4419852156) | May 27, 2026 |
| Boston Dynamics | Raytheon Full-time Radio Frequency (RF) Production Support Electrical Engineer I (Onsite) 🇺🇸 | El Segundo, CA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4419816848) | May 27, 2026 |
| Boston Dynamics | Raytheon Full Time 2026 - RF Design Engineer I 🇺🇸 | Tucson, AZ | Early Career | [Apply](https://www.linkedin.com/jobs/view/4419816849) | May 27, 2026 |
| Tesla | Industrial Engineer, Service Distribution 🇺🇸 | San Bernardino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4419557756) | May 27, 2026 |
| Tesla | Mechanical Design Engineer, Chassis 🇺🇸 | Palo Alto, CA | - | [Apply](https://www.linkedin.com/jobs/view/4419556787) | May 27, 2026 |
| Amazon Web Services (AWS) | Machine Learning Engineer, AWS Applied AI Solution 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4419546940) | May 27, 2026 |
| Nvidia | Circuit Design Engineer - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer---New-College-Grad-2026_JR2018635) | May 27, 2026 |
| Meta | Research Scientist Intern, Robotic Control Policy (PhD) 🇺🇸 | Burlingame, CA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4350245449) | May 27, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall Intern 🇺🇸 | Seattle, WA | Intern | [Apply](https://www.linkedin.com/jobs/view/4370383843) | May 27, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall Intern 🇺🇸 | Cupertino, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4370389530) | May 27, 2026 |
| Stripe | Android Engineer, Terminal Global Payments 🇺🇸 | San Francisco, CA, Seattle, WA | - | [Apply](https://stripe.com/jobs/search?gh_jid=7778627) | May 27, 2026 |
| SpaceX | Software Engineer, Satellite Operations (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8382088002?gh_jid=8382088002) | May 27, 2026 |
| SpaceX | Software Engineer, HITL - Top Secret Clearance 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8397596002?gh_jid=8397596002) | May 27, 2026 |
| SpaceX | Software Engineer, Tracking (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8414648002?gh_jid=8414648002) | May 27, 2026 |
| SpaceX | Software Engineer, C++ - Top Secret Clearance 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8377056002?gh_jid=8377056002) | May 27, 2026 |
| SpaceX | Software Engineer, Data - Top Secret Clearance 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8397673002?gh_jid=8397673002) | May 27, 2026 |
| SpaceX | GNC Software Engineer - Top Secret Clearance 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8560746002?gh_jid=8560746002) | May 27, 2026 |
| Nvidia | Synthetic Data Generation and User Simulation PhD Research Intern — Fall 2026 🇺🇸 | US, CA, Remote | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Data-Generation-and-User-Simulation-Research-Intern---Fall-2026_JR2018317) | May 27, 2026 |
| DoorDash | Machine Learning Engineer, Marketplace Optimization 🇺🇸 | San Francisco, CA<br>Sunnyvale, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7580407) | May 27, 2026 |
| Boston Dynamics | Junior Network Administrator, McKinney, TX Onsite 🇺🇸 | McKinney, TX | - | [Apply](https://www.linkedin.com/jobs/view/4409785431) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Boston, Massachusetts, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086960007?gh_jid=5086960007) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5002801007?gh_jid=5002801007) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Seattle, Washington, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086958007?gh_jid=5086958007) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086962007?gh_jid=5086962007) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Atlanta, Georgia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086964007?gh_jid=5086964007) | May 27, 2026 |
| Anduril | Security Software Engineer - Endpoint Security 🇺🇸 | Ashville, Ohio, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086967007?gh_jid=5086967007) | May 27, 2026 |
| Anduril | Security Software Engineer 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5134986007?gh_jid=5134986007) | May 27, 2026 |
| Anduril | Electrical Engineer, Maneuver Dominance 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4687724007?gh_jid=4687724007) | May 27, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Atlanta, Georgia, United States<br>Broomfield, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States<br>Seattle, Washington, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | May 27, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall Intern 🇺🇸 | Herndon, VA | Intern | [Apply](https://www.linkedin.com/jobs/view/4370387705) | May 27, 2026 |
| SpaceX | Electrical Engineer, Launch Pad (Starship) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8564730002?gh_jid=8564730002) | May 26, 2026 |
| Anduril | Flight Test Engineer, Ghost 🇺🇸 | San Clemente, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5146974007?gh_jid=5146974007) | May 26, 2026 |
| Anduril | DevOps Engineer 🇺🇸 | Reston, Virginia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5146861007?gh_jid=5146861007) | May 26, 2026 |
| Uber | Data Center Engineer, Electrical 🇺🇸 | San Francisco, California, United States | - | [Apply](https://www.uber.com/careers/list/159160) | May 26, 2026 |
| Uber | Data Center Engineer, Structured Cabling & Physical Network 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/159171) | May 26, 2026 |
| Nvidia | Compiler Engineer, Compute Front-End - New College Grad 2026 🇺🇸 | 3 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Senior-Compiler-Engineer---Compute-Front-End--New-College-Grad-2026_JR2013488) | May 26, 2026 |
| SpaceX | Fire Protection Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552269002?gh_jid=8552269002) | May 26, 2026 |
| Roblox | Software Engineer, Monetization Products 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7947219?gh_jid=7947219) | May 26, 2026 |
| Lambda Labs | Data Center Electrical Modeling Intern - 2026 🇺🇸 | San Jose Office (Zanker) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/9c964b0d-984b-4220-a1ee-ea237a4f14ea) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS 🇺🇸 | New York, United States | - | [Apply](https://www.linkedin.com/jobs/view/4410261539) | May 26, 2026 |
| Adobe | Machine Learning Engineer 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Machine-Learning-Engineer_R169199-1) | May 26, 2026 |
| Tesla | Software Engineer, Robotaxi Experience, Vehicle Software 🇺🇸 | Palo Alto, CA | - | [Apply](https://www.linkedin.com/jobs/view/4419115395) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, United States | - | [Apply](https://www.linkedin.com/jobs/view/4410556994) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4410557977) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Cupertino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4410562840) | May 26, 2026 |
| xAI | Software Engineer - Data 🇺🇸 | Palo Alto, CA | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5124616007) | May 26, 2026 |
| xAI | Member of Technical Staff 🇺🇸 | Memphis, TN | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5044403007) | May 26, 2026 |
| xAI | Data Engineer 🇺🇸 | Palo Alto, CA | - | [Apply](https://job-boards.greenhouse.io/xai/jobs/5120884007) | May 26, 2026 |
| Uber | 2026 Fall Software Engineering Internship, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | BS Student, Intern | [Apply](https://www.uber.com/careers/list/159161) | May 26, 2026 |
| SpaceX | Launch Engineer, Fluid Systems (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8504994002?gh_jid=8504994002) | May 26, 2026 |
| Scale AI | Machine Learning Research Engineer, Agents - Enterprise GenAI 🇺🇸 | San Francisco, CA<br>New York, NY | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4625344005) | May 26, 2026 |
| Robinhood | Support Engineer 🇺🇸 | Westlake, TX | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/7847491?t=gh_src=&gh_jid=7847491) | May 26, 2026 |
| DoorDash | Software Engineer, Backend (All Teams) 🇺🇸 | Los Angeles, CA<br>Sunnyvale, CA<br>San Francisco, CA<br>New York, NY<br>Seattle, WA<br>Ann Arbor, MI | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/5630445) | May 26, 2026 |
| DoorDash | Software Engineer, Infrastructure - Autonomy & Robotics 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/6367350) | May 26, 2026 |
| DoorDash | Systems Engineer 🇺🇸 | San Francisco, CA<br>Oakland, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7350485) | May 26, 2026 |
| DoorDash | Mechanical Design Engineer — UAV Wire Harness 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7927350) | May 26, 2026 |
| DoorDash | Electrical Distribution Engineer (Harness / EDS) 🇺🇸 | Oakland, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7779237) | May 26, 2026 |
| DoorDash | Composite & Prototype Engineering Technician 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7650045) | May 26, 2026 |
| DoorDash | AI Research Fellowship, (Summer and Fall 2026) 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7848317) | May 26, 2026 |
| Boston Dynamics | 2026 Fulltime-Raytheon Electrical Engineer I (Onsite) 🇺🇸 | McKinney, TX | Early Career | [Apply](https://www.linkedin.com/jobs/view/4410554206) | May 26, 2026 |
| Boston Dynamics | Raytheon Full Time 2026 - Semiconductor Foundry Engineer I 🇺🇸 | Andover, MA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4401707304) | May 26, 2026 |
| Anduril | Robotics Software Engineer, Verification & Validation 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5083521007?gh_jid=5083521007) | May 26, 2026 |
| Anduril | Robotics Software Engineer, Sensor Integration 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5096506007?gh_jid=5096506007) | May 26, 2026 |
| Anduril | Robotics Software Engineer, Behaviors 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5121816007?gh_jid=5121816007) | May 26, 2026 |
| Anduril | Mechanical Engineer, Maneuver Dominance 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5116599007?gh_jid=5116599007) | May 26, 2026 |
| Anduril | Maritime Operations Engineer - Mission Autonomy 🇺🇸 | Channel Islands, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5069872007?gh_jid=5069872007) | May 26, 2026 |
| Anduril | GSOC Jr Operator 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5103111007?gh_jid=5103111007) | May 26, 2026 |
| Anduril | Early Career Manufacturing Engineer 🇺🇸 | Santa Ana, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5009798007?gh_jid=5009798007) | May 26, 2026 |
| Amazon Web Services (AWS) | Front-End Engineer, EC2 Core Platform 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4401512967) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Carle Place, NY | - | [Apply](https://www.linkedin.com/jobs/view/4410576155) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Bellevue, WA | - | [Apply](https://www.linkedin.com/jobs/view/4410562839) | May 26, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Brooklyn, NY | - | [Apply](https://www.linkedin.com/jobs/view/4410566783) | May 26, 2026 |
| Applied Intuition | Defense Product Software Engineer (C++) 🇺🇸 | Ann Arbor, Michigan, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4683342005?gh_jid=4683342005) | May 25, 2026 |
| SpaceX | Aerodynamics Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558715002?gh_jid=8558715002) | May 25, 2026 |
| Tesla | Mechanical Design Engineer, Chassis 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4418906630) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer in Test 🇺🇸 | California - Pleasanton | - | [Apply](https://jobs.lever.co/veeva/452d7860-6d5f-45e0-bc00-6a2e8852698d) | May 25, 2026 |
| Veeva Systems | Associate Quality Engineer 🇺🇸 | California - Pleasanton | - | [Apply](https://jobs.lever.co/veeva/79e78774-d044-4a48-9130-d8e18e2d7876) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer in Test 🇺🇸 | Massachusetts - Boston | - | [Apply](https://jobs.lever.co/veeva/8683a486-a11b-44be-8824-d3afdaa37b2d) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer - Seeking 2025 & 2026 Grads 🇺🇸 | California - Pleasanton | New Grad | [Apply](https://jobs.lever.co/veeva/8fe22df0-02b4-453d-919c-c8998cf913f6) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer - Seeking 2025 & 2026 Grads 🇺🇸 | Ohio - Columbus | New Grad | [Apply](https://jobs.lever.co/veeva/907dccc7-0052-41e9-920b-28e5ba6aaba9) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer - Seeking 2025 & 2026 Grads 🇺🇸 | Missouri - Kansas City | New Grad | [Apply](https://jobs.lever.co/veeva/93aa70b0-3f70-449a-ab56-ffa7df61a488) | May 25, 2026 |
| Veeva Systems | Associate Quality Engineer 🇺🇸 | Massachusetts - Boston | - | [Apply](https://jobs.lever.co/veeva/aca8cd98-e800-45b9-94bc-cb2c3077b49d) | May 25, 2026 |
| Veeva Systems | Associate Quality Engineer - Infrastructure 🇺🇸 | Massachusetts - Boston | - | [Apply](https://jobs.lever.co/veeva/c45f9436-6174-4b16-9459-3bebb588b474) | May 25, 2026 |
| Veeva Systems | Associate Software Engineer - Seeking 2025 & 2026 Grads 🇺🇸 | North Carolina - Raleigh | New Grad | [Apply](https://jobs.lever.co/veeva/e31a2a3c-a508-459c-9f77-a2692a95f233) | May 25, 2026 |
| Spotify | Machine Learning Engineer I, Personalization , Minesweeper 🇺🇸 | New York, NY | Early Career | [Apply](https://jobs.lever.co/spotify/fd79c3f5-1b2c-47c0-a3c6-4972b559e1c1) | May 25, 2026 |
| Snap | Embedded Software Engineer, Level 3 🇺🇸 | San Diego, CA | - | [Apply](https://www.linkedin.com/jobs/view/4369994145) | May 25, 2026 |
| Shield AI | Power Electronics - Electrical Engineer I 🇺🇸 | Dallas, Texas | Early Career | [Apply](https://jobs.lever.co/shieldai/0af53b2b-e1ba-4e73-9e94-a4a689cabab9) | May 25, 2026 |
| Shield AI | Power Electronics - Thermal Engineer I (R4842) 🇺🇸 | Dallas, Texas | Early Career | [Apply](https://jobs.lever.co/shieldai/f6bbec19-f1c6-44ce-9af5-132b25b6e83a) | May 25, 2026 |
| Shield AI | Electrical Engineer I (SD) 🇺🇸 | San Diego, California | Early Career | [Apply](https://jobs.lever.co/shieldai/1b229cdc-9a0b-4704-b39b-b3b4c6e3fa89) | May 25, 2026 |
| Shield AI | Engineer I, Electromechanical (R4951) 🇺🇸 | United States | Early Career | [Apply](https://jobs.lever.co/shieldai/37f1de6d-d17b-437b-af16-d8ce8d7d0782) | May 25, 2026 |
| Shield AI | Electrical Engineer I (BOS) (R5046) 🇺🇸 | Boston, MA | Early Career | [Apply](https://jobs.lever.co/shieldai/37fa20c1-57dc-4aa1-9515-ecc87f22f31b) | May 25, 2026 |
| Shield AI | Associate Engineer, Manufacturing (R4637) 🇺🇸 | Dallas, Texas | - | [Apply](https://jobs.lever.co/shieldai/78842190-deba-4864-9ef9-272009cb15a4) | May 25, 2026 |
| Shield AI | Electrical Engineering Spring Co-op (January 2027) (R4475) 🇺🇸 | Dallas, Texas | Intern | [Apply](https://jobs.lever.co/shieldai/87d982f2-8b2b-4c73-9a19-71e461c7b724) | May 25, 2026 |
| Shield AI | Electrical Engineer I (TX) 🇺🇸 | Dallas, Texas | Early Career | [Apply](https://jobs.lever.co/shieldai/c9321f8a-b367-4dcb-9308-bd64ae6bac1d) | May 25, 2026 |
| Shield AI | EWIS Harness Design - Engineer I (R5018) 🇺🇸 | Dallas, Texas | Early Career | [Apply](https://jobs.lever.co/shieldai/dc29adac-fe50-41c1-a466-71b7700626ba) | May 25, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | Washington, D.C. | Intern | [Apply](https://jobs.lever.co/palantir/5c4c65c5-77da-4d36-856c-4ade87631019) | May 25, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/5c7bb70c-83ea-43e7-8055-0c8f319f4333) | May 25, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - Commercial 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/e6789b17-62fb-4226-a079-f8c17ff19e2d) | May 25, 2026 |
| Palantir | Forward Deployed Software Engineer - Warp Speed 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/13f99633-43b5-4459-8e84-25073f257c18) | May 25, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/315f695d-04d1-4a9a-848e-cb2bec7a997e) | May 25, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - France 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/ac0dc094-2480-43c2-8495-26ade227ff4f) | May 25, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - Poland 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/d582cd84-14fd-4aa3-b413-15982d286bd9) | May 25, 2026 |
| Palantir | Deployment Strategist, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/a49d4181-a289-435a-b581-7f5af0497c8e) | May 25, 2026 |
| Palantir | Forward Deployed Software Engineer 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0) | May 25, 2026 |
| Luma AI | Software Engineer - Product 🇺🇸 | SF Bay Area, CA | - | [Apply](https://jobs.gem.com/lumalabs-ai/am9icG9zdDodtsh6pWUJjQgE8lXoaEJi) | May 25, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4345165721) | May 25, 2026 |
| 1X Technologies | AI Residency 🇺🇸 | San Carlos, United States | - | [Apply](https://1x.recruitee.com/o/ai-resident) | May 25, 2026 |
| 1X Technologies | Materials and Process Innovation Engineer 🇺🇸 | San Carlos, United States | PhD | [Apply](https://1x.recruitee.com/o/materials-and-process-innovation-engineer) | May 25, 2026 |
| 1X Technologies | Mechanical Engineer - Hand Motors and Actuators 🇺🇸 | San Carlos, United States | - | [Apply](https://1x.recruitee.com/o/mechanical-engineer-hand-motors-and-actuators) | May 25, 2026 |
| Tesla | Industrial Engineer, Outbound Flow & Optimization 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4418656210) | May 24, 2026 |
| Nvidia | System Software Engineer - Performance 🇺🇸 | 6 Locations | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/System-Software-Engineer---Performance_JR2018651) | May 24, 2026 |
| Tesla | Manufacturing Engineer, Material Flow Simulation 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4418663151) | May 24, 2026 |
| Tesla | Associate Civil Engineer 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4418645220) | May 24, 2026 |
| Tesla | Industrial Engineer, People & Site Flow Design 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4418644227) | May 24, 2026 |
| Microsoft | Security Research Intern - AI Focus 🇺🇸 | Herzliya, Tel Aviv District, IL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556862170) | May 24, 2026 |
| Tesla | Associate Environmental Engineer 🇺🇸 | Sparks, NV | - | [Apply](https://www.linkedin.com/jobs/view/4418456588) | May 23, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Cupertino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4345225752) | May 23, 2026 |
| Tesla | Associate Industrial Engineer 🇺🇸 | Lathrop, CA | - | [Apply](https://www.linkedin.com/jobs/view/4418445871) | May 23, 2026 |
| CoreWeave | Software Engineer, Observability 🇺🇸 | New York, NY / Sunnyvale, CA | - | [Apply](https://coreweave.com/careers/job?4587675006&board=coreweave&gh_jid=4587675006) | May 23, 2026 |
| CoreWeave | Software Engineer, Inference AI/ML 🇺🇸 | Sunnyvale, CA / Bellevue, WA | - | [Apply](https://coreweave.com/careers/job?4609928006&board=coreweave&gh_jid=4609928006) | May 23, 2026 |
| CoreWeave | Operations Engineer, HPC Networking 🇺🇸 | Livingston, NJ / New York, NY / Sunnyvale, CA / Bellevue, WA | - | [Apply](https://coreweave.com/careers/job?4673462006&board=coreweave&gh_jid=4673462006) | May 23, 2026 |
| Boston Dynamics | Coyote Test Engineer 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4409498694) | May 23, 2026 |
| Amazon Web Services (AWS) | Software Engineer- AI/ML, AWS Neuron 🇺🇸 | Cupertino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4316841545) | May 23, 2026 |
| Amazon Web Services (AWS) | Software Dev Engineer, Amazon Connect 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4418453055) | May 23, 2026 |
| Zillow | Machine Learning Engineer, Zillow Shopping AI 🇺🇸 | United States | - | [Apply](https://www.linkedin.com/jobs/view/4341008321) | May 22, 2026 |
| SpaceX | Software Engineer (Thermal & Fluid Analysis) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8562437002?gh_jid=8562437002) | May 22, 2026 |
| SpaceX | Software Engineer, Flight Software (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8562284002?gh_jid=8562284002) | May 22, 2026 |
| SpaceX | Software Engineer, Flight Software (Starship) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8562450002?gh_jid=8562450002) | May 22, 2026 |
| SpaceX | Propulsion Engineer, Thermal & Fluid Analysis (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8562385002?gh_jid=8562385002) | May 22, 2026 |
| SpaceX | Hardware Reliability Engineer, PCB Manufacturing (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8487667002?gh_jid=8487667002) | May 22, 2026 |
| Robinhood | Software Engineer, Backend 🇺🇸 | Menlo Park, CA | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/7263592?t=gh_src=&gh_jid=7263592) | May 22, 2026 |
| Robinhood | Android Engineer 🇺🇸 | New York, NY | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/6669758?t=gh_src=&gh_jid=6669758) | May 22, 2026 |
| Robinhood | Android Engineer 🇺🇸 | Menlo Park, CA | - | [Apply](https://boards.greenhouse.io/robinhood/jobs/7776330?t=gh_src=&gh_jid=7776330) | May 22, 2026 |
| Nvidia | PhD Software Engineering Intern, Decision Intelligence - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Software-Engineering-Intern--Decision-Intelligence---Fall-2026_JR2017522) | May 22, 2026 |
| Nvidia | System Software Engineer - GPU 🇺🇸 | US, CA, Santa Clara | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/System-Software-Engineer---GPU_JR2013295) | May 22, 2026 |
| Nvidia | Verification and Validation Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Verification-and-Validation-Engineer---New-College-Grad-2026_JR2018584-1) | May 22, 2026 |
| Boston Dynamics | 2026 Fulltime- RF Electrical Engineer I- Onsite 🇺🇸 | Marlborough, MA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4418079685) | May 22, 2026 |
| Boston Dynamics | 2026 Raytheon Full Time Embedded Software Engineer I 🇺🇸 | Indianapolis, IN | Early Career | [Apply](https://www.linkedin.com/jobs/view/4418090416) | May 22, 2026 |
| Boston Dynamics | Electrical Engineer I (Onsite) 🇺🇸 | Marlborough, MA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4399844979) | May 22, 2026 |
| Boston Dynamics | Mechanical Engineer I (Onsite) 🇺🇸 | Tewksbury, MA | Early Career | [Apply](https://www.linkedin.com/jobs/view/4418084525) | May 22, 2026 |
| Tesla | Internship, Data Analyst, Energy (Fall 2026) 🇺🇸 | Fremont, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4416576546) | May 21, 2026 |
| Uber | Application Developer L3 – Identity & Access Management (IAM) 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/159177) | May 21, 2026 |
| Tesla | Internship, Electrical Engineer, Energy Engineering (Fall 2026) 🇺🇸 | Palo Alto, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4416576548) | May 21, 2026 |
| Tesla | Internship, Software Engineer, IT Apps (Fall 2026) 🇺🇸 | Fremont, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4416580546) | May 21, 2026 |
| Tesla | Internship, Process Engineer, Energy (Fall 2026) 🇺🇸 | Austin, TX | Intern | [Apply](https://www.linkedin.com/jobs/view/4416588529) | May 21, 2026 |
| Stripe | Software Engineer 🇺🇸 | New York, NY | - | [Apply](https://stripe.com/jobs/search?gh_jid=7926587) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495882002?gh_jid=8495882002) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558857002?gh_jid=8558857002) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558858002?gh_jid=8558858002) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Palo Alto, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558859002?gh_jid=8558859002) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8560537002?gh_jid=8560537002) | May 21, 2026 |
| SpaceX | Software Engineer (Platform Team) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8560546002?gh_jid=8560546002) | May 21, 2026 |
| SpaceX | Software Engineer, Data (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8476427002?gh_jid=8476427002) | May 21, 2026 |
| SpaceX | Software Engineer, Flight Software (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8551932002?gh_jid=8551932002) | May 21, 2026 |
| SpaceX | Software Engineer, Embedded Software (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552752002?gh_jid=8552752002) | May 21, 2026 |
| SpaceX | Process Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8561097002?gh_jid=8561097002) | May 21, 2026 |
| SpaceX | Full Stack Software Engineer, Data (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8540435002?gh_jid=8540435002) | May 21, 2026 |
| SpaceX | Facilities Engineer, Launch Infrastructure 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8491778002?gh_jid=8491778002) | May 21, 2026 |
| SpaceX | Facilities Engineer, Mechanical (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8540341002?gh_jid=8540341002) | May 21, 2026 |
| SpaceX | Design Verification Engineer (Silicon Engineering) 🇺🇸 | Austin, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8559067002?gh_jid=8559067002) | May 21, 2026 |
| Skydio | Middleware Software Engineer Intern - Fall 2026 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/7d9dbb60-4ca1-4ba8-8bae-5ebfded4a915) | May 21, 2026 |
| Point72 | Summer 2027 Quantitative Developer Internship 🇺🇸 | New York | Bachelors, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297613002?gh_jid=7297613002) | May 21, 2026 |
| Point72 | Summer 2027 Quantitative Research Internship 🇺🇸 | New York | PhD Student, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297642002?gh_jid=7297642002) | May 21, 2026 |
| Point72 | Quantitative Researcher - Machine Learning 🇺🇸 | New York | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/7297513002?gh_jid=7297513002) | May 21, 2026 |
| Point72 | Quantitative Analyst / Software Developer 🇺🇸 | New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/7297622002?gh_jid=7297622002) | May 21, 2026 |
| Point72 | Quantitative Researcher - Systematic Credit 🇺🇸 | Chicago, New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/7297625002?gh_jid=7297625002) | May 21, 2026 |
| Point72 | Quantitative Software Developer Intern 🇺🇸 | New York, London, or Paris | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297666002?gh_jid=7297666002) | May 21, 2026 |
| Point72 | Quantitative Research Intern 🇺🇸 | New York, Seattle | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297667002?gh_jid=7297667002) | May 21, 2026 |
| Point72 | Machine Learning Researcher - Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7302611002?gh_jid=7302611002) | May 21, 2026 |
| Point72 | Quantitative Researcher Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7586061002?gh_jid=7586061002) | May 21, 2026 |
| Point72 | Quantitative Developer Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7609197002?gh_jid=7609197002) | May 21, 2026 |
| Point72 | Quantitative Software Developer 🇺🇸 | New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/7825863002?gh_jid=7825863002) | May 21, 2026 |
| Point72 | Quantitative Research Intern (NLP) 🇺🇸 | New York | PhD Student, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/8018862002?gh_jid=8018862002) | May 21, 2026 |
| Point72 | Machine Learning Engineer 🇺🇸 | New York | PhD Student | [Apply](https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002) | May 21, 2026 |
| Point72 | Data Engineer 🇺🇸 | New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002) | May 21, 2026 |
| Point72 | Data Scientist 🇺🇸 | Chicago, New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/8372544002?gh_jid=8372544002) | May 21, 2026 |
| Nvidia | ASIC Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Design-Engineer---New-College-Grad-2026_JR2017581) | May 21, 2026 |
| Nvidia | Quantum Error Correction Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Error-Correction-Research-Scientist-Intern---Fall-2026_JR2018628) | May 21, 2026 |
| MongoDB | Software Engineer, Code Generation 🇺🇸 | California<br>Colorado<br>Montana<br>Nevada<br>New Mexico<br>Oregon<br>Utah<br>Washington | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7311666) | May 21, 2026 |
| Lambda Labs | Data Center Mechanical Engineering Intern - 2026 🇺🇸 | San Jose Office (Zanker) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/62fcad14-b225-427c-ad86-6bb52377a997) | May 21, 2026 |
| Boston Dynamics | Full Time Raytheon 2026 - Power & Digital Electrical Engineer I 🇺🇸 | Fort Wayne, IN | Early Career | [Apply](https://www.linkedin.com/jobs/view/4399215612) | May 21, 2026 |
| Applied Intuition | Software Engineer - Systems Engineering AI Tooling 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4670757005?gh_jid=4670757005) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Seattle, Washington, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5002792007?gh_jid=5002792007) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5002794007?gh_jid=5002794007) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Boston, Massachusetts, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086896007?gh_jid=5086896007) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Atlanta, Georgia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086919007?gh_jid=5086919007) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086925007?gh_jid=5086925007) | May 21, 2026 |
| Anduril | Security Software Engineer - Crypto Services 🇺🇸 | Ashville, Ohio, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5086936007?gh_jid=5086936007) | May 21, 2026 |
| Anduril | Mission Operations Engineer, Connected Warfare (Active Clearance) 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4159543007?gh_jid=4159543007) | May 21, 2026 |
| Anduril | Mission Operations Engineer, Connected Warfare (Active Clearance) 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4182443007?gh_jid=4182443007) | May 21, 2026 |
| Anduril | Mission Operations Engineer 🇺🇸 | Atlanta, Georgia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5100663007?gh_jid=5100663007) | May 21, 2026 |
| Anduril | Mission Operations Engineer 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5115435007?gh_jid=5115435007) | May 21, 2026 |
| Anduril | Mechanical Engineer, Manufacturing Test 🇺🇸 | Costa Mesa, California, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4988675007?gh_jid=4988675007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer 🇺🇸 | Costa Mesa, California, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4644883007?gh_jid=4644883007) | May 21, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080387007?gh_jid=5080387007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080535007?gh_jid=5080535007) | May 21, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5111318007?gh_jid=5111318007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer, Intelligence Systems (2nd Shift) 🇺🇸 | Santa Ana, California, United States | MS Student | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5135616007?gh_jid=5135616007) | May 21, 2026 |
| Anduril | GNC Engineer, Space 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870847007?gh_jid=4870847007) | May 21, 2026 |
| Anduril | GNC Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870871007?gh_jid=4870871007) | May 21, 2026 |
| Anduril | Industrial Engineer, Production Controls & Simulation 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5108276007?gh_jid=5108276007) | May 21, 2026 |
| Anduril | Flight Software Engineer, Embedded C/C++, Air Dominance & Strike 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4164476007?gh_jid=4164476007) | May 21, 2026 |
| Anduril | Flight Software Engineer, Embedded C/C++, Air Dominance & Strike - Advanced Effects 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5035788007?gh_jid=5035788007) | May 21, 2026 |
| Anduril | Early Career Mechanical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802167007?gh_jid=4802167007) | May 21, 2026 |
| Anduril | Early Career Electrical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802172007?gh_jid=4802172007) | May 21, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016001007?gh_jid=5016001007) | May 21, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016334007?gh_jid=5016334007) | May 21, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall 2026 🇺🇸 | Seattle, WA | Intern | [Apply](https://www.linkedin.com/jobs/view/4340731344) | May 21, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall 2026 🇺🇸 | Cupertino, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4340741422) | May 21, 2026 |
| Meta | Fundamental AI Researcher - FAIR 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4403726002) | May 20, 2026 |
| Meta | Hardware Electrical Engineer 🇺🇸 | Sunnyvale, CA | - | [Apply](https://www.linkedin.com/jobs/view/4404145493) | May 20, 2026 |
| Meta | Fundamental AI Researcher - FAIR 🇺🇸 | Menlo Park, CA | - | [Apply](https://www.linkedin.com/jobs/view/4403288993) | May 20, 2026 |
| Boston Dynamics | 2026 Fulltime- Reliability Engineering I- Onsite 🇺🇸 | Tewksbury, MA | - | [Apply](https://www.linkedin.com/jobs/view/4415347363) | May 20, 2026 |
| AMD | L3 Application Support Engineer 🇺🇸 | Austin, TX | - | [Apply](https://www.linkedin.com/jobs/view/4405873854) | May 20, 2026 |
| Amazon Web Services (AWS) | (Fall 2026) Annapurna Labs at AWS Internship (US) - Machine Learning Systems & Silicon Innovation 🇺🇸 | Cupertino, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4402899470) | May 20, 2026 |
| Meta | Hardware Test & Automation Engineer 🇺🇸 | Redmond, WA | - | [Apply](https://www.linkedin.com/jobs/view/4403760434) | May 20, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Arlington, VA | - | [Apply](https://www.linkedin.com/jobs/view/4415531120) | May 20, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, United States | - | [Apply](https://www.linkedin.com/jobs/view/4415533071) | May 20, 2026 |
| Zillow | AI Applied Scientist - PhD Intern, Foundational AQ & EQ 🇺🇸 | United States | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4305147733) | May 20, 2026 |
| Zillow | Machine Learning Engineer, Agentic AI 🇺🇸 | United States | - | [Apply](https://www.linkedin.com/jobs/view/4385528913) | May 20, 2026 |
| Stripe | PhD Machine Learning Engineer, Intern 🇺🇸 | San Francisco, New York City, Seattle | PhD, New Grad, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7216664) | May 20, 2026 |
| Stripe | PhD Data Scientist, Intern 🇺🇸 | San Francisco, New York City, Seattle, Chicago | PhD, New Grad, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7874965) | May 20, 2026 |
| SpaceX | Software Engineer (Starshield) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8501199002?gh_jid=8501199002) | May 20, 2026 |
| SpaceX | Software Engineer (Starshield) 🇺🇸 | Washington, DC | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558282002?gh_jid=8558282002) | May 20, 2026 |
| SpaceX | SMT Process Engineer 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558345002?gh_jid=8558345002) | May 20, 2026 |
| SpaceX | Software Engineer, Engineering Simulation & Automation (Vehicle Engineering) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8559054002?gh_jid=8559054002) | May 20, 2026 |
| SpaceX | RF Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8517637002?gh_jid=8517637002) | May 20, 2026 |
| SpaceX | OS/Platform Software Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552882002?gh_jid=8552882002) | May 20, 2026 |
| SpaceX | Hardware Development Engineer, PCBA Manufacturing (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8558344002?gh_jid=8558344002) | May 20, 2026 |
| SpaceX | Flight Software Engineer (Starlink Mobile) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8556909002?gh_jid=8556909002) | May 20, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform  (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552893002?gh_jid=8552893002) | May 20, 2026 |
| SpaceX | AI Software Engineer (Vehicle Engineering) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8559015002?gh_jid=8559015002) | May 20, 2026 |
| Snap | Security Engineer, Level 3 🇺🇸 | Palo Alto, CA | - | [Apply](https://www.linkedin.com/jobs/view/4377053302) | May 20, 2026 |
| Roblox | Software Engineer, User Sharing 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7767204?gh_jid=7767204) | May 20, 2026 |
| Roblox | Software Engineer, Creator Translation 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7786397?gh_jid=7786397) | May 20, 2026 |
| Roblox | Software Engineer, Communication Safety 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7888723?gh_jid=7888723) | May 20, 2026 |
| Roblox | Software Engineer, Core Services 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7943533?gh_jid=7943533) | May 20, 2026 |
| Roblox | [2026] Applied Scientist - PhD Intern 🇺🇸 | San Mateo, CA, United States | PhD, Intern | [Apply](https://careers.roblox.com/jobs/7142298?gh_jid=7142298) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Multimodal AI, Computer Vision and Graphics - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7323437?gh_jid=7323437) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Recommendation Systems - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7350081?gh_jid=7350081) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, AI Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7403998?gh_jid=7403998) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer,  Engine Optimization - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7421746?gh_jid=7421746) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Social - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7463634?gh_jid=7463634) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Account Identity - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7473686?gh_jid=7473686) | May 20, 2026 |
| Roblox | [2026] Software Engineer, Game Developer 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7557909?gh_jid=7557909) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Foundation AI - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD Student, New Grad | [Apply](https://careers.roblox.com/jobs/7577436?gh_jid=7577436) | May 20, 2026 |
| MongoDB | Software Engineer, Developer Productivity 🇺🇸 | New York City | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7851388) | May 20, 2026 |
| Microsoft | Data Center Technicians Intern 🇺🇸 | Middenmeer, NH, NL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867635) | May 20, 2026 |
| Lambda Labs | Field Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Second St) | MS Student, Intern | [Apply](https://jobs.ashbyhq.com/lambda/e0e555b9-a009-43c4-bd64-57e74cfd67f1) | May 20, 2026 |
| Google | Network Operations Residency Program, University Graduate, August 2026 Start 🇺🇸 | Atlanta, GA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/118981017938600646) | May 20, 2026 |
| Google | Engineering Analyst, Trust and Safety Payments 🇺🇸 | Sunnyvale, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/143948727982138054) | May 20, 2026 |
| Google | Silicon Design Verification Engineer 🇺🇸 | Mountain View, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/86602986070909638) | May 20, 2026 |
| Boston Dynamics | Raytheon Full Time 2026 - Production Support Electrical Engineer I 🇺🇸 | Plano, TX | Early Career | [Apply](https://www.linkedin.com/jobs/view/4405643119) | May 20, 2026 |
| Boston Dynamics | Program Supplier Quality Engineer 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4386722727) | May 20, 2026 |
| Amazon Web Services (AWS) | (Fall 2026) Annapurna Labs at AWS Internship (US) - Machine Learning Systems & Silicon Innovation 🇺🇸 | Austin, TX | Intern | [Apply](https://www.linkedin.com/jobs/view/4402890706) | May 20, 2026 |
| AMD | L3 Application Support Engineer 🇺🇸 | North Carolina, United States | - | [Apply](https://www.linkedin.com/jobs/view/4405884201) | May 20, 2026 |
| Amazon Web Services (AWS) | Network Development Engineer Intern - Fall 2026 🇺🇸 | Herndon, VA | Intern | [Apply](https://www.linkedin.com/jobs/view/4340331747) | May 20, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | East Palo Alto, CA | - | [Apply](https://www.linkedin.com/jobs/view/4415863691) | May 20, 2026 |
| SpaceX | Software Engineer, CDN  (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8448505002?gh_jid=8448505002) | May 19, 2026 |
| SpaceX | Software Engineer (Components) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8557032002?gh_jid=8557032002) | May 19, 2026 |
| SpaceX | Full Stack Software Engineer (Build Reliability) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8555791002?gh_jid=8555791002) | May 19, 2026 |
| Nvidia | AI Software Engineer, Kernel Libraries - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Software-Engineer--Kernel-Libraries---New-College-Grad-2026_JR2018472) | May 19, 2026 |
| Nvidia | Software Engineer, AI and DL Kernel Libraries - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineer--AI-and-DL-Kernel-Libraries---New-College-Grad-2026_JR2018473) | May 19, 2026 |
| Nvidia | Quantum Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Research-Scientist-Intern---Fall-2026_JR2018244) | May 19, 2026 |
| Microsoft | Research Science PhD Internship Opportunities - Coding Agents 🇺🇸 | Cambridge, England, GB | PhD, Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867906) | May 19, 2026 |
| Etched | Chip Simulation Software Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/27e5bd6b-9357-45f0-9e79-cfa2bf4eeba8) | May 19, 2026 |
| Etched | Supercomputing Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/b45e357c-07ea-4499-9911-1d3cc9b9ac71) | May 19, 2026 |
| Etched | PD Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/bd8c5768-7efa-4a18-9e56-485ccaf4ec77) | May 19, 2026 |
| SpaceX | Development Test Engineer, Structures (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8551872002?gh_jid=8551872002) | May 18, 2026 |
| Plaid | Software Engineer - Product Security 🇺🇸 | New York City Office | - | [Apply](https://jobs.ashbyhq.com/plaid/675be915-3aed-4fe2-8f8b-f56dde88cf8a) | May 18, 2026 |
| Microsoft | Research Intern - Self-Improving AI 🇺🇸 | Cambridge, MA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867858) | May 18, 2026 |
| SpaceX | Operations Engineer (Facilities) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8551671002?gh_jid=8551671002) | May 15, 2026 |
| SpaceX | Full Stack Software Engineer, Data 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8553026002?gh_jid=8553026002) | May 15, 2026 |
| SpaceX | Full Stack Software Engineer, Data 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8553080002?gh_jid=8553080002) | May 15, 2026 |
| SpaceX | Data & Control Systems Engineer 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8552660002?gh_jid=8552660002) | May 15, 2026 |
| Nvidia | Software R&D Engineer, Digital Logic Synthesis - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-R-D-Engineer--Digital-Logic-Synthesis---New-College-Grad-2026_JR2018263) | May 15, 2026 |
| Uber | Software Engineer I 🇺🇸 | Sunnyvale, California, United States | Early Career | [Apply](https://www.uber.com/careers/list/158657) | May 14, 2026 |
| SpaceX | Security Software Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8543668002?gh_jid=8543668002) | May 14, 2026 |
| SpaceX | Full Stack Software Engineer (Starlink) 🇺🇸 | Palo Alto, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8501225002?gh_jid=8501225002) | May 14, 2026 |
| Pinterest | Master's Fall Machine Learning Internship (ATG - Visual Search) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | MS Student, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7253017) | May 14, 2026 |
| Pinterest | PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | PhD, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7255640) | May 14, 2026 |
| Nvidia | Software R&D Engineer, VLSI Physical Design - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Software-R-D-Engineer--VLSI-Physical-Design---New-College-Grad-2026_JR2018183) | May 14, 2026 |
| Nvidia | Circuit Design Engineer, Power Modeling and Simulation - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer--Power-Modeling-and-Simulation---New-College-Grad-2026_JR2018108) | May 14, 2026 |
| Lambda Labs | Security Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Fremont St) | MS Student, BS Student, Intern | [Apply](https://jobs.ashbyhq.com/lambda/0663f04c-097d-414f-b0a0-414a7cf153d6) | May 14, 2026 |
| Glean | Software Engineer, Product Backend 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4428090005) | May 14, 2026 |
| Glean | Software Engineer, Frontend 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006733005) | May 14, 2026 |
| Glean | Software Engineer, Fullstack 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006734005) | May 14, 2026 |
| Glean | Machine Learning Engineer, Search Quality 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006735005) | May 14, 2026 |
| Glean | Software Engineer, Billing & Revenue Platform 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4675862005) | May 14, 2026 |
| Apptronik | Simulation Engineer 🇺🇸 | Austin, TX | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/5806487004?gh_jid=5806487004) | May 14, 2026 |
| Apptronik | Junior Electrical Engineer - HRI 🇺🇸 | Austin, TX | - | [Apply](https://boards.greenhouse.io/apptronik/jobs/5996199004?gh_jid=5996199004) | May 14, 2026 |
| Meta | Software Engineer, Machine Learning 🇺🇸 | Fremont, CA | - | [Apply](https://www.linkedin.com/jobs/view/4351751274) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Brooklyn, NY | - | [Apply](https://www.linkedin.com/jobs/view/4413754708) | May 13, 2026 |
| Meta | Software Engineer, Machine Learning 🇺🇸 | San Mateo, CA | - | [Apply](https://www.linkedin.com/jobs/view/4255812821) | May 13, 2026 |
| Boston Dynamics | Low Observable Materials Engineer 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4413936972) | May 13, 2026 |
| Boston Dynamics | Low Observable Material Engineer 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4413959016) | May 13, 2026 |
| Meta | Research Scientist Intern, Monetization Generative AI - LLM (PhD) 🇺🇸 | Seattle, WA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4324778842) | May 13, 2026 |
| Meta | Software Engineer, AI Native 🇺🇸 | Bellevue, WA | - | [Apply](https://www.linkedin.com/jobs/view/4376614472) | May 13, 2026 |
| Boston Dynamics | 2026 Raytheon Part Time -Systems Engineer Co-op (Remote) 🇺🇸 | Richardson, TX | Intern | [Apply](https://www.linkedin.com/jobs/view/4411969435) | May 13, 2026 |
| Amazon Web Services (AWS) | Machine Learning Engineer, AWS Applied AI Solution 🇺🇸 | Seattle, WA | - | [Apply](https://www.linkedin.com/jobs/view/4381958807) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Carle Place, NY | - | [Apply](https://www.linkedin.com/jobs/view/4413770473) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, United States | - | [Apply](https://www.linkedin.com/jobs/view/4413756688) | May 13, 2026 |
| Zillow | Applied Scientist, New Construction 🇺🇸 | United States | - | [Apply](https://www.linkedin.com/jobs/view/4370817385) | May 13, 2026 |
| Together AI | Data Warehouse Engineer 🇺🇸 | San Francisco | - | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5074064007) | May 13, 2026 |
| Together AI | Analytics Engineer — Data Warehouse 🇺🇸 | San Francisco | - | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5101651007) | May 13, 2026 |
| SpaceX | Security Software Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8543784002?gh_jid=8543784002) | May 13, 2026 |
| SpaceX | Security Software Engineer (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8543817002?gh_jid=8543817002) | May 13, 2026 |
| Snap | Security Engineer, Level 3 🇺🇸 | Los Angeles, CA | - | [Apply](https://www.linkedin.com/jobs/view/4382377612) | May 13, 2026 |
| Ramp | Software Engineer, Credit 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/5598f7b8-4ae2-4105-a2b4-2d0f55c54c40) | May 13, 2026 |
| Nvidia | PhD Research Intern, Security and Privacy - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Security-and-Privacy---Fall-2026_JR2010492-1) | May 13, 2026 |
| Meta | Research Scientist Intern PhD, Applied Research 🇺🇸 | Menlo Park, CA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4350155408) | May 13, 2026 |
| Meta | Research Scientist Intern, Robotic Control Policy (PhD) 🇺🇸 | Redmond, WA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4291466172) | May 13, 2026 |
| Meta | Research Scientist Intern, Monetization Generative AI - LLM (PhD) 🇺🇸 | Bellevue, WA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4301800816) | May 13, 2026 |
| Meta | Research Scientist Intern, Monetization Generative AI - LLM (PhD) 🇺🇸 | Menlo Park, CA | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4302643436) | May 13, 2026 |
| Meta | Software Engineer, Machine Learning 🇺🇸 | Redmond, WA | - | [Apply](https://www.linkedin.com/jobs/view/4255810910) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | Bellevue, WA | Intern | [Apply](https://www.linkedin.com/jobs/view/4312023968) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | New York, NY | Intern | [Apply](https://www.linkedin.com/jobs/view/4312031471) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | Menlo Park, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4312033417) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | Boston, MA | Intern | [Apply](https://www.linkedin.com/jobs/view/4312039282) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | Seattle, WA | Intern | [Apply](https://www.linkedin.com/jobs/view/4312043129) | May 13, 2026 |
| Meta | Research Scientist Intern, AI Alignment 🇺🇸 | San Francisco, CA | Intern | [Apply](https://www.linkedin.com/jobs/view/4324709679) | May 13, 2026 |
| Meta | Software Engineer, Machine Learning 🇺🇸 | San Francisco, CA | - | [Apply](https://www.linkedin.com/jobs/view/4345574669) | May 13, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/4393214814) | May 13, 2026 |
| Boston Dynamics | Electrical Engineers II, Power & Analog, Design & Production Support – Actively Growing Our Engineering Team! 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4390339202) | May 13, 2026 |
| Boston Dynamics | 2026 Fulltime - Raytheon Power Electronics & Controls Electrical Engineer I(Onsite) 🇺🇸 | Huntsville, AL | Early Career | [Apply](https://www.linkedin.com/jobs/view/4384129405) | May 13, 2026 |
| Boston Dynamics | Low Observable Materials Engineer 🇺🇸 | Tucson, AZ | - | [Apply](https://www.linkedin.com/jobs/view/4413934988) | May 13, 2026 |
| Boston Dynamics | Chemicals and Materials Engineer I 🇺🇸 | Tucson, AZ | Early Career | [Apply](https://www.linkedin.com/jobs/view/4411982062) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer, AWS 🇺🇸 | Cupertino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4412413253) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Arlington, VA | - | [Apply](https://www.linkedin.com/jobs/view/4413752719) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer Intern, AWS Data Services - Fall 2026 (US) 🇺🇸 | Seattle, WA | Intern | [Apply](https://www.linkedin.com/jobs/view/4411283596) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | New York, NY | - | [Apply](https://www.linkedin.com/jobs/view/4413747862) | May 13, 2026 |
| Amazon Web Services (AWS) | Software Development Engineer 🇺🇸 | Cupertino, CA | - | [Apply](https://www.linkedin.com/jobs/view/4413767529) | May 13, 2026 |
| SpaceX | Software Engineer, Hardware Test & Automation (Optical Payloads) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8545930002?gh_jid=8545930002) | May 12, 2026 |
| SpaceX | Network Software Integration Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8459808002?gh_jid=8459808002) | May 12, 2026 |
| Snowflake | Software Engineer - Snowflake Postgres 🇺🇸 | US-CA-Menlo Park | - | [Apply](https://jobs.ashbyhq.com/snowflake/19ff5740-e678-4f43-a6c6-29bab94fbc21) | May 12, 2026 |
| Nvidia | DFT Engineer - New College Grad 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/DFT-Engineer---New-College-Grad_JR2016865) | May 12, 2026 |
| Nvidia | Signal and Power Integrity Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Signal-and-Power-Integrity-Engineer---New-College-Grad-2026_JR2017741) | May 12, 2026 |
| Fireworks AI | Support Engineer 🇺🇸 | San Mateo, CA | - | [Apply](https://job-boards.greenhouse.io/fireworksai/jobs/4009077009) | May 12, 2026 |
| SpaceX | New Graduate Engineer, Mechanical (Starlink) 🇺🇸 | Redmond, WA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8542046002?gh_jid=8542046002) | May 11, 2026 |
| SpaceX | Mechanical Design Engineer, Gateways (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8542789002?gh_jid=8542789002) | May 11, 2026 |
| SpaceX | Data & Control Systems Technician (Starship Launch Hardware) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8543809002?gh_jid=8543809002) | May 11, 2026 |
| Nvidia | Power Architect - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Power-Architect---New-College-Grad-2026_JR2017842) | May 11, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | May 11, 2026 |
| DRW | Software Engineer - Prediction Markets (Python) 🇺🇸 | Chicago | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7713854) | May 11, 2026 |
| Nvidia | GPU System and Scheduling Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-System-and-Scheduling-Architect---New-College-Grad-2026_JR2016691-1) | May 10, 2026 |
| SpaceX | New Graduate Engineer, Electrical - Satellites (Starlink) 🇺🇸 | Redmond, WA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8541336002?gh_jid=8541336002) | May 08, 2026 |
| Snowflake | Software Engineer Intern (Security) - Fall 2026 🇺🇸 | US-CA-Menlo Park | Intern | [Apply](https://jobs.ashbyhq.com/snowflake/a488959b-6874-4563-acb2-af747c3dc6f7) | May 08, 2026 |
| Scale AI | Software Engineer - New Grad 🇺🇸 | San Francisco, CA | New Grad | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4605996005) | May 08, 2026 |
| Applied Intuition | Software Engineer - AI Engineering 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4677060005?gh_jid=4677060005) | May 08, 2026 |
| Xaira Therapeutics | AI Research Engineer 🇺🇸 | Seattle, Washington, United States<br>South San Francisco, California, United States | - | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007) | May 07, 2026 |
| Xaira Therapeutics | AI in Residence 🇺🇸 | South San Francisco, California, United States | - | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5089321007) | May 07, 2026 |
| Nvidia | ASIC Physical Design Engineer, Netlisting - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Physical-Design-Engineer--Netlisting---New-College-Grad-2026_JR2017681) | May 07, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | US, MA, Westford | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2017593) | May 07, 2026 |
| Google | Optical Validation Engineer, Google Cloud 🇺🇸 | Sunnyvale, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/143702138877289158) | May 07, 2026 |
| Applied Intuition | Software Engineer - Calibration 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4373450005?gh_jid=4373450005) | May 07, 2026 |
| Tempus AI | Engineer I - Laboratory Automation 🇺🇸 | Chicago | Early Career | [Apply](https://tempus.wd5.myworkdayjobs.com/en-US/Tempus_Careers/job/Chicago/Engineer-I---Laboratory-Automation_JR202600414) | May 06, 2026 |
| SpaceX | Lead Starship Engineer (Ship Vehicle Assembly) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533755002?gh_jid=8533755002) | May 06, 2026 |
| OpenAI | Networking Operating System Firmware Engineer 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/openai/f6b9903c-9034-436b-a4ec-4c8643a6d0dd) | May 06, 2026 |
| Nvidia | Verification Engineer - New College Grad 2026 🇺🇸 | 3 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Verification-Engineer---New-College-Grad-2026_JR2017633) | May 06, 2026 |
| Nvidia | Applied Deep Learning PhD Research Intern, Reinforcement Learning for LLMs - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Deep-Learning-PhD-Research-Intern--Reinforcement-Learning-for-LLMs---Fall-2026_JR2012398) | May 06, 2026 |
| Meta | Research Scientist Intern PhD, Applied Research 🇺🇸 | New York, NY | PhD, Intern | [Apply](https://www.linkedin.com/jobs/view/4350195363) | May 06, 2026 |
| Google | Hardware Validation Engineer, Cloud Platforms 🇺🇸 | Sunnyvale, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/135325114404086470) | May 06, 2026 |
| Discord | Data Engineer, Analytics 🇺🇸 | San Francisco Bay Area | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8371252002) | May 06, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530798002?gh_jid=8530798002) | May 05, 2026 |
| Skydio | Software Engineer Intern Fall 2026/Winter 2027 🇺🇸 | San Mateo, California, United States | MS Student, Intern | [Apply](https://jobs.ashbyhq.com/skydio/f6320e9b-4eed-408d-8d37-d509fb0406ee) | May 05, 2026 |
| Nvidia | Power Methodology and Modeling Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Power-Methodology-and-Modeling-Engineer---New-College-Grad-2026_JR2017486-1) | May 05, 2026 |
| Nvidia | Machine Learning Applications and Compiler Engineer, LPX - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Machine-Learning-Applications-and-Compiler-Engineer--LPX---New-College-Grad-2026_JR2016939) | May 05, 2026 |
| Inceptive | Internship 🇺🇸 | Palo Alto, CA | Intern | [Apply](https://job-boards.greenhouse.io/inceptive/jobs/5103191007) | May 05, 2026 |
| DRW | Research Engineer 🇺🇸 | New York City | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/6973885) | May 05, 2026 |
| DRW | Quantitative Researcher 🇺🇸 | New York | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7650182) | May 05, 2026 |
| DRW | Software Engineer - Prediction Markets (Python) 🇺🇸 | New York City | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7728142) | May 05, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | San Francisco HQ | - | [Apply](https://jobs.ashbyhq.com/plaid/5c5d4414-347c-4caa-be88-384dec2d074b) | May 04, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | Seattle Office | - | [Apply](https://jobs.ashbyhq.com/plaid/664df3be-6be0-432f-8a35-ec7af986fd0d) | May 04, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | New York City Office | - | [Apply](https://jobs.ashbyhq.com/plaid/7e10c0b5-a09a-4e07-aaa8-899a7f82a0c9) | May 04, 2026 |
| Nvidia | Formal Verification Intern - Fall 2026 🇺🇸 | 2 Locations | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Formal-Verification-Intern---Fall-2026_JR2017490) | May 04, 2026 |
| Adobe | Junior Software Development Engineer 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Junior-Software-Development-Engineer_R168092) | May 04, 2026 |
| SpaceX | Software Engineer, Telemetry - Top Secret Clearance (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533686002?gh_jid=8533686002) | May 01, 2026 |
| SpaceX | Software Engineer, Continuous Integration (Starship) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533853002?gh_jid=8533853002) | May 01, 2026 |
| SpaceX | Software Engineer, Continuous Integration (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8533859002?gh_jid=8533859002) | May 01, 2026 |
| Nvidia | GPU Power Architect - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/GPU-Power-Architect---New-College-Grad-2026_JR2017169) | May 01, 2026 |
| SpaceX | Space Lasers Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402935002?gh_jid=8402935002) | Apr 30, 2026 |
| SpaceX | Spaceport Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8464867002?gh_jid=8464867002) | Apr 30, 2026 |
| SpaceX | Space Lasers Engineer, Satellites (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8479578002?gh_jid=8479578002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Starlink Ground Network) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8342599002?gh_jid=8342599002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8385191002?gh_jid=8385191002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Starshield) - Top Secret Clearance 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8387886002?gh_jid=8387886002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Power Systems Controls (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8395307002?gh_jid=8395307002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Vehicle Engineering) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8397542002?gh_jid=8397542002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Starlink Growth 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8403855002?gh_jid=8403855002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Starlink Growth 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8403929002?gh_jid=8403929002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Starlink Growth 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8403945002?gh_jid=8403945002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Product Development (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8436728002?gh_jid=8436728002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Simulation 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8443290002?gh_jid=8443290002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Low Latency Computing (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8450095002?gh_jid=8450095002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Telemetry (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8451998002?gh_jid=8451998002) | Apr 30, 2026 |
| SpaceX | Software Engineer, PCBA (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8456289002?gh_jid=8456289002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Starlink Network 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8458001002?gh_jid=8458001002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Starlink Network 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8477137002?gh_jid=8477137002) | Apr 30, 2026 |
| SpaceX | Software Infrastructure Engineer, Flight Software (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8478283002?gh_jid=8478283002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Simulations (Application Software) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8487534002?gh_jid=8487534002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8525359002?gh_jid=8525359002) | Apr 30, 2026 |
| SpaceX | Software Engineer, High Performance Computing (Starlink) 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530338002?gh_jid=8530338002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Low Latency Computing (Starlink) 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530342002?gh_jid=8530342002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Flight Software (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8322723002?gh_jid=8322723002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Additive Manufacturing (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8327721002?gh_jid=8327721002) | Apr 30, 2026 |
| SpaceX | Software Engineer, High Performance Computing 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8365469002?gh_jid=8365469002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Geospatial Data (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8389619002?gh_jid=8389619002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Components Test (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8391434002?gh_jid=8391434002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Embedded Software (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8436708002?gh_jid=8436708002) | Apr 30, 2026 |
| SpaceX | Software Engineer, DevOps (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8443737002?gh_jid=8443737002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Data - Top Secret Clearance (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8449846002?gh_jid=8449846002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Beam Planning (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8450082002?gh_jid=8450082002) | Apr 30, 2026 |
| SpaceX | Software Engineer, High Performance Computing (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8450116002?gh_jid=8450116002) | Apr 30, 2026 |
| SpaceX | Software Engineer, C++ (Starlink) 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8451960002?gh_jid=8451960002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Design Software (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8466837002?gh_jid=8466837002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Design Software (Starship) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8466905002?gh_jid=8466905002) | Apr 30, 2026 |
| SpaceX | Software Engineer, C++ (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8477124002?gh_jid=8477124002) | Apr 30, 2026 |
| SpaceX | Simulation Software Engineer (Application Software) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8488034002?gh_jid=8488034002) | Apr 30, 2026 |
| SpaceX | Software Engineer (Flight Reliability) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8512876002?gh_jid=8512876002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Beam Planning (Starlink) 🇺🇸 | Sunnyvale, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530316002?gh_jid=8530316002) | Apr 30, 2026 |
| SpaceX | Software Engineer, Development Test (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8532395002?gh_jid=8532395002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8380527002?gh_jid=8380527002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8380536002?gh_jid=8380536002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8392887002?gh_jid=8392887002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8420836002?gh_jid=8420836002) | Apr 30, 2026 |
| SpaceX | Security Engineer (Blue Team) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8426411002?gh_jid=8426411002) | Apr 30, 2026 |
| SpaceX | Security Engineer (Blue Team) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8426423002?gh_jid=8426423002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer, Applied Computing (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8440980002?gh_jid=8440980002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer, Applied Computing (Starshield) 🇺🇸 | Washington, DC | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8441008002?gh_jid=8441008002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer (Starlink) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8445643002?gh_jid=8445643002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8479234002?gh_jid=8479234002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer, Applied Computing (Starshield) 🇺🇸 | Palo Alto, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8483747002?gh_jid=8483747002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer (Starshield) 🇺🇸 | Washington, DC | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8483980002?gh_jid=8483980002) | Apr 30, 2026 |
| SpaceX | Security Software Engineer (Starshield) 🇺🇸 | Palo Alto, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8483982002?gh_jid=8483982002) | Apr 30, 2026 |
| SpaceX | Propulsion Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8324817002?gh_jid=8324817002) | Apr 30, 2026 |
| SpaceX | RF Engineer (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8369901002?gh_jid=8369901002) | Apr 30, 2026 |
| SpaceX | Quality Systems Engineer (Starlink Aviation) 🇺🇸 | Woodinville, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8372252002?gh_jid=8372252002) | Apr 30, 2026 |
| SpaceX | RF Systems Analysis Engineer, Regulatory (Starlink) 🇺🇸 | Washington, DC | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8389697002?gh_jid=8389697002) | Apr 30, 2026 |
| SpaceX | Propulsion Thermal Analyst (Raptor Combustion Devices) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8391522002?gh_jid=8391522002) | Apr 30, 2026 |
| SpaceX | Propulsion Engineer (Raptor Test) 🇺🇸 | McGregor, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8395154002?gh_jid=8395154002) | Apr 30, 2026 |
| SpaceX | RF Silicon Software Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8439627002?gh_jid=8439627002) | Apr 30, 2026 |
| SpaceX | PVD Process Engineer, Solar Cells (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8490537002?gh_jid=8490537002) | Apr 30, 2026 |
| SpaceX | Propulsion Engineer (Raptor Fleet Operations) 🇺🇸 | McGregor, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495923002?gh_jid=8495923002) | Apr 30, 2026 |
| SpaceX | Propulsion Analyst, Structures (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8377562002?gh_jid=8377562002) | Apr 30, 2026 |
| SpaceX | Process Safety Engineer (Raptor/Starship) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8407507002?gh_jid=8407507002) | Apr 30, 2026 |
| SpaceX | Process Engineer (Starlink/Akoustis) 🇺🇸 | Canandaigua, NY | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8473718002?gh_jid=8473718002) | Apr 30, 2026 |
| SpaceX | Propulsion Analyst, Chamber and Nozzle (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8486119002?gh_jid=8486119002) | Apr 30, 2026 |
| SpaceX | Propulsion Engineer, Combustion Devices Manufacturing (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8511177002?gh_jid=8511177002) | Apr 30, 2026 |
| SpaceX | Propulsion Engineer, Components Manufacturing (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8512813002?gh_jid=8512813002) | Apr 30, 2026 |
| SpaceX | Operations Engineer (Starlink Production) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8355754002?gh_jid=8355754002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Software (Starlink) 🇺🇸 | Redmond, WA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8376990002?gh_jid=8376990002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Software (Starlink) 🇺🇸 | Bastrop, TX | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8399140002?gh_jid=8399140002) | Apr 30, 2026 |
| SpaceX | Optical Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402772002?gh_jid=8402772002) | Apr 30, 2026 |
| SpaceX | Operations Engineer (Raptor) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402855002?gh_jid=8402855002) | Apr 30, 2026 |
| SpaceX | Operations Engineer, Environmental Health & Safety 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8427659002?gh_jid=8427659002) | Apr 30, 2026 |
| SpaceX | Platform Engineer, Flight Software (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8478286002?gh_jid=8478286002) | Apr 30, 2026 |
| SpaceX | Operations Engineer (Starlink Growth) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8496306002?gh_jid=8496306002) | Apr 30, 2026 |
| SpaceX | NDE Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402832002?gh_jid=8402832002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Software (Starlink) 🇺🇸 | Sunnyvale, CA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8446263002?gh_jid=8446263002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Electrical 🇺🇸 | Hawthorne, CA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8483305002?gh_jid=8483305002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Software 🇺🇸 | Hawthorne, CA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8493079002?gh_jid=8493079002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Mechanical (Starshield) 🇺🇸 | Hawthorne, CA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8493166002?gh_jid=8493166002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Propulsion (Starship) 🇺🇸 | Starbase, TX | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8497447002?gh_jid=8497447002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Mechanical (Starship) 🇺🇸 | Starbase, TX | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8497499002?gh_jid=8497499002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Mechanical 🇺🇸 | McGregor, TX | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8497524002?gh_jid=8497524002) | Apr 30, 2026 |
| SpaceX | New Graduate Engineer, Propulsion (Raptor) 🇺🇸 | Hawthorne, CA | New Grad | [Apply](https://boards.greenhouse.io/spacex/jobs/8517361002?gh_jid=8517361002) | Apr 30, 2026 |
| SpaceX | Materials Engineer, Polymers 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8393663002?gh_jid=8393663002) | Apr 30, 2026 |
| SpaceX | Maintenance Engineer, High Pressure Die Casting (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8398621002?gh_jid=8398621002) | Apr 30, 2026 |
| SpaceX | Launch Operations Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8447293002?gh_jid=8447293002) | Apr 30, 2026 |
| SpaceX | IT Network Infrastructure Engineer, Launch 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8458745002?gh_jid=8458745002) | Apr 30, 2026 |
| SpaceX | Launch Engineer, Stage 0 Propellant Generation (Starship) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8470330002?gh_jid=8470330002) | Apr 30, 2026 |
| SpaceX | Launch Reliability Engineer 🇺🇸 | Vandenberg, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8476233002?gh_jid=8476233002) | Apr 30, 2026 |
| SpaceX | Launch Reliability Engineer (Launch Pads & Recovery) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8526975002?gh_jid=8526975002) | Apr 30, 2026 |
| SpaceX | IC Package Engineer (Starlink/Akoustis) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8356899002?gh_jid=8356899002) | Apr 30, 2026 |
| SpaceX | Full Stack Software Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8365490002?gh_jid=8365490002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Engineer (Starlink Aviation) 🇺🇸 | Woodinville, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8378489002?gh_jid=8378489002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8397640002?gh_jid=8397640002) | Apr 30, 2026 |
| SpaceX | Full Stack Software Engineer (Components) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8421359002?gh_jid=8421359002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Engineer, Components (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8426161002?gh_jid=8426161002) | Apr 30, 2026 |
| SpaceX | Hardware Development Engineer, Gateway Failure Analysis (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8440611002?gh_jid=8440611002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Engineer, Electrical (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8489910002?gh_jid=8489910002) | Apr 30, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495131002?gh_jid=8495131002) | Apr 30, 2026 |
| SpaceX | Full Stack Software Engineer (Application Software) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Specialist, Microelectronics Failure Analysis (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8500797002?gh_jid=8500797002) | Apr 30, 2026 |
| SpaceX | Hardware Reliability Technician, Microelectronics Test (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530560002?gh_jid=8530560002) | Apr 30, 2026 |
| SpaceX | Fluids Systems Engineer, Solar Cell Factory (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8346155002?gh_jid=8346155002) | Apr 30, 2026 |
| SpaceX | Flight Software Infrastructure Engineer (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8477451002?gh_jid=8477451002) | Apr 30, 2026 |
| SpaceX | Failure Analysis Engineer, Microelectronics (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8498761002?gh_jid=8498761002) | Apr 30, 2026 |
| SpaceX | Equipment Reliability Engineer, Solar Cells (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8520607002?gh_jid=8520607002) | Apr 30, 2026 |
| SpaceX | Facilities Engineer, Solar Cell Factory (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8524791002?gh_jid=8524791002) | Apr 30, 2026 |
| SpaceX | Embedded Software Engineer, Satellite Antenna (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8468958002?gh_jid=8468958002) | Apr 30, 2026 |
| SpaceX | Embedded Software Engineer, OS/Platform (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8511391002?gh_jid=8511391002) | Apr 30, 2026 |
| SpaceX | Electrical Engineer, Hardware Reliability (Starlink Product) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8405853002?gh_jid=8405853002) | Apr 30, 2026 |
| SpaceX | Electrical Test and Reliability Engineer, Gateways (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8445519002?gh_jid=8445519002) | Apr 30, 2026 |
| SpaceX | Electrical Test and Reliability Engineer, Satellites (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8476268002?gh_jid=8476268002) | Apr 30, 2026 |
| SpaceX | Electrical Engineer, Propellant Generation (Starship) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8500856002?gh_jid=8500856002) | Apr 30, 2026 |
| SpaceX | Device Physics Engineer, Solar Cells (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8501065002?gh_jid=8501065002) | Apr 30, 2026 |
| SpaceX | Electrical Engineer, PCB (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8509293002?gh_jid=8509293002) | Apr 30, 2026 |
| SpaceX | Electrical On-orbit Hardware Reliability Engineer, Satellites (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8526673002?gh_jid=8526673002) | Apr 30, 2026 |
| SpaceX | Electrical Test Engineer, PCB (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8532471002?gh_jid=8532471002) | Apr 30, 2026 |
| SpaceX | Data Analyst, Supply Chain (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8330510002?gh_jid=8330510002) | Apr 30, 2026 |
| SpaceX | Critical Lift & Transport Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8413684002?gh_jid=8413684002) | Apr 30, 2026 |
| SpaceX | Critical Lift & Transport Engineer (Falcon) 🇺🇸 | Vandenberg, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8456320002?gh_jid=8456320002) | Apr 30, 2026 |
| SpaceX | Design Criteria Engineer (Starshield) 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8492189002?gh_jid=8492189002) | Apr 30, 2026 |
| SpaceX | Data Scientist (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8494810002?gh_jid=8494810002) | Apr 30, 2026 |
| SpaceX | Design Criteria Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8499349002?gh_jid=8499349002) | Apr 30, 2026 |
| SpaceX | Data Engineer (Starlink Growth) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8522503002?gh_jid=8522503002) | Apr 30, 2026 |
| SpaceX | Civil/Structural Engineer 🇺🇸 | McGregor, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8407221002?gh_jid=8407221002) | Apr 30, 2026 |
| SpaceX | City Engineer (Starship) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8465383002?gh_jid=8465383002) | Apr 30, 2026 |
| SpaceX | Civil Engineer, Land Development (Starship Launch Pad) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8483977002?gh_jid=8483977002) | Apr 30, 2026 |
| SpaceX | Civil Engineer, Land Development (Starship Infrastructure) 🇺🇸 | Cape Canaveral, FL | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8529553002?gh_jid=8529553002) | Apr 30, 2026 |
| SpaceX | BAW Filter Design Engineer (Starlink/Akoustis) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8356343002?gh_jid=8356343002) | Apr 30, 2026 |
| SpaceX | BAW Device Engineer (Starlink/Akoustis) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8357111002?gh_jid=8357111002) | Apr 30, 2026 |
| SpaceX | Chemical Process Engineer (Starship Launch Systems) 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402132002?gh_jid=8402132002) | Apr 30, 2026 |
| SpaceX | Business Operations Analyst (Starlink) 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8519655002?gh_jid=8519655002) | Apr 30, 2026 |
| SpaceX | Backend Software Engineer, GNC (Starlink) 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8398679002?gh_jid=8398679002) | Apr 30, 2026 |
| SpaceX | Aviation Certification Engineer (Starlink) 🇺🇸 | Woodinville, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8403060002?gh_jid=8403060002) | Apr 30, 2026 |
| SpaceX | Application Software Engineer, Data 🇺🇸 | Starbase, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8420526002?gh_jid=8420526002) | Apr 30, 2026 |
| SpaceX | Application Software Engineer, Data 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8530277002?gh_jid=8530277002) | Apr 30, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Redmond, WA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8402778002?gh_jid=8402778002) | Apr 30, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Hawthorne, CA | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8494238002?gh_jid=8494238002) | Apr 30, 2026 |
| SpaceX | Application Software Engineer 🇺🇸 | Bastrop, TX | - | [Apply](https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002) | Apr 30, 2026 |
| Nvidia | ASIC Clocks Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Clocks-Verification-Engineer---New-College-Grad-2026_JR2013336) | Apr 30, 2026 |
| Google | Security Engineer, Access Security Team 🇺🇸 | New York, NY, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/105043434598736582) | Apr 30, 2026 |
| Benchling | Software Engineer, Developer Enablement 🇺🇸 | San Francisco, CA | - | [Apply](https://jobs.ashbyhq.com/benchling/671d4911-7cb5-41da-9bb0-e497fa1874f8) | Apr 29, 2026 |
| Nvidia | Hardware Applications Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Hardware-Applications-Engineer---New-College-Grad-2026_JR2016940) | Apr 28, 2026 |
| Google | Data Engineer, Geo 3P and Developer Data Operations 🇺🇸 | Mountain View, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/86745576837653190) | Apr 28, 2026 |
| Benchling | Software Engineer, Agents 🇺🇸 | San Francisco, CA | - | [Apply](https://jobs.ashbyhq.com/benchling/815d941c-dff6-40cb-8307-57695acb37a7) | Apr 28, 2026 |
| Airbnb | iOS Software Engineer, Airbnb - New Grad 🇺🇸 | San Francisco, CA, Seattle, WA | New Grad | [Apply](https://careers.airbnb.com/positions/7859317?gh_jid=7859317) | Apr 28, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (iOS) 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Early Career | [Apply](https://www.uber.com/careers/list/158011) | Apr 27, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (Android) 🇺🇸 | Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Early Career | [Apply](https://www.uber.com/careers/list/158037) | Apr 27, 2026 |
| Ramp | Software Engineer, Production Engineering 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/be496b52-cfbf-494e-b862-61fb4a188b24) | Apr 27, 2026 |
| Nvidia | Solutions Architect, Data Processing - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Solutions-Architect--Data-Processing---New-College-Grad-2026_JR2017017) | Apr 27, 2026 |
| Nvidia | Low Power ASIC Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Low-Power-ASIC-Engineer---New-College-Grad-2026_JR2017001) | Apr 27, 2026 |
| Nvidia | Software Engineering Intern, JAX - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--JAX---Fall-2026_JR2009745) | Apr 27, 2026 |
| Nvidia | Applied Machine Learning Engineer, Circuit Design - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Machine-Learning-Engineer--Circuit-Design---New-College-Grad-2026_JR2011517) | Apr 27, 2026 |
| Notion | Software Engineer, New Grad (AI) 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9) | Apr 27, 2026 |
| CrowdStrike | GenAI Engineering Intern  - SkillBridge (Remote) 🇺🇸 | USA - Remote | Intern | [Apply](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers/job/USA---Remote/GenAI-Engineering-Intern----SkillBridge--Remote-_R26742) | Apr 27, 2026 |
| Adobe | 2026 University Graduate - Research Scientist/Engineer 🇺🇸 | San Francisco | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/XMLNAME-2026-University-Graduate---Research-Scientist-Engineer_R160690) | Apr 27, 2026 |
| Adobe | 2026 Intern - Research Scientist/Engineer 🇺🇸 | 7 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Research-Scientist-Engineer_R160317) | Apr 27, 2026 |
| Adobe | 2026 University Graduate - Machine Learning Engineer 🇺🇸 | Seattle | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/Seattle/XMLNAME-2026-University-Graduate---Machine-Learning-Engineer_R160133) | Apr 27, 2026 |
| Adobe | 2026 AI/ML Intern - Machine Learning Engineer/Researcher  Intern 🇺🇸 | 3 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer-Intern_R160706) | Apr 27, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R159512) | Apr 27, 2026 |
| Adobe | 2026 AI/ML Intern - Machine Learning Engineer 🇺🇸 | 7 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer_R158493) | Apr 27, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R168026) | Apr 27, 2026 |
| Adobe | Software Development Engineer - Front End 🇺🇸 | San Francisco | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Software-Development-Engineer---Front-End_R168188) | Apr 27, 2026 |
| Figure AI | Electrical Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | BS Student, New Grad, Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | Apr 25, 2026 |
| Figure AI | Electrical Interconnect Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676468006) | Apr 25, 2026 |
| Physical Intelligence | Mechatronics Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/0bcf909e-b38b-4276-91a1-e55c4c56a33a) | Apr 24, 2026 |
| Physical Intelligence | Hardware Systems Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/96bc1142-f406-4df3-aaa0-4bcce85f457f) | Apr 24, 2026 |
| Google | Modular Data Center Product Engineer, Design 🇺🇸 | Seattle, WA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/98426115135021766) | Apr 24, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/11aedfd6-8321-45af-b71e-492ea7ed3fff) | Apr 24, 2026 |
| Applied Intuition | Software Engineer - Python 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4674857005?gh_jid=4674857005) | Apr 24, 2026 |
| Notion | Software Engineer, New Grad 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555) | Apr 23, 2026 |
| Figma | Data Scientist, Core Data -  PhD (2026) 🇺🇸 | New York, NY • United States<br>San Francisco, CA • New York, NY | PhD | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) | Apr 22, 2026 |
| Skydio | Autonomy Engineer Intern - Deep Learning (Computational Photography) 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/d13e3179-e646-4873-84a6-d492a692bc25) | Apr 21, 2026 |
| Google | Security Engineer, Access Risk Intelligence and Security Mitigation 🇺🇸 | New York, NY, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/74402318644060870) | Apr 21, 2026 |
| Figure AI | Embedded Software Intern [Fall 2026] 🇺🇸 | San Jose, CA | BS Student, New Grad, Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4397706006) | Apr 21, 2026 |
| Applied Intuition | Software Engineer - Maps Infrastructure 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4045242005?gh_jid=4045242005) | Apr 21, 2026 |
| Applied Intuition | Software Engineer - Developer Infrastructure 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4581501005?gh_jid=4581501005) | Apr 21, 2026 |
| Applied Intuition | Software Engineer - Kafka 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4584510005?gh_jid=4584510005) | Apr 21, 2026 |
| Applied Intuition | Software Engineer - C++ 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://boards.greenhouse.io/appliedintuition/jobs/4669681005?gh_jid=4669681005) | Apr 21, 2026 |
| Snowflake | Software Engineer - Observe 🇺🇸 | US-CA-Menlo Park | - | [Apply](https://jobs.ashbyhq.com/snowflake/07e50e24-84ac-4002-ad26-9de1d991362c) | Apr 20, 2026 |
| Snowflake | Analyst, Finance Analytics & AI 🇺🇸 | US-CA-Menlo Park | - | [Apply](https://jobs.ashbyhq.com/snowflake/b241904d-7d42-41f0-9674-82e53d964846) | Apr 20, 2026 |
| OpenAI | Performance Modeling Engineer ~2 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/openai/4f6be73e-9a1d-4ec6-8b0e-b2af0b4becfb) | Apr 20, 2026 |
| Skydio | Product Support Engineer Intern 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/8df0689e-a489-4c72-a1f7-09dfe59745b8) | Apr 16, 2026 |
| Google | Product Safety Test Engineer, Platforms 🇺🇸 | Sunnyvale, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/119519945066193606) | Apr 16, 2026 |
| Snowflake | Product Analyst 🇺🇸 | US-CA-Menlo Park | - | [Apply](https://jobs.ashbyhq.com/snowflake/7c53d7f5-1a7f-4fdb-a8c1-b59060d9551d) | Apr 14, 2026 |
| Etched | DFT Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/5f1f5739-3b58-467c-b351-ff183c94d96d) | Apr 13, 2026 |
| Uber | Graduate 2026 Software Engineer I, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Early Career | [Apply](https://www.uber.com/careers/list/158009) | Apr 09, 2026 |
| Databricks | PhD GenAI Research Scientist Intern 🇺🇸 | San Francisco, California | PhD, Intern | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002) | Apr 09, 2026 |
| Skydio | Product Support Engineer 🇺🇸 | San Mateo, California, United States | - | [Apply](https://jobs.ashbyhq.com/skydio/a4f131a0-4dde-46ce-85a1-c83fc3e0f21e) | Apr 08, 2026 |
| Notion | Software Engineer Intern (Fall 2026) 🇺🇸 | San Francisco, California | Intern | [Apply](https://jobs.ashbyhq.com/notion/5b15697c-fa91-4511-9482-c98a6ff29f90) | Apr 06, 2026 |
| Snowflake | Industry Architect – Advertising & Media 🇺🇸 | US-CA-Remote | - | [Apply](https://jobs.ashbyhq.com/snowflake/bd9d7653-f818-40ba-b98e-cbee8261581a) | Apr 03, 2026 |
| Benchling | Software Engineer, Developer Platform 🇺🇸 | San Francisco, CA | New Grad | [Apply](https://jobs.ashbyhq.com/benchling/c83238cc-1f7c-4216-b2a5-418306ca4d2b) | Mar 27, 2026 |
| Skydio | Supply Chain Intern 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/2d21f482-3224-4906-a1bb-6a64436774cb) | Mar 23, 2026 |
| OpenAI | Infrastructure Partnership Delivery Lead – Stargate 🇺🇸 | Remote - US | - | [Apply](https://jobs.ashbyhq.com/openai/176b9de4-a5cf-4655-987c-872da1f5fe57) | Mar 21, 2026 |
| Sierra | Intern, Agent Development (Fall 2026) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://jobs.ashbyhq.com/sierra/c74d600c-235c-4d42-8546-b178b7adefc2) | Mar 19, 2026 |
| Skydio | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision 🇺🇸 | San Mateo, California, United States | PhD, Intern | [Apply](https://jobs.ashbyhq.com/skydio/8d3979a8-c791-4825-8cf4-9b25479b9519) | Mar 08, 2026 |
| Figure AI | Mechanical Engineer, Battery 🇺🇸 | San Jose, CA | - | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4656559006) | Feb 20, 2026 |
| OpenAI | Research Engineer / Machine Learning Engineer - Applied Voice 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/openai/46cd47bc-d4de-4826-aa2e-8b2e0da3c409) | Feb 17, 2026 |
| Replit | Support Engineer I (Weekend Shift) 🇺🇸 | Foster City, CA | Early Career | [Apply](https://jobs.ashbyhq.com/replit/951e0ebb-a957-45fa-8763-d56ba46750b4) | Feb 10, 2026 |
| Etched | RTL Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/157ed4f4-6e3b-4ec9-b93f-3e363e92041e) | Feb 07, 2026 |
| Etched | Infrastructure Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/1b073af4-6764-45ca-a22d-40a4823f0877) | Feb 07, 2026 |
| Etched | Firmware Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/699f3ab2-07e4-466c-9d76-3d4a3abb4ebc) | Feb 07, 2026 |
| Etched | Electrical Platform Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/904ddf46-55fc-4a8f-8b49-f32cfe88116a) | Feb 07, 2026 |
| Etched | DV Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/dacedaca-c4ca-4964-85a7-8df1738005bb) | Feb 07, 2026 |
| Etched | Mech / Thermal Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f05e3218-5ec7-41d1-bc99-bb7014422229) | Feb 07, 2026 |
| Google | Hardware Validation Engineer, ML Products, University Graduate 🇺🇸 | Sunnyvale, CA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/107128442041836230) | Jan 27, 2026 |
| OpenAI | RTL & Co-design Engineer (junior) 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/openai/77b815de-b7c5-4b87-8582-e8c752aea849) | Jan 22, 2026 |
| Recursion Pharma | Interested in an internship? 🇺🇸 | Remote Opportunity - United States<br>Salt Lake City, Utah | Intern | [Apply](https://job-boards.greenhouse.io/recursionpharmaceuticals/jobs/7540026) | Jan 20, 2026 |
| Ramp | Software Engineer, Core Product 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/5fe4c64e-9336-4384-9e6f-ff32eeb3fdae) | Jan 20, 2026 |
| Skydio | Autonomy Engineer Intern Fall 2026 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/17f6173b-c96f-4b02-a6b5-da0a91ad95e5) | Dec 15, 2025 |
| Skydio | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 🇺🇸 | San Mateo, California, United States | Intern | [Apply](https://jobs.ashbyhq.com/skydio/c84945f0-b8e0-4272-b636-265d6611a8eb) | Dec 15, 2025 |
| Etched | Inference Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/6f23713f-5409-45b7-aae8-adb8710cdbc3) | Dec 08, 2025 |
| Google | Network Operations Residency Program, University Graduate, 2026 Start 🇺🇸 | Thornton, CO, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/110139330885755590) | Nov 21, 2025 |
| Replit | Software Engineering Intern (Summer 2026) 🇺🇸 | Foster City, CA | PhD Student, MS Student, BS Student, Intern | [Apply](https://jobs.ashbyhq.com/replit/12737078-74c7-4e63-98a7-5e8da1e9deb1) | Oct 01, 2025 |
| Google | Student Researcher, PhD, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / Goleta, CA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA | PhD Student | [Apply](https://www.google.com/about/careers/applications/jobs/results/138166347879064262) | Sep 29, 2025 |
| Google | Student Researcher, BS/MS, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA / Princeton, NJ, USA | MS Student, BS Student | [Apply](https://www.google.com/about/careers/applications/jobs/results/140245524367188678) | Sep 29, 2025 |
| Mercor | Data Scientist 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/mercor/982a0751-e9eb-4b96-ac93-a1fd1d2f9152) | Aug 30, 2025 |
| Ramp | Software Engineer Internship, Android 🇺🇸 | New York, NY (HQ) | New Grad, Intern | [Apply](https://jobs.ashbyhq.com/ramp/67fadb77-43d8-4449-954b-d4cf2c6d3b8b) | Aug 07, 2025 |
| Ramp | University Grad \| Software Engineer \| Frontend 🇺🇸 | New York, NY (HQ) | New Grad | [Apply](https://jobs.ashbyhq.com/ramp/a1229aec-1105-4c47-8533-b912e732ed89) | Aug 01, 2025 |
| Ramp | Mobile Engineer, iOS 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f) | Jul 31, 2025 |
| Ramp | Mobile Engineer, Android 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040) | Jul 31, 2025 |


<details>
<summary><b>Closed positions (151)</b> &mdash; click to expand</summary>


| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Compute Services 🇺🇸~~ | New York, United States | - | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Compute Services 🇺🇸~~ | Seattle, WA | - | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Marketplace 🇺🇸~~ | Seattle, WA | - | Closed | May 27, 2026 |
| ~~Meta~~ | ~~Research Scientist Intern PhD, Applied Research 🇺🇸~~ | Bellevue, WA | PhD, Intern | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Brooklyn, NY | - | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Cupertino, CA | - | Closed | May 27, 2026 |
| ~~Tesla~~ | ~~Quality Engineer, Plastics 🇺🇸~~ | Sparks, NV | - | Closed | May 27, 2026 |
| ~~Meta~~ | ~~Software Engineer, AI Native 🇺🇸~~ | Menlo Park, CA | - | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~C/C++ Hardware / Software Co-Design SDE, Machine Learning Acceleration Systems 🇺🇸~~ | Cupertino, CA | - | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Network Development Engineer Intern - Fall Intern 🇺🇸~~ | Arlington, VA | Intern | Closed | May 27, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Compute Services 🇺🇸~~ | Cupertino, CA | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Compute Services 🇺🇸~~ | Sunnyvale, CA | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS Compute Services 🇺🇸~~ | Austin, TX | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | New York, NY | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Seattle, WA | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Carle Place, NY | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Cupertino, CA | - | Closed | May 26, 2026 |
| ~~Microsoft~~ | ~~Research Sciences INTERN 🇺🇸~~ | Bengaluru, KA, IN | Intern | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Brooklyn, NY | - | Closed | May 26, 2026 |
| ~~Boston Dynamics~~ | ~~Mechanical Engineers II, Design – Actively Growing our Engineering Team! 🇺🇸~~ | Tucson, AZ | - | Closed | May 26, 2026 |
| ~~xAI~~ | ~~Security Engineer - Detection & Response 🇺🇸~~ | New York, NY<br>Palo Alto, CA | - | Closed | May 26, 2026 |
| ~~Boston Dynamics~~ | ~~2026  Raytheon Full Time- Software Engineer I -(Onsite) 🇺🇸~~ | Huntsville, AL | Early Career | Closed | May 26, 2026 |
| ~~Anduril~~ | ~~Embedded Software Engineer, EW 🇺🇸~~ | Costa Mesa, California, United States | - | Closed | May 26, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Arlington, VA | - | Closed | May 26, 2026 |
| ~~Tesla~~ | ~~Equipment Engineer, Reman 🇺🇸~~ | Lathrop, CA | - | Closed | May 25, 2026 |
| ~~Tesla~~ | ~~Application Support Engineer, Factory Software 🇺🇸~~ | Fremont, CA | - | Closed | May 25, 2026 |
| ~~Veeva Systems~~ | ~~Associate Automation Engineer - RTSM 🇺🇸~~ | Pennsylvania - Philadelphia | - | Closed | May 25, 2026 |
| ~~Veeva Systems~~ | ~~Associate Automation Engineer - RTSM 🇺🇸~~ | North Carolina - Raleigh | - | Closed | May 25, 2026 |
| ~~Veeva Systems~~ | ~~Associate Automation Engineer - RTSM 🇺🇸~~ | Massachusetts - Boston | - | Closed | May 25, 2026 |
| ~~Tesla~~ | ~~Associate Facilities Operations Engineer 🇺🇸~~ | Sparks, NV | - | Closed | May 25, 2026 |
| ~~Tesla~~ | ~~Professional Engineering Trainee, PEAK Program (Summer 2026) 🇺🇸~~ | Fremont, CA | - | Closed | May 25, 2026 |
| ~~Tesla~~ | ~~Associate Shift Engineer, Cell Tabless 🇺🇸~~ | Austin, TX | - | Closed | May 25, 2026 |
| ~~Shield AI~~ | ~~Associate Infrastructure Engineer (R4897) 🇺🇸~~ | San Francisco, California | - | Closed | May 25, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Full-time - Manufacturing Engineer - Onsite (MA) 🇺🇸~~ | Andover, MA | - | Closed | May 25, 2026 |
| ~~Boston Dynamics~~ | ~~2026-Fulltime- Systems Engineer I – Onsite McKinney, Texas 🇺🇸~~ | McKinney, TX | Early Career | Closed | May 25, 2026 |
| ~~Tesla~~ | ~~Associate Mechanical Design Engineer 🇺🇸~~ | Brooklyn Park, MN | - | Closed | May 24, 2026 |
| ~~Tesla~~ | ~~Associate Controls Engineer 🇺🇸~~ | Austin, TX | - | Closed | May 24, 2026 |
| ~~Tesla~~ | ~~Mechanical Design Engineer, Chassis, Semi 🇺🇸~~ | Fremont, CA | - | Closed | May 24, 2026 |
| ~~Boston Dynamics~~ | ~~Systems Safety Engineer 🇺🇸~~ | Tewksbury, MA | - | Closed | May 24, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Arlington, VA | - | Closed | May 24, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~C/C++ Hardware / Software Co-Design SDE, Machine Learning Acceleration Systems 🇺🇸~~ | Cupertino, CA | - | Closed | May 23, 2026 |
| ~~Tesla~~ | ~~Associate Facilities Engineer 🇺🇸~~ | Fremont, CA | - | Closed | May 23, 2026 |
| ~~Tesla~~ | ~~Supplier Industrialization Engineer, Closures & Mechatronics 🇺🇸~~ | Fremont, CA | - | Closed | May 23, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Raytheon Part Time Co-op - Software  Engineer (Remote) 🇺🇸~~ | State College, PA | Intern | Closed | May 23, 2026 |
| ~~Boston Dynamics~~ | ~~Electrical Computer Aided Designer Engineer (ECAD) 1 🇺🇸~~ | Tucson, AZ | - | Closed | May 23, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Raytheon Part Time Co-op - Software  Engineer (Remote) 🇺🇸~~ | Dulles, VA | Intern | Closed | May 23, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Raytheon Part Time Co-op - Software  Engineer (Remote) 🇺🇸~~ | Aurora, CO | Intern | Closed | May 23, 2026 |
| ~~Boston Dynamics~~ | ~~Mechanical Engineer I (Onsite) 🇺🇸~~ | Portsmouth, RI | Early Career | Closed | May 23, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, Internet Monitoring 🇺🇸~~ | Santa Clara, CA | - | Closed | May 23, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Embedded Software Engineer, Annapurna Labs 🇺🇸~~ | Cupertino, CA | - | Closed | May 22, 2026 |
| ~~Tesla~~ | ~~Internship, Operational Automation Engineer, Residential Energy (Fall 2026) 🇺🇸~~ | Draper, UT | Intern | Closed | May 22, 2026 |
| ~~Tesla~~ | ~~Internship, Energy Optimization Software (Fall 2026) 🇺🇸~~ | Austin, TX | Intern | Closed | May 22, 2026 |
| ~~Tesla~~ | ~~Internship, Software Engineer, Code Hardening & Framework Resilience, Robotaxi (Fall 2026) 🇺🇸~~ | Palo Alto, CA | Intern | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~2027 Mission Systems Operations - Systems Engineer I - Onsite 🇺🇸~~ | Alexandria, VA | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~Raytheon Full Time 2026 - Technical Support Engineer I 🇺🇸~~ | McKinney, TX | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~Electrical Engineer I (Onsite) 🇺🇸~~ | Portsmouth, RI | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~Raytheon Full Time 2026 - RF Mechanical Engineer I 🇺🇸~~ | Tucson, AZ | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Full-time - Software Engineer I (Space and RF Sensors) - Onsite 🇺🇸~~ | Fort Wayne, IN | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~Electrical Engineer I (Onsite) 🇺🇸~~ | Tucson, AZ | Early Career | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Raytheon Part Time Co-op-Java Software Engineer (Remote) 🇺🇸~~ | State College, PA | Intern | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~Mechanical Engineer I (Onsite) 🇺🇸~~ | Marlborough, MA | Early Career | Closed | May 22, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | New York, United States | - | Closed | May 22, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Full-time - Manufacturing Engineer I - Onsite (AZ) 🇺🇸~~ | Tucson, AZ | Early Career | Closed | May 21, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Seattle, WA | - | Closed | May 21, 2026 |
| ~~Tesla~~ | ~~Internship, Data Engineer, Energy (Fall 2026) 🇺🇸~~ | Palo Alto, CA | Intern | Closed | May 21, 2026 |
| ~~Tesla~~ | ~~Internship, Software Engineer, Energy Engineering (Fall 2026) 🇺🇸~~ | Palo Alto, CA | Intern | Closed | May 21, 2026 |
| ~~Snap~~ | ~~Security Engineer, Level 3 🇺🇸~~ | Bellevue, WA | - | Closed | May 21, 2026 |
| ~~Anduril~~ | ~~Early Career Software Engineer 🇺🇸~~ | Seattle, Washington, United States | New Grad | Closed | May 21, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Brooklyn, NY | - | Closed | May 21, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | New York, United States | - | Closed | May 21, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Network Development Engineer Intern - Fall 2026 🇺🇸~~ | Arlington, VA | Intern | Closed | May 21, 2026 |
| ~~Netflix~~ | ~~Software Engineer in Test 5 - Apple Player 🇺🇸~~ | Los Gatos,California,United States of America | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | New York, NY | - | Closed | May 20, 2026 |
| ~~Boston Dynamics~~ | ~~2026 Fulltime-Raytheon FPGA Electrical Engineer I 🇺🇸~~ | Huntsville, AL | Early Career | Closed | May 20, 2026 |
| ~~Zillow~~ | ~~AI Applied Scientist - PhD Intern, Evaluation Systems and Metrics 🇺🇸~~ | United States | PhD, Intern | Closed | May 20, 2026 |
| ~~Zillow~~ | ~~AI Applied Scientist - PhD Intern, Foundational IQ 🇺🇸~~ | United States | PhD, Intern | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, Amazon S3 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Netflix~~ | ~~Software Engineer in Test 5 - Apple Player 🇺🇸~~ | Los Gatos,California,United States of America | - | Closed | May 20, 2026 |
| ~~Boston Dynamics~~ | ~~Program Controls Financial Analyst (Entry level) *HYBRID* 🇺🇸~~ | Andover, MA | New Grad | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, Amazon Quick Suite 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Zillow~~ | ~~AI Applied Scientist - PhD Intern, Next-Gen Agentic and Multi-Modal Home Exploration Experience 🇺🇸~~ | United States | PhD, Intern | Closed | May 20, 2026 |
| ~~Palo Alto Networks~~ | ~~AI Financial Analyst 🇺🇸~~ | Santa Clara, CA | New Grad | Closed | May 20, 2026 |
| ~~Meta~~ | ~~Software Engineer, AI Native 🇺🇸~~ | New York, NY | - | Closed | May 20, 2026 |
| ~~Meta~~ | ~~Fundamental AI Researcher - FAIR 🇺🇸~~ | New York, NY | - | Closed | May 20, 2026 |
| ~~AMD~~ | ~~Intern - RF Engineering (Summer 2026) 🇺🇸~~ | West Union, SC | Intern | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, Training & Certifications 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~(Fall 2026) Annapurna Labs at AWS Internship (US) - Machine Learning Systems & Silicon Innovation 🇺🇸~~ | Seattle, WA | Intern | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Data Engineer I, AWS WW Field Enablement, Analytics and Product Operations 🇺🇸~~ | Seattle, WA | Early Career | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | East Palo Alto, CA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | East Palo Alto, CA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | East Palo Alto, CA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | East Palo Alto, CA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Cupertino, CA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 20, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Brooklyn, NY | - | Closed | May 19, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Bellevue, WA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | Brooklyn, NY | - | Closed | May 13, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Austin, TX | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Non-Destructive Testing Engineer 🇺🇸~~ | Manassas, VA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Cupertino, CA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | New York, United States | - | Closed | May 13, 2026 |
| ~~Meta~~ | ~~Research Scientist Intern, Machine Perception for Input and Interaction (PhD) 🇺🇸~~ | Redmond, WA | PhD, Intern | Closed | May 13, 2026 |
| ~~Meta~~ | ~~Production Engineering 🇺🇸~~ | United States | - | Closed | May 13, 2026 |
| ~~Boston Dynamics~~ | ~~Raytheon Full Time 2026 - RF Systems Engineer I 🇺🇸~~ | Forest, MS | Early Career | Closed | May 13, 2026 |
| ~~Boston Dynamics~~ | ~~Digital Hardware Engineer I 🇺🇸~~ | Huntsville, AL | Early Career | Closed | May 13, 2026 |
| ~~Boston Dynamics~~ | ~~Raytheon Full Time 2026 - Digital Electronics Electrical Engineer I 🇺🇸~~ | Tewksbury, MA | Early Career | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AWS 🇺🇸~~ | New York, United States | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, DC Assistant Development 🇺🇸~~ | Bellevue, WA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer, AI Upgrades & Transformation 🇺🇸~~ | East Palo Alto, CA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Arlington, VA | - | Closed | May 13, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | Seattle, WA | - | Closed | May 13, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Sunnyvale, CA | - | Closed | May 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Menlo Park, CA | - | Closed | May 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | United States | - | Closed | May 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Burlingame, CA | - | Closed | May 12, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Santa Clara, CA | - | Closed | May 11, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | Seattle, WA | - | Closed | May 11, 2026 |
| ~~Meta~~ | ~~Software Engineer, Machine Learning 🇺🇸~~ | New York, NY | - | Closed | May 11, 2026 |
| ~~Adobe~~ | ~~2026 Intern - Data Scientist 🇺🇸~~ | San Jose | Intern | Closed | May 11, 2026 |
| ~~Amazon Web Services (AWS)~~ | ~~Software Development Engineer 🇺🇸~~ | New York, NY | - | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Agents & Efficiency 🇺🇸~~ | Cambridge, England, GB | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Intelligent Quantum Systems Architecture 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Fault Tolerant Quantum System Architecture 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Frontiers 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Nvidia~~ | ~~Software Engineering Intern, AI Tools - Fall 2026 🇺🇸~~ | US, CA, Santa Clara | Intern | Closed | May 06, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starlink Mobile) 🇺🇸~~ | Sunnyvale, CA | - | Closed | May 05, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Starlink Mobile) 🇺🇸~~ | Redmond, WA | - | Closed | May 05, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Propulsion Simulation & Data Analysis 🇺🇸~~ | Hawthorne, CA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Software Engineer (Special Projects) - Top Secret Clearance 🇺🇸~~ | Hawthorne, CA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Satellite Systems (Starshield) 🇺🇸~~ | Hawthorne, CA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Software Engineer, Hardware Test & Automation (Starlink) 🇺🇸~~ | Redmond, WA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Software Engineer 🇺🇸~~ | McGregor, TX | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Production Project Engineer (Starlink) 🇺🇸~~ | Bastrop, TX | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Printed Circuit Board (PCB) Reliability Engineer (Starlink) 🇺🇸~~ | Bastrop, TX | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Mechanical (Starlink) 🇺🇸~~ | Bastrop, TX | New Grad | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Electrical (Starlink) 🇺🇸~~ | Bastrop, TX | New Grad | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~New Graduate Engineer, Mechanical (Cape Canaveral) 🇺🇸~~ | Cape Canaveral, FL | New Grad | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Mechanisms Engineer (Starship) 🇺🇸~~ | Hawthorne, CA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Launch Engineer, Fluids (Starship) 🇺🇸~~ | Cape Canaveral, FL | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Hardware Test Engineer (Starlink) 🇺🇸~~ | Redmond, WA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Financial Systems Analyst 🇺🇸~~ | Hawthorne, CA | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Electrical Test Development Engineer, Customer Hardware (Starlink) 🇺🇸~~ | Bastrop, TX | - | Closed | Apr 30, 2026 |
| ~~SpaceX~~ | ~~Chemical Engineer, PCB (Starlink) 🇺🇸~~ | Bastrop, TX | - | Closed | Apr 30, 2026 |
| ~~Nvidia~~ | ~~System Software Engineer - Tegra 🇺🇸~~ | US, CA, Santa Clara | - | Closed | Apr 26, 2026 |
| ~~Nvidia~~ | ~~Deep Learning Architect, LLM Inference - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 26, 2026 |
| ~~Nvidia~~ | ~~ASIC Verification Engineer - New College Grad 2026 🇺🇸~~ | 2 Locations | New Grad | Closed | Apr 25, 2026 |

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

