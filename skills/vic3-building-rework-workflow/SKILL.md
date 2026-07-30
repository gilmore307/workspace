---
name: "vic3-building-rework-workflow"
description: "Require active Vic3 map companion entries inside frames"
---

# Vic3 Building Rework Workflow

Use for Victoria 3 modding that changes building routes, production methods, production method groups, static modifiers, events, decisions, journal entries, on_actions, scripted effects/triggers, localization, docs, verifier rules, or launcher metadata.

## First Checks

1. Treat `/root/projects/vic3/steam-install/game` as the authoritative current base-game reference.
2. Work on `/root/projects/vic3/mod/1_13` for the main mod unless Chentong names another mod root.
3. Run repository-relative verification commands from `/root/projects/vic3` unless an absolute path is shown.
4. Do not touch `.metadata/` or `metadata.json` unless launcher metadata or `replace_paths` is directly required by the accepted change.
5. Playable mod `.txt` script files must be UTF-8 with BOM. Runtime `lexer.cpp` BOM warnings are mod warnings and must be fixed, not treated as noise.
6. Inspect the current vanilla owner file before editing any vanilla-derived mod file.
7. Classify each touched file before editing: additive module file, narrow database replacement, same-path vanilla-derived override, `replace_path` deletion cover, localization/UI/resource, or docs/verifier.
8. For every vanilla-derived top-level object that will be replaced, retired, or partially copied, diff the mod-intended object against the current vanilla owner object before writing the final annotation.

## Module Ownership

- A `zz_<module>` stem is a feature boundary across folders.
- Do not hide unrelated mechanics in an existing module because it already loads late.
- Building-system names follow four layers:
  - `common/building_groups/` and `common/buildings/`: use same-path vanilla filenames when order or whole building definition shape requires it.
  - `common/production_method_groups/` and `common/production_methods/`: single-building changes use the real building stem, such as `zz_07_university`.
  - Automation PM files use the owning buildings-domain stem plus `_automation`, such as `zz_01_industry_automation`.
  - Outside those four folders, use module theme plus folder/domain, such as `zz_new_goods_modifier_type_definitions`.
- Special accepted stems: `zz_name_pool` for combined culture name pools, `zz_new_goods` for added goods support, and `zz_pop_need` for consolidated pop-need classification.
- `common/pop_needs/zz_pop_need.txt` is the consolidated carrier for cross-module pop-need classification. Do not create parallel module-specific pop-need carrier files such as `zz_01_*_pop_needs` unless Chentong explicitly accepts a narrower exception.

## Override Policy

- Prefer additive or narrow `zz_<module>` files with database entry modes (`REPLACE:`, `REPLACE_OR_CREATE:`, `INJECT:`) when the loader supports them and the current vanilla owner does not need to disappear before validation.
- Use same-path/full-file override when one of these is true:
  - deletion/suppression of a vanilla key, branch, hook, event, JE, decision, scripted effect, custom loc, visual hook, modifier type, generated modifier type, or mechanism cannot be done narrowly;
  - a retired source key is deleted and current vanilla owner files still parse or validate references to it before late database replacements apply;
  - many keys in one vanilla file are intentionally modified;
  - top-level block order is intentionally changed;
  - the loader requires file-level replacement or a `replace_path` for additive-merge folders;
  - history/setup files require a complete current-vanilla copy.
- If a same-path override exists only from convenience, retire it into narrow module files.
- If `company_types` or similar files only retarget `building_munition_plant` references, use narrow module `REPLACE:` blocks rather than same-path covers. If the same current vanilla owner file must be same-path covered for another accepted reason, that cover owns all related modified hunks in that file and the overlapping `zz_` replacements must be removed.
- If a vanilla-derived static modifier block only retargets one modifier effect and the folder already supports database entry modes, use a narrow module `REPLACE:` block instead of a same-path static-modifier cover. If the source generated modifier type is deleted and the current vanilla static-modifier owner validates the old key before late replacements apply, use a same-path cover for that owner and remove the duplicate narrow replacement.
- If a file is fully derived from a vanilla file, mark only the actual modified/deleted places inline. Do not frame the entire copied vanilla block as though every line is mod-owned.
- For global hooks such as `on_actions`, replacing a broad top-level hook requires listing the exact vanilla hook branch being removed. Preserve unrelated vanilla branches unchanged. An emptied hook is a blocker unless every removed branch is individually justified and commented with original vanilla text.
- Do not pull unrelated hook behavior into a module just because it is in the same vanilla top-level block.

