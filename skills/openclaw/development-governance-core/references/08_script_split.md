# Script Split Rules

OpenClaw must prevent premature fragmentation.

Do not split scripts, modules, docs, workflows, or tasks merely because a function or subtopic exists.

## Split Gates

A split is allowed only when at least one gate is true:

1. The logic or content is reused by multiple scripts or workflows.
2. A stable branch starts here.
3. A complete workflow ends here.
4. It is a clear side branch such as test, fixture, mock, or entry wrapper.
5. The file is already large enough to hurt understanding or modification.

## Weak Split Rule

If the split reason is weak, keep the logic in the current file as an internal function first.

Do not create a new file just to make a single function look tidy.

## Codex Constraint

Every Codex execution key should include:

```text
Do not create extra files unless one of the script split gates is met.
```

## Acceptance Review

When reviewing Codex output, OpenClaw checks:

- Did Codex create new files?
- For each new file, which split gate was met?
- Are new files named with `universal-catalog` terms?
- Did Codex create generic folders such as `utils`, `helpers`, or `common`?
- Is the split useful for future understanding or modification?
- Would an internal function have been better?

## Valid Split Examples

Reused by multiple scripts:

```text
src/config/load_config.py is used by CLI startup and service startup.
```

Stable branch starts here:

```text
src/input/parse_json.py and src/input/parse_csv.py differ by stable input type.
```

Complete workflow ends here:

```text
src/workflow/build_output.py produces the final workflow output.
```

Side branch:

```text
tests/config/test_load_config.py
fixtures/config/default_config.json
```

File size hurts understanding:

```text
A 900-line parser has three stable stages and is difficult to modify safely.
```

## Invalid Split Examples

Avoid:

```text
src/utils.py
src/helpers.py
src/common.py
src/new_parser.py
src/final_config.py
```

Avoid splitting:

- because a helper function exists
- because a file looks slightly long
- because Codex prefers more files
- because a name sounds reusable but nothing reuses it
- because the task was underspecified

## Task Split Parallel

Task splitting follows the same spirit.

Do not create many tiny tasks unless each has a real boundary, separate acceptance point, separate workflow step, or separate blocker.
