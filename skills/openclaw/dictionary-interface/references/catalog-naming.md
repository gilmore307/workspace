# Dictionary Interface

This skill is about how OpenClaw and Codex interact with `universal-catalog` during normal project work.

It does not define the catalog schema.
It does not decide catalog kinds on its own.
It does not let Codex self-register names.

## What `universal-catalog` currently is

Right now `universal-catalog` is the shared register for stable server-wide referenced values used across future trading-oriented work.

Current concrete coverage is centered on catalog items such as:

- `field`
- `template`
- `repo`
- `path`
- `config`

Do not assume a proposed future kind is already formal just because it was discussed in chat.

## Operational rule

When naming matters:

1. Check whether `universal-catalog` already has a suitable shared name.
2. If yes, reuse it.
3. If no, decide whether the work should pause for catalog registration or proceed with an explicitly temporary name.
4. If temporary naming is allowed, make sure Codex reports it back for OpenClaw review.
5. After the task, OpenClaw decides whether to register, rename, or reject that temporary name.

## OpenClaw responsibilities

OpenClaw should:

- keep `universal-catalog` updated as an ongoing maintenance responsibility
- prefer catalog-approved names in task packages, schemas, receipts, paths, and templates
- treat missing shared names as catalog gaps rather than as permission for casual invention
- review Codex-reported temporary names and register the accepted ones itself
- update related skills when naming policy or catalog authority changes

## Codex responsibilities

Codex should:

- reuse catalog-approved names first
- avoid inventing new permanent-looking formal names
- avoid self-registering anything into `universal-catalog`
- report every temporary new name it introduced, including where and why it was needed

## What counts as drift

Naming drift includes cases like:

- two names for one shared concept
- a new shared field or config key invented without catalog review
- path, repo, or template naming that ignores an existing catalog entry
- Codex introducing a temporary name and failing to report it
- project docs or receipts pretending a name is formal when it has not been reviewed

## Acceptance check

Before accepting naming-sensitive work, check:

- Was an existing catalog name reused where possible?
- Did Codex report every temporary new name?
- Does any new shared name now need registration in `universal-catalog`?
- Do docs, code, and task artifacts use the same accepted name for the same concept?

## Important restraint

Do not overstate catalog authority.

If `universal-catalog` does not yet formally own a category, say that plainly instead of pretending the authority already exists.
