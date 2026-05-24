# Eval improvement recommendations
**Metrics:** precision 40.6% | recall 96.4% | precision on regex+ 40.6% | FP=593 FN=15
**Budget (FAIL):** FP ≤ 6 (got 593), FN ≤ 0 (got 15)

## Suggested fixes (by impact)

### 1. False positives: `explicit ec technical` (322 jobs)
Tighten filters for 'explicit ec technical' (e.g. senior level, YOE bar, non-dev titles).
- **xAI** — Member of Technical Staff
  - https://job-boards.greenhouse.io/xai/jobs/5044403007
- **xAI** — Security Engineer - Detection & Response
  - https://job-boards.greenhouse.io/xai/jobs/5008186007
- **xAI** — Software Engineer - Data
  - https://job-boards.greenhouse.io/xai/jobs/5124616007

### 2. False positives: `explicit ec technical (requirements)` (115 jobs)
Tighten filters for 'explicit ec technical (requirements)' (e.g. senior level, YOE bar, non-dev titles).
- **Scale AI** — Machine Learning Research Engineer, Agents - Enterprise GenAI
  - https://job-boards.greenhouse.io/scaleai/jobs/4625344005
- **DRW** — Trading Systems Engineer
  - https://job-boards.greenhouse.io/drweng/jobs/6776683
- **Point72** — Data Engineer
  - https://boards.greenhouse.io/point72/jobs/7829230002?gh_jid=7829230002

### 3. False positives: `implicit ec technical` (41 jobs)
Tighten filters for 'implicit ec technical' (e.g. senior level, YOE bar, non-dev titles).
- **OpenAI** — Networking Operating System Firmware Engineer
  - https://jobs.ashbyhq.com/openai/f6b9903c-9034-436b-a4ec-4c8643a6d0dd
- **Veeva Systems** — Associate Automation Engineer - RTSM
  - https://jobs.lever.co/veeva/21f44b64-3f46-47ea-bf53-3db0f8e4199b
- **Veeva Systems** — Associate Automation Engineer - RTSM
  - https://jobs.lever.co/veeva/48287009-b3b3-49b8-bc20-affe6be39fd2

### 4. False positives: `open-level technical ic` (40 jobs)
Tighten filters for 'open-level technical ic' (e.g. senior level, YOE bar, non-dev titles).
- **Glean** — Software Engineer, Billing & Revenue Platform
  - https://job-boards.greenhouse.io/gleanwork/jobs/4675862005
- **CoreWeave** — Software Engineer, Observability
  - https://coreweave.com/careers/job?4587675006&board=coreweave&gh_jid=4587675006
- **DRW** — Software Engineer, Cumberland/FICCO Tools Engineering
  - https://job-boards.greenhouse.io/drweng/jobs/7288315

### 5. False positives: `entry-level research or ds` (34 jobs)
Tighten filters for 'entry-level research or ds' (e.g. senior level, YOE bar, non-dev titles).
- **Anthropic** — Research Engineer, Economic Research Data Platform
  - https://job-boards.greenhouse.io/anthropic/jobs/5071132008
- **Anthropic** — Research Engineer, Pretraining
  - https://job-boards.greenhouse.io/anthropic/jobs/5119713008
- **Anthropic** — Research Engineer / Research Scientist, Pre-training
  - https://job-boards.greenhouse.io/anthropic/jobs/5135168008

### 6. False positives: `technical intern` (30 jobs)
Tighten filters for 'technical intern' (e.g. senior level, YOE bar, non-dev titles).
- **Perplexity AI** — UK Internship Program
  - https://jobs.ashbyhq.com/perplexity/79a07e2d-6150-4929-80fe-bbe13a641763
- **Cloudflare** — DCSC Automation Coordinator Intern
  - https://boards.greenhouse.io/cloudflare/jobs/7751595?gh_jid=7751595
- **Cloudflare** — Global Trade Compliance Intern (Summer 2026)
  - https://boards.greenhouse.io/cloudflare/jobs/7799138?gh_jid=7799138

### 7. False positives: `spacex early swe credential` (10 jobs)
Tighten filters for 'spacex early swe credential' (e.g. senior level, YOE bar, non-dev titles).
- **SpaceX** — Application Software Engineer
  - https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002
- **SpaceX** — Application Software Engineer, Data
  - https://boards.greenhouse.io/spacex/jobs/8420526002?gh_jid=8420526002
- **SpaceX** — Full Stack Software Engineer (Application Software)
  - https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002

### 8. False positives: `fellowship program` (1 jobs)
Tighten filters for 'fellowship program' (e.g. senior level, YOE bar, non-dev titles).
- **Palantir** — American Tech Fellowship for Veterans
  - https://jobs.lever.co/palantir/b88cd6e1-22b7-49d6-b215-1ca262a05728

### 9. False negatives: `SpaceX Level I SWE/embedded role (bachelor + internship/1yr bar)` (12 jobs)
Broaden or add signal for cases labeled 'SpaceX Level I SWE/embedded role (bachelor + internship/1yr bar)'.
- **SpaceX** — Embedded Security Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8543670002?gh_jid=8543670002
- **SpaceX** — Embedded Security Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8459609002?gh_jid=8459609002
- **SpaceX** — Embedded Software Engineer (Starlink)
  - https://boards.greenhouse.io/spacex/jobs/8379277002?gh_jid=8379277002

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
