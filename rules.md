# Vulnerability Reward Program (VRP) & Security Triage Standard Operating Procedures

This document outlines the standard operating procedures, routing rules, and triage workflows for security specialists operating within the organization's Vulnerability Reward Program (VRP) and Security Response intake systems.

---

## 1. Triage Intake Queue Operations

When operating in the primary **Intake Queue**, your primary objective is initial assessment and communication routing. 

* **No Deep Technical Investigation:** Do not attempt to reproduce vulnerabilities, execute proof-of-concepts, or perform deep code analysis in this queue. Those activities belong in the **Technical Investigation Queue**.
* **Intake Scope:** Reports in this queue generally fall into two categories:
  1. New reports (unverified, incomplete, or potentially invalid).
  2. Follow-up responses on existing reports (both valid and invalid).
* **Engagement Decision:** Because reports in this queue have already passed automated form validation, determine whether the case requires active engagement or can be closed. If no response is warranted, close the report directly. If a reporter replies later, the system will automatically reopen the ticket.

### Routing Valid Vulnerabilities
When you encounter a report with sufficient technical detail that represents a plausible, actionable security risk:
* **Do NOT file a product bug directly from the Intake Queue.**
* Route the ticket immediately to the **Technical Investigation Queue** by assigning an appropriate operational priority (**P0 to P3** using the workbench action bar).

---

## 2. Borderline & Low-Risk Vulnerabilities

For submissions that describe valid technical behavior but present minimal security impact or borderline risks:
* **Request Attack Scenarios:** Ask the researcher to provide a concrete, realistic attack scenario demonstrating practical exploitation.
* **Denial & Risk Acceptance:** If the researcher cannot provide a convincing exploitation scenario, close the report using a standard *Won't Fix*, *Not a Bug*, or *Acceptable Risk* canned response.
* **Mandatory Justification Rule:** Whenever you use a canned response to deny a report or accept a risk, **you must include a clear technical justification**. Explain *why* the organization accepts the risk, detailing any compensating security controls, architecture boundaries, or mitigations that render the severity low.
* **Soft-Closing (Delayed Close):** For cases where you are currently unconvinced of a security impact, you may move the ticket to the **Delayed Close** state. This removes the ticket from active queue focus while providing the researcher a window to submit compelling counter-evidence before final closure.

---

## 3. Open Source VRP & Merged Patch Workflow

For open-source software (OSS) projects owned by the organization, qualification under the Vulnerability Reward Program requires specific reproduction or remediation deliverables depending on the project tier and vulnerability class.

### Memory Corruption in Tier 0 and Tier 1 Repositories
All memory corruption vulnerabilities reported against **Tier 0 (Flagship)** and **Tier 1** repositories strictly require one of the following two deliverables for qualification:
1. **Exact OSS-Fuzz Reproduction Steps:** The report must utilize an existing OSS-Fuzz target and provide the exact commands and reproduction steps required to build the fuzzer image and reproduce the crash; OR
2. **An Already Merged Patch:** An official code fix that has already been submitted, reviewed, and merged into the target repository.

### Initial Intake & Patch Verification
When an OSS report is submitted without the required OSS-Fuzz reproduction format or a merged patch, send the standard Open Source VRP canned response explaining these exact requirements. When a researcher returns claiming their patch has been merged, verify all of the following conditions:
1. **Repository Ownership:** The target repository is an officially owned organization OSS project.
2. **Repository Match:** The merged patch resides in the exact repository specified in the vulnerability report.
3. **Author Identity Match:** The git commit author matches the VRP reporter. Verify that the researcher's name/email in the commit matches their registered VRP profile.
   * *Verification Tip:* In GitHub or standard git web viewers, navigate to the commit hash URL (e.g., `https://github.com/[org]/[repo]/commit/[hash]`) and append `.patch` to the URL. Inspect the `From:` header line to confirm the author's email and name.
   * If the identity does not match, escalate via internal channels before proceeding.
4. **Technical Relevance:** The commit description and code changes directly correspond to the reported vulnerability.
5. **Commit Status & Timeliness:** The pull request/commit status is officially **Merged**, and the patch date is recent and relevant to the reporting timeline.

### Forwarding to the VRP Panel
Once all patch conditions are verified, forward the report to the reward panel by filing an internal tracking bug:
* **Template / Routing:** Select the standard OSS VRP Patch-Only workflow.
* **Priority & Component:** Assign **P3 (Low)** under `Security > VRP > OSS Patch Tracking`.
* **Description & Fields:** In the generated description, replace any placeholder tags (e.g., `TODO(assignee):`) with the direct link to the merged patch (`https://github.com/[org]/[repo]/pull/[ID]`). Retain the rest of the auto-generated description.
* **Canned Response Cleanup:** In the preview step before posting, remove generic boilerplate paragraphs (such as *"We have filed a bug with the responsible product team..."*) so the update is clean and accurate.
* **Finalization:** 
  1. Update the internal tracking bug status to **Fixed**.
  2. Apply the **VRP Panel Tag** to the communications ticket so the external researcher is automatically notified that their report has advanced to reward grading.

---

## 4. Identifying Cloud Tenant & Customer Assets

When investigating reports involving third-party domains, IP addresses, or cloud-hosted endpoints, you must verify whether the asset is actually owned and operated by the organization or is merely hosted by a cloud customer/tenant.

