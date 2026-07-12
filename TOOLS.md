# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Secret Aliases

Store local secrets outside the workspace under `/root/secrets/` and refer to them by alias instead of value.

Examples:
- `github` → source-level GitHub JSON secret file for git operations; JSON key `pat`
- `okx` → source-level OKX JSON secret file for crypto data/trading access; JSON keys `api_key`, `secret_key`, `passphrase`, `allowed_ip_address`, `api_key_remark_name`
- `alpaca` → source-level Alpaca JSON secret file for stock/ETF bars, quotes, trades, and news data access; JSON keys `api_key`, `secret_key`, `endpoint`
- `fred`, `census`, `bea`, `bls` → source-level economic-data provider JSON secret files; JSON key `api_key`
- `network-framework` → source-level network-framework JSON secret file, if revived; prefer JSON keys over split files

Registry:
- `/root/secrets/registry.json`

Rules for secret storage, lookup, and use:
- never put secret values into workspace files, git-tracked config, or `trading-main/registry/`
- one provider/source should normally use one JSON secret file: `/root/secrets/<source>.json`
- JSON secret keys should use registered/canonical snake_case names when shared, e.g. `api_key`, `secret_key`, `passphrase`, `endpoint`, `allowed_ip_address`, `api_key_remark_name`, `pat`
- when a secret needs a shared reviewed name, register a `kind = config` entry in `trading-main/registry/` whose payload is the source-level secret alias, not the secret value and not the raw file contents; the registry `path` may mirror the local JSON file path
- keep the real secret material only under `/root/secrets/...`
- prefer alias-based resolution over hard-coded paths in project code
- helpers should use registry config ids for automation; do not add key-input secret helper APIs. Secret resolution order is: registry config id → config payload source alias → `/root/secrets/registry.json` entry → source-level JSON secret file → optional JSON field
- token/password helpers should usually return one trimmed JSON field; SSH-key style helpers may return the resolved path when the consumer needs a file path instead of inline text

## Projects Root

Store formal repositories under `/root/projects/`.

## Victoria 3 Modding

- Tiger Mod Validator for Victoria 3 is installed as `vic3-tiger` at `/usr/local/bin/vic3-tiger`, symlinked to `/root/tools/tiger/v1.19.0/vic3-tiger-linux-v1.19.0/vic3-tiger`.
- Installed release: Tiger Validator `v1.19.0`; release notes say Vic3 support targets 1.13.8, so treat results against `/root/projects/vic3/game` 1.13.9 as close but not perfect.
- Full Steam Victoria 3 install root: `/root/projects/vic3/steam-install`; use this for Tiger's `--game` argument because it contains `game/`, `clausewitz/`, and `jomini/`.
- GitHub base checkout: `/root/projects/vic3/game`; useful as source reference but not sufficient for Tiger by itself.
- Current mod descriptor for launcher testing: `/root/Documents/Paradox Interactive/Victoria 3/mod/com.github.gilmore307.mod.1_13_colonial.mod`.

## Trading Python Environment

- Canonical Python for all trading-related repositories: `/root/projects/trading-manager/.venv/bin/python`.
- Use this interpreter for trading-model, trading-manager, trading-storage, trading-data, trading-dashboard helper scripts, tests, model generation/evaluation, registry checks, and scheduler/stage commands that run Python.
- Do not use system `python3` for trading project dependency-bearing commands except for OS/bootstrap checks or when explicitly diagnosing interpreter drift.
- When installing trading Python dependencies, record them in `/root/projects/trading-manager/requirements.txt` before installing into the manager venv.
- Common command pattern: `PYTHONPATH=src /root/projects/trading-manager/.venv/bin/python <module-or-script>`.

## ThetaData Terminal

- Local historical option-source acquisition uses ThetaData Terminal on `127.0.0.1:25503`.
- Managed service: `thetadata-terminal.service`.
- Working directory: `/root/tools/thetadata-terminal`.
- Service command uses `ThetaTerminalv3.jar`, `config.toml`, `creds.txt`, and logs under `/tmp/thetadata-terminal-logs`.
- Quick check: `systemctl is-active thetadata-terminal.service` and `ss -ltnp '( sport = :25503 )'`.

## OpenClaw / Codex CLI Auto Update

- Maintained script: `/root/.openclaw/workspace/scripts/openclaw-codex-auto-update.sh`.
- Systemd user units: `/root/.config/systemd/user/openclaw-codex-auto-update.service` and `/root/.config/systemd/user/openclaw-codex-auto-update.timer`, symlinked to the maintained unit files in `/root/.openclaw/workspace/scripts/`.
- Schedule: daily at 04:15 America/New_York with up to 45 minutes randomized delay.
- Behavior: updates global `@openai/codex@latest`, then runs `openclaw update --yes --timeout 1800 --json` so OpenClaw uses its supported updater, plugin sync, completion refresh, and gateway restart path.
- The timer intentionally omits catch-up persistence so enabling it during the day does not immediately restart the active gateway because a previous 04:15 run was missed.
- Quick checks: `systemctl --user list-timers openclaw-codex-auto-update.timer --no-pager`, `systemctl --user status openclaw-codex-auto-update.timer`, and `journalctl --user -u openclaw-codex-auto-update.service -n 100 --no-pager`.

## SMB

- Host share: `//100.104.174.7/OpenClaw` (Windows: `\\100.104.174.7\OpenClaw`) exposes `/root/projects` for user `openclaw` over Tailscale only.
- Samba config binds to `lo 100.104.174.7/10` with `hosts allow = 127. 100.64.0.0/10`.
- `smbd` can start before Tailscale has its address and bind only to localhost; fixed with `/etc/systemd/system/smbd.service.d/10-wait-for-tailscale.conf` waiting briefly for `tailscale0` before start.
- Quick check: `ss -ltnp '( sport = :445 or sport = :139 )'` should show `100.104.174.7:445` and `100.104.174.7:139`.
