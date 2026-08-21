# Claudovsky for Gemini

Gemini has no GitHub-installable plugin/skill system either — same situation as ChatGPT. The two real customization surfaces are:

| | Scope | Maps to |
|---|---|---|
| **Saved info** | account-wide, every chat, always-on | [`always-on.md`](./always-on.md) — the default, recommended path |
| **Gems** | only when someone opens that specific Gem | [`per-session.md`](./per-session.md) — the session-based, opt-in alternative |

Both require pasting text into Gemini's UI — there's no command-line install. What's versioned here in GitHub is the source text; "installing" means a human copies it into Settings (Saved info) or the Gem builder (Gems) once.

A Gem can be shared by link — since September 2025 Gemini supports this natively, and it's the closest Gemini equivalent to "anyone can install this." Whoever opens the link gets their own reusable copy, not a live-shared session, and it doesn't change someone's regular Gemini chats the way Saved info does.

Unverified: exact current menu labels for Saved info and Gem creation/sharing (Google renames and moves these periodically). Confirm against Gemini's own UI/help docs before publishing instructions publicly.
