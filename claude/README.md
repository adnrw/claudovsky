# Claudovsky for Claude

Two ways to get Yiddish flavor in Claude: paste it into your account once and it's on by default, or invoke it per-conversation without touching your regular settings.

| | Scope | Maps to |
|---|---|---|
| **Always-on** | account-wide, on by default every new chat | [`always-on.md`](./always-on.md) — paste into Settings → Instructions for Claude (or Claude Code's `CLAUDE.md`, snippet in [`snippets/`](./snippets/)) |
| **Per-session** | off by default, invoke with `/claudovsky` or "talk Yiddish" | [`per-session.md`](./per-session.md) — upload `claudovsky.skill` via the Skills panel, or install the Claude Code plugin below |

Full copy-paste blocks and exact setup steps live on those two pages, not here.

## Claude Code / Cowork plugin

This folder is also the installable plugin — `.claude-plugin/` and `skills/claudovsky/` live here, not the repo root; only the marketplace manifest stays at the true repo root and points in here.

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then `/claudovsky` at the start of a session, or set up the always-on `CLAUDE.md` snippet instead. Cowork installs from the same marketplace format — point its plugin/marketplace-add flow at `adnrw/claudovsky` (not yet verified end-to-end).

## Keeping the bundled dictionary in sync

`dictionary/dictionary.md` at the repo root is the master copy. `skills/claudovsky/reference/dictionary.md` here, plus the compact word lists in every platform's `always-on.md`/`per-session.md`, are hand-propagated from it — update the root first, then copy the change out.
