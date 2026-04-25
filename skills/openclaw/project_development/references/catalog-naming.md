# Registry Naming

This skill is about how OpenClaw and Codex interact with `trading-main/registry/` during normal project work.

It does not define the registry schema.
It does not decide registry kinds on its own.
It does not let Codex self-register names.

## What `trading-main/registry/` currently is

Right now `trading-main/registry/` is the shared register for stable server-wide referenced values used across OpenClaw-managed project work on this machine.

Current concrete coverage is centered on registry items such as:

- `field`
- `output`
- `repo`
- `path`
- `config`
- `term`
- `script`
- default status vocabularies such as `task_lifecycle_state`, `review_readiness`, `acceptance_outcome`, `test_status`, `maintenance_status`, and `docs_status`

Do not assume a proposed future kind is already formal just because it was discussed in chat.

## Operational rule

When naming matters:

1. Check whether `trading-main/registry/` already has a suitable shared name or default vocabulary value.
2. If yes, reuse it.
3. If no, decide whether the work should pause for registry registration or proceed with an explicitly temporary name.
4. If temporary naming is allowed, make sure Codex reports it back for OpenClaw review.
5. After the task, OpenClaw decides whether to register, rename, or reject that temporary name.

## OpenClaw responsibilities

OpenClaw should:

- keep `trading-main/registry/` updated as an ongoing maintenance responsibility
- prefer registry-approved names in task packages, schemas, receipts, paths, outputs, script locators, and shared status vocabularies
- treat missing shared names as registry gaps rather than as permission for casual invention
- review Codex-reported temporary names and register the accepted ones itself
- update related skills when naming policy or registry authority changes

## Codex responsibilities

Codex should:

- reuse registry-approved names first
- avoid inventing new permanent-looking formal names
- avoid self-registering anything into `trading-main/registry/`
- report every temporary new name it introduced, including where and why it was needed

## What counts as drift

Naming drift includes cases like:

- two names for one shared concept
- a new shared field, output key, script locator, config key, term definition, or default status value invented without registry review
- path, repo, output, script, term, or status naming that ignores an existing registry entry
- Codex introducing a temporary name and failing to report it
- project docs or receipts pretending a name is formal when it has not been reviewed

## Acceptance check

Before accepting naming-sensitive work, check:

- Was an existing registry name reused where possible?
- Did Codex report every temporary new name?
- Does any new shared name or shared status vocabulary now need registration in `trading-main/registry/`?
- Do docs, code, and task artifacts use the same accepted name for the same concept?

## Important restraint

Do not overstate registry authority.

If `trading-main/registry/` does not yet formally own a category, say that plainly instead of pretending the authority already exists.
