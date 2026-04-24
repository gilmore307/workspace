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
