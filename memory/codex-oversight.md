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
- For repair agents, do not stop at a local patch: verify, commit/push repository edits, and either rerun the failed operation or record why it must remain queued.
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
- unreconciled repair patches left uncommitted or unretried
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

- **Pattern:** incomplete clean-start cleanup
- **Typical failure:** stops or restarts only the currently visible process while leaving older runtime state, receipts, logs, error catalogs, dashboard read models, or generated database feature/model/control-plane rows active
- **Prevention warning:** for clean-start tasks, explicitly preserve downloaded source data, stop active writers, quarantine active runtime/read-model artifacts, and reset non-source generated DB tables before claiming a clean state
- **Review check:** verify active runtime paths are empty, dashboard read models no longer contain stale failures, non-source DB tables are zeroed, source tables still retain rows, and services are either intentionally stopped or restarted from the clean baseline
- **Severity:** high
- **Last seen:** 2026-05-18
- **Example task or path:** trading clean-start reset across `trading-manager`, `trading-model`, `trading-execution`, `trading-storage`, and generated DB tables

- **Pattern:** uses trash/recycle storage when direct deletion was requested
- **Typical failure:** moves obsolete files to trash after Chentong explicitly asked to delete them, leaving the data retained under a different path
- **Prevention warning:** if the instruction says delete/remove old files or artifacts, use permanent deletion for the targeted files; use trash only when recoverability is requested or deletion intent is ambiguous
- **Review check:** after deletion, verify both the original path and trash/recycle locations no longer contain the targeted files
- **Severity:** high
- **Last seen:** 2026-05-19
- **Example task or path:** `trading-manager/storage/runtime/agent_error_handling/server_error_catalog.jsonl`

- **Pattern:** repair agent leaves an uncommitted local fix without operational closure
- **Typical failure:** patches source code and passes dry-run checks, but does not commit/push the fix, rerun or queue the failed stage, or update the error disposition, so the runtime still appears broken
- **Prevention warning:** require repair receipts to prove durable code state and runtime closure: committed changes plus rerun result, retry recommendation, or explicit blocker
- **Review check:** inspect git status, the failed operation status, and the error artifact before accepting `repaired` or `repaired_verified`
- **Severity:** high
- **Last seen:** 2026-05-26
- **Example task or path:** `erragent_e3390e96ee0df733` / `layer_02_sector_context.feature_generation`

## Update rule

Only keep patterns that are recurrent, costly, or predictive. Do not turn this into a noisy diary.
