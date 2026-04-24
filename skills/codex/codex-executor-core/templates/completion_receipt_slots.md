# Completion Receipt Slots

Use these canonical slot names when a project writes a formal completion receipt.
This template standardizes slot concepts and field names, not one mandatory JSON wrapper.

Exact JSON nesting, path naming, and value vocabularies remain project-defined unless the project documents them explicitly.

## Required Slots

- `TASK_IDENTITY` (`task_identity`) — stable identity for the completed task
- `WORKFLOW_IDENTITY` (`workflow_identity`) — workflow identity that owns the task
- `CHANGE_SUMMARY` (`change_summary`) — short summary of what changed
- `CHANGED_FILES` (`changed_files`) — changed file list
- `COMMAND_LIST` (`command_list`) — commands Codex ran
- `TEST_STATUS` (`test_status`) — summary test status reported by Codex
- `TEST_OUTPUT` (`test_output`) — test output or concise test evidence
- `ISSUE_LIST` (`issue_list`) — issues, blockers, or known gaps
- `REVIEW_READINESS` (`review_readiness`) — whether Codex reports the task ready for OpenClaw review

## Optional Slots

- `TASK_LIFECYCLE_STATE` (`task_lifecycle_state`) — task state label when the project records one in the receipt
- `TEMPORARY_NEW_NAMES` (`temporary_new_names`) — temporary names introduced during execution, when applicable
- `OUTPUT_REFERENCE` (`output_reference`) — output path or artifact reference when applicable

## Notes

- Reuse previously ratified shared slots from `universal-catalog` where they fit.
- Standardizing slot names here does not standardize task-state labels, review-readiness values, test-status vocabularies, or one single receipt container shape.
- Codex may report readiness or not-readiness, but must not report final acceptance or rejection.
