# Claudovsky for ChatGPT — Custom GPT (session-based alternative)

This is the **opt-in, per-conversation** mode: it only applies when someone opens this specific Custom GPT — not to their regular ChatGPT chats. Use this if you want a shareable "Claudovsky" GPT people can visit on purpose, rather than changing their whole account's behavior.

**Setup:**
1. ChatGPT → "Explore GPTs" → "Create" (GPT Builder).
2. Name it (e.g. "Claudovsky").
3. In the "Instructions" field, paste the text below.
4. Optional: under "Knowledge," upload `../src/dictionary.md` for the full word list with usage notes and the flagged/uncertain entries — the model can reference it for edge cases beyond the compact list already in the instructions.
5. Publish and share the GPT's link, or submit to the GPT Store, so others can install it by visiting the link and clicking "Use."

**Instructions field:**

{{INSTRUCTIONS_BLOCK}}

Unlike the Custom Instructions path ([`always-on.md`](./always-on.md)), this doesn't touch anyone's default ChatGPT behavior — it's contained entirely to sessions where someone deliberately opens this GPT.
