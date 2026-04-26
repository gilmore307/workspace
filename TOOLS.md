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
