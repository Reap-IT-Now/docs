# REAP documentation review

This branch contains the complete documentation structure and a designed landing page. It is a review edition, not a verified product manual.

## Ready foundation

- Branded landing page, navigation, category entry pages, support pages, and direct security resources.
- Existing Slack integration guide retained without edits.
- Security page links to the current public statements instead of inventing compliance, retention, or collection guarantees.
- The documentation home provides a guided setup path and direct access to all ten capabilities, integrations, security, and support. There is no What's new page.

## Technical drafts

- `getting-started/overview.mdx`: Overview and key concepts.
- `getting-started/requirements.mdx`: Requirements.
- `getting-started/quickstart.mdx`: Quickstart.
- `deployment/clusters-and-connectors.mdx`: Clusters and connectors.
- `deployment/device-credentials.mdx`: Device credentials.
- `deployment/sites-and-discovery.mdx`: Sites and device discovery.
- `capabilities/incident-analysis.mdx`: Incident analysis.
- `capabilities/topology-and-path-tracer.mdx`: Topology and Path Tracer.
- `capabilities/runbooks.mdx`: Runbooks.
- `capabilities/inventory.mdx`: Inventory.
- `capabilities/config-drift.mdx`: Config drift.
- `capabilities/change-management.mdx`: Change management.
- `capabilities/chat.mdx`: Chat.
- `capabilities/cve-analysis.mdx`: CVE analysis.
- `capabilities/flow-analytics.mdx`: Flow Analytics.
- `capabilities/monitoring.mdx`: Monitoring.
- `integrations/servicenow.mdx`: ServiceNow.
- `integrations/microsoft-teams.mdx`: Microsoft Teams.
- `integrations/netbox.mdx`: NetBox.
- `security/users-and-permissions.mdx`: Users and permissions.

Each draft is tagged Draft, is noindex, and contains a visible review note. Remaining validation requirements are tracked below. These metadata settings are not access control. Keep this branch as a review preview until the procedures are ready.

## Validation needed

1. Deployment owner: see the September 27 discovery review for the now-documented AWS setup path and the remaining production requirements and validation checks.
2. Product owner: match labels and flows to the customer-deployed version. Use the user-approved capability page titles. Procedures retain source labels such as Incidents, Chat, Change Management, CVEs, Running config, Topology v2, Path Tracer, Flow Analytics, and Telemetry / Telemetry Explorer. "Ask REAP" is a search keyword.
3. Integration owners: complete and test Teams, ServiceNow, and NetBox procedures, permissions, dependencies, expected results, and failure recovery.
4. Security owner: validate deployment-specific data categories and link approved architecture or data-flow material when available.
5. Customer success: validate the first-question quickstart end to end.

## Publication workflow

For each guide, replace editorial notes with verified instructions, test its expected outcome, remove Draft/noindex, and verify links. Publish only completed guides. Keep Capabilities flat until multiple meaningful clusters of complete content emerge; do not create empty job-based groups.

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
- Keep Getting started and Deployment screenshot-free. Resolve ambiguous steps with exact control names, field tables, and input guidance.
- Validate narrow-screen navigation and layouts on actual target devices.
- Establish the custom documentation domain separately; this work does not configure docs.reapitnow.ai.
- Treat the security page as an entry point to published policies, not a field-level collection matrix. Confirm data categories, destinations, retention/deletion, residency, and AI processing/subprocessor details before making deployment-specific claims.
- On production promotion, remove the review banner and exclude any unpublished drafts from both navigation and the production build.

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

## Discovery guide review — September 27, 2026

Sources:
- REAP-Getting-Started-Guide(1).docx: complete paragraph/table extraction and all five embedded screenshots.
- REAP-Discovery-Transcript(1).txt: complete transcript.
- REAP-Discovery(2).mov: 629.79-second recording, reviewed with frames across the complete timeline, the source screenshots, and the final state. The demonstration is an OnPrem site using a connector hosted on AWS EC2; it does not demonstrate account signup or other connector deployment modes.
- Read-only reap-ui source at `62b4546c51fa84f71f7b16d8d1363e9876653d91`: ConnectivitySitesPage, CredentialWizard, AssignmentDrawer, DiscoveryJobDrawer, and DiscoveryRunDrawer. Source behavior is not proof of rollout to every customer version.

