---
name: project_development
description: Steward an OpenClaw-managed software project end to end: first-principles project shape, docs spine, module numbering, source/script boundaries, registry naming, implementation dispatch, review, verification, maintenance, commits, and cross-repository alignment. Use for creating, restructuring, implementing, documenting, reviewing, or closing project work when OpenClaw owns the development boundary.
---

# Project Development

Use this skill when OpenClaw is responsible for the shape and health of a software project.

## Core rule

OpenClaw owns project shape: boundaries, names, docs, contracts, dispatch, review, acceptance, maintenance, commits, and cross-repo consistency.
Implementation agents may perform bounded work, but OpenClaw remains responsible for the structure and final acceptance.

## First principles

Apply these before following any historical route:

- Structure before implementation.
- Boundaries before wiring.
- Current contract before route history.
- One canonical home for each fact.
- Names are interfaces; register or document them before depending on them.
- Explicit contracts before hidden behavior.
- Point-in-time evidence before model/trading claims.
- Safe gates before service, provider, broker, database, or storage mutation.
- Small coherent change before broad refactor.
- Root cause before patch.
- Tests follow behavior.
- Remove stale implementation instead of preserving compatibility prose by default.
- Acceptance over aesthetic polish.

## Default workflow

1. Inspect the current repository state, docs spine, source/script layout, tests, and registry references before editing.
2. Decide the canonical home for each fact: project docs, skill rule, registry row, source contract, test, or runtime state.
3. Shape the docs/source boundary first when the request changes architecture, naming, contracts, or ownership.
4. Make one coherent acceptance-sized change; do not chain unrelated cleanups just because they are nearby.
5. Update all active references when renaming paths, modules, scripts, contract ids, or registry-backed names.
6. Run the smallest meaningful verification gate, expanding when the change crosses repos or contracts.
7. Commit and push accepted file-editing work unless the user explicitly says not to.

## Canonical homes

- Workspace-wide project-development rules live in this skill, not in individual repositories.
- Stable user preferences live in `USER.md`.
- Host/environment notes live in `TOOLS.md`.
- Repository-specific current rules live in that repository's docs.
- Active task/decision/memory ledgers live in that repository's docs trunk.
- Registry-backed shared names live in `trading-manager/scripts/registry/` through SQL migrations.
- Historical narrative belongs in Git history, append-only migrations, or dated memory; do not keep route-change narrative in active docs once the current contract is clear.

## Documentation spine rule

Use this numbering scheme for OpenClaw-managed trading repositories unless a repository documents a narrower exception approved by the user.

### Unnumbered entry files

- `README.md` is the repository entry/index.
- `docs/README.md` is optional and should only index a large docs directory.

### `00`-`09`: repository trunk

These are the current first-read files. Use the same meanings across repositories:

- `docs/00_scope.md` — repository boundary: what this repo owns and does not own.
- `docs/01_context.md` — upstream/downstream map, operating assumptions, dependencies, and environment context.
- `docs/02_architecture.md` — internal shape: major components, flows, layering, and directory/module map.
- `docs/03_contracts.md` — accepted external/internal contracts, interfaces, schemas, gates, and acceptance criteria.
- `docs/04_task.md` — current active tasks, blockers, and next gates.
- `docs/05_decision.md` — current effective decision ledger.
- `docs/06_memory.md` — durable project note policy and repo-specific continuity rules.

Do not create repo-specific synonyms such as `02_workflow`, `02_model_stack`, or `03_acceptance` when the file owns the trunk architecture or contract role. Put repo-specific detail inside the fixed trunk file or in a numbered module file.

### `10`-`79`: business / implementation modules

Use two-digit module bands for major business or implementation areas:

- `10_*`, `20_*`, `30_*`, etc. are major module anchors.
- `11_*`, `12_*` or `21_*`, `22_*` are subdocs inside the same module band.
- Module bands should correspond to `src/` packages and `scripts/` entrypoint groups when implementation exists.
- If exact directory matching is impossible, `docs/02_architecture.md` must state the mapping.
- Number by durable module ownership, not by discovery chronology.

Example pattern:

```text
docs/20_registry.md        -> src/trading_registry/ + scripts/registry/
docs/30_task_system.md     -> src/trading_manager_tasks/ + scripts/tasks/
docs/40_scheduler.md       -> scheduler/runtime entrypoints and service docs
```

### `90`-`99`: appendix / compatibility only

Use `90_*` through `99_*` only for appendices, audits, compatibility notes, or historical reference that must remain visible but is not part of the normal current path.

Do not use `100_*` or higher for active docs. If active docs would exceed `99`, merge, split, or renumber by module ownership.

### Renames and registry references

When a docs file is renamed and registry rows point to it, add a `trading-manager/scripts/registry/sql/schema_migrations/` migration and regenerate `trading-manager/scripts/registry/current.csv`. Do not hand-edit generated registry snapshots.

Repository README/docs may list the current local docs spine, but they should not duplicate this shared numbering policy.

## Source, scripts, and registry rules

- `src/` owns importable/reusable implementation: packages, connectors, validators, normalizers, contracts, and pipeline logic.
- `scripts/` owns executable wrappers, smoke runners, maintenance commands, migrations, and operational entrypoints.
- `scripts/` may import `src/`; `src/` must not import `scripts/`.
- Avoid generic `source/` directories because `source` is reserved for provider/data-source meaning.
- Registry `kind=script` names stable callable commands/entrypoints, not ordinary source files or implementation directories.
- Use `implementation_path`, `source_file`, or `source_dir` for code locations; use `provider` or `data_source` for external data origins.
- Keep names aligned with `trading-manager/scripts/registry/` when a name is shared across repositories, automation, or artifacts.
- Reuse registry-registered status vocabularies unless the project explicitly accepts a narrower local vocabulary.

## Cross-repository and data safety

- Treat provider calls, broker/order/account mutation, service starts/stops, destructive SQL, artifact deletion, and storage lifecycle actions as gated operations.
- Separate historical/modeling services from realtime trading and broker execution unless an accepted contract explicitly connects them.
- Define durable data ownership, migration responsibility, backup/restore expectations, and retention tradeoffs before touching databases or high-volume storage.
- Preserve append-only SQL migration history. Fix current state with a new migration instead of rewriting applied migrations.
- Prefer quarantine/trash and backups over irreversible deletion.
- For point-in-time modeling systems, keep raw evidence, interpreted events, labels, and promotion claims separated by explicit clocks and gates.

## Delegation and review

- Dispatch implementation work at medium granularity: one coherent acceptance path, not tiny fragments or broad sweeps.
- Give implementers allowed paths, existing names to reuse, forbidden surfaces, required gates, and expected completion receipt.
- Review completion receipts against docs, code, tests, registry, generated artifacts, and known recurring mistakes before acceptance.
- OpenClaw owns README files, docs spine, acceptance receipts, registry naming, and post-acceptance commits by default. Delegate those only by explicit exception.

## Verification expectations

Use the smallest gate that proves the change, then expand for cross-boundary work:

- Docs-only: path/reference scan, markdown inspection, and `git diff --check`.
- Python code: targeted tests or full `unittest`, plus `python3 -m compileall` when useful.
- TypeScript/frontend: typecheck/build/test as appropriate.
- Registry changes: migration apply/dry-run and generated snapshot review.
- Renames: stale-reference scan across active docs/source/tests/scripts and registry current; exclude immutable migration history only intentionally.
- Runtime/service work: inspect service status/log evidence and safety flags before claiming success.

## Resources

- `references/skill-map.md`
- `references/status-vocabularies.md`
- `references/data-structure.md`
- `references/`
- `templates/`
