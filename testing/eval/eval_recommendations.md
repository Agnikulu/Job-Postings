# Eval improvement recommendations
**Metrics:** precision 52.9% | recall 95.0% | precision on regex+ 52.9% | FP=355 FN=21
**Budget (FAIL):** FP ≤ 6 (got 355), FN ≤ 0 (got 21)

## Suggested fixes (by impact)

### 1. False positives: `explicit ec technical` (170 jobs)
Tighten filters for 'explicit ec technical' (e.g. senior level, YOE bar, non-dev titles).
- **xAI** — Member of Technical Staff
  - https://job-boards.greenhouse.io/xai/jobs/5044403007
- **xAI** — Security Engineer - Detection & Response
  - https://job-boards.greenhouse.io/xai/jobs/5008186007
- **xAI** — Software Engineer - Data
  - https://job-boards.greenhouse.io/xai/jobs/5124616007

### 2. False positives: `explicit ec technical (requirements)` (99 jobs)
Tighten filters for 'explicit ec technical (requirements)' (e.g. senior level, YOE bar, non-dev titles).
- **Scale AI** — Machine Learning Research Engineer, Agents - Enterprise GenAI
  - https://job-boards.greenhouse.io/scaleai/jobs/4625344005
- **Point72** — Data Engineer
  - https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002
- **Point72** — Machine Learning Engineer
  - https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002

### 3. False positives: `entry-level research or ds` (27 jobs)
Tighten filters for 'entry-level research or ds' (e.g. senior level, YOE bar, non-dev titles).
- **Xaira Therapeutics** — AI Research Engineer
  - https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007
- **Adobe** — Data Scientist
  - https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/Data-Scientist_R165959-1
- **Meta** — AI Research Scientist, CoreML - Monetization AI
  - https://www.linkedin.com/jobs/view/4246321800

### 4. False positives: `open-level technical ic` (23 jobs)
Tighten filters for 'open-level technical ic' (e.g. senior level, YOE bar, non-dev titles).
- **Glean** — Software Engineer, Billing & Revenue Platform
  - https://job-boards.greenhouse.io/gleanwork/jobs/4675862005
- **CoreWeave** — Software Engineer, Observability
  - https://coreweave.com/careers/job?4587675006&board=coreweave&gh_jid=4587675006
- **Ramp** — Software Engineer, Core Product
  - https://jobs.ashbyhq.com/ramp/5fe4c64e-9336-4384-9e6f-ff32eeb3fdae

### 5. False positives: `implicit ec technical` (22 jobs)
Tighten filters for 'implicit ec technical' (e.g. senior level, YOE bar, non-dev titles).
- **OpenAI** — Networking Operating System Firmware Engineer
  - https://jobs.ashbyhq.com/openai/f6b9903c-9034-436b-a4ec-4c8643a6d0dd
- **Veeva Systems** — Associate Automation Engineer - RTSM
  - https://jobs.lever.co/veeva/21f44b64-3f46-47ea-bf53-3db0f8e4199b
- **Veeva Systems** — Associate Automation Engineer - RTSM
  - https://jobs.lever.co/veeva/48287009-b3b3-49b8-bc20-affe6be39fd2

### 6. False positives: `spacex early swe credential` (10 jobs)
Tighten filters for 'spacex early swe credential' (e.g. senior level, YOE bar, non-dev titles).
- **SpaceX** — Application Software Engineer
  - https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002
- **SpaceX** — Application Software Engineer, Data
  - https://boards.greenhouse.io/spacex/jobs/8420526002?gh_jid=8420526002
- **SpaceX** — Full Stack Software Engineer (Application Software)
  - https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002

### 7. False positives: `technical intern` (4 jobs)
Tighten filters for 'technical intern' (e.g. senior level, YOE bar, non-dev titles).
- **Skydio** — Supply Chain Intern
  - https://jobs.ashbyhq.com/skydio/2d21f482-3224-4906-a1bb-6a64436774cb
