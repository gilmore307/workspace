# Acceptance

Only OpenClaw may produce final acceptance.
If an acceptance slot is unresolved, record the gap in `04_task.md` and fill it before dependent work can be accepted cleanly.

Boundary:
Own consolidated acceptance rules, verification commands, review evidence, and rejection reasons here.
Do not use this file for project purpose, runtime architecture, dependency explanation, or current task queue state.

## Acceptance Summary

Summarize the accepted current slice and the next acceptance gate.

## Acceptance Rules

### For current shipped code

- Record the rules the currently shipped code must continue to satisfy.

### For docs-only changes

- Record how documentation-only changes are reviewed and accepted.

### For the next code-bearing slice

- Record the gate the next implementation slice must satisfy before acceptance.

## Verification Commands

- List the current required verification commands.
- State which existing command path future slices must extend instead of inventing parallel verification paths.

## Required Review Evidence

- List the evidence OpenClaw requires during review.

## Rejection Reasons

- List the conditions that force rejection or return.
