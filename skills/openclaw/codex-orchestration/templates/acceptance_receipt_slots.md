# Acceptance Receipt Slots

Use these canonical slot names when a project writes a formal acceptance receipt.
This template standardizes slot concepts and field names, not one mandatory JSON wrapper.

Exact JSON nesting, path naming, and value vocabularies remain project-defined unless the project documents them explicitly.

## Required Slots

- `TASK_IDENTITY` (`task_identity`) — stable identity for the reviewed task
- `WORKFLOW_IDENTITY` (`workflow_identity`) — workflow identity that owns the task
- `ACCEPTANCE_OUTCOME` (`acceptance_outcome`) — OpenClaw review outcome for the task
- `ACCEPTANCE_REFERENCE` (`acceptance_reference`) — file, path, or section used as the acceptance basis
- `REVIEWED_FILES` (`reviewed_files`) — files reviewed during acceptance
- `REVIEWED_COMMANDS` (`reviewed_commands`) — commands reviewed during acceptance
- `TEST_STATUS` (`test_status`) — summary test status used in the review
- `TEST_OUTPUT` (`test_output`) — test output or concise test evidence used in the review
- `ISSUE_LIST` (`issue_list`) — remaining issues, rejection reasons, or follow-up concerns
- `ACCEPTANCE_SUMMARY` (`acceptance_summary`) — concise acceptance decision summary

## Optional Slots

- `DECISION_REFERENCES` (`decision_references`) — related decision records when relevant
- `NEXT_TASK_REFERENCE` (`next_task_reference`) — next linked task when follow-up work is needed

## Notes

- Reuse previously ratified shared slots from `universal-catalog` where they fit.
- Standardizing slot names here does not standardize acceptance-outcome vocabularies, issue classifications, or one single receipt container shape.
- Only OpenClaw writes the acceptance receipt and final acceptance outcome.
