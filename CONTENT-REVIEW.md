# REAP documentation review

This branch contains the complete documentation structure and a designed landing page. It is a review edition, not a verified product manual.

## Ready foundation

- Branded landing page, navigation, category entry pages, support pages, and direct security resources.
- Existing Slack integration guide retained without edits.
- Security page links to the current public statements instead of inventing compliance, retention, or collection guarantees.
- What's new distinguishes documentation updates from product releases.

## Technical drafts

- `getting-started/overview.mdx`: Overview and key concepts.
- `getting-started/requirements.mdx`: Requirements.
- `getting-started/quickstart.mdx`: Quickstart.
- `deployment/clusters-and-connectors.mdx`: Clusters and connectors.
- `deployment/device-credentials.mdx`: Device credentials.
- `deployment/sites-and-discovery.mdx`: Sites and device discovery.
- `capabilities/inventory-and-topology.mdx`: Inventory and topology.
- `capabilities/chat.mdx`: Chat.
- `capabilities/incidents.mdx`: Incidents.
- `capabilities/runbooks.mdx`: Runbooks.
- `capabilities/change-management.mdx`: Change Management.
- `capabilities/cves.mdx`: CVEs.
- `capabilities/configuration-history.mdx`: Running config.
- `integrations/servicenow.mdx`: ServiceNow.
- `integrations/microsoft-teams.mdx`: Microsoft Teams.
- `integrations/netbox.mdx`: NetBox.
- `security/users-and-permissions.mdx`: Users and permissions.

Each draft is tagged Draft, is noindex, and contains a visible review note. Remaining validation requirements are tracked below. These metadata settings are not access control. Keep this branch as a review preview until the procedures are ready.

## Validation needed

1. Deployment owner: supported runtimes, sizing, network/firewall rules, bootstrap procedure, ready states, credential assignments, and a tested discovery example.
2. Product owner: match labels and flows to the customer-deployed version. Current source labels are Chat, Change Management, CVEs, Running config, and Topology v2. "Ask REAP" is a search keyword.
3. Integration owners: complete and test Teams, ServiceNow, and NetBox procedures, permissions, dependencies, expected results, and failure recovery.
4. Security owner: validate deployment-specific data categories and link approved architecture or data-flow material when available.
5. Customer success: validate the first-question quickstart end to end.

## Publication workflow

For each guide, replace editorial notes with verified instructions and screenshots, test its expected outcome, remove Draft/noindex, and verify links. Publish only completed guides. Keep Capabilities flat until multiple meaningful clusters of complete content emerge; do not create empty job-based groups.

The public main branch remains the previously published Slack documentation until this review edition is ready.

## Sources consulted

- Uploaded REAP Slack integration guide and REAP branding files.
- Read-only REAP UI source in Reap-IT-Now/reap-ui, inspected September 25, 2026. Source labels establish the draft wording; they do not prove availability in every customer deployment.
- https://reapitnow.ai/security
- https://reapitnow.ai/privacy
- Official Mintlify page, navigation, and component documentation.

No files in REAP engineering repositories were modified.

## Audit corrections

- Landing cards now have one interactive link, without a button nested inside the anchor.
- Integration cards identify the three draft guides before a reader opens them.
- Slack prerequisite and troubleshooting links point to the relevant sections.
- Runbooks includes authoring, template review, publishing, and controlled initial execution, grounded in the UI source.
- Change Management explicitly covers unchanged conditions, incomplete checks, and preservation of pre-change evidence.
- The preview has a visible review banner. Its pages are not a replacement for the live documentation.
- Starter README content has been replaced with REAP-specific editing and publishing guidance.

## Remaining acceptance evidence

- Run the quickstart against a supported customer deployment; a rendered guide is not evidence that deployment steps work.
- Verify Slack installation, routing, individual linking, ticket assignment, and runbook results end to end. The supplied Word guide is the content source, not a substitute for a live integration test.
- Add verified screenshots where they resolve ambiguous UI steps.
- Validate narrow-screen navigation and layouts on actual target devices.
- Establish the custom documentation domain separately; this work does not configure docs.reapitnow.ai.
- Treat the security page as an entry point to published policies, not a field-level collection matrix. Confirm data categories, destinations, retention/deletion, residency, and AI processing/subprocessor details before making deployment-specific claims.
- On production promotion, remove the review banner, update the review-edition note in What's new, and exclude any unpublished drafts from both navigation and the production build.

## Capability content review — September 25, 2026

All seven capability pages now lead with functionality and customer value, then a practical example, then usage instructions. The overview maps customer goals to each capability. Examples are illustrative prompts and scenarios, not claimed live test results.