Content changes:
- Replaced setup outlines with the recorded sequence: create site, create cluster and attach site, create connector record, download connector user data, deploy the approved REAP AMI, configure credentials and assignments, verify routing/readiness, create a manual job, start a separate run, and verify Inventory.
- Kept the detailed procedures in the three existing Deployment guides. Quickstart and Setup overview link to their specific sections and avoid repeating the full procedures.
- Explained credentials versus assignments and discovery jobs versus runs in Key concepts.
- Corrected the discovery cluster field: it is inherited from the site's attachment and is read-only in the current UI, not a cluster selector.
- Added the exact CLI/SNMP v3 fields, optional enable password, assignment enablement, scope and filters, run counters, stop action, and outcome checks.
- Preserved the first network question as the quickstart outcome; Chat is sourced from the existing source-reviewed guide, not claimed to be shown in this discovery recording.
- Added five screenshots from the supplied guide with alt text and captions identifying example names, subnet, and counts.
- Renamed overview navigation entries to Setup overview, Choose a workflow, and Available integrations. The five top-level groups and all existing URLs remain intact.

Recording-specific limits retained:
- The internal AMI name, t2.medium example, 8 GiB storage, existing security group, AWS identifiers, and lab routing script are not customer deployment requirements.
- The guide asks for the approved AMI/sizing/access/network settings instead of inventing values or exporting internal lab commands.
- The actual downloaded YAML was not supplied. Its encoding options and bootstrap internals were not inferred.
- A site's Healthy label is distinct from a connector readiness state; the recording does not establish every final connector state or registration time.
- The sample run reports 22 devices and 42 links. These are illustrative counts, not acceptance thresholds.
- Topology is still processing near the end of the recording; no fully populated topology result is promised at run completion.
- The visible assignment examples cover Arista/Palo Alto, while Aruba also appears in the resulting inventory. The assignment examples do not prove credential coverage for all vendors.
- The submitted CIDR and resulting inventory include different address ranges. No strict CIDR boundary or neighbor-expansion semantics are asserted.
- A NetBox error and inconsistent overview counters appear in the recording; completion is assessed from the run and Inventory, without inventing a NetBox prerequisite.

Remaining deployment publication checks (supersede the generic setup blockers in the September 25 audit):
1. Obtain production-approved AMI distribution, sizing/storage, AWS permissions/access, bootstrap encoding guidance, and exact endpoints, ports, DNS/proxy and routing requirements.
2. Confirm connector ready/error states and recovery actions against the deployed customer version.
3. Validate device privilege requirements, assignment overlap/priority precedence and rotation behavior.
4. Confirm discovery target/neighbor behavior and expected inventory/topology coverage.
5. Execute the full quickstart, including a first Chat answer with inspectable evidence, in a supported customer environment. This review did not deploy infrastructure or connect to customer devices.
6. Keep the six revised technical setup/concept pages tagged Draft and noindex until these checks are complete.

Verification:
- Seven saved page bodies match the prepared copy after Mintlify's whitespace and image-format normalization.
- All 108 internal page, section, and image links across 26 pages resolve to existing targets; native component tags are balanced.
- Navigation contains no page label identical to its parent section label. All 17 existing technical drafts retain their Draft/noindex metadata.
- The five uploaded PNG blobs match the supplied screenshots; no raw video, bootstrap payload, diagnostic terminal, or AWS account screenshot was published.
- Mintlify build for content commit `92103d4c7f2476a1f8bf60aa914fc9885e80e657` succeeded.
- Rendered landing page and setup guides were inspected in the Mintlify preview.

## Sanity check — September 26, 2026 (Pacific time)

Rechecked the saved review branch against the complete supplied Word guide and transcript, the previously reviewed recording evidence, and the relevant UI source at `62b4546c51fa84f71f7b16d8d1363e9876653d91`. Reviewed all 26 page metadata blocks, internal targets, navigation group labels, and remaining editorial/source gaps.

Two corrections:
- The end of the discovery guide and the setup overview previously sent readers back to the beginning of Quickstart to ask a network question. Both now link directly to Chat's usage section. The discovery-to-Chat link was clicked and verified in the preview.
- What's new now includes the September 26 setup guide update, the five screenshots, distinct sidebar names, and the continuing draft status. It makes no product release claim.

Verification:
- All 109 internal page, section, and image links resolve to existing targets.
- No page label duplicates its parent navigation group; the existing 17 technical drafts retain Draft/noindex.
- All three saved page files match the intended changes and preserve their frontmatter.
- Relevant UI checks confirm the read-only inherited cluster, the required seed/CIDR input, assignment scopes/default priority, and credential field names.
- Preview inspection covered the discovery page and landing page in dark theme and the updated documentation entry in light theme.
- Mintlify build `9fe664853c2ffa508d0065727d9c4b556259a1c0` succeeded.
- Engineering repositories and the production docs branch were not changed.

Limits remain explicit: this is a reviewed documentation preview, not proof of a tested customer deployment. Production requirements and the recorded behavior questions above still need confirmation. Teams, ServiceNow, NetBox, and Users and permissions still contain incomplete draft guidance. Do not treat a successful documentation build as validation of those product workflows.

