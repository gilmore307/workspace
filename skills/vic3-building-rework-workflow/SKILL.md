---
name: "vic3-building-rework-workflow"
description: "Tighten Vic3 mod file ownership and provenance rules"
---

# Vic3 Modding Workflow

Use this workflow when changing Victoria 3 mod content, rebasing old mod content onto the latest game version, making same-path overrides, changing GUI, buildings, production method groups, production methods, employment, construction pacing, or merging/removing a vanilla route.

## Canonical Home

- Vic3 modding workflow rules belong in this skill or in the Vic3 project docs, not in bottom-level workspace memory files such as `TOOLS.md`, `SOUL.md`, `AGENTS.md`, or `MEMORY.md`.
- Host-specific paths and tools may stay in `TOOLS.md`; modding decisions, migration policy, file ownership rules, and code annotation rules stay here or in the Vic3 repository docs.

## Principles

- Latest game version first: base the mod on the latest available/current installed Victoria 3 vanilla game version, not on the historical version where the mod feature was first written.
- Before each migration batch, confirm the active vanilla base and target module version. If the repository target is behind the latest installed game, treat version rebasing as part of the task boundary before porting old mod intent.
- Old mods are reference material only. Reuse old intent, names, icons, exact localization, or UI behavior only when they are still wanted; do not copy old explanatory text, stale comments, obsolete structures, or old-version response content into the current mod.
- Treat vanilla-version drift as normal. If a diff exists only because the game updated since the old mod version, follow the latest vanilla game instead of preserving the old mod file.
- Preserve intended mod behavior. If a diff represents the mod's chosen mechanic, UI behavior, balance, migration, or retired route, carry that intent forward onto the latest vanilla structure.
- Do not make or preserve unrelated gameplay edits just to clear Tiger, parser, or verifier noise. If a vanilla field produces tool noise but there is no accepted mod intent to change it, keep vanilla behavior and document the warning as inherited/tool-limited instead of changing gameplay.
- Every active mod diff must have a remembered reason and a gameplay/UI/runtime effect. If the reason cannot be stated as a current accepted feature, compatibility cover, retired-route closure, or loader necessity, remove the diff or quarantine it for review.
- Annotate intentional mod diffs in code. Each deliberate gameplay, GUI, history, event, script, or localization change should have a nearby comment explaining why the mod diverges from vanilla and what the player/system effect is, so future game updates can separate vanilla drift from intended mod behavior.
- Keep comments useful and local. Comments should identify the mod feature, retired route, migration reason, compatibility reason, balance target, player-facing effect, or validation limitation; avoid restating syntax.
- Close retired routes in the same batch. Do not leave the old building, key, table, route, override, or reference active for later cleanup.

## Module File Ownership And Naming

Use feature/module names as ownership boundaries. A numbered module prefix such as `zz_01_light_arms_factory` or `zz_10_conscription` identifies the mod feature, not discovery order.

- Keep related files for the same feature under the same module prefix across Victoria 3 data directories.
- Preserve the feature stem and adapt only the directory-specific suffix. For example, if the static modifier file is `common/static_modifiers/zz_01_light_arms_factory_static_modifiers.txt`, companion files should be named like `common/production_methods/zz_01_light_arms_factory.txt`, `common/scripted_buttons/zz_01_light_arms_factory_scripted_buttons.txt`, `common/scripted_triggers/zz_01_light_arms_factory_scripted_triggers.txt`, and localization `zz_01_light_arms_factory_l_<language>.yml`.
- Do not place unrelated mechanics inside an existing module file because the file is convenient or already loaded late. Create or reuse the correct feature module instead.
- When a cross-cutting vanilla object must be patched for a feature, put the narrow `REPLACE:` or `INJECT:` block in that feature's module file and explain the dependency. Example: munitions event modifiers that point at the retired standalone `building_munition_plant` belong with the light-arms factory module because that module owns the building-route retirement.
- If a same-path full-file override is required, its header and nearby `# MOD:` comments must still name the owning feature/module for each changed hunk.
- When a file is split, update docs and verifier checks to prevent the retired broad file or wrong module filename from returning.

## Comment And Header Standard

Headers and inline comments are there to preserve current intent, not to produce boilerplate.

- `Purpose` must name the business feature or gameplay surface, such as "light-arms factory ammunition-route compatibility", "unincorporated-state throughput penalties", "colonial administration gates", or "conscription structure pressure". Do not write generic text like "Defines mod data for content modifiers".
- `Mod Changes` must summarize the actual behavior change: what vanilla behavior is replaced, removed, redirected, or added, and what effect it has in game.
- `Dependencies` must list meaningful mod or vanilla keys that explain why the file exists.
- `Compatibility Risk` must describe the concrete update risk: vanilla object replacement, same-path override drift, retired-key references, GUI layout fragility, parser limitations, or low-risk additive localization.
- Near each intentional diff, use a short `# MOD:` comment that explains why the change exists and what it does. When replacing vanilla, keep a nearby `# VANILLA REPLACED` or `# VANILLA REMOVED` comment unless the file format cannot safely hold comments.
- Do not keep giant generated headers whose fields do not answer why the file exists. Short, accurate comments are better than complete but empty templates.

## Same-Path Override Rule

Use this rule when Victoria 3 loader behavior requires overriding a file by the same path/name instead of using narrow database entry-mode files.

