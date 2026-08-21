# Claudovsky for ChatGPT

ChatGPT has no GitHub-installable plugin/skill system — that's a Claude Code-specific mechanism (the old OpenAI "Plugins" feature was retired). The two real customization surfaces are:

| | Scope | Maps to |
|---|---|---|
| **Custom Instructions** | account-wide, every chat, always-on | [`always-on.md`](./always-on.md) — the default, recommended path |
| **Custom GPT** | only when someone opens that specific GPT | [`per-session.md`](./per-session.md) — the session-based, opt-in alternative |

Both require pasting text into ChatGPT's UI — there's no command-line install. What's versioned here in GitHub is the source text; "installing" means a human copies it into Settings (Custom Instructions) or the GPT Builder (Custom GPT) once.

A Custom GPT can be published with a shareable link or listed on the GPT Store, which is the closest ChatGPT equivalent to "anyone can install this" — but it's still a UI click ("Use this GPT"), not a repo-based install, and it doesn't change someone's regular ChatGPT chats the way Custom Instructions does.

Unverified: exact current field labels in Settings → Personalization (OpenAI renames these periodically) and whether GPT Store submission requirements have changed. Confirm against ChatGPT's own UI/help docs before publishing instructions publicly.
