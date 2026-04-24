# Dictionary Interface

This reference tells Codex how to behave around `universal-catalog`.

It does not define the catalog schema.
It does not authorize Codex to register names.
It does not turn chat discussion into formal catalog authority.

## Current catalog reality

`universal-catalog` currently centers on shared stable items such as:

- `field`
- `output`
- `repo`
- `path`
- `config`
- `term`
- `script`
- default status vocabularies such as `task_lifecycle_state`, `review_readiness`, `acceptance_outcome`, and `test_status`

If a possible future kind is still under discussion, treat it as discussion, not settled authority.

## Codex rule

When naming matters:

1. Reuse an existing catalog-approved name or default vocabulary value if one fits.
2. If no suitable shared name exists, do not silently invent a permanent one.
3. If the task cannot proceed without a new name, use an explicitly temporary name.
4. Report that temporary name in the completion receipt with where and why it was introduced.

## What to report

If you introduced a temporary name, report:

- the name
- where it appears
- why an existing catalog name did not fit
- whether you think it should be registered or replaced

## Drift to avoid

Avoid:

- two names for one shared concept
- replacing an accepted catalog name with a fresh synonym
- inventing a shared field, output key, repo label, path label, script locator, config key, term definition, or default status value without reporting it
- pretending an unreviewed name is already formal
