# Claudovsky

Claude, ChatGPT, or Gemini — but with Yiddish words sprinkled naturally into its answers.

**Before:** "Cripps had 27 touches and 2 goals, the captain leading the way for his team.

**After:** "Cripps had 27 touches and 2 goals, such a mensch doing his thing for the team."

## How it works

Claudovsky works in two different ways:

- **Always-on:** include Claudovsky's prompt in your AI platform's account context/instructions, and it will pepper Yiddish words into every new conversation.
- **Manually invoked per-session:** during a chat, you can invoke Claudovsky one conversation at a time and it doesn't touch your regular chats.

Claudovsky will also refrain from adding Yiddish words when it detects you're discussing something sensitive.

### Intensity

Claudovsky has three intensity levels, switchable anytime:

- **Nebbish:** light touch, a Yiddish word here and there
- **Mensch:** a Yiddish word or two per paragraph
- **Macher (default):** a Yiddish word added to most sentences

## Installation

Claudvosky installation is slightly different depending on your AI platform and how you want it to work.

| Platform | Always-on | Per-session |
|---|---|---|
| Claude | [`claude/always-on.md`](./claude/always-on.md) — paste into Settings → Instructions for Claude | [`claude/per-session.md`](./claude/per-session.md) — upload the `.skill` file via Settings → Skills, then invoke with `/claudovsky` |
| ChatGPT | [`chatgpt/always-on.md`](./chatgpt/always-on.md) — paste into Settings → Personalization → Custom Instructions | [`chatgpt/per-session.md`](./chatgpt/per-session.md) — build/open the shared "Claudovsky" Custom GPT |
| Gemini | [`gemini/always-on.md`](./gemini/always-on.md) — paste into Saved info | [`gemini/per-session.md`](./gemini/per-session.md) — build/open the shared "Claudovsky" Gem |

Each platform's page has the full copy-paste block and instructions on what to do with it.

## Dictionary

Every word Claudovsky is allowed to use (with definitions and usage examples) lives in [`dictionary/dictionary.md`](./dictionary/dictionary.md). 

If your platform allows it, Claudovsky will check for dicitonary updates once per conversation for the latest words; otherwise it will use the list on your local machine.

## License

CC BY-NC-SA 4.0 — see [`LICENSE`](./LICENSE).
