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
- `github/pat` → GitHub HTTPS token for git operations
- `network-framework/companion-token` → network-framework phase-1 status companion bearer token

Registry:
- `/root/secrets/registry.json`

Rules for secret storage, lookup, and use:
- never put secret values into workspace files, git-tracked config, or `universal-catalog`
- when a secret needs a shared reviewed name, register a `kind = config` entry in `universal-catalog` whose payload is the secret alias, not the secret value and not the raw file contents
- keep the real secret material only under `/root/secrets/...`
- prefer alias-based resolution over hard-coded paths in project code
- helpers should resolve secrets in this order: catalog config key → secret alias → `/root/secrets/registry.json` entry → local secret file
- token/password helpers should usually return trimmed secret text; SSH-key style helpers may return the resolved path when the consumer needs a file path instead of inline text

## Projects Root

Store formal repositories under `/root/projects/`.
