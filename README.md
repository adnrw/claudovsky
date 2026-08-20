# Claudovsky

Sprinkles real Yiddish words into an AI assistant's responses. Default behavior is always-on, with three switchable intensity levels (Nebbish / Mensch / Macher) and a spoken toggle to turn it off and back on. A session-based opt-in mode is also available for people who don't want it running by default.

Organized by assistant — each is packaged and documented independently, since Claude and ChatGPT have genuinely different customization mechanisms (no shared "plugin" concept between them):

```
claude/       # Claude Code plugin, marketplace listing, CLAUDE.md snippet,
              # and the non-technical Claude Desktop/Mobile install path
chatgpt/      # Custom Instructions (always-on) and Custom GPT (session-based)
dictionary/   # dictionary.md — the single canonical, editable word list,
              # fetched live by both packagings when possible (see below)
LICENSE       # CC BY-NC-SA 4.0
```

**Not a developer?** Go straight to [`claude/EASY-INSTALL.md`](./claude/EASY-INSTALL.md) or [`chatgpt/custom-instructions-snippet.md`](./chatgpt/custom-instructions-snippet.md) depending which you use. Copy-paste into a settings box, no GitHub account, no terminal, works on phone/web/desktop. That's the actual product for most people.

Everything else (`claude/.claude-plugin/`, `claude/skills/`, ChatGPT's Custom GPT path) is developer/power-user packaging — for people who use Claude Code, want a shareable one-click install for a group, or want to publish this on a marketplace/GPT Store.

No tools, no external API calls beyond the optional live dictionary fetch — this only changes word choice and tone, so it works entirely offline once installed if fetching isn't available.

## Updating the dictionary

Edit `dictionary/dictionary.md` and push. That's the single source of truth, published at:

```
https://raw.githubusercontent.com/adnrw/claudovsky/main/dictionary/dictionary.md
```

**No install today gives fully silent, zero-action updates.** Claude Code plugin marketplaces don't auto-refresh (multiple open feature requests for this: [#51350](https://github.com/anthropics/claude-code/issues/51350), [#38271](https://github.com/anthropics/claude-code/issues/38271), [#31462](https://github.com/anthropics/claude-code/issues/31462)) — plugin users need `/plugin marketplace update` manually. And a pasted Custom Instructions/Custom GPT block is static text; it never re-fetches on its own.

The workaround, wired into every packaging: each instruction set tells the assistant to fetch the raw URL above once per conversation if it has a web-fetch/browsing tool available, and fall back to its bundled/pasted word list if not. This is best-effort, not guaranteed. One real gap: `claude/skills/yiddish/reference/dictionary.md` is a bundled offline copy of the same file and is **not** auto-synced from `dictionary/dictionary.md` — update both by hand, or the bundled fallback drifts stale for anyone without web-fetch.

## License

CC BY-NC-SA 4.0 — see [`LICENSE`](./LICENSE). Worth noting: CC licenses are built for creative/content works, not code, but this repo is almost entirely instructions and word lists rather than software, so it fits fine. If you ever add actual code (scripts, an MCP server, etc.), that would sit oddly under a CC license — flag it if that happens and we can split licenses per-directory.

## Status / TODO

- [ ] Push this repo to GitHub (`adnrw/claudovsky`) — not yet pushed as of writing this
- [ ] Confirm exact install command syntax against current Claude Code docs (verified against docs.claude.com as of Aug 2026, but plugin CLI syntax is young and may shift)
- [ ] Verify Claude Code's plugin loader actually resolves a nested plugin root (`claude/.claude-plugin/plugin.json` via a `git-subdir` marketplace entry) — untested since the reorg, was previously at repo root
- [ ] Test Cowork install path directly — assumes parity with Claude Code, unverified
- [ ] Verify the live-fetch-on-conversation-start instruction actually fires reliably in practice, across Claude and ChatGPT — untested, best-effort only
- [ ] Set up a way to keep `dictionary/dictionary.md` and `claude/skills/yiddish/reference/dictionary.md` in sync automatically instead of by hand
