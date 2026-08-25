# Claudovsky for Claude

Two ways to get Yiddish flavor in Claude: paste it into your account once and it's on by default, or invoke it per-conversation without touching your regular settings.

| | Scope | Maps to |
|---|---|---|
| **Always-on** | account-wide, on by default every new chat | [`always-on.md`](./always-on.md) — paste into Settings → Instructions for Claude (also covers the Claude Code/Cowork `CLAUDE.md` alternative) |
| **Per-session** | off by default, invoke with `/claudovsky` or "talk Yiddish" | [`per-session.md`](./per-session.md) — upload `claudovsky.skill` via the Skills panel |

Full copy-paste blocks and exact setup steps live on those two pages, not here.

## Keeping the bundled dictionary in sync

`src/dictionary.md` at the repo root is the master copy. The compact word lists in every platform's `always-on.md`/`per-session.md`, and the copy bundled inside `claudovsky.skill`, are generated from it by `src/build.py` — edit `src/dictionary.md`, run the script, nothing else needs hand-editing. `build.py` renders the skill's contents straight into the zip in memory — nothing is unpacked to disk first.
