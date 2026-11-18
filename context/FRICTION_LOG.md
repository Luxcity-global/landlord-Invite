# Proptii Onboarding Friction Log & Operating Protocol

> **Source of Truth & Operational Guide**
> **Live Google Sheet:** [Proptii - Onboarding Friction Log (Google Sheets)](https://docs.google.com/spreadsheets/d/1dvwE-CiY89uDOpFnxzv0ldqOONYRc4MEPamxK8HVfjQ/edit)
> **Mandate:** Own onboarding friction. Observe live landlord sessions, record raw friction points, and ship the highest-impact UI/UX fix within 48 hours (2 working days).
> **Related Local Files:** 
> - Excel Master: `context/Proptii_Friction_Log_Master.xlsx`
> - CSV Import Template: `context/FRICTION_LOG_TEMPLATE.csv`
> - Onboarding Checklist UI: `src/onboarding-checklist.html`
> - Sprint Plan: `context/SPRINT_PLAN.md`

---

## 1. Observer Protocol for Live Onboarding Calls

The CEO conducts the live call with the landlord; you attend as a dedicated observer and scribe.

* **Golden Rule of Observation:** **Remain completely silent** unless the CEO explicitly addresses you. The moment you offer guidance, explain a UI element, or assist the landlord, you invalidate the test and obscure where they would have stumbled on their own.
* **Primary Focus Window (Steps 2 through 5):**
  * **Step 2:** Adding their first property.
  * **Step 3:** Booking or logging a real viewing.
  * **Step 4:** Sending the first invite to a tenant.
  * **Step 5:** Response to the qualitative question: *"What nearly stopped you?"*
* **Logging Discipline:** Record each friction event immediately during the call or within 10 minutes of completion.

---

## 2. Standard Schema & Column Specifications

Every logged incident requires the **7 Core Columns** from the brief, plus operational tracking attributes:

| Column | Header Name | Description & Strict Input Standards |
| :--- | :--- | :--- |
| **1** | `Log ID` | Unique identifier (e.g., `FRIC-001`, `FRIC-002`). |
| **2** | `Date` | Date of the onboarding session (`YYYY-MM-DD`). |
| **3** | `Landlord` | Landlord full name, or anonymized code from account log (e.g., `LL-104`). |
| **4** | `Checklist Step` | Exact step where friction occurred (Steps 1–6, or Pre-Call Audit). |
| **5** | `What Happened` | **Objective factual record** of observed behavior. State what happened on screen, not speculation or root-cause theory. |
| **6** | `Their Words` | **Word-for-word verbatim quote** spoken by the landlord when stuck. |
| **7** | `Severity` | Categorized as **`Blocks`**, **`Slows`**, or **`Annoys`** (see hierarchy below). |
| **8** | `Proposed Fix` | Specific, actionable UI, copy, or engineering intervention. |
| **9** | `Status` | `Open`, `In Progress`, `Shipped`, or `Won't Fix`. |
| **10** | `Fix SLA / Target` | 48-hour deadline for top fix from call date. |
| **11** | `Language Bank?` | `Yes` / `No` — flag whether phrasing should be captured in `context/LANGUAGE_BANK.md`. |

---

## 3. Prioritization Hierarchy & SLAs

Friction items are prioritized strictly by impact to user completion:

$$\text{Blocks} \succ \text{Slows} \succ \text{Annoys}$$

1. **`Blocks` (Critical):** The landlord is unable to continue the workflow without external intervention or gives up entirely.
   * *Resolution SLA:* Must be triaged immediately; top blocker must ship within **2 working days (48 hours)**.
2. **`Slows` (Major):** The landlord completes the step, but hesitates, requires verbal steering, or experiences noticeable confusion.
   * *Resolution SLA:* Reviewed in Tuesday/Thursday reviews; resolved in the current or subsequent sprint.
3. **`Annoys` (Minor):** The landlord completes the step unaided, but expresses mild irritation or notes an awkward pattern.
   * *Resolution SLA:* Batched into periodic UX polish releases.
4. **Tie-Breaker Rule:** When two friction points share the same severity, prioritize the fix that impacts the higher volume of landlords.
5. **Language Bank Ingestion:** Any verbatim phrasing that reveals real customer mental models, landlord terminology, or copy clarity must be logged directly into `context/LANGUAGE_BANK.md`.

---

## 4. Weekly Operating Cadence

| Cadence | Forum / Channel | Mandatory Action |
| :--- | :--- | :--- |
| **09:30 Daily** | Google Chat Digest | Review automated activity digest; flag newly stalled landlords or drop-offs. |
| **11:00 Daily** | 15-Minute Stand-up | Report raw observations from recent calls and status of active 48-hour fixes. |
| **Monday Post-Standup** | 30-Minute Sprint Kick-off | Present the **Top 3 Open Friction Items** to PM and Engineering. |
| **Tue & Thu** | 30-Minute Friction Review | Co-run with CEO & PM using this log. **Commit to 1 concrete shipped fix per session.** |
| **Friday Afternoon** | Gate Review | Audit shipped fixes versus open backlog; review resolution velocity. |
| **Week 4 Milestone** | PM Handoff (Tue 8 Dec) | Deliver comprehensive self-serve onboarding spec synthesized from all log entries. |

---

## 5. Live Friction Log (Baseline & Seed Entries)

*The four baseline fixes identified during the initial landlord & tenant dashboard audit:*

| Log ID | Date | Landlord / Account | Step | What Happened (Objective Observation) | Their Words (Verbatim) | Severity | Proposed Fix | Status | Target Date | Lang Bank? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FRIC-001` | 2026-11-12 | System Baseline Audit | Pre-Call Audit | Tenant dashboard empty states: Panels state only that nothing exists yet (no referencing, viewings, saved properties). | *"Where do I go from here?" / "Nothing happens when I log in."* | **Blocks** | Replace each empty state with one concrete next action, offering Property Intelligence report where relevant. | `IN_PROGRESS` | 2026-11-14 | No |
| `FRIC-002` | 2026-11-12 | System Baseline Audit | Pre-Call Audit | Locked navigation items: Contracts and tenant referencing tabs display a padlock icon with zero explanation. | *"Why is referencing locked? Do I have to pay first?"* | **Blocks** | Explicitly state what criteria unlocks each tab and provide direct link to trigger that action. | `IN_PROGRESS` | 2026-11-14 | No |
| `FRIC-003` | 2026-11-12 | System Baseline Audit | Pre-Call Audit | Intelligence reports misfiled: Filed under tenancy agreements on landlord dashboard; under contract alerts on tenant dashboard. | *"Where is the EPC and planning report I ran earlier?"* | **Slows** | Reclassify reports into distinct document type; coordinate data migration with Head of Engineering. | `OPEN` | 2026-11-17 | No |
| `FRIC-004` | 2026-11-12 | System Baseline Audit | Pre-Call Audit | Landlord analytics panel: Large empty card with low utility during quiet periods. | *"Is this broken or just empty?"* | **Annoys** | Add proactive portfolio prompts (compliance reminders: Gas Safety, EICR, EPC expiry) to give recurring weekly value. | `OPEN` | 2026-11-20 | No |

---

## 6. How to Use with Google Sheets

1. **Option A (Instant Open & Sync):** Upload `context/Proptii_Friction_Log_Master.xlsx` directly to Google Drive. Right-click and choose **Open with Google Sheets**. It includes:
   - Frozen headers & Proptii brand typography/colors (`#004B71` Navy, `#136C9E` Blue, `#DC5F12` Orange).
   - Pre-configured Data Validation dropdowns for `Step`, `Severity`, `Status`, and `Language Bank`.
   - Automatic color-coded conditional formatting (`Blocks` = Red, `Slows` = Amber, `Annoys` = Yellow).
   - Embedded `Summary & Metrics` formula sheet for automated KPI reporting.
2. **Option B (CSV Import):** In an existing or new Google Sheet, click `File > Import > Upload` and select `context/FRICTION_LOG_TEMPLATE.csv`.
