---
name: "storage-lifecycle-review"
description: "Review persistent artifact lifecycle mutations and retention."
---

# Storage Lifecycle Review

Use this skill when an agent must judge whether a persistent artifact, table, path, cache, side product, dashboard/read model, receipt, manifest, script/doc surface, or obsolete route may be retained, compacted, compressed, archived, restored, deleted, retired, or otherwise lifecycle-mutated.

This skill does not decide project architecture, documentation homes, registry naming, source/script structure, memory routing, repair strategy, or active implementation design. Those belong to their owning skills. Storage lifecycle review asks a narrower question:

> May this persistent artifact/table/path be backed up, retained, compacted, compressed, archived, restored, deleted, or retired, given policy, consumers, protection status, canonical ownership, and restore evidence?

When lifecycle safety depends on canonical ownership, current route, memory routing, project structure, or repair status, require evidence from the owning skill or return `defer` / `insufficient_evidence`.

## Goals

- Keep storage controllable, auditable, dashboard-ready, concise, and storage-efficient.
- Preserve source evidence and canonical state that cannot be safely rebuilt or reacquired.
- Keep enough information to verify decisions, reproduce durable facts, restore required state, and support dashboards or operators.
- Avoid long-term duplicate CSV, JSONL, cache, snapshot, manifest, or side-product copies after a canonical home is verified.
- Ensure side products exist only for a concrete use need.

## Owning Skill Boundaries

Use or require evidence from these skills when needed:

- `project_development`: project shape, active docs/source/script boundaries, registry-backed names, canonical project facts, obsolete route closure, replacement-route acceptance, and cross-repository consistency.
- `memory_management`: durable information routing across `USER.md`, `TOOLS.md`, `AGENTS.md`, `MEMORY.md`, daily memory, handoff files, and project docs.
- `server-error-repair`: autonomous bug repair, code/config patches, reruns, reconciliation, dashboard/read-model repair, failure closure, and repair receipts.
- Domain review skills: promotion, runtime model lifecycle, event, regime, target context, failure register, or trade-operation evidence when lifecycle mutation would remove or archive domain decision evidence.

Storage lifecycle review may approve or reject the storage mutation after the owning skill establishes the current contract, canonical home, or repair status.

## Scope

This skill covers lifecycle mutation review for:

- source/provider data and source receipts;
- SQL tables, views, materialized views, dumps, exports, and derived table artifacts;
- dashboard caches, read models, snapshots, aggregates, and presentation artifacts;
- runtime receipts, task keys, logs, manifests, loop directories, scheduler decisions, stage evidence, and repair side products;
- model/runtime/evaluation artifacts when the question is retention, archive, compaction, compression, deletion, or restore;
- cold evidence, compressed evidence, backups, and restore indexes;
- scripts, docs, configs, service units, generated files, and obsolete routes only when their backup, retention, archival, retirement, or deletion is being reviewed.

Active script/doc design, docs spine, registry naming, source/script split, and project route selection remain `project_development` responsibilities.

## Lifecycle Action Taxonomy

Separate review actions from final artifact handling methods.

Reviewable lifecycle actions include:

- `backup`: create or validate a protective copy, logical dump, restore point, or evidence snapshot.
- `restore`: recover or read back a prior artifact, table, path, or state.
- `keep`: explicitly retain an artifact because it has current consumer, audit, source, restore, or canonical value.
- `retention_update`: change lifecycle policy, retention window, protected status, or exception rules.
- `cleanup`: execute a defined lifecycle policy over a target scope.
- `compact`: produce a concise summary, manifest, aggregate, decision contract, or read model before final handling.
- `archive`: move evidence into compressed cold storage with an index and restore route.
- `delete`, `compress`, and `rolling_retention`: final handling methods.
- `migrate`, `retire`, `replace`: lifecycle actions tied to route/table/path transitions after the owning project/domain skill establishes the current route.

Final artifact handling should normally reduce to three concrete methods:

