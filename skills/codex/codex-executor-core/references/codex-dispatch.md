# Codex Dispatch

OpenClaw dispatches Codex through a task package called an execution key.

The execution key is a bounded instruction contract, not a casual chat request.

This reference defines the minimum information a Codex task package should communicate.

Exact execution-key schema is not standardized here.

## Dispatch Principle

```text
Codex should never have to guess the roadmap.
```

OpenClaw must provide:

- context
- goal
- scope
- acceptance reference
- allowed paths
- blocked paths
- tests
- expected output
- constraints
- output reference
- receipt reference

## Common Execution Key Contents

An execution key should include:

- task identity
- workflow identity
- repository path
- task goal
- task scope
- acceptance reference
- decision references when relevant
- allowed paths
- blocked paths
- test commands or test expectation
- expected output
- constraints
- output reference when required
- completion receipt reference

If a project formalizes exact key names, document them in the project instead of assuming they already exist.

## Suggested Path

```text
.openclaw/task/execution_key/{task_identity}_execution_key.json
```

This path is a default only. If a project chooses another control path, document it in `docs/01_context.md` or the repository root `README.md`.

Path naming is not standardized here beyond being explicit and documented.

## Dispatch Checklist

Before dispatching Codex, OpenClaw checks:

- Is the task ready for dispatch?
- Does `docs/03_acceptance.md` contain the referenced acceptance rule?
- Are allowed paths and blocked paths explicit?
- Is the task small enough to complete coherently?
- Are required tests named or clearly not required?
- Are output and receipt references provided when needed?
- Are dictionary constraints included?
- Are script split gates included?
- Are docs protected unless Codex is explicitly asked to edit them?

## Recommended Constraints

Include constraints such as:

```text
Do not add new production dependencies without approval.
Use formal names approved by universal-catalog.
Do not self-register new names; report temporary new names for OpenClaw review.
Do not modify docs/03_acceptance.md unless explicitly requested.
Do not create extra files unless a script split gate is met.
Do not touch secrets, .env, credentials, or sibling repositories.
Return a completion receipt.
```

## Example Execution Key

No canonical JSON schema is defined here yet.

This skill should not be treated as the authority for exact key names.

A valid execution key must still communicate the required slots above.

## Bad Dispatch

Avoid:

```text
Please improve the config system. You can decide how.
```

This is not a dispatch. It is an invitation to scope drift.
