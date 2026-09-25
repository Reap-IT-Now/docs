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

Each draft is tagged Draft, is noindex, and contains its remaining validation requirements. These metadata settings are not access control. Keep this branch as a review preview until the procedures are ready.

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