## Capability scope update: September 28, 2026

The current Capabilities section contains exactly the ten pages requested by the user, in their requested order: Incident analysis; Topology and Path Tracer; Runbooks; Inventory; Config drift; Change management; Chat; CVE analysis; Flow Analytics; Monitoring. This supersedes the earlier combined Inventory/topology page and capability overview. Capabilities remains flat.

Changes:
- Split Inventory from Topology and Path Tracer; added the source-reviewed Path Tracer procedure.
- Renamed and moved Incidents, CVEs, and Running config to the requested capability names and canonical paths. Config drift explains both snapshot differences over time and startup versus running differences where available.
- Added Flow Analytics and Monitoring with functionality, value, practical examples, prerequisites, instructions, and interpretation limits.
- Retained the established Runbooks, Chat, and Change management functionality-first guides and updated related links.
- Removed the old capability overview and combined page. Added permanent redirects for all five replaced URLs. Updated the landing page, setup continuations, related guides, and documentation update entry.

New and refreshed sources: read-only reap-ui at `d3d322fba4f9c727c5c6071ed596875150c75f31`: ShellPage, AppRoutes, InventoryPage, DeviceRunningConfigPage, topology/TopologyV2Page, topology/TopologyPathTracerPage, FlowAnalyticsPage, and GrafanaExplorerPage. Existing source-reviewed Runbooks, Chat, incident, change-management, and CVE behavior remains as documented in the earlier reviews.

Accuracy limits:
- Path Tracer documents available endpoint, traffic selector, evidence-level, time, and clarification controls. A requested evidence level is not a guarantee of available evidence; a graph is not proof of application health or a live packet test.
- Flow Analytics reports observed exporter records. Multiple sources may observe the same traffic; sampling does not establish completeness, protocol/port service names are not application identification, and chart gaps do not establish zero traffic. The chart's selected-range summary does not filter other panels.
- Monitoring uses the product's Telemetry navigation and Telemetry Explorer workspace. Organization trend time ranges are distinguished from the latest Signals, Features, and Conditions views. Missing data does not establish health.
- All ten capability guides retain Draft/noindex and a visible review note. The site now has 20 technical drafts. Source review is not evidence of deployment to every customer release.

Verification:
- Exactly ten capability files exist and all ten appear in the requested sidebar order, with no additional overview or hidden legacy capability pages.
- All 28 saved MDX bodies match the prepared copy after formatting normalization. All 118 internal page, section, and image links resolve; native component tags are balanced.
- Five capability redirects and the existing quickstart redirect are present with valid destinations.
- Mintlify builds succeeded for content commit `8439e2905322223ebbd57a256334dbf523f03c19` and redirect commit `cd654a3c0e3c67b89087954590f2ed6f3f70f5de`.
- Rendered landing page, capability sidebar, and the new/separated capability routes were inspected. The Slack guide is unchanged in the GitHub comparison.

Before customer publication, validate Path Tracer against representative endpoints and returned evidence, Flow Analytics against supported exporter data, and Monitoring against reporting devices and condition states. The earlier deployment and integration publication checks still apply. No engineering repository or production docs changes were made.

## Capability sanity check: September 27, 2026 (Pacific time)

Reviewed the saved ten-page capability edition against current reap-ui source at `d3d322fba4f9c727c5c6071ed596875150c75f31`. Rechecked the Runbooks creation, launch, scheduling, and approval controls; Chat entry controls; Change Management plan, baseline, and post-check controls; incident evidence sections; CVE assessment labels; and configuration comparison behavior. Rechecked the source already used for Inventory, Topology and Path Tracer, Flow Analytics, and Monitoring. No additional source-label or procedural mismatch was identified in this review.

Corrected the latest public What's new date from September 28 to September 27 to reflect the user's publication date in America/Los_Angeles. Historical internal review dates above used UTC where not otherwise stated.

Validation passed for the requested ten titles and exact order, ten capability files with no legacy files, 118 internal page/section/image links across 28 pages, six redirects including the existing quickstart redirect, balanced native components, and Draft/noindex on every capability page. The landing page and Monitoring table were inspected in dark mode, and the corrected update was verified in light mode. Saved content matches the intended date correction, and Mintlify build `0dd0d89399be423f5be8916946b99becec7a41b8` succeeded.

This is a documentation/source audit, not a customer deployment test. Existing publication blockers remain: deployed-version workflow validation, production deployment requirements, and incomplete draft integration/administration guidance. No production documentation or engineering repository was changed.

## Documentation home redesign: September 28, 2026 (UTC)