- **Inceptive** — Internship
  - https://job-boards.greenhouse.io/inceptive/jobs/5103191007
- **Recursion Pharma** — Interested in an internship?
  - https://job-boards.greenhouse.io/recursionpharmaceuticals/jobs/7540026

### 8. False negatives: `SpaceX Level I SWE/embedded role (bachelor + internship/1yr bar)` (12 jobs)
Broaden or add signal for cases labeled 'SpaceX Level I SWE/embedded role (bachelor + internship/1yr bar)'.
- **SpaceX** — Embedded Security Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8543670002?gh_jid=8543670002
- **SpaceX** — Embedded Security Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8459609002?gh_jid=8459609002
- **SpaceX** — Embedded Software Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8379277002?gh_jid=8379277002

### 9. False negatives: `Fall 2026 engineering/software intern or co-op (US sites)` (3 jobs)
Broaden or add signal for cases labeled 'Fall 2026 engineering/software intern or co-op (US sites)'.
- **SpaceX** — Fall 2026 Engineering Internship/Co-op
  - https://boards.greenhouse.io/spacex/jobs/8403206002?gh_jid=8403206002
- **SpaceX** — Fall 2026 Graduate Engineer Internship/Co-op
  - https://boards.greenhouse.io/spacex/jobs/8403223002?gh_jid=8403223002
- **SpaceX** — Fall 2026 Software Engineering Internship/Co-op
  - https://boards.greenhouse.io/spacex/jobs/8403219002?gh_jid=8403219002

### 10. False negatives: `SpaceX early SWE bar (BS + 1yr including internship)` (1 jobs)
Broaden or add signal for cases labeled 'SpaceX early SWE bar (BS + 1yr including internship)'.
- **SpaceX** — Software Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8379301002?gh_jid=8379301002

### 11. False negatives: `Welding Build Engineer (Starship); ec keyword in title/requirements` (1 jobs)
Broaden or add signal for cases labeled 'Welding Build Engineer (Starship); ec keyword in title/requirements'.
- **SpaceX** — Welding Build Engineer (Starship)
  - https://boards.greenhouse.io/spacex/jobs/8550354002?gh_jid=8550354002

### 12. False negatives: `Graduate 2026 PhD Software Engineer II (AV Labs…; explicit ec title` (1 jobs)
Broaden or add signal for cases labeled 'Graduate 2026 PhD Software Engineer II (AV Labs…; explicit ec title'.
- **Uber** — Graduate 2026 PhD Software Engineer II (AV Labs), United States
  - https://www.uber.com/careers/list/159120

### 13. False negatives: `2026 AI/ML Intern - Machine Learning Engineer; early-career technical US role (hand-reviewed)` (1 jobs)
Broaden or add signal for cases labeled '2026 AI/ML Intern - Machine Learning Engineer; early-career technical US role (hand-reviewed)'.
- **Adobe** — 2026 AI/ML Intern - Machine Learning Engineer
  - https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer_R158493

### 14. False negatives: `2026 AI/ML Intern - Machine Learning Engineer/Researche; early-career technical US role (hand-reviewed)` (1 jobs)
Broaden or add signal for cases labeled '2026 AI/ML Intern - Machine Learning Engineer/Researche; early-career technical US role (hand-reviewed)'.
- **Adobe** — 2026 AI/ML Intern - Machine Learning Engineer/Researcher  Intern
  - https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-AI-ML-Intern---Machine-Learning-Engineer-Intern_R160706

### 15. False negatives: `2026 Intern - Research Scientist/Engineer; early-career technical US role (hand-reviewed)` (1 jobs)
Broaden or add signal for cases labeled '2026 Intern - Research Scientist/Engineer; early-career technical US role (hand-reviewed)'.
- **Adobe** — 2026 Intern - Research Scientist/Engineer
  - https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Research-Scientist-Engineer_R160317
