# Claudovsky

Sprinkles real Yiddish words into an AI assistant's responses. Default behavior is always-on; a session-based opt-in mode is also available for people who don't want it running by default.

**Not a developer? Start at [`EASY-INSTALL.md`](./EASY-INSTALL.md).** It's copy-paste into a settings box, no GitHub account, no terminal, works on phone/web/desktop. That's the actual product for most people who'll use this.

Everything below — the Claude plugin, marketplace files, and Custom GPT setup — is the developer/power-user packaging: for people who use Claude Code, want a one-click shareable install for a group, or want to publish this on a marketplace/GPT Store. Packaged for Claude (Code/Cowork, as a plugin) and for ChatGPT (as a Custom GPT — see `chatgpt/`, since ChatGPT has no plugin-install mechanism).

No tools, no external API calls — this only changes word choice and tone, so it works entirely offline once installed.

## What's in here

```
.claude-plugin/
  plugin.json         # plugin manifest
  marketplace.json     # lets people install straight from this repo
skills/yiddish/
  SKILL.md              # the instruction Claude follows (session-based mode)
  reference/dictionary.md  # the approved word list, meanings, usage notes
snippets/
  always-on-claude-md.md   # copy-paste snippet — the default always-on mode
chatgpt/
  custom-instructions-snippet.md  # ChatGPT equivalent of always-on default
  gpt-builder-instructions.md     # ChatGPT equivalent of session-based mode
  README.md                       # why ChatGPT packaging looks different
```

## Two ways this activates — default is always-on

**Always-on (default, recommended):** Copy `snippets/always-on-claude-md.md` into your own `~/.claude/CLAUDE.md` (global) or project's `CLAUDE.md` / project instructions. This is a manual one-time paste, not part of the plugin install — skills can't rewrite your CLAUDE.md for you automatically, so "always on" genuinely does require this one step, once. After that it's on for every session by default. Say "stop with the Yiddish" any time to turn it off for that session; ask again to bring it back.

**Session-based (opt-in alternative):** If you'd rather it be off by default and only turn on when asked, skip the CLAUDE.md snippet and just install the plugin. Say something like "talk Yiddish" or run `/claudovsky:yiddish`, and Claude sprinkles words in for the rest of that conversation only. Nothing persists to the next session.

## Installing (Claude Code)

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then either invoke `/claudovsky:yiddish` at the start of a session, or set up the always-on snippet above.

## Installing (Cowork / claude.ai)

Cowork installs plugins from the same marketplace repo format. Point Cowork's plugin/marketplace add flow at `adnrw/claudovsky`. This hasn't been tested end-to-end yet — verify once the repo is public.

## Updating the dictionary

Edit `skills/yiddish/reference/dictionary.md` and push. That's the single source of truth, published at:

```
https://raw.githubusercontent.com/adnrw/claudovsky/main/skills/yiddish/reference/dictionary.md
```

**No install today gives fully silent, zero-action updates.** Claude Code plugin marketplaces don't auto-refresh (multiple open feature requests for this: [#51350](https://github.com/anthropics/claude-code/issues/51350), [#38271](https://github.com/anthropics/claude-code/issues/38271), [#31462](https://github.com/anthropics/claude-code/issues/31462)) — plugin users need `/plugin marketplace update` manually. And a pasted Custom Instructions/Custom GPT block is static text; it never re-fetches on its own.

The workaround, wired into every packaging above: each instruction set tells the assistant to fetch the raw URL above once per conversation if it has a web-fetch/browsing tool available, and fall back to its bundled/pasted word list if not. This is best-effort, not guaranteed — depends on that tool being enabled on the user's account, adds a small amount of latency, and a model could in principle skip it. It's the closest thing to "update the file and everyone just gets it," but it is not a hard guarantee the way a real package manager would be.

## License

CC BY-NC-SA 4.0 — see [`LICENSE`](./LICENSE). Worth noting: CC licenses are built for creative/content works, not code, but this repo is almost entirely instructions and word lists rather than software, so it fits fine. If you ever add actual code (scripts, an MCP server, etc.), that would sit oddly under a CC license — flag it if that happens and we can split licenses per-directory.

## Status / TODO

- [ ] Push this repo to GitHub (`adnrw/claudovsky`) — not yet pushed as of writing this
- [ ] Confirm exact install command syntax against current Claude Code docs (verified against docs.claude.com as of Aug 2026, but plugin CLI syntax is young and may shift)
- [ ] Test Cowork install path directly — README currently assumes parity with Claude Code, unverified
- [ ] Verify the live-fetch-on-conversation-start instruction actually fires reliably in practice, across Claude and ChatGPT — untested, best-effort only
- [ ] Decide whether to add a LICENSE (MIT is referenced in plugin.json but no LICENSE file exists yet)
