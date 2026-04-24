# Data Structure and Persistence

Use this reference when a project introduces or changes durable data, database tables, migrations, retention, backups, or high-volume storage.

## Core rule

Design data ownership before implementation.

For every durable data surface, define:

- the active storage owner
- the table or file boundary
- the schema-change path
- whether the data is small static reference data or high-volume active data
- backup and restore expectations
- retention or pruning expectations when disk may be constrained
- which docs file owns the decision

## Database boundary

Prefer one durable database boundary per deployment context when multiple related tables will grow together.

Use separate tables for separate data classes instead of separate databases unless there is a real boundary such as:

- different access control
- different backup/restore cadence
- different lifecycle or retention policy
- different operational owner
- different deployment target

Name tables for the data class they own. Do not use a repository name as the whole database name when the database is expected to hold several future data classes.

## Migration responsibility

Migrations manage database schema version evolution.

Migrations are responsible for:

- creating, modifying, and dropping table structures
- adding, removing, and changing columns
- creating indexes
- creating constraints, foreign keys, and uniqueness rules
- creating necessary schema-level objects
- recording how the database structure moves from one version to another
- inserting only extremely small, stable lookup/bootstrap rows that schema or code directly depends on

Migrations are not responsible for:

- ordinary business data
- test data
- data produced during user/runtime operation
- large initialization datasets
- frequently changing configuration data
- high-volume active datasets

## Storage placement rule

SQL is for data with long-term storage value and structured query value.

Put data in SQL when it is:

- durable project/application state that must survive restarts
- relational or query-heavy data with stable schema expectations
- canonical metadata used by multiple workflows or tools
- low- to medium-churn reference/config records that are not secrets
- task/state/checkpoint data that needs transactional consistency
- data that benefits from indexes, constraints, joins, or uniqueness rules

Do not put data in SQL by default when it is:

- high-volume logs or traces
- frequent append-only runtime noise
- transient cache data
- generated artifacts that can be rebuilt
- large binary blobs, media, screenshots, or documents
- raw model transcripts or verbose debugging output with limited long-term value
- temporary import/export staging data

Use files or append-only log storage with retention for operational logs. Use object/file storage for large blobs and generated artifacts. Use explicit pruning for caches and temporary data.

Use CSV when a table-like artifact has strong human-review value and is primarily meant to be opened, inspected, shared, or archived by a person rather than queried transactionally. Good CSV candidates include summary reports, review tables, audit exports, and small hand-checkable snapshots.

## Table granularity rule

A dedicated SQL table is justified when a dataset is large enough, structurally stable enough, or queried often enough to benefit from database behavior.

Good SQL-table candidates include:

- large fixed-schema datasets, such as thousands of stock bars or time-series rows
- datasets that need indexed lookup, filtering, aggregation, joins, or constraints
- datasets that will be appended to or updated over time while preserving a stable schema
- datasets that multiple workflows need to query consistently

Avoid creating a dedicated SQL table for tiny isolated datasets whose main value is storage or human inspection. For example, a 10-row fixed-format sample is usually better as CSV or JSON unless it participates in a larger relational workflow.

Ask before adding a table:

- Is the schema stable and worth naming?
- Is the row count or growth path large enough to justify database management?
- Will code query it repeatedly, join it, filter it, or enforce constraints?
- Would CSV/JSON be simpler and equally reliable?

## Large-data rule

When disk is finite, prioritize active data integrity over exhaustive auditability.

Do not duplicate high-volume active data into Git as SQL literals or full-row history unless a task explicitly justifies:

- why the duplicate copy is necessary
- expected data volume
- disk budget
- retention window
- restore procedure

Use the database as the active data store and define a backup/restore policy instead of making migrations or docs become a second database.

## Audit tradeoff

Keep lightweight audit surfaces by default:

- migration ledger for applied schema/data-change scripts
- Git commits for reviewed migration files
- small operational summaries when useful

Avoid default full-row revision tables for high-volume data. Add them only when the project documents a concrete audit requirement and retention policy.

## Docs routing

Route database facts to the narrowest project doc:

- `00_scope.md`: whether durable storage is in or out of project scope
- `01_context.md`: database engine, deployment assumptions, backup dependencies
- `02_workflow.md`: data flows, writers, readers, migration application flow
- `03_acceptance.md`: migration/test/backup verification gates and rejection rules
- `04_task.md`: current data-structure work items
- `05_decision.md`: ratified choices such as database boundary, migration model, retention policy, or audit tradeoff

## Acceptance prompts

Before dispatching implementation that touches durable data, define:

- active database/table names
- migration file naming/location
- whether any bootstrap rows are small and stable enough to belong in a migration
- forbidden data duplication paths
- backup or restore check appropriate to the project stage
- minimum verification command