### Verification Rule for Tenant IP Addresses
If you check the domain or IP registration/WHOIS data and see the following information:
`*** The IP addresses under this Org-ID are in use by Google Cloud customers ***`

This asset is **outside of the scope of the program**, as it is owned and operated by an external customer/tenant rather than the organization itself. Hosting a third-party application on our cloud infrastructure does not place the customer's application code within our VRP scope.
* **Resolution Action:** Close the report immediately as **Out of Scope (Not Owned)** (or *Invalid / Not Applicable*) and explain to the reporter that the IP/domain belongs to a cloud customer rather than an internal service.

---

## 5. Misdirected & Out-of-Scope Reports

Handling misdirected reports is the lowest operational priority and should only be processed during remaining capacity. 
* **Avoid Encouraging Non-Security Traffic:** Actively engaging in manual dialogue on non-security issues encourages future misdirected submissions.
* **Out-of-Scope Categories:** Account recovery (lost passwords, hijacked accounts), product feature complaints or UI confusion, general feature requests, and legal/copyright inquiries.
* **Resolution Action:** Utilize automated closing workflows (e.g., the **Invalid** action button in the workbench). This triggers an auto-responder directing the user to standard customer support channels without expending manual triage time.

---

## 6. Communication & Technical Escalations

Because technical reproduction occurs in the deep investigation queue and reward grading occurs in panel voting, the majority of Intake Queue activity consists of researcher dialogue and follow-up questions.

### Routing Technical Follow-ups
If a researcher provides new technical evidence or follow-up data on a previously investigated ticket, route it back to the **Technical Investigation Queue** (P0–P3). 
* **Avoid Context Switching:** Do not interrupt your intake flow to conduct deep technical reproduction yourself.
* **Mandatory Context Notes:** Always append a clear internal note summarizing what new context was provided and what specific aspect requires engineering re-evaluation. Without context notes, investigation teams are likely to bounce the ticket back.

### The Core Communication Principle
* **Rule: If you do not fully understand a bug, do not try to explain or defend it.**
* This principle applies equally when communicating with external researchers and internal engineering teams. You cannot make a credible technical judgment or defend an architectural decision unless you completely grasp the underlying mechanics.
* Our response program is built on transparent, high-quality technical dialogue. If a submission exceeds your current technical understanding, ask the researcher for clarification, consult a subject matter expert, or file an internal consultation bug. Never guess or provide unsupported technical claims.

---

## 7. Customer Support & Administrative Requests

Maintaining responsive communication is essential for researcher trust. Handle administrative inquiries according to these guidelines:

### Status & Dashboard Inquiries
* Researchers receive automated notifications when bugs are fixed, verified, or awarded. They can also track payment status directly via their **VRP Researcher Dashboard**.
* When answering status queries, consult the workbench sidebar, which displays real-time panel decisions, reward amounts, and transaction statuses.

### CVE Number Requests
If a researcher requests a CVE identifier, verify that the report is in scope for CVE assignment:
* File a blocking tracking bug with the responsible product engineering team and add the **CVE Numbering Authority (CNA)** team (`cve-coordination@example.com`) to the CC list.
* Instruct the engineering team to complete the internal CVE request form (`http://intranet/cve-request`). Triage specialists are not expected to know internal component specifics required by the form.
* For complex CVE inquiries or disputes regarding publication timelines, let the CNA team own the dialogue on the ticket.

### Hall of Fame & Credit Attribution
* Credit and ranking on the Hall of Fame are tied directly to user profiles and finalized during triage/panel processing.
* If a researcher asks why their name is not prominently displayed, explain that rankings are determined by cumulative severity and volume of valid findings.
* Profiles are permanently linked to single user accounts; accounts cannot be merged or transferred. Direct technical platform issues to the *Send Feedback* tool, ensuring researchers understand it is not for ranking disputes.

### Payouts & VRP Panel Appeals
* **Payment Administration:** Direct all tax, banking, or charity donation inquiries to the finance team at `payouts@example.com`.
* **Panel Decision Appeals:** If a researcher asks to appeal a reward amount or categorization, use the **Send to Panel** workbench action.
* **Filtering Appeals:** The reward panel meets twice weekly. Only forward appeals that present substantive, professional arguments (e.g., *Why was this categorized as Tier 2 rather than Tier 1?* or *Can this reward be split to charity?*). Do not forward unfounded complaints, emotional rants, or demand letters (e.g., *I spent a week on this, $100 is a joke!* or threats to contact the press). Require the researcher to provide clear, objective justification before escalating to the panel.

---

## 8. Escalating Complex Cases

When an intake ticket exceeds standard workflows or requires specialized intervention, escalate it to the **Triage Escalations Queue**.

### Escalation Criteria
1. **Unresolved Technical Arguments:** A researcher presents a sophisticated technical rebuttal or edge case that you cannot independently evaluate (and which does not cleanly belong in standard engineering investigation).
2. **Undocumented Process Queries:** Administrative, legal, or special payment edge cases not covered by standard documentation.
3. **Access Limitations:** You lack the required system permissions, tenant access, or tool visibility to verify the claim.

### Escalation Procedure
* Apply the **Tag: Triage Escalation** to the ticket.
* Leave a comprehensive internal note detailing the exact reason for the escalation, what investigations were already performed, and what specific decision is required from the escalation lead.
* If you wish to track the educational outcome of an escalated case, star the ticket to monitor its resolution in your workbench.




