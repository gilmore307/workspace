# Workspace Scripts

This directory owns host-maintenance scripts that are small enough to live with the OpenClaw workspace but are invoked by local services or operators.

## Files

- `openclaw-codex-auto-update.sh` updates the global Codex CLI package and then runs the OpenClaw updater through its supported CLI path.
- `openclaw-codex-auto-update.service` is the user-level systemd oneshot that runs the update script.
- `openclaw-codex-auto-update.timer` schedules the update once per day without missed-run catch-up.

Run `OPENCLAW_CODEX_AUTO_UPDATE_DRY_RUN=1 scripts/openclaw-codex-auto-update.sh` to verify the path without installing packages or restarting the gateway.
