# Default Status Vocabularies

Use these default vocabularies when a project records formal status fields.
These defaults should be reused from `trading-main/registry/` unless the project docs explicitly define an override.

## task_lifecycle_state

- `designing`
- `ready_to_dispatch`
- `dispatched`
- `executing`
- `blocked`
- `ready_for_acceptance`
- `accepted`
- `rejected`
- `closed`
- `cancelled`

## review_readiness

- `ready`
- `not_ready`
- `blocked`

## acceptance_outcome

- `accepted`
- `rejected`
- `returned`
- `blocked`

## test_status

- `passed`
- `failed`
- `not_run`
- `partially_run`
- `not_required`

## maintenance_status

- `healthy`
- `needs_attention`
- `blocked`

## docs_status

- `aligned`
- `drifted`
- `blocked`

## Override rule

A project may override these vocabularies only when it documents the replacement values and the conversion boundary clearly.
Do not silently drift from the defaults.
