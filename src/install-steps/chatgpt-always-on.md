# Claudovsky for ChatGPT — Custom Instructions (default, always-on)

ChatGPT has no plugin/skill install mechanism — the closest things are Custom Instructions (account-wide, every chat) and Custom GPTs (only active in that specific GPT). This is the **default, always-on** path: it applies to every conversation on your account, same spirit as the Claude CLAUDE.md snippet.

**Setup:** ChatGPT → Settings → Personalization → Custom Instructions. Paste the block below into "Anything else ChatGPT should know about you?" (or the equivalent free-text field — labels shift between ChatGPT versions).

{{INSTRUCTIONS_BLOCK}}

Note: `sechnaytched` is taken on Andrew's word, not independently verified against a standard Yiddish source — see the confidence notes in [`../src/dictionary.md`](../src/dictionary.md).

Want it off by default and only on for one chat instead? See [`per-session.md`](./per-session.md). Using Claude or Gemini? See [`../claude/always-on.md`](../claude/always-on.md) or [`../gemini/always-on.md`](../gemini/always-on.md).
