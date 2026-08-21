# Claudovsky

Claude, ChatGPT, or Gemini — but with Yiddish words sprinkled naturally into its answers.

**Before:** "The sales guy gave us his whole pitch about why we should switch vendors."
**After:** "The sales guy gave us his whole schpiel about why we should switch vendors — total tsuris."

Three intensity levels, switchable anytime just by asking:

- **Nebbish** — light touch, a word here and there
- **Mensch** — a word or two per paragraph
- **Macher** — a word in most sentences

Turn it off anytime by saying "stop with the Yiddish"; bring it back the same way.

## Two flavors, every platform

**Always-on:** paste once into your account settings, and it applies to every new conversation from then on by default.

**Per-session:** off by default; you turn it on for one conversation at a time and it doesn't touch your regular chats.

| Platform | Always-on | Per-session |
|---|---|---|
| Claude | [`claude/always-on.md`](./claude/always-on.md) — paste into Settings → Instructions for Claude | [`claude/per-session.md`](./claude/per-session.md) — upload the `.skill` file via Settings → Skills, then say "talk Yiddish" or `/claudovsky` |
| ChatGPT | [`chatgpt/always-on.md`](./chatgpt/always-on.md) — paste into Settings → Personalization → Custom Instructions | [`chatgpt/per-session.md`](./chatgpt/per-session.md) — build/open the shared "Claudovsky" Custom GPT |
| Gemini | [`gemini/always-on.md`](./gemini/always-on.md) — paste into Saved info | [`gemini/per-session.md`](./gemini/per-session.md) — build/open the shared "Claudovsky" Gem |

Each platform's page has the full copy-paste block and exact settings location. None of these are true one-click GitHub installs — every path needs one manual paste or upload, once, because none of Claude, ChatGPT, or Gemini currently offer a GitHub-triggered install for this kind of thing.

## The word list

Every word it's allowed to use, with meanings, lives in [`dictionary/dictionary.md`](./dictionary/dictionary.md). It only uses words from that list — nothing invented. Where a page's copy-paste block or Custom GPT/Gem has a web-fetch tool available, it fetches this file fresh once per conversation for the latest words; otherwise it falls back to the list baked into that page.

## For developers

The Claude Code plugin lives at the repo root (`.claude-plugin/`, `skills/`) — that's the standard, documented location Claude Code expects, and what makes `/plugin marketplace add adnrw/claudovsky` work. See [`claude/README.md`](./claude/README.md) for plugin/marketplace details, [`chatgpt/README.md`](./chatgpt/README.md) and [`gemini/README.md`](./gemini/README.md) for how those two platforms' non-plugin packaging works.

## License

CC BY-NC-SA 4.0 — see [`LICENSE`](./LICENSE).
