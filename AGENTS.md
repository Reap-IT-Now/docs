# REAP documentation

This repository is the standalone Mintlify documentation site for REAP. Only change documentation and documentation assets here.

## Structure
Keep the main navigation to Getting started, Deployment, Capabilities, Integrations, and Security and administration. Keep Capabilities flat. Include exactly these ten pages in this order unless the user changes the product scope: Incident analysis; Topology and Path Tracer; Runbooks; Inventory; Config drift; Change management; Chat; CVE analysis; Flow Analytics; Monitoring. Do not add a separate Capabilities overview page or combine Inventory with Topology. Support is a utility link. The root documentation home is the primary entry point, with a quickstart path and direct links to the ten capabilities, integrations, and security. Do not add a What's new or changelog page unless the user requests it.

The quickstart leads from organization access through connectivity, credentials, site discovery, and a first network question with evidence. Link to canonical deployment guides rather than duplicating their procedures.

## Voice and naming
Use active voice, second person, concise paragraphs, and sentence case headings. Preserve exact UI labels when naming product controls or features. Bold UI controls and use code formatting for commands, paths, and identifiers.

Use REAP for the brand and Capabilities for the feature section. Use the user-approved capability page names above, and preserve the actual UI labels inside procedures. Explain each capability's functionality, value, and a practical example before its usage steps. Keep search synonyms where customers may use an older or informal name.

## Accuracy and publishing
Use supplied guides and verified behavior as the source of truth. Never invent deployment sizes, firewall rules, permissions, security claims, supported integrations, or release notes.

Draft technical pages use tag: Draft, noindex: true, and a visible review note. These settings are not access control. Keep drafts in a review branch rather than publishing them as final customer documentation.

Before promotion, verify instructions against the deployed product, replace review notes with customer instructions, verify expected outcomes, and remove draft metadata. See CONTENT-REVIEW.md for this edition's source gaps.

## Design and validation
Use native Mintlify components and configuration. Keep custom CSS scoped to the landing page through .reap-home. Preserve logo, favicon, responsive behavior, keyboard focus, and light/dark themes.

Use Mintlify navigation tools and MDX validation. Check all internal links, preserve the existing Slack guide, inspect the rendered landing page and a guide, and confirm a successful Mintlify build before delivery.