- Start from the latest vanilla file, not the old mod file.
- Make the smallest current-version edit that preserves the intended mod behavior.
- Do not silently delete vanilla content from a same-path override. When removing or replacing an original block, keep the original block in place as `#`-commented lines and add a nearby mod note explaining why it is disabled or replaced.
- Place the replacement block close to the commented original when practical, with a short marker such as `# MOD: ...`.
- If a whole original section is intentionally retired, comment the section header and body instead of removing it, unless the file format cannot tolerate comments there. If comments are unsafe for that format, document the exception in the repository docs and verifier notes.
- For large same-path overrides, prefer retaining commented originals only around changed blocks rather than duplicating the entire file as comments.
- After a game update, review these `# MOD:` markers first: keep vanilla changes that are only upstream drift, and reapply only the marked mod intent.

## Diff Provenance Review

Before editing or accepting a migration:

1. Compare latest vanilla, current mod, and old mod when old content is involved.
2. Classify each difference as one of:
   - `vanilla drift`: caused by upstream game changes; follow latest vanilla.
   - `mod intent`: intended behavior/UI/balance; port onto latest vanilla.
   - `loader necessity`: same-path or full-file override required by engine behavior.
   - `compatibility cover`: narrow replacement needed because another accepted mod route retired or renamed a vanilla key.
   - `cleanup`: retired content that should be removed or disabled.
   - `tool limitation`: Tiger/verifier/parser mismatch that should be documented without changing gameplay unless the user accepts the gameplay change.
3. Ensure each `mod intent`, `loader necessity`, `compatibility cover`, and `cleanup` change is represented by a nearby code comment or a narrow project-doc/verifier note.
4. Do not treat old-version numeric differences caused by upstream game updates as missing mod content by default.
5. Before accepting any changed vanilla value, answer: who requested this, what feature owns it, what player/system behavior changes, and why a narrower file cannot own it.

## Standard Workflow

1. Baseline the latest game.
   - Read latest vanilla building, PM group, PM, technology, localization, company, event, GUI, history, and scripted-reference files relevant to the change.
   - For building balance work, export or consult the building production-method statistics from the latest vanilla base.
   - Use weekly output value, input value, wage bill, static profit, and operating margin as the primary balance fields.
   - Treat construction points as capacity/pacing, not operating profitability.

2. Design before editing gameplay files.
   - State the owning feature module and intended file stem before splitting or adding files.
   - State the new route, UI behavior, building shape, production-line independence, PM group layout, unlock technologies, employment route, outputs, inputs, and construction-point pacing as applicable.
   - Compare against the correct baseline: either the same latest vanilla surface or the combined old separate routes being merged.
   - Include wages in cost calculations.
   - Prefer integer quantities and multiples of 5; small values under 10 may use smaller integers.
   - Balance profitability by adjusting inputs, outputs, and employment, not by using one-time construction cost.
   - Get the design accepted before implementation when the change affects gameplay balance, UI workflow, or route ownership.

3. Implement as one coherent route-closing batch.
   - Use the latest game keys and schemas.
   - Use explicit Database Entry Modes where Victoria 3/Tiger expects them: `REPLACE:`, `INJECT:`, `REPLACE_OR_CREATE:`, etc.
   - Add custom plain keys only after checking they do not collide with latest vanilla.
   - Prefer feature-scoped `zz_*` files with entry-mode blocks for database objects.
   - Keep module stems consistent across directories and localization.
   - Use same-path full-file overrides only where the loader requires it, such as GUI files, event replacement, history files, or city-data files that cannot be narrowed safely.
   - If a vanilla route is retired, make it impossible to build or otherwise remove the active route, and migrate every latest vanilla reference in the same batch.
   - Search for both canonical and alias/plural forms of retired keys.

4. Keep overrides narrow by loader behavior.
   - For database objects, prefer narrow entry-mode files over full-file copies.
   - For same-path overrides, keep latest vanilla structure and comment out original changed blocks with `#` rather than silently deleting them.
   - After mechanical replacement, remove duplicate list items and duplicate merged modifiers.
   - For city-data, remove retired building mesh rows rather than creating duplicate keys for the surviving building, while preserving nearby commented original rows when the file is same-path overridden and comments are safe.

5. Localize deliberately.
   - Reuse old mod localization only when the exact old key exists and the wording remains intended.
   - Otherwise use latest vanilla localization or add a current direct translation.
   - Keep localization files under the same feature stem as the owning mechanics.
   - If localization is removed because a route is retired, leave a narrow comment or verifier cover explaining the retired route rather than preserving stale display text.

6. Verify before acceptance.
   - Run residual-reference scans for every retired key and alias. Remaining hits must be intentional and documented, such as a non-buildable compatibility placeholder, a retained legacy PM-group name, or a commented original block in a same-path override.
   - Scan changed files for useful `# MOD:` markers or equivalent local comments on intentional diffs; reject generic generated headers that do not identify the feature and gameplay effect.
   - Scan feature files for module-stem drift: related files should share the same `zz_<module>` stem across `common/*`, `events/`, `gui/`, and localization unless a same-path override is required.
   - Run the Vic3 repository verifier against the active target module, for example `python3 scripts/verify_vic3_module.py mod/<target_module>`.
   - Run Tiger against the active target module and latest installed game root, for example `vic3-tiger --game /root/projects/vic3/steam-install /root/projects/vic3/mod/<target_module> --no-color -c`.
   - Run `git diff --check` for touched repositories.
   - Report Tiger's final fatal/error/warning/untidy/tip counts and separate new issues from inherited vanilla/Tiger-version warnings.

7. Commit and push.
   - Commit project documentation and playable mod changes in their own repositories.
   - Push the playable mod repository when it has a remote.
   - Ignore unrelated OpenClaw workspace files and unrelated user changes.
