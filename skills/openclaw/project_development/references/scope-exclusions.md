# Scope Exclusions

This skill is intentionally focused on OpenClaw development governance.

It does not define project-specific storage policy.

## Excluded For Now

Out of scope:

- storage retention rules
- automated cleanup policy
- SQL governance
- deployment policy
- release policy
- backup policy
- secret rotation policy
- trading-main registry schema ownership
- fixed vocabulary maintenance

These may be handled by separate skills, project-specific docs, or dedicated projects when needed. Fixed vocabulary belongs to the separate `trading-main/registry/` project.

## Why Storage Policy Is Excluded

Storage policy depends on project type:

- some projects need temporary task output only
- some projects need durable audit receipts
- some projects need short-lived logs
- some projects need privacy-sensitive deletion
- some projects need external compliance rules

A generic OpenClaw development skill should not impose these policies too early.

## Allowed Minimal Path Guidance

This skill may recommend project-local task exchange paths such as:

```text
.openclaw/task/register/
.openclaw/task/execution_key/
.openclaw/task/completion_receipt/
.openclaw/task/acceptance_receipt/
.openclaw/task/output/
```

But it does not decide how long these files are kept.

## When To Add Storage Policy Later

Add storage policy only when:

- the Owner asks
- project docs require it
- outputs are accumulating in a way that affects maintenance
- privacy, cost, compliance, or storage pressure requires policy
- the project has clear classes of temporary and durable data

When added, write storage policy into project-specific docs or a dedicated project-specific skill.
