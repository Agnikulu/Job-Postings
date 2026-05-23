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

- **Open positions:** 402
- **All-time tracked:** 619
- **Active companies:** 79
- **Last updated:** `2026-05-23 03:27 UTC`

## Legend

- **Role flag** -> Country (currently US-only, `🇺🇸`).
- **Education** -> Multi-label tag from `{PhD, Masters, Bachelors, New Grad, Intern}`.
- **Apply** -> Direct link to the company's job board posting.
- **Date Posted** -> When the company posted the role (parsed from each ATS).
   Falls back to when our scraper first observed the URL.

## Open positions

| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=3&pageNum=4&refId=3yKshxMIy5cT6hv4%2Fn5%2FqA%3D%3D&trackingId=jaLi8F%2FCHcdozhCqDzCDRg%3D%3D) | May 23, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=3&pageNum=5&refId=qa1kF9LMu6JXdumYtNXb1Q%3D%3D&trackingId=sSaBVrIB76wlqDg%2FLLDigQ%3D%3D) | May 23, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=2&pageNum=7&refId=c5OvCi%2F2r5IjjyHZJ8BcQQ%3D%3D&trackingId=BhX9CZqMs%2FpPeINjcYrZjw%3D%3D) | May 23, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=3&pageNum=8&refId=Oxq2KA5cawE%2B9CII66Z%2BHw%3D%3D&trackingId=ALGGkaLmL8Tit3nfphe8sQ%3D%3D) | May 23, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=3&pageNum=9&refId=XqOpc1FxetCCpCqrvFMBpQ%3D%3D&trackingId=RDCGjCJnEUqApV9cEILpPA%3D%3D) | May 23, 2026 |
| LinkedIn | Fellow, Software Engineering- Infrastructure 🇺🇸 | Mountain View, CA | - | [Apply](https://www.linkedin.com/jobs/view/fellow-software-engineering-infrastructure-at-linkedin-4393214814?position=3&pageNum=11&refId=XHizPVGGuMjjqvtPWnhIbQ%3D%3D&trackingId=wbuGaYkMM5utTKf1mf09XQ%3D%3D) | May 23, 2026 |
| Nvidia | Field Application Engineer - New College Graduate 2026 🇺🇸 | 4 Locations | - | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Field-Application-Engineer---New-College-Graduate-2026_JR2018580) | May 23, 2026 |
| Nvidia | Verification and Validation Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Verification-and-Validation-Engineer---New-College-Grad-2026_JR2018584-1) | May 23, 2026 |
| Nvidia | PhD Software Engineering Intern, Decision Intelligence - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Software-Engineering-Intern--Decision-Intelligence---Fall-2026_JR2017522) | May 23, 2026 |
| Nvidia | PhD Data Generation and User Simulation Research Intern — Fall 2026 🇺🇸 | US, CA, Remote | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Data-Generation-and-User-Simulation-Research-Intern---Fall-2026_JR2018317) | May 23, 2026 |
| Anduril | Robotics Software Engineer, Verification & Validation 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5083521007?gh_jid=5083521007) | May 22, 2026 |
| Anduril | Robotics Software Engineer, Behaviors 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5121816007?gh_jid=5121816007) | May 22, 2026 |
| Rippling | Software Engineer II, Backend Full Stack - Spend Product 🇺🇸 | New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/5b4e74c8-6493-44cb-98fe-2344b4fcd6b5) | May 22, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556861512) | May 22, 2026 |
| Scale AI | Mission Software Engineer, Public Sector 🇺🇸 | Colorado Springs, CO<br>Honolulu, HI<br>St. Louis, MO<br>Washington, DC | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4481921005) | May 22, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556761675) | May 22, 2026 |
| Google | Data Center Technician, Hardware 🇺🇸 | Atlanta, GA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/131868960663446214) | May 22, 2026 |
| DoorDash | DoorDash for Business Support Representative 🇺🇸 | Tempe, AZ | New Grad | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7768489) | May 22, 2026 |
| Anduril | Deployment Systems Technician 🇺🇸 | Waltham, Massachusetts, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5062621007?gh_jid=5062621007) | May 22, 2026 |
| Microsoft | Technical Support Engineering - Entry Level 🇺🇸 | Pune, MH, IN | New Grad | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867925) | May 22, 2026 |
| Google | Data Center Technician I 🇺🇸 | Lincoln, NE, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/91739328870261446) | May 22, 2026 |
| Uber | Software Engineer II, AdTech 🇺🇸 | Sunnyvale, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/156801) | May 22, 2026 |
| Uber | Software Engineer II - Michelangelo 🇺🇸 | Seattle, Washington, United States / Sunnyvale, California, United States | PhD, Masters | [Apply](https://www.uber.com/careers/list/158931) | May 22, 2026 |
| Rippling | Software Engineer II, Backend - Platform Team 🇺🇸 | Seattle, WA / San Francisco, CA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/18d9c9ed-c878-4e78-83a0-6e24cf0bcc9d) | May 22, 2026 |
| Rippling | Software Engineer II, Backend Full Stack - HR Product 🇺🇸 | San Francisco, CA / Seattle, WA | - | [Apply](https://ats.rippling.com/rippling/jobs/6d996cf7-a72f-40e6-b617-892139f81a2a) | May 22, 2026 |
| Rippling | Software Engineer II, Backend - Financial Product 🇺🇸 | Seattle, WA / San Francisco, CA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/844d2bdf-d672-46d9-a763-6788ba803248) | May 22, 2026 |
| Rippling | Software Engineer II, Backend - HR Product 🇺🇸 | San Francisco, CA / Seattle, WA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/86e4b180-a27e-4b86-bc80-6b7cefa2e1c9) | May 22, 2026 |
| Rippling | Software Engineer II, Backend Full Stack - Financial Product 🇺🇸 | San Francisco, CA / Seattle, WA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/b8488190-09b1-4506-9194-726939df73bd) | May 22, 2026 |
| Rippling | Security Engineer II, Offensive Security 🇺🇸 | Seattle, WA / San Francisco, CA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/e6a1faf6-a9ae-456b-b2a1-009844934956) | May 22, 2026 |
| Rippling | Software Engineer II, Backend - IT Product 🇺🇸 | Seattle, WA / San Francisco, CA / New York, NY | - | [Apply](https://ats.rippling.com/rippling/jobs/ebc7a777-aa35-4333-ac95-ebc98e375f75) | May 22, 2026 |
| Rippling | Software Engineer II, Frontend Full Stack - HR Product 🇺🇸 | Seattle, WA / San Francisco, CA | - | [Apply](https://ats.rippling.com/rippling/jobs/f64fe029-c299-4ace-9e28-1837a6db1604) | May 22, 2026 |
| Palantir | Forward Deployed Software Engineer - Warp Speed 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/13f99633-43b5-4459-8e84-25073f257c18) | May 22, 2026 |
| Palantir | Backend Software Engineer - Defense 🇺🇸 | Washington, D.C. | - | [Apply](https://jobs.lever.co/palantir/1345438c-ebfc-4fa5-b545-30c1414f317c) | May 22, 2026 |
| Palantir | Backend Software Engineer - Defense 🇺🇸 | Palo Alto, CA | - | [Apply](https://jobs.lever.co/palantir/a8174f9c-6f46-46b4-8e15-d1ff9e37c9eb) | May 22, 2026 |
| Palantir | Backend Software Engineer - Defense 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/d33e0c31-ac7e-4f57-ba74-36f2df6ae2f5) | May 22, 2026 |
| Palantir | Forward Deployed Software Engineer 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0) | May 22, 2026 |
| Palantir | Backend Software Engineer - Infrastructure, Foundations 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/palantir/fb2d3222-dbd8-4e03-8d39-47b820e9509c) | May 22, 2026 |
| Nvidia | Quantum Error Correction Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Error-Correction-Research-Scientist-Intern---Fall-2026_JR2018628) | May 22, 2026 |
| Mistral AI | Software Engineer, Backend (New-York) 🇺🇸 | New York, NY | - | [Apply](https://jobs.lever.co/mistral/f2e8ba75-bf5a-4976-bb96-c5d3e0f99366) | May 22, 2026 |
| Microsoft | Site Reliability Engineer II 🇺🇸 | Hyderabad, TS, IN / Bengaluru, KA, IN | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556853243) | May 22, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Bengaluru, KA, IN | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556862777) | May 22, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Bengaluru, KA, IN | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556863046) | May 22, 2026 |
| Luma AI | Software Engineer, Inference 🇺🇸 | SF Bay Area, CA / London, UK | - | [Apply](https://jobs.gem.com/lumalabs-ai/am9icG9zdDo8-N5tRXErv9eJJp_TyVo8) | May 22, 2026 |
| Luma AI | Software Engineer - Product 🇺🇸 | SF Bay Area, CA | Bachelors, New Grad | [Apply](https://jobs.gem.com/lumalabs-ai/am9icG9zdDodtsh6pWUJjQgE8lXoaEJi) | May 22, 2026 |
| Luma AI | Software Engineer, Data Infrastructure - Research 🇺🇸 | SF Bay Area, CA / London, UK | - | [Apply](https://jobs.gem.com/lumalabs-ai/5e6c11ba-de76-4e0c-a024-1003693754eb) | May 22, 2026 |
| CoreWeave | Operations Engineer, HPC Networking 🇺🇸 | Livingston, NJ / New York, NY / Sunnyvale, CA / Bellevue, WA | - | [Apply](https://coreweave.com/careers/job?4673462006&board=coreweave&gh_jid=4673462006) | May 22, 2026 |
| Anduril | Security Software Engineer 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5134986007?gh_jid=5134986007) | May 22, 2026 |
| Anduril | Robotics Software Engineer, Sensor Integration 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5096506007?gh_jid=5096506007) | May 22, 2026 |
| Anduril | Mission Software Engineer, Maneuver Dominance 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5102918007?gh_jid=5102918007) | May 22, 2026 |
| Anduril | Mechanical Engineer, Maneuver Dominance 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5116599007?gh_jid=5116599007) | May 22, 2026 |
| Anduril | Maritime Operations Engineer - Mission Autonomy 🇺🇸 | Channel Islands, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5069872007?gh_jid=5069872007) | May 22, 2026 |
| Anduril | GSOC Jr Operator 🇺🇸 | Costa Mesa, California, United States | Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5103111007?gh_jid=5103111007) | May 22, 2026 |
| Anduril | Electrical Engineer, Maneuver Dominance 🇺🇸 | Costa Mesa, California, United States | Bachelors, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4687724007?gh_jid=4687724007) | May 22, 2026 |
| Anduril | Division Operations Associate 🇺🇸 | Costa Mesa, California, United States | Bachelors, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5112754007?gh_jid=5112754007) | May 22, 2026 |
| Uber | Graduate 2026 PhD Scientist II (AEA/ASSA Economists Only), Reservations 🇺🇸 | Seattle, Washington, United States | PhD, Masters, Bachelors | [Apply](https://www.uber.com/careers/list/158984) | May 22, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Broomfield, Colorado, United States<br>Costa Mesa, California, United States<br>Fort Collins, Colorado, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007) | May 22, 2026 |
| Anduril | Early Career Manufacturing Engineer 🇺🇸 | Santa Ana, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5009798007?gh_jid=5009798007) | May 22, 2026 |
| Nvidia | ASIC Design Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Design-Engineer---New-College-Grad-2026_JR2017581) | May 22, 2026 |
| Uber | Program Manager, uBecome Intern Experience & Community 🇺🇸 | San Francisco, California, United States | Bachelors, New Grad, Intern | [Apply](https://www.uber.com/careers/list/157992) | May 21, 2026 |
| Uber | Application Developer L3 – Identity & Access Management (IAM) 🇺🇸 | Sunnyvale, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/159177) | May 21, 2026 |
| Stripe | Android Engineer, Terminal Global Payments 🇺🇸 | San Francisco, CA, Seattle, WA | - | [Apply](https://stripe.com/jobs/search?gh_jid=7778627) | May 21, 2026 |
| Point72 | Quantitative Researcher - Machine Learning 🇺🇸 | New York | PhD | [Apply](https://boards.greenhouse.io/point72/jobs/7297513002?gh_jid=7297513002) | May 21, 2026 |
| Point72 | Quantitative Analyst / Software Developer 🇺🇸 | New York | PhD | [Apply](https://boards.greenhouse.io/point72/jobs/7297622002?gh_jid=7297622002) | May 21, 2026 |
| Point72 | Quantitative Researcher - Systematic Credit 🇺🇸 | Chicago, New York | PhD, Masters | [Apply](https://boards.greenhouse.io/point72/jobs/7297625002?gh_jid=7297625002) | May 21, 2026 |
| Point72 | Quantitative Software Developer 🇺🇸 | New York | PhD | [Apply](https://boards.greenhouse.io/point72/jobs/7825863002?gh_jid=7825863002) | May 21, 2026 |
| Point72 | Software Engineer, Fundamental Research Tools 🇺🇸 | New York | - | [Apply](https://boards.greenhouse.io/point72/jobs/8377045002?gh_jid=8377045002) | May 21, 2026 |
| Point72 | Market Intelligence Emerging Talent Network 🇺🇸 | New York, NY | Masters, Bachelors, New Grad, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/6656054002?gh_jid=6656054002) | May 21, 2026 |
| Point72 | Equity Quantitative Researcher 🇺🇸 | New York | PhD, Masters | [Apply](https://boards.greenhouse.io/point72/jobs/7297561002?gh_jid=7297561002) | May 21, 2026 |
| Point72 | Machine Learning Engineer 🇺🇸 | New York | PhD | [Apply](https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002) | May 21, 2026 |
| Point72 | Fundamental Research Fellowship, Canvas 🇺🇸 | New York, NY | - | [Apply](https://boards.greenhouse.io/point72/jobs/8492784002?gh_jid=8492784002) | May 21, 2026 |
| Point72 | Data Engineer 🇺🇸 | New York | PhD | [Apply](https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002) | May 21, 2026 |
| Point72 | Data Scientist 🇺🇸 | Chicago, New York | PhD, Masters, Bachelors | [Apply](https://boards.greenhouse.io/point72/jobs/8372544002?gh_jid=8372544002) | May 21, 2026 |
| MongoDB | Software Engineer, Code Generation 🇺🇸 | California<br>Colorado<br>Montana<br>Nevada<br>New Mexico<br>Oregon<br>Utah<br>Washington | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7311666) | May 21, 2026 |
| Lambda Labs | Data Center Mechanical Engineering Intern - 2026 🇺🇸 | San Jose Office (Zanker) | Intern | [Apply](https://jobs.ashbyhq.com/lambda/62fcad14-b225-427c-ad86-6bb52377a997) | May 21, 2026 |
| DRW | Trade Systems Engineer 🇺🇸 | Chicago | Bachelors | [Apply](https://job-boards.greenhouse.io/drweng/jobs/6821173) | May 21, 2026 |
| DoorDash | Systems Engineer 🇺🇸 | San Francisco, CA<br>Oakland, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7350485) | May 21, 2026 |
| DoorDash | Software Engineer, Backend (All Teams) 🇺🇸 | Los Angeles, CA<br>Sunnyvale, CA<br>San Francisco, CA<br>New York, NY<br>Seattle, WA<br>Ann Arbor, MI | PhD, Masters, Bachelors | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/5630445) | May 21, 2026 |
| DoorDash | Software Engineer, Infrastructure - Autonomy & Robotics 🇺🇸 | San Francisco, CA | PhD, Masters, Bachelors | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/6367350) | May 21, 2026 |
| DoorDash | Software Engineer II, Data Engineering 🇺🇸 | San Francisco, CA<br>Sunnyvale, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/6458514) | May 21, 2026 |
| DoorDash | Mechanical Design Engineer — UAV Wire Harness 🇺🇸 | San Francisco, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7927350) | May 21, 2026 |
| DoorDash | Machine Learning Engineer, Marketplace Optimization 🇺🇸 | San Francisco, CA<br>Sunnyvale, CA | PhD, Masters, Bachelors | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7580407) | May 21, 2026 |
| DoorDash | Electrical Distribution Engineer (Harness / EDS) 🇺🇸 | Oakland, CA | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7779237) | May 21, 2026 |
| DoorDash | Composite & Prototype Engineering Technician 🇺🇸 | San Francisco, CA | Masters | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7650045) | May 21, 2026 |
| DoorDash | Associate Strategic Account Development Executive - Platform 🇺🇸 | Tempe, AZ<br>Atlanta, GA<br>Phoenix, AZ<br>Houston, TX<br>Dallas, TX Tampa, FL<br>Orlando, FL<br>Raleigh, NC<br>Charlotte, NC<br>Charleston, SC<br>Las Vegas, NV<br>Salt Lake City, UT | - | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7863361) | May 21, 2026 |
| CoreWeave | Software Engineer, Inference AI/ML 🇺🇸 | Sunnyvale, CA / Bellevue, WA | Masters, Intern | [Apply](https://coreweave.com/careers/job?4609928006&board=coreweave&gh_jid=4609928006) | May 21, 2026 |
| CoreWeave | Software Engineer II, Developer Experience 🇺🇸 | Livingston, NJ / New York, NY / Sunnyvale, CA / Bellevue, WA | - | [Apply](https://coreweave.com/careers/job?4678606006&board=coreweave&gh_jid=4678606006) | May 21, 2026 |
| Anduril | Robotics Software Engineer, Maritime 🇺🇸 | Quincy, Massachusetts, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5047315007?gh_jid=5047315007) | May 21, 2026 |
| Anduril | Robotics Software Engineer, Maritime 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5051580007?gh_jid=5051580007) | May 21, 2026 |
| Anduril | Robotics Software Engineer, Maritime 🇺🇸 | Boston, Massachusetts, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5091916007?gh_jid=5091916007) | May 21, 2026 |
| Anduril | Mission Operations Engineer, Connected Warfare (Active Clearance) 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4159543007?gh_jid=4159543007) | May 21, 2026 |
| Anduril | Mission Operations Engineer, Connected Warfare (Active Clearance) 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4182443007?gh_jid=4182443007) | May 21, 2026 |
| Anduril | Mission Operations Engineer 🇺🇸 | Atlanta, Georgia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5100663007?gh_jid=5100663007) | May 21, 2026 |
| Anduril | Mission Operations Engineer 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5115435007?gh_jid=5115435007) | May 21, 2026 |
| Anduril | Mechanical Engineer, Manufacturing Test 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4988675007?gh_jid=4988675007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4644883007?gh_jid=4644883007) | May 21, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080387007?gh_jid=5080387007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer, Intelligence Systems 🇺🇸 | Ashville, Ohio, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5080535007?gh_jid=5080535007) | May 21, 2026 |
| Anduril | Manufacturing Software Engineer, Intelligence Systems 🇺🇸 | Santa Ana, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5111318007?gh_jid=5111318007) | May 21, 2026 |
| Anduril | Manufacturing Test Engineer, Intelligence Systems (2nd Shift) 🇺🇸 | Santa Ana, California, United States | Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5135616007?gh_jid=5135616007) | May 21, 2026 |
| Anduril | Guidance Navigation and Control (GNC) Engineer, Air Dominance & Strike - Advanced Effects 🇺🇸 | Costa Mesa, California, United States | PhD, Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5024955007?gh_jid=5024955007) | May 21, 2026 |
| Anduril | GSOC Operator - SkillBridge 🇺🇸 | Costa Mesa, California, United States | Bachelors, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5033583007?gh_jid=5033583007) | May 21, 2026 |
| Anduril | Industrial Engineer II 🇺🇸 | Costa Mesa, California, United States | Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5037999007?gh_jid=5037999007) | May 21, 2026 |
| Anduril | Industrial Engineer, Production Controls & Simulation 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5108276007?gh_jid=5108276007) | May 21, 2026 |
| Anduril | GNC Engineer, Space 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870847007?gh_jid=4870847007) | May 21, 2026 |
| Anduril | GNC Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4870871007?gh_jid=4870871007) | May 21, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Costa Mesa, California, United States | PhD, Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016001007?gh_jid=5016001007) | May 21, 2026 |
| Anduril | Computer Vision Engineer, Space 🇺🇸 | Washington, District of Columbia, United States | PhD, Masters, Bachelors | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5016334007?gh_jid=5016334007) | May 21, 2026 |
| Anduril | Business Operations Associate, Production 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4619191007?gh_jid=4619191007) | May 21, 2026 |
| Anduril | Business Operations Associate 🇺🇸 | Costa Mesa, California, United States | - | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4951316007?gh_jid=4951316007) | May 21, 2026 |
| Adobe | Software Development Engineer 3— Acrobat Web 🇺🇸 | 2 Locations | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer-3--Acrobat-Web_R168301) | May 21, 2026 |
| DoorDash | AI Research Fellowship, (Summer and Fall 2026) 🇺🇸 | San Francisco, CA | PhD | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/7848317) | May 21, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/315f695d-04d1-4a9a-848e-cb2bec7a997e) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | Washington, D.C. | Intern | [Apply](https://jobs.lever.co/palantir/5c4c65c5-77da-4d36-856c-4ade87631019) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - USG 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/5c7bb70c-83ea-43e7-8055-0c8f319f4333) | May 21, 2026 |
| Palantir | Deployment Strategist, Internship - US Government 🇺🇸 | Honolulu, HI | Intern | [Apply](https://jobs.lever.co/palantir/a49d4181-a289-435a-b581-7f5af0497c8e) | May 21, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - France 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/ac0dc094-2480-43c2-8495-26ade227ff4f) | May 21, 2026 |
| Palantir | Forward Deployed Software Engineer, Internship - Poland 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/d582cd84-14fd-4aa3-b413-15982d286bd9) | May 21, 2026 |
| Palantir | Year at Palantir - Forward Deployed Software Engineer, Internship - Commercial 🇺🇸 | New York, NY | Intern | [Apply](https://jobs.lever.co/palantir/e6789b17-62fb-4226-a079-f8c17ff19e2d) | May 21, 2026 |
| Uber | Graduate 2026 PhD Software Engineer II (AV Labs), United States 🇺🇸 | San Francisco, California, United States / Sunnyvale, California, United States | PhD | [Apply](https://www.uber.com/careers/list/159120) | May 21, 2026 |
| Point72 | Summer 2027 Quantitative Developer Internship 🇺🇸 | New York | Bachelors, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297613002?gh_jid=7297613002) | May 21, 2026 |
| Point72 | Summer 2027 Quantitative Research Internship 🇺🇸 | New York | PhD, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297642002?gh_jid=7297642002) | May 21, 2026 |
| Point72 | Quantitative Software Developer Intern 🇺🇸 | New York, London, or Paris | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297666002?gh_jid=7297666002) | May 21, 2026 |
| Point72 | Quantitative Research Intern 🇺🇸 | New York, Seattle | PhD, Masters, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7297667002?gh_jid=7297667002) | May 21, 2026 |
| Point72 | Machine Learning Researcher - Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7302611002?gh_jid=7302611002) | May 21, 2026 |
| Point72 | Quantitative Researcher Intern 🇺🇸 | New York | PhD, Masters, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7586061002?gh_jid=7586061002) | May 21, 2026 |
| Point72 | Quantitative Developer Intern 🇺🇸 | New York | Intern | [Apply](https://boards.greenhouse.io/point72/jobs/7609197002?gh_jid=7609197002) | May 21, 2026 |
| Point72 | Quantitative Research Intern (NLP) 🇺🇸 | New York | PhD, Masters, Bachelors, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/8018862002?gh_jid=8018862002) | May 21, 2026 |
| Point72 | Quantitative Portfolio Analyst – 2026 Grad 🇺🇸 | New York, New York | PhD, Masters, Bachelors, Intern | [Apply](https://boards.greenhouse.io/point72/jobs/8169967002?gh_jid=8169967002) | May 21, 2026 |
| Anduril | Early Career Mechanical Engineer 🇺🇸 | Costa Mesa, California, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802167007?gh_jid=4802167007) | May 21, 2026 |
| Anduril | Early Career Electrical Engineer 🇺🇸 | Costa Mesa, California, United States | Masters, Bachelors, New Grad, Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4802172007?gh_jid=4802172007) | May 21, 2026 |
| Anduril | Early Career Software Engineer 🇺🇸 | Seattle, Washington, United States | New Grad | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/4824364007?gh_jid=4824364007) | May 21, 2026 |
| Netflix | Software Engineer in Test 5 - Apple Player 🇺🇸 | Los Gatos,California,United States of America | - | [Apply](https://explore.jobs.netflix.net/careers/job/790316003628) | May 20, 2026 |
| Uber | Software Engineer II - AV Labs 🇺🇸 | Sunnyvale, California, United States | PhD, Masters, Bachelors | [Apply](https://www.uber.com/careers/list/159272) | May 20, 2026 |
| Uber | Software Engineer II 🇺🇸 | Sunnyvale, California, United States | Masters, Bachelors | [Apply](https://www.uber.com/careers/list/154195) | May 20, 2026 |
| Stripe | Backend Engineer, Core Technology 🇺🇸 | US-Remote, Chicago | - | [Apply](https://stripe.com/jobs/search?gh_jid=6042172) | May 20, 2026 |
| Stripe | Backend Engineer, Payments and Risk 🇺🇸 | US | - | [Apply](https://stripe.com/jobs/search?gh_jid=6163230) | May 20, 2026 |
| Stripe | Backend Engineer, Payments and Risk 🇺🇸 | US | - | [Apply](https://stripe.com/jobs/search?gh_jid=7232592) | May 20, 2026 |
| Stripe | Cloud Security Engineer 🇺🇸 | Seattle | - | [Apply](https://stripe.com/jobs/search?gh_jid=7867389) | May 20, 2026 |
| Roblox | Software Engineer, User Sharing 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7767204?gh_jid=7767204) | May 20, 2026 |
| Roblox | Software Engineer, Creator Translation 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7786397?gh_jid=7786397) | May 20, 2026 |
| Roblox | Software Engineer, Communication Safety 🇺🇸 | San Mateo, CA, United States | - | [Apply](https://careers.roblox.com/jobs/7888723?gh_jid=7888723) | May 20, 2026 |
| Roblox | Software Engineer, Core Services 🇺🇸 | San Mateo, CA, United States | Bachelors | [Apply](https://careers.roblox.com/jobs/7943533?gh_jid=7943533) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Multimodal AI, Computer Vision and Graphics - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7323437?gh_jid=7323437) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Recommendation Systems - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7350081?gh_jid=7350081) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, AI Platform - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7403998?gh_jid=7403998) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer,  Engine Optimization - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7421746?gh_jid=7421746) | May 20, 2026 |
| Roblox | [2026] Senior Machine Learning Engineer, Account Identity - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7473686?gh_jid=7473686) | May 20, 2026 |
| Nvidia | Software Engineer, AI and DL Kernel Libraries - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineer--AI-and-DL-Kernel-Libraries---New-College-Grad-2026_JR2018473) | May 20, 2026 |
| MongoDB | Software Engineer 3, Search Systems Replication & Routing 🇺🇸 | San Francisco | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7235322) | May 20, 2026 |
| MongoDB | Software Engineer, Developer Productivity 🇺🇸 | New York City | Intern | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7851388) | May 20, 2026 |
| MongoDB | Software Engineer 3, Atlas Search Systems 🇺🇸 | San Francisco | - | [Apply](https://www.mongodb.com/careers/job/?gh_jid=7523920) | May 20, 2026 |
| Microsoft | Software Engineer 2 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556749568) | May 20, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556753717) | May 20, 2026 |
| Microsoft | Quantum Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556761664) | May 20, 2026 |
| Microsoft | Software Engineer 2 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556866801) | May 20, 2026 |
| Microsoft | Backend Software Engineer II 🇺🇸 | Barcelona, CT, ES / Madrid, MD, ES | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867876) | May 20, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556868080) | May 20, 2026 |
| Google | Network Operations Residency Program, University Graduate, August 2026 Start 🇺🇸 | Atlanta, GA, USA | Bachelors, New Grad, Intern | [Apply](https://www.google.com/about/careers/applications/jobs/results/118981017938600646) | May 20, 2026 |
| Google | Engineering Analyst, Trust and Safety Payments 🇺🇸 | Sunnyvale, CA, USA | Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/143948727982138054) | May 20, 2026 |
| Google | Silicon Design Verification Engineer 🇺🇸 | Mountain View, CA, USA | Masters, Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/86602986070909638) | May 20, 2026 |
| EvolutionaryScale | Postdoctoral Fellow, Transcription Regulation using Genomics and Machine Learning 🇺🇸 | New York, NY (Onsite) | - | [Apply](https://job-boards.greenhouse.io/biohub/jobs/7658780) | May 20, 2026 |
| Anthropic | Research Engineer, Economic Research Data Platform 🇺🇸 | San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5071132008) | May 20, 2026 |
| Anthropic | Anthropic Fellows Program, AI Security 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5030244008) | May 20, 2026 |
| Anthropic | Anthropic Fellows Program, AI Safety 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5183044008) | May 20, 2026 |
| Anthropic | Anthropic Fellows Program, ML Systems & Performance 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5183051008) | May 20, 2026 |
| Anthropic | Anthropic Fellows Program, Reinforcement Learning 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5183052008) | May 20, 2026 |
| Anthropic | Anthropic Fellows Program - The Anthropic Institute Fellows (Economics & Policy) 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5183053008) | May 20, 2026 |
| Microsoft | Data Center Technicians Intern 🇺🇸 | Middenmeer, NH, NL | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867635) | May 20, 2026 |
| Lambda Labs | Field Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Second St) | Masters, Intern | [Apply](https://jobs.ashbyhq.com/lambda/e0e555b9-a009-43c4-bd64-57e74cfd67f1) | May 20, 2026 |
| Roblox | [2026] Applied Scientist - PhD Intern 🇺🇸 | San Mateo, CA, United States | PhD, Intern | [Apply](https://careers.roblox.com/jobs/7142298?gh_jid=7142298) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Social - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7463634?gh_jid=7463634) | May 20, 2026 |
| Roblox | [2026] Software Engineer, Game Developer 🇺🇸 | San Mateo, CA, United States | Bachelors | [Apply](https://careers.roblox.com/jobs/7557909?gh_jid=7557909) | May 20, 2026 |
| Roblox | [2026] Data Scientist, Foundation AI - PhD Early Career 🇺🇸 | San Mateo, CA, United States | PhD, New Grad | [Apply](https://careers.roblox.com/jobs/7577436?gh_jid=7577436) | May 20, 2026 |
| Stripe | PhD Machine Learning Engineer, Intern 🇺🇸 | San Francisco, New York City, Seattle | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7216664) | May 20, 2026 |
| Stripe | PhD Data Scientist, Intern 🇺🇸 | San Francisco, New York City, Seattle, Chicago | PhD, Intern | [Apply](https://stripe.com/jobs/search?gh_jid=7874965) | May 20, 2026 |
| Nvidia | Quantum Research Scientist Intern - Fall 2026 🇺🇸 | US, CA, Remote | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Remote/Quantum-Research-Scientist-Intern---Fall-2026_JR2018244) | May 20, 2026 |
| Nvidia | AI Software Engineer, Kernel Libraries - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/AI-Software-Engineer--Kernel-Libraries---New-College-Grad-2026_JR2018472) | May 20, 2026 |
| Pinterest | Software Engineer II, Backend 🇺🇸 | Toronto, ON, CA | Masters, Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=5132899) | May 19, 2026 |
| Microsoft | Software Engineer II - CoreAI 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556637527) | May 19, 2026 |
| Microsoft | Software Engineer II - CoreAI 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556638528) | May 19, 2026 |
| Microsoft | Software Engineer II - CoreAI 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556657543) | May 19, 2026 |
| Adobe | Research Scientist 🇺🇸 | 3 Locations | PhD | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Research-Scientist_R166368) | May 19, 2026 |
| Microsoft | Research Science PhD Internship Opportunities - Coding Agents 🇺🇸 | Cambridge, England, GB | PhD, Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867906) | May 19, 2026 |
| Etched | Chip Simulation Software Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/27e5bd6b-9357-45f0-9e79-cfa2bf4eeba8) | May 19, 2026 |
| Etched | Supercomputing Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/b45e357c-07ea-4499-9911-1d3cc9b9ac71) | May 19, 2026 |
| Etched | PD Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/bd8c5768-7efa-4a18-9e56-485ccaf4ec77) | May 19, 2026 |
| Etched | Core Ops Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/f32908bd-8abc-495c-ab69-ac893b6c924d) | May 19, 2026 |
| Uber | Machine Learning Engineer II - AV Labs 🇺🇸 | Sunnyvale, California, United States | PhD, Masters, Bachelors | [Apply](https://www.uber.com/careers/list/158789) | May 18, 2026 |
| Uber | Software Engineer II 🇺🇸 | New York, New York, United States | Masters, Bachelors | [Apply](https://www.uber.com/careers/list/154824) | May 18, 2026 |
| Pinterest | Software Engineer II, Backend 🇺🇸 | San Francisco, CA, US<br>Seattle, WA, US | Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=4813946) | May 18, 2026 |
| Pinterest | Data Scientist II, Experimentation 🇺🇸 | San Francisco, CA, US<br>Remote, US | PhD | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7896291) | May 18, 2026 |
| Microsoft | Software Engineer II-Backend Software 🇺🇸 | Vancouver, BC, CA | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556753318) | May 18, 2026 |
| Microsoft | Software Engineer II 🇺🇸 | Redmond, WA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556859896) | May 18, 2026 |
| Microsoft | Applied AI Engineer II 🇺🇸 | Redmond, WA, US / Atlanta, GA, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556864775) | May 18, 2026 |
| Google | Security Engineer II, Uppercase Research 🇺🇸 | Austin, TX, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/75870343834542790) | May 18, 2026 |
| Microsoft | Research Intern - Self-Improving AI 🇺🇸 | Cambridge, MA, US / New York, NY, US | Intern | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556867858) | May 18, 2026 |
| Uber | Software Engineer II- Grocery & Retail 🇺🇸 | San Francisco, California, United States / Sunnyvale, California, United States | Masters | [Apply](https://www.uber.com/careers/list/153449) | May 16, 2026 |
| Nvidia | Software R&D Engineer, Digital Logic Synthesis - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-R-D-Engineer--Digital-Logic-Synthesis---New-College-Grad-2026_JR2018263) | May 16, 2026 |
| Uber | Software Engineer II - Uber Eats 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters | [Apply](https://www.uber.com/careers/list/157540) | May 15, 2026 |
| Uber | Software Engineer II - Middleware - AV Labs 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158889) | May 15, 2026 |
| Datadog | Security Engineer II - Vulnerability Lifecycle 🇺🇸 | New York, New York, USA | PhD, Bachelors | [Apply](https://careers.datadoghq.com/detail/7851502/?gh_jid=7851502) | May 15, 2026 |
| Datadog | Associate Marketing Data Analyst - Marketing Analytics 🇺🇸 | New York, New York, USA | - | [Apply](https://careers.datadoghq.com/detail/7837084/?gh_jid=7837084) | May 15, 2026 |
| Nvidia | Circuit Design Engineer, Power Modeling and Simulation - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Circuit-Design-Engineer--Power-Modeling-and-Simulation---New-College-Grad-2026_JR2018108) | May 15, 2026 |
| Nvidia | Software R&D Engineer, VLSI Physical Design - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Software-R-D-Engineer--VLSI-Physical-Design---New-College-Grad-2026_JR2018183) | May 15, 2026 |
| Vercel | Software Engineer, Next.js 🇺🇸 | Hybrid - San Francisco | - | [Apply](https://job-boards.greenhouse.io/vercel/jobs/5993753004) | May 14, 2026 |
| Uber | Software Engineer II 🇺🇸 | Seattle, Washington, United States | Bachelors | [Apply](https://www.uber.com/careers/list/158659) | May 14, 2026 |
| Uber | Software Engineer II - Maps & Localization - AV Labs 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158690) | May 14, 2026 |
| Uber | Software Engineer II 🇺🇸 | Sunnyvale, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/158660) | May 14, 2026 |
| Uber | Software Engineer I 🇺🇸 | Sunnyvale, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/158657) | May 14, 2026 |
| Uber | Software Engineer II 🇺🇸 | San Francisco, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/158661) | May 14, 2026 |
| Pinterest | Software Engineer II, Simulation, tvScientific 🇺🇸 | San Francisco, CA, US<br>Remote, US | - | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7642265) | May 14, 2026 |
| Pinterest | Software Engineer II, Backend, tvScientific 🇺🇸 | San Francisco, CA, US<br>Remote, US | Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7782552) | May 14, 2026 |
| Pinterest | Software Engineer II, ML Platform, tvScientific 🇺🇸 | San Francisco, CA, US<br>Remote, US | Masters | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7782571) | May 14, 2026 |
| Pinterest | Machine Learning Engineer II, Core Engineering 🇺🇸 | Toronto, ON, CA | PhD, Masters | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7473497) | May 14, 2026 |
| Pinterest | Security Software Engineer II, Corporate Security 🇺🇸 | San Francisco, CA, US<br>Remote, US | Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7494666) | May 14, 2026 |
| Pinterest | Security Software Engineer II, Detection and Response 🇺🇸 | San Francisco, CA, US<br>Remote, US | Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7770914) | May 14, 2026 |
| Pinterest | Security Software Engineer II, Security Operations 🇺🇸 | Chicago, IL, US<br>Remote, US | Bachelors | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7816431) | May 14, 2026 |
| Microsoft | Service Engineer II 🇺🇸 | Hyderabad, TS, IN | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556865811) | May 14, 2026 |
| Glean | Software Engineer, Frontend 🇺🇸 | Mountain View, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006733005) | May 14, 2026 |
| Glean | Software Engineer, Fullstack 🇺🇸 | Mountain View, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006734005) | May 14, 2026 |
| Glean | Software Engineer, Product Backend 🇺🇸 | Mountain View, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4428090005) | May 14, 2026 |
| Glean | Software Engineer, Developer Productivity 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4614706005) | May 14, 2026 |
| Glean | Software Engineer, Context Platform 🇺🇸 | Mountain View, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4638008005) | May 14, 2026 |
| Glean | Software Engineer, Billing & Revenue Platform 🇺🇸 | Mountain View, CA | - | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4675862005) | May 14, 2026 |
| Glean | Machine Learning Engineer, Search Quality 🇺🇸 | Mountain View, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4006735005) | May 14, 2026 |
| Databricks | Counsel, Commercial 🇺🇸 | Bellevue, Washington<br>Denver, Colorado<br>Mountain View, California<br>New York City, New York<br>San Francisco, California<br>Seattle, Washington<br>Washington, D.C. | - | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=8463179002) | May 14, 2026 |
| Lambda Labs | Security Engineering Intern - Summer 2026 🇺🇸 | San Francisco Office (Fremont St) | Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/lambda/0663f04c-097d-414f-b0a0-414a7cf153d6) | May 14, 2026 |
| Pinterest | Master's Fall Machine Learning Internship (ATG - Visual Search) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | Masters, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7253017) | May 14, 2026 |
| Pinterest | PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) 🇺🇸 | San Francisco, CA, US<br>Palo Alto, CA, US<br>Seattle, WA, US<br>New York, NY, US | PhD, Intern | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7255640) | May 14, 2026 |
| Nvidia | PhD Research Intern, Security and Privacy - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Security-and-Privacy---Fall-2026_JR2010492-1) | May 14, 2026 |
| Uber | Software Engineer II, AV Labs 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/158888) | May 13, 2026 |
| Together AI | Data Warehouse Engineer 🇺🇸 | San Francisco | New Grad | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5074064007) | May 13, 2026 |
| Together AI | Analytics Engineer — Data Warehouse 🇺🇸 | San Francisco | New Grad | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5101651007) | May 13, 2026 |
| Uber | Software Engineer II, Mobile, AV Labs 🇺🇸 | Sunnyvale, California, United States | Bachelors | [Apply](https://www.uber.com/careers/list/158726) | May 13, 2026 |
| Ramp | Software Engineer, Credit 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/5598f7b8-4ae2-4105-a2b4-2d0f55c54c40) | May 13, 2026 |
| Nvidia | DFT Engineer - New College Grad 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/DFT-Engineer---New-College-Grad_JR2016865) | May 13, 2026 |
| Notion | Software Engineer, Agent Dev Velocity 🇺🇸 | San Francisco, California | - | [Apply](https://jobs.ashbyhq.com/notion/c565d3b0-0dcf-4bcd-b29b-4168479ac78e) | May 13, 2026 |
| Microsoft | Software Engineer II, Foundry Agents - CoreAI 🇺🇸 | Redmond, WA, US / Mountain View, CA, US / New York, NY, US | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556863227) | May 13, 2026 |
| Microsoft | Software Engineer 2 🇺🇸 | Bengaluru, KA, IN / Hyderabad, TS, IN | - | [Apply](https://apply.careers.microsoft.com/careers/job/1970393556864867) | May 13, 2026 |
| Google | Equipment Technician, Vacuum, Semiconductor, Raxium 🇺🇸 | Fremont, CA, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/81545552558203590) | May 13, 2026 |
| Adobe | Software Development Engineer 3 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer-3_R164610) | May 13, 2026 |
| Nvidia | Signal and Power Integrity Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Signal-and-Power-Integrity-Engineer---New-College-Grad-2026_JR2017741) | May 13, 2026 |
| Uber | Machine Learning Engineer II, Pricing 🇺🇸 | Sunnyvale, California, United States / San Francisco, California, United States / Seattle, Washington, United States / New York, New York, United States | PhD, Masters, Bachelors | [Apply](https://www.uber.com/careers/list/146338) | May 12, 2026 |
| Snowflake | Software Engineer - Snowflake Postgres 🇺🇸 | US-CA-Menlo Park | Masters | [Apply](https://jobs.ashbyhq.com/snowflake/19ff5740-e678-4f43-a6c6-29bab94fbc21) | May 12, 2026 |
| EvolutionaryScale | Group Leader, Immune Cell Reprogramming 🇺🇸 | New York, NY (Hybrid) | PhD, New Grad | [Apply](https://job-boards.greenhouse.io/biohub/jobs/7286324) | May 12, 2026 |
| Adobe | 2026 Intern - Data Scientist 🇺🇸 | San Jose | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Data-Scientist_R161453) | May 12, 2026 |
| Nvidia | Systems Software Engineer - New College Grad 2026 🇺🇸 | US, OR, Hillsboro | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-OR-Hillsboro/Systems-Software-Engineer---New-College-Grad-2026_JR2017083) | May 12, 2026 |
| Uber | Software Engineer II ML, Merchant Intel 8 🇺🇸 | New York, New York, United States | PhD | [Apply](https://www.uber.com/careers/list/156031) | May 08, 2026 |
| Together AI | Backend Software Engineer — Data Platform & AI Data Products 🇺🇸 | San Francisco | - | [Apply](https://job-boards.greenhouse.io/togetherai/jobs/5064263007) | May 08, 2026 |
| Scale AI | Software Engineer, Frontier AI Infrastructure 🇺🇸 | San Francisco, CA<br>St. Louis, MO<br>New York, NY<br>Washington, DC | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4363623005) | May 08, 2026 |
| Scale AI | Software Engineer, ARC Team 🇺🇸 | San Francisco, CA<br>St. Louis, MO<br>New York, NY<br>Washington, DC | - | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4673771005) | May 08, 2026 |
| Scale AI | Machine Learning Research Engineer, Agents - Enterprise GenAI 🇺🇸 | San Francisco, CA<br>New York, NY | PhD, Masters | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4625344005) | May 08, 2026 |
| Nvidia | ASIC Physical Design Engineer, Netlisting - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Physical-Design-Engineer--Netlisting---New-College-Grad-2026_JR2017681) | May 08, 2026 |
| Uber | 2026 Fall Software Engineering Internship, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters, Bachelors, Intern | [Apply](https://www.uber.com/careers/list/159161) | May 08, 2026 |
| Snowflake | Software Engineer Intern (Security) - Fall 2026 🇺🇸 | US-CA-Menlo Park | Intern | [Apply](https://jobs.ashbyhq.com/snowflake/a488959b-6874-4563-acb2-af747c3dc6f7) | May 08, 2026 |
| Nvidia | GPU Verification Engineer - New College Grad 2026 🇺🇸 | US, MA, Westford | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-MA-Westford/GPU-Verification-Engineer---New-College-Grad-2026_JR2017593) | May 08, 2026 |
| Scale AI | Software Engineer - New Grad 🇺🇸 | San Francisco, CA | New Grad | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4605996005) | May 08, 2026 |
| Scale AI | Technical Advisor Specialist (Part-Time Internship) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://job-boards.greenhouse.io/scaleai/jobs/4611533005) | May 08, 2026 |
| Xaira Therapeutics | AI Research Engineer 🇺🇸 | Seattle, Washington, United States<br>South San Francisco, California, United States | Bachelors | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007) | May 07, 2026 |
| Xaira Therapeutics | AI in Residence 🇺🇸 | South San Francisco, California, United States | PhD, Masters | [Apply](https://job-boards.greenhouse.io/xairatherapeutics/jobs/5089321007) | May 07, 2026 |
| Nvidia | Verification Engineer - New College Grad 2026 🇺🇸 | 3 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Verification-Engineer---New-College-Grad-2026_JR2017633) | May 07, 2026 |
| Google | Optical Validation Engineer, Google Cloud 🇺🇸 | Sunnyvale, CA, USA | Masters, Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/143702138877289158) | May 07, 2026 |
| DRW | Research Engineer (FICCO) 🇺🇸 | Chicago | Bachelors | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7377915) | May 07, 2026 |
| Nvidia | Applied Deep Learning PhD Research Intern, Reinforcement Learning for LLMs - Fall 2026 🇺🇸 | US, CA, Santa Clara | PhD, Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Deep-Learning-PhD-Research-Intern--Reinforcement-Learning-for-LLMs---Fall-2026_JR2012398) | May 07, 2026 |
| Nvidia | Software Engineering Intern, AI Tools - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--AI-Tools---Fall-2026_JR2016805) | May 07, 2026 |
| Google | Hardware Validation Engineer, Cloud Platforms 🇺🇸 | Sunnyvale, CA, USA | PhD, Masters, Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/135325114404086470) | May 06, 2026 |
| Discord | Data Engineer, Analytics 🇺🇸 | San Francisco Bay Area | - | [Apply](https://job-boards.greenhouse.io/discord/jobs/8371252002) | May 06, 2026 |
| Anthropic | Anthropic Fellows Program 🇺🇸 | London, UK<br>Ontario, CAN<br>Remote-Friendly, United States<br>San Francisco, CA | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5023394008) | May 06, 2026 |
| Nvidia | Machine Learning Applications and Compiler Engineer, LPX - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Machine-Learning-Applications-and-Compiler-Engineer--LPX---New-College-Grad-2026_JR2016939) | May 06, 2026 |
| Nvidia | Power Methodology and Modeling Engineer - New College Grad 2026 🇺🇸 | US, TX, Austin | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/Power-Methodology-and-Modeling-Engineer---New-College-Grad-2026_JR2017486-1) | May 06, 2026 |
| Uber | Software Engineer II - Grocery & Retail 🇺🇸 | New York, New York, United States | Masters | [Apply](https://www.uber.com/careers/list/156728) | May 05, 2026 |
| Snowflake | Product Finance Analyst 🇺🇸 | US-CA-Menlo Park | Bachelors, New Grad | [Apply](https://jobs.ashbyhq.com/snowflake/7c4b66d9-71e0-4a43-8e80-d20b5a3efc28) | May 05, 2026 |
| Nvidia | Formal Verification Intern - Fall 2026 🇺🇸 | 2 Locations | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Formal-Verification-Intern---Fall-2026_JR2017490) | May 05, 2026 |
| DRW | Research Engineer 🇺🇸 | New York City | Bachelors | [Apply](https://job-boards.greenhouse.io/drweng/jobs/6973885) | May 05, 2026 |
| DRW | Software Engineer, Research – Cumberland Systematic 🇺🇸 | Chicago | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7283668) | May 05, 2026 |
| DRW | Software Engineer, Cumberland/FICCO Tools Engineering 🇺🇸 | New York City | Bachelors | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7392396) | May 05, 2026 |
| DRW | Software Engineer, Research – Cumberland Systematic 🇺🇸 | New York City | - | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7743648) | May 05, 2026 |
| DRW | Quantitative Researcher 🇺🇸 | New York | PhD, Bachelors | [Apply](https://job-boards.greenhouse.io/drweng/jobs/7650182) | May 05, 2026 |
| Adobe | Junior Software Development Engineer 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Junior-Software-Development-Engineer_R168092) | May 05, 2026 |
| Inceptive | Internship 🇺🇸 | Palo Alto, CA | Intern | [Apply](https://job-boards.greenhouse.io/inceptive/jobs/5103191007) | May 05, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | San Francisco HQ | Intern | [Apply](https://jobs.ashbyhq.com/plaid/5c5d4414-347c-4caa-be88-384dec2d074b) | May 04, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | Seattle Office | Intern | [Apply](https://jobs.ashbyhq.com/plaid/664df3be-6be0-432f-8a35-ec7af986fd0d) | May 04, 2026 |
| Plaid | Software Engineer, Backend 🇺🇸 | New York City Office | Intern | [Apply](https://jobs.ashbyhq.com/plaid/7e10c0b5-a09a-4e07-aaa8-899a7f82a0c9) | May 04, 2026 |
| Figma | Software Engineer, Full Stack 🇺🇸 | San Francisco, CA • New York, NY • United States | - | [Apply](https://boards.greenhouse.io/figma/jobs/5691911004?gh_jid=5691911004) | May 04, 2026 |
| Cognition AI | Research, Post-Training 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cognition/72d3db28-07d3-4c28-b49f-1bdf6e8e0f10) | May 01, 2026 |
| Nvidia | ASIC Clocks Verification Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/ASIC-Clocks-Verification-Engineer---New-College-Grad-2026_JR2013336) | May 01, 2026 |
| Uber | Software Engineer II - Fullstack, Grocery 🇺🇸 | Sunnyvale, California, United States | - | [Apply](https://www.uber.com/careers/list/154688) | Apr 30, 2026 |
| Google | Security Engineer, Access Security Team 🇺🇸 | New York, NY, USA | Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/105043434598736582) | Apr 30, 2026 |
| GitLab | Intermediate Backend Engineer,  SSCS: Supply Chain 🇺🇸 | Remote, India | - | [Apply](https://job-boards.greenhouse.io/gitlab/jobs/8480565002) | Apr 30, 2026 |
| GitLab | Intermediate Backend Engineer, Database Automation (Ruby) 🇺🇸 | Remote, India | - | [Apply](https://job-boards.greenhouse.io/gitlab/jobs/8481029002) | Apr 30, 2026 |
| Google DeepMind | Frontier AI Research Scientist, DeepMind 🇺🇸 | Mountain View, CA, USA | PhD | [Apply](https://www.google.com/about/careers/applications/jobs/results/110687296503587526) | Apr 29, 2026 |
| Benchling | Software Engineer, Developer Enablement 🇺🇸 | San Francisco, CA | Intern | [Apply](https://jobs.ashbyhq.com/benchling/671d4911-7cb5-41da-9bb0-e497fa1874f8) | Apr 29, 2026 |
| Nvidia | Hardware Applications Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Hardware-Applications-Engineer---New-College-Grad-2026_JR2016940) | Apr 29, 2026 |
| Nvidia | Applied Machine Learning Engineer, Circuit Design - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Machine-Learning-Engineer--Circuit-Design---New-College-Grad-2026_JR2011517) | Apr 28, 2026 |
| Google | Data Engineer, Geo 3P and Developer Data Operations 🇺🇸 | Mountain View, CA, USA | Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/86745576837653190) | Apr 28, 2026 |
| EvolutionaryScale | Group Leader, Immunology 🇺🇸 | New York, NY (Hybrid) | PhD, New Grad | [Apply](https://job-boards.greenhouse.io/biohub/jobs/7535647) | Apr 28, 2026 |
| Benchling | Software Engineer, Agents 🇺🇸 | San Francisco, CA | - | [Apply](https://jobs.ashbyhq.com/benchling/815d941c-dff6-40cb-8307-57695acb37a7) | Apr 28, 2026 |
| Adobe | Software Development Engineer - Front End 🇺🇸 | San Francisco | Masters, Bachelors | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/Software-Development-Engineer---Front-End_R168188) | Apr 28, 2026 |
| Airbnb | iOS Software Engineer, Airbnb - New Grad 🇺🇸 | San Francisco, CA, Seattle, WA | New Grad | [Apply](https://careers.airbnb.com/positions/7859317?gh_jid=7859317) | Apr 28, 2026 |
| Ramp | Software Engineer, Engineering Platform 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/198150d6-789a-4ef8-999f-93a49656d4f1) | Apr 27, 2026 |
| Ramp | Software Engineer, Production Engineering 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/be496b52-cfbf-494e-b862-61fb4a188b24) | Apr 27, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (iOS) 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters, Bachelors | [Apply](https://www.uber.com/careers/list/158011) | Apr 27, 2026 |
| Uber | Graduate 2026 Software Engineer I, Mobile (Android) 🇺🇸 | Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters, Bachelors | [Apply](https://www.uber.com/careers/list/158037) | Apr 27, 2026 |
| Notion | Software Engineer, New Grad (AI) 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9) | Apr 27, 2026 |
| Nvidia | ASIC Verification Engineer - New College Grad 2026 🇺🇸 | 2 Locations | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-TX-Austin/ASIC-Verification-Engineer---New-College-Grad-2026_JR2012573) | Apr 25, 2026 |
| Figure AI | Electrical Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Bachelors, New Grad, Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676467006) | Apr 25, 2026 |
| Figure AI | Electrical Interconnect Engineering Intern [Fall 2026] 🇺🇸 | San Jose, CA | Masters, Bachelors, Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4676468006) | Apr 25, 2026 |
| Nvidia | Low Power ASIC Engineer - New College Grad 2026 🇺🇸 | US, CA, Santa Clara | New Grad | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Low-Power-ASIC-Engineer---New-College-Grad-2026_JR2017001) | Apr 25, 2026 |
| Nvidia | Software Engineering Intern, JAX - Fall 2026 🇺🇸 | US, CA, Santa Clara | Intern | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Software-Engineering-Intern--JAX---Fall-2026_JR2009745) | Apr 25, 2026 |
| Google | Modular Data Center Product Engineer, Design 🇺🇸 | Seattle, WA, USA | Masters, Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/98426115135021766) | Apr 24, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R168026) | Apr 24, 2026 |
| Physical Intelligence | Mechatronics Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/0bcf909e-b38b-4276-91a1-e55c4c56a33a) | Apr 24, 2026 |
| Physical Intelligence | Hardware Systems Intern 🇺🇸 | San Francisco | Intern | [Apply](https://jobs.ashbyhq.com/physicalintelligence/96bc1142-f406-4df3-aaa0-4bcce85f457f) | Apr 24, 2026 |
| Etched | Thermo-Mech CFD Simulation Intern 🇺🇸 | San Jose | Intern | [Apply](https://jobs.ashbyhq.com/etched/11aedfd6-8321-45af-b71e-492ea7ed3fff) | Apr 24, 2026 |
| Adobe | Research Scientist 🇺🇸 | San Jose | PhD | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Research-Scientist_R166575) | Apr 23, 2026 |
| Adobe | Research Scientist 🇺🇸 | San Jose | PhD | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Research-Scientist_R167353) | Apr 23, 2026 |
| Uber | Software Engineer II - iOS, Engagement Growth 🇺🇸 | New York, New York, United States | Bachelors | [Apply](https://www.uber.com/careers/list/155187) | Apr 23, 2026 |
| Adobe | 2026 Intern - Research Scientist/Engineer 🇺🇸 | 7 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Research-Scientist-Engineer_R160317) | Apr 23, 2026 |
| Adobe | 2026 AI/ML Intern - Machine Learning Engineer/Researcher  Intern 🇺🇸 | 3 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer-Intern_R160706) | Apr 23, 2026 |
| Adobe | Machine Learning Engineer 3 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Machine-Learning-Engineer-3_R157544-1) | Apr 23, 2026 |
| Adobe | Software Development Engineer 3 🇺🇸 | San Jose | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer-3_R165606-1) | Apr 23, 2026 |
| Adobe | Data Scientist 🇺🇸 | San Jose | Masters, Bachelors | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Data-Scientist_R165959-1) | Apr 23, 2026 |
| Adobe | Security Engineer 3 🇺🇸 | 2 Locations | - | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/Seattle/Security-Engineer-3_R167561) | Apr 23, 2026 |
| Adobe | Software Development Engineer 🇺🇸 | San Jose | Bachelors | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Software-Development-Engineer_R159512) | Apr 23, 2026 |
| Adobe | 2026 AI/ML Intern - Machine Learning Engineer 🇺🇸 | 7 Locations | Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer_R158493) | Apr 23, 2026 |
| Adobe | Research Scientist/Engineer - Photoshop 🇺🇸 | Seattle | PhD, Intern | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/Seattle/Research-Scientist-Engineer_R164613) | Apr 23, 2026 |
| Adobe | 2026 University Graduate - Research Scientist/Engineer 🇺🇸 | San Francisco | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Francisco/XMLNAME-2026-University-Graduate---Research-Scientist-Engineer_R160690) | Apr 23, 2026 |
| Adobe | 2026 University Graduate - Machine Learning Engineer 🇺🇸 | Seattle | New Grad | [Apply](https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/Seattle/XMLNAME-2026-University-Graduate---Machine-Learning-Engineer_R160133) | Apr 23, 2026 |
| Notion | Software Engineer, New Grad 🇺🇸 | San Francisco, California | New Grad | [Apply](https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555) | Apr 23, 2026 |
| Figma | Data Scientist, Core Data -  PhD (2026) 🇺🇸 | New York, NY • United States<br>San Francisco, CA • New York, NY | PhD, Intern | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) | Apr 22, 2026 |
| Google | Security Engineer, Access Risk Intelligence and Security Mitigation 🇺🇸 | New York, NY, USA | Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/74402318644060870) | Apr 21, 2026 |
| Figure AI | Embedded Software Intern [Fall 2026] 🇺🇸 | San Jose, CA | Bachelors, New Grad, Intern | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4397706006) | Apr 21, 2026 |
| Snowflake | Software Engineer - Observe 🇺🇸 | US-CA-Menlo Park | Bachelors | [Apply](https://jobs.ashbyhq.com/snowflake/07e50e24-84ac-4002-ad26-9de1d991362c) | Apr 20, 2026 |
| Snowflake | Analyst, Finance Analytics & AI 🇺🇸 | US-CA-Menlo Park | - | [Apply](https://jobs.ashbyhq.com/snowflake/b241904d-7d42-41f0-9674-82e53d964846) | Apr 20, 2026 |
| Google | Data Center Technician, Global Server Operations, Hardware Operations 🇺🇸 | Lenoir, NC, USA | - | [Apply](https://www.google.com/about/careers/applications/jobs/results/81691848807981766) | Apr 20, 2026 |
| Google | Product Safety Test Engineer, Platforms 🇺🇸 | Sunnyvale, CA, USA | PhD, Masters, Bachelors | [Apply](https://www.google.com/about/careers/applications/jobs/results/119519945066193606) | Apr 16, 2026 |
| Anthropic | Software Engineer, Research Data Platform 🇺🇸 | San Francisco, CA \| New York City, NY | - | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5191226008) | Apr 16, 2026 |
| Figma | Account Executive, SMB 🇺🇸 | San Francisco, CA • New York, NY | Intern | [Apply](https://boards.greenhouse.io/figma/jobs/5694259004?gh_jid=5694259004) | Apr 15, 2026 |
| Snowflake | Product Analyst 🇺🇸 | US-CA-Menlo Park | Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/snowflake/7c53d7f5-1a7f-4fdb-a8c1-b59060d9551d) | Apr 14, 2026 |
| Anthropic | Full-Stack Software Engineer, Reinforcement Learning 🇺🇸 | San Francisco, CA \| New York City, NY | - | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5186067008) | Apr 14, 2026 |
| Cursor | Software Engineer, Agent Evaluation and Quality 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/2bbe9f02-83a5-4173-98be-9085d1cb5693) | Apr 13, 2026 |
| Etched | DFT Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/5f1f5739-3b58-467c-b351-ff183c94d96d) | Apr 13, 2026 |
| Databricks | Customer Enablement Specialist 🇺🇸 | Bellevue, Washington | - | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=8431927002) | Apr 09, 2026 |
| Databricks | Customer Enablement Specialist 🇺🇸 | Bellevue, Washington | - | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=8431935002) | Apr 09, 2026 |
| Uber | Graduate 2026 Software Engineer I, US 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters, Bachelors | [Apply](https://www.uber.com/careers/list/158009) | Apr 09, 2026 |
| Databricks | PhD GenAI Research Scientist Intern 🇺🇸 | San Francisco, California | PhD, Intern | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002) | Apr 09, 2026 |
| Anthropic | Research Engineer/Research Scientist, Pre-training 🇺🇸 | Remote-Friendly (Travel-Required) \| San Francisco, CA \| Seattle, WA \| New York City, NY | Bachelors | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/4616971008) | Apr 08, 2026 |
| Cursor | Software Engineer, Services Platform 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/0863d184-1b2f-42cd-9fca-37fa90efe2eb) | Apr 07, 2026 |
| Cursor | Software Engineer, Model Routing & Inference 🇺🇸 | New York | - | [Apply](https://jobs.ashbyhq.com/cursor/45c815b0-5100-4934-8558-0e750b8aed79) | Apr 07, 2026 |
| Cursor | Software Engineer, Storage 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/515926c1-f044-4aff-9d5f-0bb84cb7eca2) | Apr 07, 2026 |
| Cursor | Software Engineer, Infrastructure 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/6d576a09-f30d-4e5e-bb58-5d7ef56cb511) | Apr 07, 2026 |
| Cursor | Software Engineer, Core Services 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/77bf35db-119c-4533-8187-1e8d5ae08c45) | Apr 07, 2026 |
| Uber | Software Engineer II - Earner (multiple teams hiring) 🇺🇸 | Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | PhD | [Apply](https://www.uber.com/careers/list/157432) | Apr 06, 2026 |
| Notion | Software Engineer Intern (Fall 2026) 🇺🇸 | San Francisco, California | Intern | [Apply](https://jobs.ashbyhq.com/notion/5b15697c-fa91-4511-9482-c98a6ff29f90) | Apr 06, 2026 |
| Snowflake | Industry Architect – Advertising & Media 🇺🇸 | US-CA-Remote | Intern | [Apply](https://jobs.ashbyhq.com/snowflake/bd9d7653-f818-40ba-b98e-cbee8261581a) | Apr 03, 2026 |
| Anthropic | Software Engineer, Human Data Interface 🇺🇸 | San Francisco, CA \| New York City, NY | - | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5109273008) | Apr 03, 2026 |
| Uber | Software Engineer II - Discovery and Monetization 🇺🇸 | New York, New York, United States / San Francisco, California, United States / Sunnyvale, California, United States | Masters | [Apply](https://www.uber.com/careers/list/157638) | Apr 02, 2026 |
| Anthropic | Software Engineer, Sandboxing (Systems) 🇺🇸 | San Francisco, CA \| New York City, NY | - | [Apply](https://job-boards.greenhouse.io/anthropic/jobs/5025591008) | Apr 01, 2026 |
| Benchling | Software Engineer, Developer Platform 🇺🇸 | San Francisco, CA | Masters, Intern | [Apply](https://jobs.ashbyhq.com/benchling/c83238cc-1f7c-4216-b2a5-418306ca4d2b) | Mar 27, 2026 |
| Uber | Software Engineer II - Machine Learning, Marketplace/Maps/Membership/AV 🇺🇸 | New York, New York, United States / Seattle, Washington, United States / San Francisco, California, United States / Sunnyvale, California, United States | PhD, Masters, Bachelors | [Apply](https://www.uber.com/careers/list/153473) | Mar 25, 2026 |
| Sierra | Intern, Agent Development (Fall 2026) 🇺🇸 | San Francisco, CA | Intern | [Apply](https://jobs.ashbyhq.com/sierra/c74d600c-235c-4d42-8546-b178b7adefc2) | Mar 19, 2026 |
| Clay | Software Engineer, Developer Experience (AI) 🇺🇸 | New York | - | [Apply](https://jobs.ashbyhq.com/claylabs/9b008b26-189b-45cf-83d8-fee117d32874) | Mar 16, 2026 |
| Cursor | Software Engineer, Billing 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/47994d20-cc6a-436b-8da0-2eceabfd413e) | Mar 12, 2026 |
| Cursor | Software Engineer, Bugbot 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/88d47f97-0bea-448c-9abb-4720e4acf17a) | Mar 12, 2026 |
| Cursor | Software Engineer, Enterprise Platform 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/b6807f07-c4b7-4435-8c4c-0bef35865ad7) | Mar 12, 2026 |
| Figure AI | Mechanical Engineer, Battery 🇺🇸 | San Jose, CA | Masters, Bachelors | [Apply](https://job-boards.greenhouse.io/figureai/jobs/4656559006) | Feb 20, 2026 |
| Etched | RTL Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/157ed4f4-6e3b-4ec9-b93f-3e363e92041e) | Feb 07, 2026 |
| Etched | Infrastructure Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/1b073af4-6764-45ca-a22d-40a4823f0877) | Feb 07, 2026 |
| Etched | Firmware Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/699f3ab2-07e4-466c-9d76-3d4a3abb4ebc) | Feb 07, 2026 |
| Etched | Electrical Platform Intern 🇺🇸 | San Jose | Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/904ddf46-55fc-4a8f-8b49-f32cfe88116a) | Feb 07, 2026 |
| Etched | DV Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/dacedaca-c4ca-4964-85a7-8df1738005bb) | Feb 07, 2026 |
| Etched | Mech / Thermal Intern 🇺🇸 | San Jose | Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/f05e3218-5ec7-41d1-bc99-bb7014422229) | Feb 07, 2026 |
| Google | Hardware Validation Engineer, ML Products, University Graduate 🇺🇸 | Sunnyvale, CA, USA | New Grad | [Apply](https://www.google.com/about/careers/applications/jobs/results/107128442041836230) | Jan 27, 2026 |
| Cursor | Software Engineer, ML Research 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/0aa0650b-f93c-416e-9e2f-4fdf1556fd14) | Jan 27, 2026 |
| Cursor | Software Engineer, ML Infrastructure 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/c66cde5e-9cb6-4a2e-a330-9323e1edf2a9) | Jan 27, 2026 |
| Ramp | Software Engineer, Core Product 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/5fe4c64e-9336-4384-9e6f-ff32eeb3fdae) | Jan 20, 2026 |
| Recursion Pharma | Interested in an internship? 🇺🇸 | Remote Opportunity - United States<br>Salt Lake City, Utah | Intern | [Apply](https://job-boards.greenhouse.io/recursionpharmaceuticals/jobs/7540026) | Jan 20, 2026 |
| Cursor | Software Engineer, Data Infrastructure 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/8d07fe0f-34aa-458b-88e8-091469a963dc) | Jan 18, 2026 |
| Sierra | Software Engineer, Security 🇺🇸 | San Francisco, CA | - | [Apply](https://jobs.ashbyhq.com/sierra/201c6046-acb5-4fd4-a685-e993f34ec0d1) | Jan 07, 2026 |
| Cursor | Software Engineer, Developer Productivity 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/010063bd-6083-4fc0-a455-e6f0193b5347) | Dec 15, 2025 |
| Etched | Inference Intern 🇺🇸 | San Jose | PhD, Masters, Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/etched/6f23713f-5409-45b7-aae8-adb8710cdbc3) | Dec 08, 2025 |
| Google | Network Operations Residency Program, University Graduate, 2026 Start 🇺🇸 | Thornton, CO, USA | Bachelors, New Grad, Intern | [Apply](https://www.google.com/about/careers/applications/jobs/results/110139330885755590) | Nov 21, 2025 |
| Clay | Software Engineer, Backend 🇺🇸 | New York | - | [Apply](https://jobs.ashbyhq.com/claylabs/248aa0c7-034f-47d3-a57e-ce16736eeab6) | Nov 21, 2025 |
| Cursor | Software Engineer, Client Infrastructure 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/e08262e8-c089-488d-9b59-9e21f7702b64) | Nov 19, 2025 |
| Cursor | Software Engineer, Growth 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/0ec39ed7-a5dc-4551-bb26-b7f4f9fb4a74) | Oct 30, 2025 |
| Cursor | Software Engineer, Agent Harness 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/6e6f5bc2-eb32-40e2-bba9-cfa56479600d) | Oct 27, 2025 |
| Notion | Software Engineer, Product Infrastructure 🇺🇸 | San Francisco, California | - | [Apply](https://jobs.ashbyhq.com/notion/d41b635b-c17b-4efd-89fd-fdb2ddb62e9a) | Oct 03, 2025 |
| Google | Student Researcher, PhD, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / Goleta, CA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA | PhD, Intern | [Apply](https://www.google.com/about/careers/applications/jobs/results/138166347879064262) | Sep 29, 2025 |
| Google | Student Researcher, BS/MS, Winter/Summer 2026 🇺🇸 | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA / Princeton, NJ, USA | Masters, Bachelors, Intern | [Apply](https://www.google.com/about/careers/applications/jobs/results/140245524367188678) | Sep 29, 2025 |
| Cursor | Software Engineer, Security 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/94cc6684-9dbf-43f9-8ffc-405614e64ddd) | Sep 03, 2025 |
| Ramp | Software Engineer Internship, Android 🇺🇸 | New York, NY (HQ) | Bachelors, Intern | [Apply](https://jobs.ashbyhq.com/ramp/67fadb77-43d8-4449-954b-d4cf2c6d3b8b) | Aug 07, 2025 |
| Ramp | University Grad \| Software Engineer \| Frontend 🇺🇸 | New York, NY (HQ) | Bachelors | [Apply](https://jobs.ashbyhq.com/ramp/a1229aec-1105-4c47-8533-b912e732ed89) | Aug 01, 2025 |
| Ramp | Mobile Engineer, iOS 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/4859cd5e-f2a9-44d7-81f7-8bfc0e62369f) | Jul 31, 2025 |
| Ramp | Mobile Engineer, Android 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/f564dcf9-9390-4a3f-896f-8047a5086040) | Jul 31, 2025 |
| Cursor | Software Engineer, Product 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/3551cdaa-cf08-4c04-adbe-a968185bc769) | Jul 29, 2025 |
| Cursor | Software Engineer, Enterprise 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/cursor/54a9cfcd-570a-4e9c-b52c-bd2336c60991) | Jul 29, 2025 |
| Notion | Software Engineer, Data Platform 🇺🇸 | San Francisco, California | - | [Apply](https://jobs.ashbyhq.com/notion/91156750-4050-4621-aa45-0fb068308d2c) | Jul 10, 2025 |
| Warp | Product Engineer 🇺🇸 | New York | - | [Apply](https://jobs.ashbyhq.com/warp/655962db-5fbe-40cc-a072-9522295b3cbc) | Apr 23, 2025 |
| Sierra | Software Engineer, Agent 🇺🇸 | San Francisco, CA | - | [Apply](https://jobs.ashbyhq.com/sierra/e9f5fdb6-91ee-4c55-9230-41ec8865650e) | Apr 18, 2025 |
| Hugging Face | Open-Source Machine Learning Engineer - International Remote 🇺🇸 | New York, New York, United States | - | [Apply](https://apply.workable.com/j/56232F23CB) | Oct 17, 2024 |
| Physical Intelligence | Research Scientist 🇺🇸 | San Francisco | - | [Apply](https://jobs.ashbyhq.com/physicalintelligence/f83ba447-2261-4832-95db-a2f88454e0ba) | Aug 24, 2024 |
| Ramp | Software Engineer, Frontend 🇺🇸 | New York, NY (HQ) | - | [Apply](https://jobs.ashbyhq.com/ramp/4e64ab86-4e30-403b-b1b9-41dc052570ce) | Mar 09, 2023 |


<details>
<summary><b>Closed positions (217)</b> &mdash; click to expand</summary>


| Company | Role | Location | Education | Apply | Date Posted |
|---------|------|----------|-----------|-------|-------------|
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 23, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 23, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 23, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 23, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 23, 2026 |
| ~~Adobe~~ | ~~Software Development Engineer 3 🇺🇸~~ | 5 Locations | - | Closed | May 23, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~LinkedIn~~ | ~~Fellow, Software Engineering- Infrastructure 🇺🇸~~ | Mountain View, CA | - | Closed | May 22, 2026 |
| ~~Uber~~ | ~~Software Engineer II - Back-end & ML/AI Infra 🇺🇸~~ | Seattle, Washington, United States | Masters, Bachelors | Closed | May 21, 2026 |
| ~~Nvidia~~ | ~~PhD Data Generation and User Simulation Research Intern — Fall 2026 🇺🇸~~ | US, CA, Santa Clara | PhD, Intern | Closed | May 21, 2026 |
| ~~Microsoft~~ | ~~Software Engineer II 🇺🇸~~ | Hyderabad, TS, IN / Noida, UP, IN / Bengaluru, KA, IN | - | Closed | May 21, 2026 |
| ~~DoorDash~~ | ~~Software Engineer, Machine Learning - Fraud 🇺🇸~~ | Sunnyvale, CA<br>San Francisco, CA | PhD, Masters | Closed | May 21, 2026 |
| ~~Microsoft~~ | ~~Stagiaire en opérations critiques / Critical Environment Ops INTERN 🇺🇸~~ | Québec City, QC, CA / Montreal, QC, CA | Intern | Closed | May 21, 2026 |
| ~~MongoDB~~ | ~~Software Engineer 3, Backup 🇺🇸~~ | New York City | - | Closed | May 20, 2026 |
| ~~Google~~ | ~~Network Operations Residency Program, University Graduate, August 2026 Start 🇺🇸~~ | Atlanta, GA, USA | New Grad | Closed | May 20, 2026 |
| ~~Roblox~~ | ~~[2026] Design & Creative Fellowship 🇺🇸~~ | San Mateo, CA, United States | - | Closed | May 20, 2026 |
| ~~Microsoft~~ | ~~Critical Environment Ops INTERN 🇺🇸~~ | ON,CA | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~GTM Intern - Fall 2026 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~PD Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Firmware Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Core Ops Intern - Spring 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~DFT Intern - Fall 2026 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Firmware Intern - Fall 2026 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Supercomputing Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~GTM Intern - Spring 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Talent Intern - Spring 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Supercomputing Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Inference Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Core Ops Intern - Summer 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~DV Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~PD Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Talent Intern - Summer 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~DV Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~DFT Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Infrastructure Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~DFT Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~GTM Intern - Summer 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Infrastructure Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Firmware Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Talent Intern - Fall 2026 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Electrical Platform Intern - Spring 2027 🇺🇸~~ | San Jose | Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Finance Intern - Summer 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Electrical Platform Intern - Summer 2027 🇺🇸~~ | San Jose | Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~ChipSim Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Finance Intern - Fall 2026 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Thermo-Mech CFD Simulation Intern - Summer 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Inference Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Mech / Thermal Intern - Fall 2026 🇺🇸~~ | San Jose | Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Thermo-Mech CFD Simulation Intern - Spring 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~ChipSim Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Infrastructure Intern - Fall 2026 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Finance Intern - Spring 2027 🇺🇸~~ | San Jose | Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Mech / Thermal Intern - Summer 2027 🇺🇸~~ | San Jose | Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~RTL Intern - Spring 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~RTL Intern - Summer 2027 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Etched~~ | ~~Mech / Thermal Intern - Spring 2027 🇺🇸~~ | San Jose | Masters, Bachelors, Intern | Closed | May 19, 2026 |
| ~~Uber~~ | ~~Software Engineer II, U4B Employee Mobility 🇺🇸~~ | San Francisco, California, United States / Sunnyvale, California, United States | Bachelors | Closed | May 18, 2026 |
| ~~Nvidia~~ | ~~Technical Marketing Engineering Intern, Robotics - Fall 2026 🇺🇸~~ | US, CA, Santa Clara | Intern | Closed | May 18, 2026 |
| ~~Reddit~~ | ~~iOS Software Engineer, Contributions 🇺🇸~~ | Remote - United States | Bachelors, Intern | Closed | May 14, 2026 |
| ~~Microsoft~~ | ~~Critical Environment Technician Intern 🇺🇸~~ | Middenmeer, NH, NL | Intern | Closed | May 14, 2026 |
| ~~Lambda Labs~~ | ~~Capital Markets & Corporate Development Intern - Summer 2026 🇺🇸~~ | San Francisco Office (Fremont St) | Intern | Closed | May 14, 2026 |
| ~~Microsoft~~ | ~~Cambridge Internship: Novel Light Source Design 🇺🇸~~ | Cambridge, England, GB | Intern | Closed | May 13, 2026 |
| ~~Airbnb~~ | ~~Data Science Intern 🇺🇸~~ | United States | Intern | Closed | May 13, 2026 |
| ~~Point72~~ | ~~Point72 Academy Investment Analyst Program for Upcoming Graduates (2027 – US) 🇺🇸~~ | Chicago, Florida, New York, San Francisco | - | Closed | May 11, 2026 |
| ~~Nvidia~~ | ~~GPU System and Scheduling Architect - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | May 10, 2026 |
| ~~Scale AI~~ | ~~National Security Hackathon 2026 - General Interest 🇺🇸~~ | San Francisco, CA<br>New York, NY<br>Washington, DC | - | Closed | May 08, 2026 |
| ~~Nvidia~~ | ~~ASIC Floorplan Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | May 07, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Agents & Efficiency 🇺🇸~~ | Cambridge, England, GB | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Intelligent Quantum Systems Architecture 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Fault Tolerant Quantum System Architecture 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Frontiers 🇺🇸~~ | Redmond, WA, US | Intern | Closed | May 06, 2026 |
| ~~Microsoft~~ | ~~Stagiaire Technicien de Centre de Données / Datacenter Technician Intern 🇺🇸~~ | Québec City, QC, CA | Intern | Closed | May 01, 2026 |
| ~~Nvidia~~ | ~~GPU Power Architect - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | May 01, 2026 |
| ~~Microsoft~~ | ~~Security Research Intern - AI Focus 🇺🇸~~ | Herzliya, Tel Aviv District, IL | Intern | Closed | Apr 28, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Socio-Technical Workflow Analysis 🇺🇸~~ | Redmond, WA, US / Cambridge, MA, US | Intern | Closed | Apr 28, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Audio and Acoustics 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Apr 23, 2026 |
| ~~Figma~~ | ~~Inside Sales Representative - Early Career (2026) 🇺🇸~~ | San Francisco, CA • New York, NY | New Grad | Closed | Apr 23, 2026 |
| ~~Nvidia~~ | ~~Deep Learning Architect, LLM Inference - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 22, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Computer Vision and Deep Learning 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~AI Chip Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~AI Chip Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~Cell Modeling and Verification Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~Circuit Design Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~Deep Learning Kernel Software Performance Architect - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~Research Scientist, Generative AI for Physical AI - PhD New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | PhD, New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~Signoff Methodology Engineer - New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~SoC ASIC Verification Engineer – New College Grad 2026 🇺🇸~~ | US, CA, Santa Clara | New Grad | Closed | Apr 21, 2026 |
| ~~Nvidia~~ | ~~ASIC Hardware Design Engineer - New College Grad 2026 🇺🇸~~ | US, TX, Austin | New Grad | Closed | Apr 21, 2026 |
| ~~Point72~~ | ~~Point72 Academy 2026-2027 Investment Analyst Program for Experienced Professionals - US 🇺🇸~~ | Chicago, Florida, New York, San Francisco | - | Closed | Apr 09, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Inference Economics and Human Agency 🇺🇸~~ | Redmond, WA, US / New York, NY, US | Intern | Closed | Apr 03, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Applied Power Systems Analysis 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Apr 03, 2026 |
| ~~Etched~~ | ~~Technical Recruiter (Entry Level) 🇺🇸~~ | San Jose | New Grad | Closed | Apr 02, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Foundation Models and Agentic Systems 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Apr 01, 2026 |
| ~~Figure AI~~ | ~~Hardware Reliability Intern [Summer 2026] 🇺🇸~~ | San Jose, CA | Intern | Closed | Mar 31, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Safety and Security 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Mar 05, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Cryptography and Applications 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Feb 20, 2026 |
| ~~Etched~~ | ~~Supercomputing Intern - Summer 2026 🇺🇸~~ | San Jose | PhD, Masters, Bachelors, Intern | Closed | Feb 07, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Azure Storage 🇺🇸~~ | Redmond, WA, US / Mountain View, CA, US | Intern | Closed | Feb 06, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Applied Speech Research 🇺🇸~~ | Berkeley, CA, US / Burlington, MA, US | Intern | Closed | Feb 04, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Agentic Programming 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Feb 03, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Applied Sciences Group 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 28, 2026 |
| ~~Google~~ | ~~Hardware Test Engineer, University Graduate, Platforms Infrastructure 🇺🇸~~ | Sunnyvale, CA, USA | New Grad | Closed | Jan 27, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Systems and Tools 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 27, 2026 |
| ~~Google~~ | ~~Hardware Test Engineer, University Graduate, Platforms Infrastructure 🇺🇸~~ | Sunnyvale, CA, USA | New Grad | Closed | Jan 27, 2026 |
| ~~Google~~ | ~~Hardware Validation Engineer, ML Products, University Graduate 🇺🇸~~ | Sunnyvale, CA, USA | New Grad | Closed | Jan 27, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Multi-Modal Sensing & Secure AI Devices 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 22, 2026 |
| ~~Google~~ | ~~Silicon CAD Engineer, University Graduate, PhD 🇺🇸~~ | Sunnyvale, CA, USA | PhD, New Grad | Closed | Jan 22, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Bayesian Methods in Geometric Computer Vision 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 21, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Office of the Chief Scientific Officer 🇺🇸~~ | Mountain View, CA, US | Intern | Closed | Jan 20, 2026 |
| ~~Microsoft~~ | ~~Research Intern - AI Evaluation and Alignment 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 16, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Foundations of GenAI 🇺🇸~~ | New York, NY, US | Intern | Closed | Jan 13, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Security, Privacy and AI 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Jan 12, 2026 |
| ~~Microsoft~~ | ~~Research Intern - Machine Learning and Optimization 🇺🇸~~ | Cambridge, MA, US / Redmond, WA, US | Intern | Closed | Dec 31, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Quantum Error Correction 🇺🇸~~ | Redmond, WA, US / Santa Barbara, CA, US | Intern | Closed | Dec 18, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Human-AI Interaction Research and Design (Health AI) 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 17, 2025 |
| ~~Microsoft~~ | ~~Research Intern - LLM Performance Optimization 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 16, 2025 |
| ~~Google~~ | ~~Hardware Architecture Modeling Engineer, PhD, University Graduate 🇺🇸~~ | Sunnyvale, CA, USA | PhD, New Grad | Closed | Dec 15, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI System Architecture Modeling and Performance 🇺🇸~~ | Hillsboro, OR, US | Intern | Closed | Dec 11, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Microsoft Teams (PhD) 🇺🇸~~ | Redmond, WA, US | PhD, Intern | Closed | Dec 09, 2025 |
| ~~Microsoft~~ | ~~Research Intern - OneDrive and SharePoint (Summer 2026) 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 09, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Office of the Chief Scientific Officer 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 09, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Diagnostic Imaging AI, Imaging Computing, Reconstruction and Inverse Problem 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 09, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Hardware 🇺🇸~~ | Vancouver, BC, CA | Intern | Closed | Dec 08, 2025 |
| ~~Etched~~ | ~~Talent Intern - Summer 2026 🇺🇸~~ | San Jose | Intern | Closed | Dec 08, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Frameworks (Network Systems and Tools) 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 05, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Network Observability 🇺🇸~~ | Mountain View, CA, US / Redmond, WA, US | Intern | Closed | Dec 05, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Computational Social Science 🇺🇸~~ | New York, NY, US | Intern | Closed | Dec 05, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Deep Learning Group 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 02, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI/ML Numerics & Efficiency 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 02, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AIP AI Knowledge Multimodal AI 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 02, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Office of Applied Research 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Dec 01, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Data Center and AI Networking 🇺🇸~~ | Mountain View, CA, US | Intern | Closed | Dec 01, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Technology for Religious Empowerment 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 26, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Memory & Orchestration in Large Language Models 🇺🇸~~ | Redmond, WA, US / Silverdale, WA, US | Intern | Closed | Nov 26, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Systems & Architecture 🇺🇸~~ | Mountain View, CA, US / Redmond, WA, US | Intern | Closed | Nov 26, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Data Center and AI Networking 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 26, 2025 |
| ~~Microsoft~~ | ~~Research Intern - MSR Inclusive Futures Team 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 26, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Medical Image Reconstruction 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 25, 2025 |
| ~~Microsoft~~ | ~~Research Intern - MSR Montreal / ML Team 🇺🇸~~ | Montreal, QC, CA | Intern | Closed | Nov 25, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Multimodal Language Models 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Model Optimization and HW Acceleration 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Training Methods for LLM Efficiency 🇺🇸~~ | Mountain View, CA, US | Intern | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Machine Learning and Optimization - Redmond 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Economics and Computation 🇺🇸~~ | Cambridge, MA, US / New York, NY, US / Redmond, WA, US | Intern | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Microsoft Research Special Projects 🇺🇸~~ | Redmond, WA, US / Cambridge, MA, US / Silverdale, WA, US | Intern | Closed | Nov 21, 2025 |
| ~~Google~~ | ~~Network Operations Residency Program, University Graduate, 2026 Start 🇺🇸~~ | Thornton, CO, USA | New Grad | Closed | Nov 21, 2025 |
| ~~Microsoft~~ | ~~Research Intern - LLM Acceleration 🇺🇸~~ | Mountain View, CA, US / Cambridge, MA, US | Intern | Closed | Nov 20, 2025 |
| ~~Microsoft~~ | ~~Research Intern - STAC, NYC (Sociotechnical Alignment Center) 🇺🇸~~ | New York, NY, US | Intern | Closed | Nov 20, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Artificial Intelligence 🇺🇸~~ | Vancouver, BC, CA | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - ML and Computational Biology for the Immune System 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Machine Learning at MSR NYC 🇺🇸~~ | New York, NY, US / Cambridge, MA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - RiSE group 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Data Systems 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Gray Systems Lab (GSL) 🇺🇸~~ | Redmond, WA, US / Mountain View, CA, US / Madison, WI, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Fundamentals of AI: Security, Agents, Systems & Control 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Hardware 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - MSR AI Interaction and Learning 🇺🇸~~ | Redmond, WA, US / New York, NY, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - MSR Software-Hardware Co-design 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - MSR Systems Research Group - Redmond 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Computer Vision and Deep Learning 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Systems For Efficient AI 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Reliability of Cloud and AI Systems 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - AI Frontiers - Reasoning & Agentic Models 🇺🇸~~ | Redmond, WA, US / New York, NY, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Hardware/Software Codesign 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Machine Learning and Statistics 🇺🇸~~ | Cambridge, MA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Systems for Reliable and Scalable AI Agents 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Artificial Intelligence 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Azure Research - Systems 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Networking Research Group 🇺🇸~~ | Redmond, WA, US | Intern | Closed | Nov 19, 2025 |
| ~~Microsoft~~ | ~~Research Intern - Foundations of Generative AI 🇺🇸~~ | New York, NY, US / Redmond, WA, US | Intern | Closed | Nov 18, 2025 |
| ~~Google~~ | ~~Student Researcher, PhD, Winter/Summer 2026 🇺🇸~~ | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / Goleta, CA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA | PhD | Closed | Sep 29, 2025 |
| ~~Google~~ | ~~Student Researcher, BS/MS, Winter/Summer 2026 🇺🇸~~ | Mountain View, CA, USA / Ann Arbor, MI, USA / Atlanta, GA, USA / Austin, TX, USA / Cambridge, MA, USA / Chicago, IL, USA / Irvine, CA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / New York, NY, USA / Palo Alto, CA, USA / Pittsburgh, PA, USA / San Bruno, CA, USA / Seattle, WA, USA / San Francisco, CA, USA / Sunnyvale, CA, USA / Washington D.C., DC, USA / Princeton, NJ, USA | Masters | Closed | Sep 29, 2025 |
| ~~Google~~ | ~~Software Engineer, PhD, Early Career, Embedded Systems and Firmware, 2026 Start 🇺🇸~~ | Sunnyvale, CA, USA / Atlanta, GA, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / Seattle, WA, USA | PhD, New Grad | Closed | Aug 26, 2025 |
| ~~Google~~ | ~~Software Engineer, PhD, Early Career, Infrastructure, 2026 Start 🇺🇸~~ | Sunnyvale, CA, USA / Atlanta, GA, USA / Austin, TX, USA / Kirkland, WA, USA / Los Angeles, CA, USA / Madison, WI, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / San Bruno, CA, USA / Seattle, WA, USA | PhD, New Grad | Closed | Aug 26, 2025 |
| ~~Google~~ | ~~Software Engineer, PhD, Early Career, AI/Machine Learning, 2026 Start 🇺🇸~~ | Sunnyvale, CA, USA / Atlanta, GA, USA / Kirkland, WA, USA / Madison, WI, USA / Mountain View, CA, USA / New York, NY, USA / Raleigh, NC, USA / Durham, NC, USA / San Bruno, CA, USA / Seattle, WA, USA | PhD, New Grad | Closed | Aug 26, 2025 |
| ~~Google~~ | ~~Software Engineer, Systems Research, PhD, Early Career 🇺🇸~~ | Sunnyvale, CA, USA / Seattle, WA, USA | PhD, New Grad | Closed | Jan 29, 2025 |

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