## Inline Provenance

- Every active gameplay/UI/runtime diff needs a `########################################` frame immediately adjacent to the exact changed key, value, or smallest changed sub-block.
- Every hash-framed `# MOD: EXPLANATION:` hunk must also include `# MOD: n/total`, where `n` is that frame's 1-based order among all MOD explanation frames in the same file and `total` is the file's total count of such frames. Numbering is per file, counts only hash-delimited frames with `# MOD: EXPLANATION:`, and must be sequential with no gaps or duplicates.
- The frame must include `# MOD: EXPLANATION:` and the concrete player/system effect.
- The frame must include the correct source label for that specific hunk: `# VANILLA ADDED:`, `# VANILLA DERIVED:`, `# VANILLA REPLACED:`, or `# VANILLA REMOVED:`. Do not choose a label generically at object scope when inner hunks have different source relationships.
- `VANILLA ADDED` is valid only when no current vanilla entry, same-path hunk, or renamed source key exists for that behavior.
- If a vanilla line/key is retargeted, renamed, disabled, or value-changed, use `VANILLA REPLACED` or `VANILLA REMOVED`, not `VANILLA ADDED`.
- Retargeting a vanilla source key to a different active target key is `VANILLA REPLACED` when the original vanilla source key existed. Example: changing `building_munition_plant_*` to `building_arms_industry_*` inside an existing vanilla company modifier is `VANILLA REPLACED`, even though the active replacement line has a different key.
- `VANILLA DERIVED` is valid only for copied vanilla context or an unchanged vanilla sub-block that remains active because the surrounding object is replaced. It is never sufficient for changed, retargeted, disabled, or removed hunks.
- `VANILLA REPLACED` must include the complete original vanilla line or smallest complete vanilla sub-block as commented text inside the frame before the active replacement.
- `VANILLA REMOVED` must include the complete deleted vanilla line or smallest complete deleted vanilla sub-block as commented text inside the frame.
- Database-mode top-level blocks that are truly new may be framed as a compact block, but vanilla-derived copied entries must frame changed lines or changed sub-blocks, not the whole copied block.
- For `REPLACE:` blocks derived from vanilla, compare against the vanilla owner block and annotate every changed or removed hunk. A generic object-header `VANILLA DERIVED` frame is not sufficient when only inner values changed.
- For PM, PMG, law, mobilization, static modifier, company, event, JE, decision, scripted effect/trigger, message, and on_action replacements, object-header-only provenance is forbidden unless the whole object is genuinely new.
- For deleted vanilla content, do not silently delete text. Keep the deleted vanilla lines commented out with `#` inside the frame and include `# VANILLA REMOVED:` or `# VANILLA REPLACED:`.
- Avoid vague generated wording such as `belongs to`, `keeps accepted route`, `full mod-owned entry`, or `this frame contains the actual modified definition`; name the concrete key, field, route, and in-game effect.
- For top-level block reordering, directly move the active block and record the reason only in the header `Block Order`; do not leave commented duplicates at the old location.
- A moved active block is not deleted vanilla content. Even when the old vanilla position disappears from the mod file, do not create a `VANILLA REMOVED` frame or commented copy for that old position.
- `Purpose` and `Mod Changes` must name the actual module and concrete behavior, not the vanilla file category.

## Numeric And Demand Changes

