# Codex Oversight

Use this file as the standing supervision record for delegated Codex work.

## How to use this file

1. Before delegation, scan the recurring mistake list and include relevant warnings in the task.
2. During review, check the completed work against the same patterns.
3. When a mistake repeats or causes real review cost, record it here.
4. Keep entries short, specific, and testable.

## Preflight prompts for Codex

Use the relevant ones before handing off work:

- Respect the exact scope; do not expand it without approval.
- Preserve naming consistency with the existing codebase and docs.
- Reuse names from `universal-catalog` when naming is part of the task; do not casually invent new permanent names.
- Do not claim completion without evidence.
- Run the smallest meaningful verification step before declaring success.
- Update docs and acceptance artifacts when the task requires them.
- Surface uncertainty instead of improvising hidden assumptions.
- If you introduced any temporary new names, report them explicitly for OpenClaw review instead of self-registering them.

## Review focus

Check these after Codex returns work:

- scope drift
- naming inconsistency
- undocumented behavior changes
- missing tests or weak verification
- incomplete acceptance evidence
- partial edits that leave stale references behind
- unreported assumptions or blockers

## Recurring mistake log

Add one entry per stable pattern.

### Template

- **Pattern:**
- **Typical failure:**
- **Prevention warning:**
- **Review check:**
- **Severity:** low | medium | high
- **Last seen:** YYYY-MM-DD
- **Example task or path:**

### Entries

- **Pattern:** claims completion with weak evidence
- **Typical failure:** says a task is done after editing files but before running the smallest meaningful test, build, lint, diff review, or inspection step
- **Prevention warning:** require explicit verification and specify the minimum acceptance gate in the task handoff
- **Review check:** reject completion claims that do not include a concrete verification result or a named blocker
- **Severity:** high
- **Last seen:** 2026-04-23
- **Example task or path:** general Codex delegation workflow

- **Pattern:** scope drift during implementation
- **Typical failure:** fixes adjacent issues, restructures unrelated code, or adds polish not requested in the task
- **Prevention warning:** restate non-goals and forbid unrelated cleanup unless approved
- **Review check:** compare delivered diff against the requested boundary and reject incidental changes without justification
- **Severity:** high
- **Last seen:** 2026-04-23
- **Example task or path:** general Codex delegation workflow

- **Pattern:** inconsistent naming or doc alignment
- **Typical failure:** introduces names, paths, or wording that do not match existing conventions, or updates code without matching doc changes
- **Prevention warning:** require reuse of existing names and call out the authoritative docs or files to align with
- **Review check:** compare identifiers, filenames, and referenced docs against the existing convention source
- **Severity:** medium
- **Last seen:** 2026-04-23
- **Example task or path:** general Codex delegation workflow

- **Pattern:** unregistered naming drift
- **Typical failure:** invents a new field, path label, config key, repo name, or filename token without checking `universal-catalog`, then treats that new name as settled
- **Prevention warning:** instruct Codex to reuse catalog-approved names first and require explicit reporting of any temporary new names it had to introduce
- **Review check:** compare new formal names against `universal-catalog`; reject silent new vocabulary and require OpenClaw registration review
- **Severity:** high
- **Last seen:** 2026-04-23
- **Example task or path:** naming-sensitive implementation and dispatch workflow

## Update rule

Only keep patterns that are recurrent, costly, or predictive. Do not turn this into a noisy diary.