Source references (read only):
- UI source: Reap-IT-Now/reap-ui at `21c80f34ab09643b6b0ee07a8092f47f38c35cf7`. Reviewed InventoryPage, TopologyV2Page, ChatAgentsPage, UnifiedIncidentsPage, UnifiedIncidentPage, RunbookNewPage, ChangeManagementPage, CVEGlobalSummaryPage, and DeviceRunningConfigPage.
- Runbooks: Reap-IT-Now/agent-core at `f4183efe86c1c16905bcbdf34efe1a6066a1f575`, network_runbook_executor README, compiler operation-contract prompt, saved-runbook invocation path, and deviceagent README. Saved procedure reuse separates semantic operations from vendor syntax; per-invocation planning and capability checks still occur.
- Change Management: same agent-core commit, network_change_management README. Plan review, explicit approval, pre-change readiness, user-triggered pre/post capture, comparison, and persisted report are implemented. Configuration push is outside this workflow.
- CVEs: Reap-IT-Now/cve-db, `main.go` evaluation logic (source search resolved commit `18dd90c347d6afd701ac96ed7077dd5523a01940`). Version checks and conditional configuration-trigger evaluation support the wording. The UI's AUDITED SAFE label is scoped to an individual assessment, not general device security.

Claims and limits preserved:
- Runbooks: reuse across supported devices and vendors, conditional on the required operations. No universal device-support promise. Instructions tied to devices or vendor commands require portability review.
- Chat: natural-language questions, scope clarification, evidence gathering for supported checks, and follow-up. No guarantee of a complete answer when inputs or access are missing.
- Change Management: plan and evidence collection, not automatic implementation. The report is limited to approved checks. Original pre-change evidence must be preserved.
- Incidents: available evidence varies by source. Slack's ServiceNow workflow dependency remains explicit.
- CVEs: signature and input coverage limit the result; remediation guidance requires review for the specific environment.
- Running config: collected snapshots, not a promise of continuously current configuration; differences do not establish causation.

Before publication, test one complete workflow per capability against the customer-deployed release:
1. Runbooks: compile a parameterized procedure, publish, execute on representative supported vendors, inspect outputs, and verify scheduling and approval behavior.
2. Chat: reproduce the example questions and verify scope resolution, evidence controls, and follow-up.
3. Change Management: complete a supported pre/post validation with explicit plan approval, readiness review, an implementation outside REAP, and persisted report.
4. Inventory/topology: verify labels, default views, layers, scope selectors, freshness, and discovery coverage.
5. Incidents: verify source-specific details, ownership, permissions, state transitions, and linked-ticket behavior.
6. CVEs: verify prerequisites, status mapping, justification, assessment time/history, and one configuration-dependent result.
7. Running config: verify collection prerequisites, snapshot retention, selection, export, and startup-drift support on an applicable device.

Content verification: all eight saved capability MDX bodies match the prepared copy; 40 internal links resolve to existing documentation pages; native component tags are balanced; Mintlify deployment for `f2a17021034374ffa3450f1573fffcd7f097d55e` succeeded.

## Follow-up flaw audit — September 25, 2026

Reviewed all 26 current documentation pages and checked the detailed workflows against reap-ui commit `6003a55ce3054f7e88707d72b33c0643e20b7ba2`.

Corrected verified issues:
- Runbooks previously skipped **Use runbook**, **Review**, and **Start execution**. Selecting a library item's name opens its detail page and does not expose the launch panel. The guide now gives the complete launch sequence and the actual **Create runbook** entry control.
- Scheduled execution previously omitted the schedule name, cadence, timezone, review, and **Create schedule** submission. The guide now distinguishes an active schedule from a paused schedule, explains the pinned version, and notes skipped overlapping and missed occurrences.
- Runbook execution approval was placed before launch. The source presents pending approval in an execution's **Waiting for approval** state. The guide now places review and **Approve change** / **Reject change** at that stage.
- Publishing was described as the action that makes a version executable. The current launch UI accepts eligible ready or published versions; the wording now reflects that distinction.
- Chat now identifies **Create thread** and **Send message**. Change Management identifies **New change**, **Approve plan**, **Run pre-checks**, and **Run post-checks**, and explains Ready, Attention, Blocked, and Inconclusive readiness.

Verification:
- All 93 internal page and section links across 26 pages resolve to existing targets; native component tags are balanced.
- Saved Runbooks and Change Management bodies match the prepared copy. Chat's only serialization difference is Mintlify escaping the plus sign, which renders as the intended + control.
- Mintlify deployment for `3b4bd6a084e8244220046a12ee22ccc939a32432` succeeded.
- Slack guide and production main were not changed by this audit.

Outstanding publication blockers:
- Requirements and deployment guides still need supported runtimes, sizing, exact firewall destinations/ports, installation commands, credential assignment behavior, and a tested setup sequence.
- ServiceNow, Teams, and NetBox remain incomplete draft setup guides. They are not self-service installation instructions.
- Product workflows have been checked against source, not executed against customer devices. End-to-end validation remains required before removing draft status.