- For buy packages, PM balance, law modifiers, upkeep, or other numeric changes, record the accepted value source: same-tier vanilla key, prior accepted mod design, or a newly accepted balance rule.
- Do not derive a low-tier or early-game demand value from a vanilla key that does not exist at that tier. Example: if vanilla `popneed_services` starts at `wealth_10`, do not create `popneed_medication` or `popneed_education` for `wealth_1` through `wealth_9` by pretending services exists there.
- When copying a vanilla need, throughput, or upkeep curve, verify that every tier/key has a current vanilla source before claiming it follows vanilla.

## Vanilla Mechanism Retirement

- For fully redesigned monument mechanics, remove obsolete vanilla mechanisms, events, decisions, journal entries, scripted effects, scripted triggers, custom loc, and visual hooks through the owning same-path cover or documented `replace_path`.
- Retired original text stays commented in the cover for rebase review, even when the active file is otherwise empty.
- If a same-path cover or database-mode `REPLACE:` disables or retires a vanilla top-level object, preserve the complete original vanilla object as commented text unless the only change is top-level block ordering.
- Do not replace a retired vanilla top-level object with only an active disabled shell. If a parser/loader key must remain active, label it as an inert parser/loader shell with no gameplay intent, then preserve the complete original vanilla object as commented text in the same cover or replacement block.
- For messages, localization, and UI/script shells, active objects must state whether they are inert placeholders, live replacements, or live modified behavior. No active shell may remain with unclear runtime status.
- Do not preserve base-game mechanisms merely to silence Tiger/parser noise. If it is not owned by an accepted mod feature, keep vanilla behavior or move base-game-only fixes to the version hotfix mod.
- Before deleting a retired key, variable route, custom loc selector, scripted effect, achievement condition, modifier type, or generated modifier type, check whether current vanilla files still parse or validate that reference before late database replacements are applied. If they do, either remove the referencing vanilla owner through a justified same-path/`replace_path` cover, or keep an inert loader-compatibility definition only when that shell is explicitly accepted and warning-free. Runtime log errors, Tiger errors, and Tiger warnings override assumptions that a late `REPLACE:` block is sufficient.
- For retired generated modifier types, do not default to keeping compatibility shells. If the source generated modifier type can be deleted and every current vanilla reference owner can be same-path covered, delete the source through its original owner path and retarget each referencing owner there. Use a narrow `script_only = yes` compatibility block only when the compatibility surface is explicitly accepted, has no gameplay effect, preserves the vanilla block as comments, and produces no Tiger/runtime warning.

## Map Rework Annotation

Use this section for state-region/province map redesigns, especially isolated map-test mods where state regions, history states, pops, buildings, capitals, region lists, and localization must move together.

- Start first-time map redesigns in a clean test mod before migrating them into the main module, unless Chentong explicitly chooses direct integration.
- Treat a named map adjustment as a project, for example `MAP-MELANESIA`, `MAP-MICRONESIA`, or `MAP-POLYNESIA`. Use the same project id across map_data, history, country definitions, region lists, and localization for that adjustment.
- In every same-path map/history/region/country file touched by a map redesign, add a short header listing all active map projects owned by that file and the old state regions they merge, split, or retarget.
- At each changed hunk, use a hash-delimited map frame that encloses the active changed line, value, or smallest changed block. The frame must include:
  - `# MAP CHANGE: n/total`, counted sequentially among map frames in that file;
  - `# MAP PROJECT: <project-id>`, matching one project listed in the file header.