1. `delete`: Use for artifacts that have no remaining consumer/use and are safely rebuildable, replaceable, erroneous, obsolete, or outside the accepted scope. Delete after active/retry/failure consumers are closed and any required compact summary already exists.
2. `compress`: Use for artifacts that are not normally read, still have audit/restore/lineage value, and are not safely rebuildable or reacquirable. Keep concise provenance, hash, source range, compression method, created time, and restore route when required.
3. `rolling_retention`: Use for repeated runtime, dashboard, log, loop, snapshot, and read-model artifacts where only recent windows matter. Keep latest/current plus a small bounded count/time/session window, and keep exceptions for unresolved failures, anomalies, active repair, or required audit windows.

`compact` is not a final retention state. It is a preparation step before delete, compress, or rolling retention: preserve the minimum summary/manifest/decision contract needed by dashboards, audit, restore, retry, or operators, then handle the verbose artifact through one of the three methods above.

`archive` means compressed cold evidence plus an index/restore route. Do not use archive as a vague alternative to deciding whether the artifact should be deleted, compressed, or kept in a rolling window.

## Triggered, Not Blind Timed Deletion

Do not rely on blind scheduled deletion as the primary lifecycle mechanism. Scheduled jobs that delete by age alone are weak evidence and easily remove the wrong thing or preserve the wrong thing.

Preferred lifecycle triggers are state transitions and producer/owner checkpoints:

- a batch, stage run, provider acquisition, replay, repair, or dashboard refresh completes;
- a task moves to succeeded, failed terminal, failed retryable, superseded, or retired;
- a compact manifest, rollup summary, or dashboard read model is verified;
- a replacement route is accepted and old consumers are migrated;
- an audit window closes;
- a rolling window advances and unresolved/anomaly exceptions are identified.

Periodic automation may still exist, but its role should be limited:

- audit/report unbounded growth, stale routes, missing compact contracts, and policy gaps;
- execute explicit rolling-retention or compact-then-delete/compress policies that already have owner, class, consumer, protected-set, and exception rules;
- never perform broad unknown-scope deletion merely because a timer fired.

A lifecycle policy is stronger when it is attached to the producer or accepted state machine than when it depends on a standalone cleanup timer.

## Lightweight Lifecycle Declaration

Do not create registration sprawl. Lifecycle facts should live in the narrowest existing canonical home whenever possible: schema/table contract, registry row, source manifest, read-model producer, compact manifest, script help, README, owner docs, or lifecycle policy selector.

For lifecycle review, collect the minimum facts needed for the decision:

- `artifact_ref`: path, table, registry id, route, or logical artifact id.
- `artifact_class`: primary lifecycle class.
- `owner`: component or repository responsible for lifecycle.
- `canonical_owner_or_home`: where the durable fact lives, or which skill/component owns deciding that.
- `consumer_or_use`: concrete consumer, dashboard, review, restore, audit, retry, debug, reconciliation, or operational need.
- `retention_policy`: `delete`, `compress`, `rolling_retention`, `keep`, or a narrow policy id that maps to one of those final handling methods or to explicit retention.

Add protected status, rebuildability, source refs, compact contract, audit window, restore route, dashboard surface, failure/repair refs, expiry time, replacement ref, or retirement status only when needed for the mutation decision.

If the lifecycle review cannot name a concrete consumer/use or canonical owner, defer or reject the artifact's persistence.

## Artifact Classes

Use these classes as lifecycle review inputs, not as a mandatory universal registration system.

### `source_evidence`

Provider/source data, raw payloads, point-in-time snapshots, filings, market data, macro releases, news captures, official disclosures, or other facts that may be unreacquirable or audit-critical.

Rules:

- Default protected.
- Trading Economics historical source data is protected source evidence unless a narrower accepted contract says otherwise.
- Do not delete unless an accepted policy proves the artifact is duplicate, erroneous, outside scope, or safely replaceable.
- Preserve source identity, capture time, available time, source hash, schema, and provenance when required.
- Prefer compression over deletion for cold source evidence.

### `canonical_state`

Accepted durable home of a fact or contract: SQL table, registry current row, accepted schema, current manifest, active contract, source-controlled maintained surface, accepted model artifact index, or another declared canonical home.

Rules:

