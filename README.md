# REAP customer documentation

This repository is the separate home for REAP's Mintlify documentation.
Mintlify is connected to `Reap-IT-Now/docs`, branch `main`.
The engineering API source remains in `Reap-IT-Now/reap-contracts`.

## Engineering repository boundary

All documentation changes and automation live here. Engineering repositories are
read-only sources. Do not create branches, commits, pull requests, webhooks,
workflows, deploy keys, or settings changes in them for this project.

The sync workflow reads only `openapi/public/v1` from `reap-contracts/main`.
It does not execute engineering scripts or build the engineering product.
Source checkout credentials are not persisted. A separate credential must have
Contents **read-only** permission for `reap-contracts` only.
The write credential is this docs repository's scoped `GITHUB_TOKEN`.

## Current setup status

The repository and Mintlify connection already exist. Customer pages and branding
still need to replace the starter kit. No API specification is included in this
setup change, and no customer documentation is published by this change.

The proposed sync workflow is disabled unless `API_DOCS_SYNC_ENABLED` is set to
`true`. Once enabled on `main`, it checks every six hours and can also run manually.
Successful validation produces a draft pull request here; there is no auto-merge.
The API source commit is recorded alongside changes. Unrelated source commits do
not create updates when the generated specification is unchanged.

## Activate synchronization

1. Confirm which public API operations are released and approved for customers.
   This docs repository is public: a draft branch is visible too. The prepared
   workflow imports the whole public/v1 contract. If only a subset is approved,
   add explicit filtering and remove unused schemas before enabling it. Never
   copy admin or internal contracts into this public repository.
2. Create a fine-grained token selecting only `Reap-IT-Now/reap-contracts` with
   repository Contents set to **Read-only**. Add it as an Actions secret named
   `CONTRACTS_READ_TOKEN` in **this docs repository**. Do not paste the token into
   chat or commit it. Any required organization approval is for read access only.
3. In this repository's Actions settings, allow GitHub Actions to create pull
   requests. The workflow explicitly requests Contents and Pull requests write
   permissions for this docs repository only.
4. Merge the reviewed setup PR here. Set the Actions repository variable
   `API_DOCS_SYNC_ENABLED` to `true` when the import scope is approved.
5. Run **Propose API documentation updates** manually and inspect its result.

The initial source inspection found malformed top-level security values and
inconsistent token grant names in introductory prose. The structural validator
may block the first import. Correct documentation copies through reviewed,
explicit transformations in this repository when justified; do not bypass
validation or modify engineering contracts under this task's authorization.

## Build the customer experience

After a valid, approved bundle exists at `api-reference/openapi.json`, reference
that local file from the API navigation in `docs.json`. Add REAP branding and
customer guides for authentication, the first API request, pagination, and errors.
Keep reference pages generated from the bundle; write explanations separately.
Verify the API base URL and examples against the released service before launch.

## Review and publish

- Validate the bundled contract with the pinned Redocly CLI in the sync workflow.
- Run `mint validate` and `mint broken-links` on the complete docs project.
- Inspect the Mintlify preview, including search, navigation, mobile layout,
  schemas, authentication fields, and copied examples.
- Test examples in an approved REAP test environment. Check successful requests,
  invalid credentials, insufficient permissions, tenant scoping, and pagination.
- Confirm the documented API version matches the released API. A contract build
  passing is not evidence of live API behavior.
- Merge a reviewed documentation PR into `docs/main` to publish through Mintlify.

GitHub's default workflow token may not trigger other GitHub Actions workflows
when it creates a PR. This sync therefore performs contract checks itself. Verify
Mintlify previews separately; do not assume every integration fires automatically.

## Validation performed for the setup

The setup is designed to be validated statically and with local reference-check
fixtures before review. A complete source import, GitHub Actions execution,
Mintlify rendering, and live API checks require activation and are separate gates.