- For `map_data/state_regions` state-region blocks, put the active merged `STATE_* = { ... }` block inside the map frame. Do not duplicate province `#Delete` / `#Add` evidence there; the actual owner/province migration evidence belongs in history state ownership.
- For history state `create_state` ownership changes, place the map frame around each changed `owned_provinces` line, not only above the merged state block. The frame must include `#Delete` with province color ids removed from each source state for that owner, `#Add` with the target state, owner country, and final active province ids, and the active `owned_provinces` line before the closing hash delimiter.
- For history pops/buildings companion files, put the active merged `s:STATE_* = { ... }` block inside the map frame. Keep `#Delete` / `#Add` lines listing the old and new state keys.
- For other non-province companion files such as capitals, character home regions, strategic regions, geographic regions, and localization, keep the same `MAP CHANGE` / `MAP PROJECT` / `#Delete` / `#Add` frame shape and put the active changed field, state entry, or smallest changed block inside the frame. If one active list line carries multiple map projects, split the list so each project-owned active state entry is enclosed by its own frame.
- In same-path map/history covers, merged-away source state blocks must remain in the file as commented source evidence near the replacement. Do not silently delete the old `STATE_*` or `s:STATE_*` blocks merely because the active text now uses the merged state.
- Do not collapse non-contiguous vanilla blocks into one replacement range merely because they belong to the same map project. Replace each contiguous owner range separately, and review the generated file for accidental deletion of intervening vanilla content before validation.
- Prefer narrow database replacements for companion files when supported and when they avoid pulling unrelated vanilla validation problems into the test mod. Same-path covers remain appropriate for state-region files and history/setup files that must remove old state keys before validation.
- Before acceptance, strip comments and scan active text for retired old state keys. Old keys may remain only in commented `Delete` evidence or in intentionally harmless localization inherited from vanilla.

## Vanilla Diff Audit

Before accepting any batch that touches `REPLACE:`, same-path covers, or retirement covers:

1. Enumerate every vanilla-derived top-level key touched by the batch.
2. Locate each current vanilla owner file and owner block.
3. Compare vanilla block to active mod block.
4. Confirm each added, replaced, removed, or moved hunk has an immediately adjacent accurate provenance frame.
5. Confirm every hash-framed `# MOD: EXPLANATION:` hunk has a correct per-file `# MOD: n/total` line and that the sequence matches the total number of MOD explanation frames in that file.
6. Confirm every `VANILLA REPLACED` and `VANILLA REMOVED` frame preserves the complete original vanilla line or smallest complete sub-block as comments.
7. Confirm no frame surrounds an unchanged line merely because it is near a real diff.
8. Confirm no active same-path override keeps unrelated vanilla changes or suppresses unrelated hooks.
9. Confirm every active disabled shell is explicitly classified as an inert parser/loader shell, live replacement, or live modified behavior.
10. Confirm every retired vanilla top-level object retains the complete original object as commented text.
11. Confirm runtime/log evidence for loader-validated retirements: no current vanilla owner should still emit errors or warnings for a key, variable, custom loc, scripted effect, achievement condition, modifier type, or generated modifier type that the mod claims to retire.
12. Report any unannotated diff as a blocker, even if Tiger and the verifier pass.

## Workflow

1. Inspect vanilla source, current mod file, docs, and verifier before editing.
2. Decide whether the change is narrow-module, same-path, or `replace_path`; prefer narrow-module unless a same-path condition is met.
3. Apply edits at the actual hunk, not at whole-file or whole-block scope unless the whole object is genuinely new.
4. Preserve deleted and replaced vanilla content as commented evidence.
5. Update docs and verifier in the same batch for new naming or override conventions.
6. Run the vanilla diff audit for any `REPLACE:`, same-path cover, or retirement cover touched by the batch.
7. Run the verification gates below.
8. Use the Codex Vic3 mod review skill as a read-only second pass before acceptance for broad batches, same-path covers, or annotation sweeps.

## Verification

Run from `/root/projects/vic3` after edits:

1. `python3 scripts/verify_vic3_module.py mod/1_13`
2. `python3 -m py_compile scripts/verify_vic3_module.py` when verifier changes, then remove any generated `__pycache__` before committing.
3. `git diff --check` and `git -C mod diff --check`.
4. `vic3-tiger --game /root/projects/vic3/steam-install /root/projects/vic3/mod/1_13 --no-color -c` for gameplay data changes; runtime encoding warnings, unknown modifier errors, and modifier-type script/code warnings are blockers.
5. Read-only Codex CLI review with GPT-5.5 when a batch touches multiple files, same-path covers, or modding rules.

Report changed/deleted files, why each override route is necessary, vanilla diff audit results, validation results, commits, and any remaining warnings.