- Do not mutate destructively without owner, consumer, schema/contract, backup/restore, and readback evidence.
- SQL-resident durable facts stay in SQL; do not preserve migrated legacy JSONL/catalog/cache files under a new storage folder just to avoid deletion.
- If canonical ownership is unclear, defer to `project_development`, `memory_management`, or the owning domain skill.

### `derived_read_model`

Dashboard, query, API, presentation, cache, or read model state derived from canonical state or source evidence.

Rules:

- Must have a real consumer or display need.
- Must identify canonical source or producer when not obvious.
- Keep latest/current plus bounded history only when history is needed.
- Use rolling retention for repeated snapshots or trends.
- Do not let dashboard snapshots become accidental canonical state.
- Dashboards and summaries may duplicate facts only as derived presentation or aggregate state.

### `runtime_evidence`

Receipts, task keys, logs, scheduler decisions, stage sidecars, loop directories, repair traces, provider dispatch records, and similar operational evidence.

Rules:

- Keep active, failed, retryable, unresolved, and recently useful evidence.
- For completed/successful high-volume evidence, compact to batch manifests or rollup summaries, then delete, compress, or roll forward the verbose records according to policy.
- Logs and JSONL files should roll into summaries and bounded tails when dashboards or operators need the data; compression alone is not a usable summary.

### `decision_evidence`

Evidence required to audit lifecycle decisions, model promotion, gate review, trade decisions, repair decisions, event interpretation, failure disposition, or policy intervention.

Rules:

- Preserve compact decision contracts: decision, inputs, hashes, thresholds, blockers, repair refs, retry refs, source refs, and rationale.
- Verbose diagnostics may be compressed or deleted only after the compact contract and source refs are verified.
- Do not delete decision evidence before the accepted audit window closes.
- Defer to the owning domain review skill when domain validity or audit value is unclear.

### `debug_side_product`

Temporary troubleshooting output, exploratory dumps, ad hoc diagnostics, failed experiment scratch data, and non-canonical convenience exports.

Rules:

- Default delete after the associated repair, experiment, or investigation closes.
- Must have an owner and use case while it exists.
- Must not become a dashboard source, model input, or accepted contract without reclassification.
- If unrebuildable debug output unexpectedly has audit value, reclassify as `cold_evidence` and compress with provenance.

### `cold_evidence`

Low-frequency evidence retained for audit, restore, lineage, or compliance but not normally read by active workflows.

Rules:

- Compress and store compact provenance.
- Keep source hash, compression method, source range, generation command, created time, and restore route when required.
- Prefer one canonical compressed copy plus concise index over duplicate verbose files.

### `obsolete_route`

Superseded persisted files, tables, views, scripts, docs, compatibility paths, artifacts, schemas, or routes being reviewed for retirement or deletion.

Rules:

- Storage review can approve deletion/archive only after `project_development` or the owner proves active consumers are migrated or the route is explicitly retired.
- Immutable migrations or historical audit records may remain when required.
- Active route design and consumer migration are not decided by this skill.

## Side Product Rule

Side-product artifacts exist only to serve a use need.

A side product is valid only when it supports at least one of:

- active retry or repair;
- failure diagnosis;
- dashboard/display or operator situational awareness;
- compact audit/decision evidence;
- restore/rebuild lineage;
- provider/source acquisition reconciliation;
- replay or evaluation reproducibility;
- short-lived debugging with expiry;
- legally or contractually required evidence.

If no real workflow will read, restore, audit, retry, reconcile, display, or debug from it, it should not persist. If it already exists, classify it as `debug_side_product` or `obsolete_route`, then delete, compress, or place under rolling retention according to policy.

## Duplicate Fact Rule

Storage lifecycle review must guard against duplicate persisted facts, but it does not own all canonical routing decisions.

Rules:

- Before approving retention or mutation, identify the canonical owner/home or require evidence from the owning skill.
- Do not keep duplicate CSV, JSONL, cache, snapshot, manifest, or catalog copies after SQL or another canonical home has been verified unless a clear audit, display, repair, replay, reconciliation, or restore role remains.
- Dashboard/read-model/display files and compact summaries may repeat facts only as derived artifacts that cite or imply their canonical source/producer.
- If the duplicate appears to be a memory-routing or project-structure problem, defer to `memory_management` or `project_development`.

