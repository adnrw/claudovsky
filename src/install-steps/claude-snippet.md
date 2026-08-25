# Always-on Claudovsky (CLAUDE.md snippet) — the default, recommended install

Skills auto-trigger by topic relevance — they won't fire on every turn just to change tone. This snippet is what makes Claudovsky **on by default, every session, no re-invoking**. It's the primary install path; the skill (`/claudovsky`) is the secondary, session-only alternative for people who don't want it always running (see main README).

Paste this into a `CLAUDE.md` (Claude Code: project or `~/.claude/CLAUDE.md` for global; Cowork: project instructions):

{{INSTRUCTIONS_BLOCK}}

This is a copy-paste step, not a plugin install — Claude Code and Cowork read CLAUDE.md / project instructions every turn, but plugins can't currently write to that file for you automatically. If the `claudovsky` plugin is also installed, this snippet will point Claude at its dictionary for consistent word choices instead of improvising.
