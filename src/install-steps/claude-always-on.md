# Claudovsky for Claude — always-on

Copy-paste, no GitHub, no terminal. Two minutes, once, and it's on by default for every new conversation from then on. Want it for just one chat instead? See [`per-session.md`](./per-session.md). Using ChatGPT or Gemini instead? See [`../chatgpt/always-on.md`](../chatgpt/always-on.md) or [`../gemini/always-on.md`](../gemini/always-on.md).

## Claude Desktop

1. Open Claude and log in.
2. Click your username (bottom left).
3. Open **Settings**.
4. Go to **General → Instructions for Claude**.
5. Paste the whole block below into that text box, underneath anything already in there:

{{INSTRUCTIONS_BLOCK}}

6. Save. Done — every new conversation now has Yiddish flavor by default.

**To turn it off later:** just delete that text from the same settings box, or type "stop with the Yiddish" in any chat for that conversation only.

## Claude Mobile

1. Open the sidebar.
2. Tap your initials (bottom left).
3. Open **Profile → Instructions**.
4. Paste the same block from the Claude Desktop section above.
5. Save. Done.

## That's it

Want it off by default and only on when you ask? See [`per-session.md`](./per-session.md) instead — no settings paste needed.

Everything else in this `claude/` folder plus the plugin files at the repo root are for people who use Claude Code, want a shareable install for a group, or want to publish this on a marketplace. See [`README.md`](./README.md) in this folder for that side of things.
