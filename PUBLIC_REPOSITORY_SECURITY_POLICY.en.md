# Mandatory Security Policy for Public Repositories

[Português](PUBLIC_REPOSITORY_SECURITY_POLICY.md) | [English](PUBLIC_REPOSITORY_SECURITY_POLICY.en.md)

## Permanent rule

Every public repository in the ARKHE | AIO ecosystem must contain only artifacts deliberately intended for public disclosure.

It is forbidden to version, in any branch or reachable history:

- product, service, application, internal automation, infrastructure, or database source code;
- credentials, tokens, private keys, private certificates, or secrets;
- environment files and variables containing sensitive values;
- personal, operational, financial, internal, or otherwise non-public data;
- configuration files that reveal credentials, private endpoints, service accounts, or authentication material.

## Allowed content

A public repository may contain documentation, policies, public metadata, and GitHub Actions workflows strictly required to validate or publish public artifacts.

A file being allowed by extension does not authorize sensitive content inside it. All content remains subject to secret scanning.

## Mandatory gate

The `Public Repository Daily Guard` workflow runs:

1. on every pull request targeting `main`;
2. on every push to `main`;
3. daily;
4. on demand.

The gate checks both the current tree and reachable Git history. Any violation fails the workflow.

## Incident handling

When a violation is detected, remediation must remove the material from the public tree and, when it existed in history, rewrite or purge the affected history before the incident is considered closed. Exposed credentials must be revoked and rotated immediately. Merely adding a file to `.gitignore` while leaving the secret in history is not sufficient.

## Cost and dependencies

Validation uses only GitHub Actions, Git, and Python available on the runner, with no mandatory paid service and no external SaaS scanner dependency.
