# Dreaming Session Cleanup

Use this reference when the user asks to inspect or remove expired dreaming sessions, or when verifying the runtime self-cleanup path after dreaming narrative sessions end.

## Scope

This cleanup is a narrow exception to normal memory routing work.

It may handle only OpenClaw memory-core narrative sessions whose session key contains:

```text
dreaming-narrative-
```

Do not use it for ordinary user, project, ACP, Codex, or chat sessions.

## Runtime self-cleanup expectation

Dreaming narrative sessions should clean themselves at run end. The runtime first asks the subagent/session runtime to delete the transient narrative session, then runs a fallback scrub. If a completed `dreaming-narrative-*` session remains referenced in `sessions.json`, the fallback should remove the store entry and archive its transcript/trajectory/checkpoint files.

Manual cleanup is the safety net for sessions that predate the self-cleanup fix, failed during cleanup, or are still within the configured TTL.

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
