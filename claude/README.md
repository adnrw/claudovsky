# Claudovsky for Claude

Not a developer? Start at [`always-on.md`](./always-on.md) (settings paste, on by default) or [`per-session.md`](./per-session.md) (upload once, turn on per chat) — no GitHub account, no terminal. Everything below is the developer/power-user packaging: Claude Code plugin, marketplace listing, CLAUDE.md snippet.

## What's in here

The installable plugin (`.claude-plugin/plugin.json`, `skills/claudovsky/`) lives inside **this `claude/` folder**, not the repo root. The repo-root `.claude-plugin/marketplace.json` — which itself has to stay at the true repo root, that part isn't relocatable — points into this folder via a `git-subdir` source, so `/plugin marketplace add adnrw/claudovsky` resolves the plugin from here:

```
claude/
  always-on.md                 # non-technical path: Claude Desktop / Mobile Settings paste
  per-session.md                # non-technical path: Skills panel .skill upload, off by default
  claudovsky.skill              # packaged .skill file for the Skills panel upload path
  snippets/
    always-on-claude-md.md      # copy-paste snippet for CLAUDE.md — the always-on default
                                 # for Claude Code / Cowork specifically
  .claude-plugin/
    plugin.json                 # plugin manifest
  skills/claudovsky/
    SKILL.md                    # the instruction Claude follows (session-based mode)
    reference/dictionary.md     # bundled fallback word list — canonical copy lives in
                                 # dictionary/dictionary.md at the repo root; keep synced
  README.md                    # this file
```

The repo-root marketplace file (stays at root, points in here):

```
.claude-plugin/
  marketplace.json           # what /plugin marketplace add adnrw/claudovsky reads —
                               # "source": "git-subdir", "path": "claude"
```

## Two ways this activates — default is always-on

**Always-on (default, recommended):** Copy `snippets/always-on-claude-md.md` into your own `~/.claude/CLAUDE.md` (global) or project's `CLAUDE.md` / project instructions. This is a manual one-time paste, not part of the plugin install — skills can't rewrite your CLAUDE.md for you automatically, so "always on" genuinely does require this one step, once. After that it's on for every session by default. Say "stop with the Yiddish" any time to turn it off for that session; ask again to bring it back. Switch intensity anytime by naming a level: Nebbish, Mensch, Macher (default). (Non-technical route to the same result: [`always-on.md`](./always-on.md) — paste into Claude Desktop/Mobile Settings instead of CLAUDE.md.)

**Session-based (opt-in alternative):** If you'd rather it be off by default and only turn on when asked, skip the CLAUDE.md snippet and just install the plugin. Say something like "talk Yiddish" or run `/claudovsky`, and Claude sprinkles words in for the rest of that conversation only. Nothing persists to the next session. (Non-technical route: [`per-session.md`](./per-session.md) — upload the `.skill` file via the Skills panel instead of the marketplace.)

## Installing (Claude Code)

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then either invoke `/claudovsky` at the start of a session, or set up the always-on snippet above. (`/claudovsky:claudovsky` also works — Claude Code always exposes the full namespaced form alongside the bare command, but the bare `/claudovsky` is what you'd actually type.)

*(Worth knowing: the bare `/claudovsky` form works because the skill's name matches the plugin's name and nothing else on your system claims that command name. If some other plugin or command you have installed already uses `/claudovsky`, Claude Code falls back to requiring the full `/claudovsky:claudovsky` form — outside our control, just how the namespacing works.)*

## Installing (Cowork / claude.ai)

Cowork installs plugins from the same marketplace repo format. Point Cowork's plugin/marketplace add flow at `adnrw/claudovsky`. This hasn't been tested end-to-end yet — verify once the repo is public.

## Why the plugin lives under `claude/`, not the repo root

`.claude-plugin/marketplace.json`'s `source` field supports a `git-subdir` type specifically for this: pointing a marketplace entry at a subdirectory of the same repo, so the plugin doesn't have to sit at the repo root of a multi-platform doc repo like this one. This is Anthropic's documented, standard approach for marketplace entries (see [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces.md)) — not a workaround. `marketplace.json` itself is the one file that can't move; it has to stay at the true repo root for `/plugin marketplace add owner/repo` to find it.

*(This restructure — `plugin.json` and `skills/claudovsky/` moved from repo root into `claude/`, `marketplace.json`'s `path` updated from `"."` to `"claude"` — hasn't been verified end-to-end yet with a real `/plugin marketplace add adnrw/claudovsky` against the pushed repo. Worth doing that check before treating this as confirmed working.)*

## Keeping the bundled dictionary in sync

`dictionary/dictionary.md` at the repo root is the master copy — edit it there, nowhere else. Everything else is propagated from it by hand (no automated sync yet): `skills/claudovsky/reference/dictionary.md` in this folder is a byte-for-byte copy, bundled so the plugin works offline without live web-fetch; the compact `Word list:` block in `always-on.md` (this folder, plus `chatgpt/always-on.md` and `gemini/always-on.md`) and in `gemini/per-session.md` are hand-condensed versions of the same entries. Update the root dictionary first, then propagate the change to each of those — skipping one leaves it silently stale for anyone without web-fetch access to the live file.
