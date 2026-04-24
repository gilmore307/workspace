---
name: project_execution
description: Execute bounded implementation work inside an OpenClaw-managed project. Use when Codex must follow an execution key, stay within allowed paths, reuse approved names, run required verification, and return a completion receipt for review.
---

# Project Execution

Use this skill when Codex is the implementation worker under OpenClaw supervision.

## Core rule

Implement inside the dispatched boundary. Do not take over planning, naming authority, or acceptance.

## Required behavior

- Read the execution key before editing.
- Stay inside allowed paths.
- Do not touch blocked paths.
- Treat `README.md`, the project docs spine, and other governance docs as blocked by default unless the execution key explicitly includes them.
- Reuse catalog-approved names when they fit.
- Keep any unavoidable new name explicitly temporary and report it.
- Do not silently expand scope.
- Run required verification when possible.
- Return the completion report format the task asks for.
- Report readiness for review, not final acceptance.

## Resources

- `references/skill-map.md`
- `references/`
- `templates/`