## Dashboard and Display Rules

Dashboard support is a lifecycle requirement, not an excuse for uncontrolled duplicate state.

- Dashboards should read compact read models, latest pointers, aggregates, or decision contracts.
- Dashboards should not depend on scanning unbounded JSONL logs, timestamped loop directories, raw receipts, or verbose gate-review dumps.
- If a display needs history, create a bounded aggregate or trend read model and use rolling retention for raw snapshots.
- If a dashboard artifact is rebuildable, keep the rebuild command and source refs when not obvious from the producer.
- If a dashboard artifact becomes operational decision evidence, reclassify it as decision or runtime evidence and define the audit window.

## SQL and Data Table Lifecycle Rules

- Treat SQL tables containing durable facts as canonical state unless a narrower contract says they are derived or temporary.
- Before dropping, truncating, migrating, or replacing a table, verify owner, consumers, schema, backup/logical dump requirements, restore route, and readback checks.
- Derived SQL tables, exports, and materialized read models must have upstream sources and a rebuild route.
- Avoid long-term compatibility tables/views after the current table contract is accepted; require owner/project-development evidence that consumers have migrated before lifecycle mutation.
- SQL-resident facts should not be duplicated into long-term JSONL or catalog files to avoid deletion.

## Script, Doc, and Project-Surface Lifecycle Rules

Scripts, docs, configs, service units, schemas, registry rows, and maintained source files are project surfaces. Their active design belongs to `project_development` or another owner.

Storage lifecycle review applies only when a persisted project surface is being backed up, archived, retained, retired, deleted, or treated as an obsolete route.

Rules:

- Require owner/current-route evidence before deleting or archiving a maintained surface.
- Require stale-reference or consumer evidence before retiring obsolete scripts/docs/configs/routes.
- Do not decide docs spine, script split, registry naming, source layout, or project architecture in this skill.
- Do not preserve obsolete wrappers, duplicate docs, or compatibility shims as storage artifacts merely to avoid deletion.

## Human Review Boundaries

Human or agent review is required when:

- deletion is irreversible or broad;
- the artifact is protected, unrebuildable, or rebuildability is unknown;
- canonical owner/home is ambiguous;
- SQL/table mutation affects durable facts;
- dashboard/read-model mutation affects active operator or automation consumers;
- decision evidence would be removed before its audit window closes;
- replacement work may leave old consumers alive;
- provider/source data, broker/account/order/position state, legal/platform constraints, or secrets may be affected;
- accepted lifecycle policy does not cover the action.

Deterministic automation may proceed when:

- policy is explicit;
- protected-set checks are clear;
- sources and rebuild/restore routes are verified when required;
- action scope is narrow and expected;
- compact contracts or summaries already preserve required evidence;
- no active consumer depends on the verbose artifact being removed.

## Required Inputs for Mutation Review

For lifecycle mutation review, require:

- lifecycle action: backup, restore, keep, retention_update, cleanup, compact, delete, compress, rolling_retention, migrate, retire, replace, or archive;
- final handling method when action is `cleanup`, `compact`, `migrate`, `retire`, `replace`, or `archive`: delete, compress, rolling_retention, keep, or not_applicable;
- target scope and concrete paths, tables, refs, or route ids;
- artifact class or minimum lifecycle declaration;
- retention policy and protected-set status;
- canonical owner/home and consumer evidence;
- backup/logical dump/restore route when required;
- readback or rebuild verification plan;
- deletion or mutation eligibility evidence;
- compact contract or summary ref when verbose artifacts are being removed;
- rolling-window and exception rules for repeated artifacts;
- risk summary and rollback/restore route if available.

## Output Contracts

Use structured prose for lightweight lifecycle classification when that is enough. Use strict JSON for lifecycle mutation review decisions. Do not create bulky classification artifacts merely because this section exists.

### Lifecycle Classification Output

