#!/usr/bin/env python3
"""Archive expired OpenClaw memory-core dreaming narrative sessions.

Default mode is dry-run. Use --execute to mutate sessions.json and move files.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DREAMING_KEY_FRAGMENT = "dreaming-narrative-"
DEFAULT_STORE = Path("/root/.openclaw/agents/main/sessions/sessions.json")
DEFAULT_WORKSPACE = Path("/root/.openclaw/workspace")
MIN_TTL_HOURS = 1.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", type=Path, default=DEFAULT_STORE, help="sessions.json path")
    parser.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE, help="workspace path for archive directory")
    parser.add_argument("--ttl-hours", type=float, default=6.0, help="minimum inactivity age before cleanup")
    parser.add_argument("--execute", action="store_true", help="apply changes; default is dry-run")
    parser.add_argument("--dry-run", action="store_true", help="preview changes without writing")
    parser.add_argument("--active-key", default="", help="session key to protect explicitly")
    return parser.parse_args()


def load_store(store_path: Path) -> dict[str, Any]:
    try:
        data = json.loads(store_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"store not found: {store_path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"store is not valid JSON: {store_path}: {exc}")
    if not isinstance(data, dict):
        raise SystemExit(f"store root is not an object: {store_path}")
    return data


def resolve_transcript_path(sessions_dir: Path, entry: dict[str, Any]) -> Path | None:
    session_file = entry.get("sessionFile")
    if isinstance(session_file, str) and session_file.strip():
        candidate = Path(session_file)
    else:
        session_id = entry.get("sessionId")
        if not isinstance(session_id, str) or not session_id.strip():
            return None
        candidate = Path(f"{session_id}.jsonl")
    resolved = candidate if candidate.is_absolute() else sessions_dir / candidate
    resolved = resolved.resolve()
    try:
        resolved.relative_to(sessions_dir.resolve())
    except ValueError:
        raise SystemExit(f"refusing transcript outside sessions dir: {resolved}")
    return resolved


def sidecar_candidates(transcript_path: Path) -> list[Path]:
    if transcript_path.suffix != ".jsonl":
        return []
    stem = transcript_path.name[:-len(".jsonl")]
    patterns = [
        f"{stem}.trajectory.jsonl",
        f"{stem}.checkpoint.*.jsonl",
    ]
    found: list[Path] = []
    for pattern in patterns:
        found.extend(sorted(transcript_path.parent.glob(pattern)))
    return found


def archive_path(archive_dir: Path, source: Path) -> Path:
    destination = archive_dir / source.name
    if not destination.exists():
        return destination
    index = 1
    while True:
        candidate = archive_dir / f"{source.name}.{index}"
        if not candidate.exists():
            return candidate
        index += 1


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def main() -> int:
    args = parse_args()
    execute = bool(args.execute and not args.dry_run)
    if args.ttl_hours < MIN_TTL_HOURS:
        raise SystemExit(f"ttl-hours must be >= {MIN_TTL_HOURS}; got {args.ttl_hours}")

    store_path = args.store.expanduser().resolve()
    workspace = args.workspace.expanduser().resolve()
    sessions_dir = store_path.parent.resolve()
    store = load_store(store_path)
    now_ms = datetime.now(tz=timezone.utc).timestamp() * 1000
    ttl_ms = args.ttl_hours * 60 * 60 * 1000

    eligible: list[dict[str, Any]] = []
    for key, raw_entry in store.items():
        if DREAMING_KEY_FRAGMENT not in key:
            continue
        if args.active_key and key == args.active_key:
            continue
        if not isinstance(raw_entry, dict):
            continue
        updated_at = raw_entry.get("updatedAt")
        if not isinstance(updated_at, (int, float)):
            continue
        age_ms = now_ms - float(updated_at)
        if age_ms < ttl_ms:
            continue
        transcript = resolve_transcript_path(sessions_dir, raw_entry)
        files = []
        if transcript and transcript.exists():
            files.append(transcript)
            files.extend(p for p in sidecar_candidates(transcript) if p.exists())
        eligible.append({
            "key": key,
            "ageHours": round(age_ms / 3600000, 2),
            "updatedAt": datetime.fromtimestamp(float(updated_at) / 1000, tz=timezone.utc).isoformat(),
            "transcript": str(transcript) if transcript else None,
            "files": [str(p) for p in files],
        })

    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    archive_dir = workspace / ".openclaw-repair" / "dreaming-session-cleanup" / timestamp
    print(json.dumps({
        "mode": "execute" if execute else "dry-run",
        "store": str(store_path),
        "ttlHours": args.ttl_hours,
        "eligibleCount": len(eligible),
        "archiveDir": str(archive_dir),
        "eligible": eligible,
    }, indent=2, ensure_ascii=False))

    if not execute or not eligible:
        return 0

    archive_dir.mkdir(parents=True, exist_ok=True)
    backup_path = archive_dir / "sessions.json.backup"
    shutil.copy2(store_path, backup_path)

    for item in eligible:
        for file_name in item["files"]:
            source = Path(file_name)
            if not source.exists():
                continue
            source.rename(archive_path(archive_dir, source))
        store.pop(item["key"], None)

    atomic_write_json(store_path, store)
    return 0


if __name__ == "__main__":
    sys.exit(main())
