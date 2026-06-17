#!/usr/bin/env bash
set -Eeuo pipefail

export HOME=/root
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

LOCK_DIR=/root/.openclaw/locks
LOCK_FILE="${LOCK_DIR}/openclaw-codex-auto-update.lock"

mkdir -p "${LOCK_DIR}"

exec 9>"${LOCK_FILE}"
if ! flock -n 9; then
  echo "Another OpenClaw/Codex auto-update is already running; exiting."
  exit 0
fi

echo "OpenClaw/Codex auto-update started at $(date --iso-8601=seconds)"

echo "Current Codex CLI: $(codex --version 2>/dev/null || echo unavailable)"
echo "Latest Codex CLI package: $(npm view @openai/codex version)"
if [[ "${OPENCLAW_CODEX_AUTO_UPDATE_DRY_RUN:-0}" == "1" ]]; then
  echo "Dry-run mode: skipping npm install and OpenClaw restart."
  openclaw update --dry-run --yes --timeout 1800 --json
  echo "OpenClaw/Codex auto-update dry-run finished at $(date --iso-8601=seconds)"
  exit 0
fi

npm --global --no-fund --no-audit install @openai/codex@latest
echo "Updated Codex CLI: $(codex --version 2>/dev/null || echo unavailable)"

echo "Current OpenClaw: $(openclaw --version 2>/dev/null || echo unavailable)"
openclaw update --yes --timeout 1800 --json
echo "Updated OpenClaw: $(openclaw --version 2>/dev/null || echo unavailable)"

echo "OpenClaw/Codex auto-update finished at $(date --iso-8601=seconds)"