```json
{
  "review_type": "artifact_lifecycle_classification",
  "artifact_ref": "string",
  "artifact_class": "source_evidence|canonical_state|derived_read_model|runtime_evidence|decision_evidence|debug_side_product|cold_evidence|obsolete_route",
  "owner": "string",
  "canonical_owner_or_home": "string|null",
  "consumer_or_use": "string",
  "retention_policy": "delete|compress|rolling_retention|keep|policy_ref|string",
  "blocking_issues": ["string"],
  "required_followups": ["string"]
}
```

### Lifecycle Mutation Review Output

```json
{
  "review_type": "storage_lifecycle_review",
  "decision": "approve|defer|reject|insufficient_evidence",
  "action": "backup|restore|keep|retention_update|cleanup|compact|delete|compress|rolling_retention|migrate|retire|replace|archive",
  "final_handling_method": "delete|compress|rolling_retention|keep|not_applicable|insufficient_evidence",
  "target_scope": "string",
  "artifact_class": "string",
  "canonical_home_status": "clear|ambiguous|missing|not_required|insufficient_evidence",
  "backup_status": "present|not_required|missing|insufficient_evidence",
  "protected_set_status": "clear|blocked|insufficient_evidence",
  "restore_route_status": "available|not_required|missing|insufficient_evidence",
  "consumer_status": "clear|blocked|insufficient_evidence",
  "compact_contract_status": "present|not_required|missing|insufficient_evidence",
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

### Periodic Audit Output

```json
{
  "review_type": "storage_lifecycle_audit",
  "scope": "string",
  "findings": [
    {
      "artifact_ref": "string",
      "artifact_class": "string|unknown",
      "issue": "unbounded_growth|duplicate_canonical_home|stale_dashboard_state|obsolete_route|oversized_verbose_evidence|missing_compact_contract|unclear_owner|unclear_consumer|unclear_rebuildability|other",
      "recommended_action": "classify|compact|compress|delete|rolling_retention|migrate|retire|keep|investigate",
      "review_required": true
    }
  ],
  "blocking_issues": ["string"],
  "required_followups": ["string"]
}
```

## Non-Negotiable Boundaries

- Do not delete, archive, restore, move, compact away, or mutate protected artifacts without policy evidence, protected-set checks, consumer checks, and restore/backup evidence when required.
- Do not approve deletion when canonical owner/home, source status, rebuildability, or consumers are ambiguous.
- Do not create lifecycle registration sprawl; put lifecycle facts in existing canonical homes whenever possible.
- Do not duplicate the same information across persisted artifacts unless it is a dashboard/read-model/summary artifact with source refs or an explicit temporary compatibility/audit surface.
- Do not create or keep side-product files that have no concrete consumer, restore path, audit role, retry role, dashboard need, reconciliation need, replay need, or short-lived debug purpose.
- Do not preserve migrated legacy JSONL/catalog/cache files under a new storage folder just to avoid deletion.
- Do not let dashboards, repair flows, or model pipelines depend on verbose side products when a compact contract is required.
- Do not use blind scheduled deletion as a substitute for owner policy, artifact classification, compact contracts, rolling-window rules, and state-transition cleanup.
- Do not leave new and old active routes coexisting as a storage workaround; require project/owner evidence and then retire or delete old persisted routes under policy.
- Do not use lifecycle review to grant authority for broker/account/order/position mutation, repair strategy, memory routing, project architecture, registry naming, or active implementation design.

## Acceptance Checks

Before accepting a lifecycle policy, compact contract, mutation automation, or cleanup decision:

- classify representative real artifacts involved in the policy;
- verify canonical owner/home and consumers;
- prove rebuildability with source refs, command refs, schema refs, and time windows when rebuildability matters;
- confirm protected source evidence is not targeted for ordinary cleanup;
- confirm dashboard consumers can read compact/latest/aggregate forms;
- verify verbose artifacts are only removed after compact contracts exist;
- verify rolling-retention exceptions preserve active, failed, retryable, unresolved, anomaly, and audit-window evidence;
- require owner/project-development evidence before retiring scripts, docs, paths, tables, routes, or maintained project surfaces;
- run the smallest meaningful dry-run, readback, restore, dashboard, or stale-reference check.
