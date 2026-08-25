# Claudovsky - a bissel Yiddish in your Claude 

Claudovsky adds Yiddish words into Claude's responses. It also works with ChatGPT and Gemini.

**Before** 

> "Cripps had 27 touches and 2 goals, the captain leading the way for his team."

**After** 

> "Cripps had 27 touches and 2 goals, what a mensch, doing his thing for the team."

## Download Claudovsky

- [Claudovsky for Claude](https://github.com/adnrw/claudovsky/releases/latest/download/claude.zip)
- [Claudovsky for ChatGPT](https://github.com/adnrw/claudovsky/releases/latest/download/chatgpt.zip)
- [Claudovsky for Gemini](https://github.com/adnrw/claudovsky/releases/latest/download/gemini.zip)

## Install and use Claudovsky

First, download the latest release for your platform using the links above.

Then, decide how you want to use Claudovsky:

- **Always-on:** Claudovsky will shtoop Yiddish words into every chat, except when you're talking about sensitive subjects. 
- **Activated per-chat:** during any chat, you can start Claudovsky and all responses in that chat will start including Yiddish words.

Follow the instructions in the download for more detail on getting it running. 

You can turn Claudovsky off at any time, in any chat by saying `Stop speaking like Claudovsky` or `Enough with the Yiddish`.

### How much Yiddish

Claudovsky has three Yiddish levels:

- **Nebbish:** light touch, a Yiddish word here and there
- **Mensch:** a Yiddish word or two per paragraph
- **Macher (default):** a Yiddish word added to most sentences

Switch at any time by telling Claudovsky to use a different level `Claudovsky, be a mensch`.

## Dictionary

Every word Claudovsky is allowed to use (with definitions and usage examples) lives in [`The Claudovsky Dictionary`](./src/dictionary.md). 

If your platform allows it, Claudovsky will check for dictionary updates once per conversation for the latest words; otherwise it will use the list on your local machine.

## License

CC BY-NC-SA 4.0 — see [`LICENSE`](./LICENSE).