Replaced the landing page with a focused documentation entry point: a branded quickstart panel, three setup milestones, navigation cards for Capabilities, Integrations, and Security and administration, a compact directory of all ten requested capabilities in the requested order, and a support strip. Capability descriptions explain their purpose. The Capabilities card jumps to that directory on the home page.

Removed What's new from the page files, navigation, footer, and support links. Its former URL permanently redirects to the root documentation home. This supersedes the earlier What's new instructions and audit entries. The root remains the default documentation entry point. The preview banner now states that Draft guides are being prepared for launch.

Verification:
- All 129 internal page, section, and image links across 27 MDX pages resolve; native component tags are balanced.
- The ten capability pages, their requested sidebar order, technical draft metadata, and the existing Slack guide are unchanged.
- Mintlify deployment for `4e93a2cbc304bf7cf5182ea01bb21def327eb360` succeeded.
- Inspected the home page and capability directory in light and dark mode. Confirmed the Capabilities card jumps to the directory and the Runbooks directory entry opens its guide. Corrected headline wrapping and spacing in Mintlify's rendered heading wrapper.
- Layout CSS is scoped to the documentation home. Responsive breakpoints are provided; this review did not test actual mobile devices.
- No engineering repository, production branch, or custom-domain configuration was changed. Existing technical publication checks remain outstanding.


## Screenshot-free setup review — September 28, 2026

This update supersedes the September 27 screenshot-based presentation for Getting started and Deployment. All five screenshot embeds and their captions have been removed from these pages. Uploaded screens are evidence only; the seven setup pages now use click paths, steps, field tables, and explicit outcome checks.

Evidence reviewed:

- The complete 121-line REAP-Discovery-Transcript(1).txt, covering the full 10-minute-30-second walkthrough, reconciled with the prior recording review above.
- All twelve newly supplied UI screens: Connectivity & Sites; Create Cluster; cluster Details, Sites before/after attachment, and Connectors; connector Details and Bootstrap; site Discover, discovery job editing, Inventory, and Topology.
- Read-only Reap-IT-Now/reap-ui at `0dda27bc650375b330c03981ff9a80f711a92909`: ConnectivitySitesPage.tsx, siteForm.ts, DiscoveryJobDrawer.tsx, DiscoveryRunDrawer.tsx, CredentialWizard.tsx, and AssignmentDrawer.tsx. The earlier DiscoveryJobDrawer at `62b4546c51fa84f71f7b16d8d1363e9876653d91` was also checked for the schedule discrepancy.

Corrections and coverage:

- OnPrem creation requires Name, Postal code, and Country in current source. Address line 1/2, City, State, Notes, and Labels remain optional; the old guide incorrectly grouped all location fields as optional.
- Cluster creation/editing includes Name, Description, key/value Labels, the normally disabled internal-inspection setting, Save, and reported status fields. Site attachment requires Attach site and confirmation of the resulting row.
- Connector creation starts from the cluster's Connectors plus icon, with Cluster preselected/locked; the global Connectors route remains documented. Editing, all fields, Cloud-init/JSON download, and the separate Reset enrollment recovery action are covered.
- AWS deployment retains the recorded sequence but uses Bootstrap > Cloud-init. No lab AMI, sizing, security group, script, customer identity, UUID, or observed customer IP is published as a requirement.
- Credentials now include common fields, conditional SSH authentication fields, SNMP fields, assignment fields, scopes, and exact filter labels/input formats. Saving credentials and assignments remains distinct.
- Jobs and runs have separate plus icons and procedures. Job fields, recurring fields, editing, Save job, run selection, Start Run, refresh, and View run are documented.
- A succeeded run may report zero devices/links. Verification checks expected Inventory attributes and Topology rather than status/counters alone. CMDB Relation View is separate from the discovered Inventory table.
- Quickstart, requirements, concepts, and setup overview follow the same sequence. Existing anchors and the ten-capability navigation are preserved. The quickstart still ends with a network question and evidence.

Remaining version-specific checks:

- The supplied discovery screenshot shows Manual, Recurring, and Auto. Both inspected source versions expose Manual and Recurring only. The guide acknowledges Auto when present and directs readers to confirm its trigger behavior; it does not invent an Auto workflow. Validate this against the deployed build before final publication.
- Recurring input details and required site location fields are grounded in current UI source because those forms/states are not shown in the new screenshots. Confirm them against the customer-deployed version.
- Supported AMI, instance sizing, network endpoints/ports, privileges, and a live end-to-end onboarding test remain required before removing the existing Draft metadata. This update is a source/documentation audit, not a connector deployment test.

No engineering repository, production branch, capability list, or custom-domain configuration is changed by this update.
