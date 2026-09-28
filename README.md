# REAP documentation

Customer documentation for REAP, built with Mintlify. This repository is separate from REAP engineering repositories.

## Structure

- Getting started: concepts, requirements, and a first-question quickstart.
- Deployment: clusters and connectors, credentials, sites, and discovery.
- Capabilities: a flat list using product UI names.
- Integrations: Slack, ServiceNow, Microsoft Teams, and NetBox.
- Security and administration: data collection, security resources, and access.
- Support and What's new: utility pages linked from the landing page and footer.

## Current review edition

The documentation-structure review branch contains 26 pages, including 17 technical drafts. Its banner distinguishes the preview from published customer documentation. The existing Slack guide is preserved.

See [CONTENT-REVIEW.md](CONTENT-REVIEW.md) for missing source material and publication requirements. Draft metadata and hidden navigation do not provide access control.

## Editing

Use the Mintlify editor for pages, navigation, and configuration. Keep landing-page styling scoped to `.reap-home` in `style.css`. Follow [AGENTS.md](AGENTS.md) for content standards.

## Review and publish

Check exact product labels and workflows against the customer-deployed version. Verify prerequisites, expected results, permissions, and troubleshooting. Remove editorial notes and draft metadata only after verification.

Before publishing, remove the review banner, update What's new, and ensure every visible link leads to a completed guide. Keep unpublished drafts excluded from the production build using `.mintignore`; removing them from navigation alone is not sufficient.

Require a successful Mintlify build, working internal links and anchors, and visual checks of the landing page and changed guides. Merge a reviewed change into the deployment branch to publish.

## Resources

- [Mintlify documentation](https://www.mintlify.com/docs)
- [Published REAP documentation](https://reap-731233b9.mintlify.io/)
