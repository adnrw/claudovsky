# Claudovsky for Claude

Not a developer? Start at [`EASY-INSTALL.md`](./EASY-INSTALL.md) — copy-paste into Settings, no GitHub account, no terminal. Everything below is the developer/power-user packaging: Claude Code plugin, marketplace listing, CLAUDE.md snippet.

## What's in here

```
.claude-plugin/
  plugin.json               # plugin manifest (plugin root = this claude/ folder)
skills/yiddish/
  SKILL.md                    # the instruction Claude follows (session-based mode)
  reference/dictionary.md     # bundled fallback word list — canonical copy lives in
                               # ../dictionary/dictionary.md at the repo root; keep synced
snippets/
  always-on-claude-md.md      # copy-paste snippet for CLAUDE.md — the always-on default
                               # for Claude Code / Cowork specifically
EASY-INSTALL.md              # non-technical path: Claude Desktop / Mobile Settings paste
```

The top-level `.claude-plugin/marketplace.json` (repo root, not in this folder) is what makes `/plugin marketplace add adnrw/claudovsky` work — it points at this `claude/` subfolder as the plugin's actual content via a `git-subdir` source.

## Two ways this activates — default is always-on

**Always-on (default, recommended):** Copy `snippets/always-on-claude-md.md` into your own `~/.claude/CLAUDE.md` (global) or project's `CLAUDE.md` / project instructions. This is a manual one-time paste, not part of the plugin install — skills can't rewrite your CLAUDE.md for you automatically, so "always on" genuinely does require this one step, once. After that it's on for every session by default. Say "stop with the Yiddish" any time to turn it off for that session; ask again to bring it back. Switch intensity anytime by naming a level: Nebbish, Mensch (default), Macher.

**Session-based (opt-in alternative):** If you'd rather it be off by default and only turn on when asked, skip the CLAUDE.md snippet and just install the plugin. Say something like "talk Yiddish" or run `/claudovsky:yiddish`, and Claude sprinkles words in for the rest of that conversation only. Nothing persists to the next session.

## Installing (Claude Code)

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then either invoke `/claudovsky:yiddish` at the start of a session, or set up the always-on snippet above.

*(Unverified: whether Claude Code's plugin loader correctly resolves `.claude-plugin/plugin.json` and `skills/` when nested under a `git-subdir` path like `claude/` rather than at repo root. This nested-plugin-root structure hasn't been tested end-to-end — worth confirming before relying on it.)*

## Installing (Cowork / claude.ai)

Cowork installs plugins from the same marketplace repo format. Point Cowork's plugin/marketplace add flow at `adnrw/claudovsky`. This hasn't been tested end-to-end yet — verify once the repo is public.

## Keeping the bundled dictionary in sync

`skills/yiddish/reference/dictionary.md` in this folder is a bundled offline fallback — it ships inside the plugin itself so it works even without live web-fetch. The canonical, editable copy is `../dictionary/dictionary.md` at the repo root. There's no automated sync between the two yet; when you update the dictionary, copy it to both places, or this bundled copy will silently drift out of date for anyone without web-fetch access.
