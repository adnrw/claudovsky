# Claudovsky for Claude

Not a developer? Start at [`always-on.md`](./always-on.md) (settings paste, on by default) or [`per-session.md`](./per-session.md) (upload once, turn on per chat) — no GitHub account, no terminal. Everything below is the developer/power-user packaging: Claude Code plugin, marketplace listing, CLAUDE.md snippet.

## What's in here

The actual installable plugin (`.claude-plugin/plugin.json`, `skills/claudovsky/`) lives at the **repo root**, not in this folder — that's the standard, documented Claude Code plugin structure, and it's what makes `/plugin marketplace add adnrw/claudovsky` reliable. This `claude/` folder holds the non-plugin, Claude-specific docs instead:

```
always-on.md                 # non-technical path: Claude Desktop / Mobile Settings paste
per-session.md                # non-technical path: Skills panel .skill upload, off by default
snippets/
  always-on-claude-md.md      # copy-paste snippet for CLAUDE.md — the always-on default
                               # for Claude Code / Cowork specifically
README.md                    # this file
```

The plugin itself, at repo root:

```
.claude-plugin/
  marketplace.json           # what /plugin marketplace add adnrw/claudovsky reads
  plugin.json                 # plugin manifest
skills/claudovsky/
  SKILL.md                    # the instruction Claude follows (session-based mode)
  reference/dictionary.md     # bundled fallback word list — canonical copy lives in
                               # dictionary/dictionary.md at the repo root; keep synced
```

## Two ways this activates — default is always-on

**Always-on (default, recommended):** Copy `snippets/always-on-claude-md.md` into your own `~/.claude/CLAUDE.md` (global) or project's `CLAUDE.md` / project instructions. This is a manual one-time paste, not part of the plugin install — skills can't rewrite your CLAUDE.md for you automatically, so "always on" genuinely does require this one step, once. After that it's on for every session by default. Say "stop with the Yiddish" any time to turn it off for that session; ask again to bring it back. Switch intensity anytime by naming a level: Nebbish, Mensch (default), Macher. (Non-technical route to the same result: [`always-on.md`](./always-on.md) — paste into Claude Desktop/Mobile Settings instead of CLAUDE.md.)

**Session-based (opt-in alternative):** If you'd rather it be off by default and only turn on when asked, skip the CLAUDE.md snippet and just install the plugin. Say something like "talk Yiddish" or run `/claudovsky`, and Claude sprinkles words in for the rest of that conversation only. Nothing persists to the next session. (Non-technical route: [`per-session.md`](./per-session.md) — upload the `.skill` file via the Skills panel instead of the marketplace.)

## Installing (Claude Code)

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then either invoke `/claudovsky` at the start of a session, or set up the always-on snippet above. (`/claudovsky:claudovsky` also works — Claude Code always exposes the full namespaced form alongside the bare command, but the bare `/claudovsky` is what you'd actually type.)

*(Worth knowing: the bare `/claudovsky` form works because the skill's name matches the plugin's name and nothing else on your system claims that command name. If some other plugin or command you have installed already uses `/claudovsky`, Claude Code falls back to requiring the full `/claudovsky:claudovsky` form — outside our control, just how the namespacing works.)*

This is now the standard plugin layout (manifest and skills at repo root, matching Claude Code's own examples) rather than the nested-subfolder structure this repo briefly used — that nested version relied on an unverified `git-subdir` marketplace trick and was never actually tested working. This version isn't clever, but it's the documented pattern, which matters more.

## Installing (Cowork / claude.ai)

Cowork installs plugins from the same marketplace repo format. Point Cowork's plugin/marketplace add flow at `adnrw/claudovsky`. This hasn't been tested end-to-end yet — verify once the repo is public.

## Keeping the bundled dictionary in sync

`skills/claudovsky/reference/dictionary.md` (repo root) is a bundled offline fallback — it ships inside the plugin itself so it works even without live web-fetch. The canonical, editable copy is `dictionary/dictionary.md`, also at the repo root. There's no automated sync between the two yet; when you update the dictionary, copy it to both places, or this bundled copy will silently drift out of date for anyone without web-fetch access.
