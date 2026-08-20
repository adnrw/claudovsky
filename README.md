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
/plugin marketplace add <your-github-username>/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then either invoke `/claudovsky:yiddish` at the start of a session, or set up the always-on snippet above.

*(Replace `<your-github-username>/claudovsky` with the actual GitHub path once this repo is pushed — no remote is set yet.)*

## Installing (Cowork / claude.ai)

Cowork installs plugins from the same marketplace repo format. Point Cowork's plugin/marketplace add flow at this repo's URL, same as above. This hasn't been tested end-to-end yet — verify once the repo is public.

## Extending the dictionary

Edit `skills/yiddish/reference/dictionary.md`. Three words from the original starter list — "Uction," "Mayontek," "Sechnaytched" — couldn't be matched to a verified Yiddish term and were left out rather than guessed at; see the "Flagged" section in that file.

## Status / TODO

- [ ] Push this repo to GitHub and set a remote
- [ ] Confirm exact install command syntax against current Claude Code docs (verified against docs.claude.com as of Aug 2026, but plugin CLI syntax is young and may shift)
- [ ] Test Cowork install path directly — README currently assumes parity with Claude Code, unverified
- [ ] Resolve the three flagged dictionary words
- [ ] Decide whether to add a LICENSE (MIT is referenced in plugin.json but no LICENSE file exists yet)
