# Claudovsky for Claude — per-session (just one chat, nothing saved permanently)

Want Yiddish flavor without changing your account settings? Use the Skills panel — a one-time upload, then invoke it whenever you want, off by default otherwise.

## The easy way: upload the .skill file

1. Get `claudovsky.skill` (in this repo, or ask whoever sent you this for the file).
2. Open Claude → your name/profile → **Settings** → **Skills**.
3. Click **Add**, then upload `claudovsky.skill`.
4. In any chat, type `/claudovsky` (or just say "talk Yiddish") to turn it on for that conversation only. Say "stop with the Yiddish" to turn it off, or just start a new chat — nothing carries over automatically.

*(Unconfirmed: exactly what the "Add" button offers — a direct file upload, or something else. Worth a quick check before relying on this as the instructions to give someone else.)*

## The developer way: install the plugin from GitHub

If you use Claude Code and want it available via the marketplace instead of a manual file upload:

```
/plugin marketplace add adnrw/claudovsky
/plugin install claudovsky@claudovsky-marketplace
```

Then type `/claudovsky` at the start of any session. See the [`README.md`](./README.md) in this folder for the full plugin details, caveats, and the always-on CLAUDE.md snippet alternative for Claude Code/Cowork specifically.
