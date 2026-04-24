# Dreaming Session Cleanup

Use this reference only when the user asks to inspect or manually remove expired dreaming sessions.

## Scope

This cleanup is a narrow exception to normal memory routing work.

It may handle only OpenClaw memory-core narrative sessions whose session key contains:

```text
dreaming-narrative-
```

Do not use it for ordinary user, project, ACP, Codex, or chat sessions.

## Expired session rule

A dreaming narrative session is eligible for manual cleanup when all are true:

- the session key contains `dreaming-narrative-`
- `updatedAt` is older than the chosen TTL
- the session is not the current active session
- the transcript file exists or the store entry is stale

Default TTL: 6 hours.

## Cleanup behavior

Use archive-first cleanup, not hard deletion:

1. copy the session store to the archive directory as a backup
2. move eligible transcript files into the archive directory
3. move matching trajectory/checkpoint sidecar files into the archive directory
4. remove eligible `dreaming-narrative-*` entries from `sessions.json`
5. write the updated store atomically

Archive directory pattern:

```text
<workspace>/.openclaw-repair/dreaming-session-cleanup/<timestamp>/
```

## Verification

Before executing:

```bash
python3 skills/openclaw/memory_management/scripts/cleanup_expired_dreaming_sessions.py --dry-run
```

To execute after reviewing the dry-run:

```bash
python3 skills/openclaw/memory_management/scripts/cleanup_expired_dreaming_sessions.py --execute
```

After execution, verify:

```bash
openclaw sessions --agent main --json
openclaw memory status --agent main
```

## Safety rules

- Never remove non-dreaming sessions.
- Never hard-delete transcripts; archive by rename.
- Do not run with a TTL below 1 hour unless the user explicitly asks.
- If a transcript path escapes the sessions directory, stop instead of cleaning it.
- If `sessions.json` cannot be parsed, stop without changes.
