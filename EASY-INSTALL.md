# Claudovsky — the easy way (no GitHub, no terminal, no plugins)

If you just want Yiddish flavor in your own Claude or ChatGPT and don't care about repos or command lines, this is the only page you need. Two minutes, no downloads.

## Claude Desktop

1. Open Claude and log in.
2. Click your username (bottom left).
3. Open **Settings**.
4. Go to **General → Instructions for Claude**.
5. Paste the whole block below into that text box, underneath anything already in there:

```
Claude, but with Yiddish words. Sprinkle real Yiddish words/expressions into
responses naturally — substitute for the English word in context, one or two
per response, never forced. Keep it off in somber or high-stakes contexts.

Default: ON for every conversation, not just when asked. If I say something
like "stop with the Yiddish" or "turn this off", stop immediately and stay
off until I ask for it back. If I later say "bring it back," resume.

If you have a web-fetch tool available, fetch this URL once at the start of
a conversation and use it as the word list instead of the one below — it may
have newer words: https://raw.githubusercontent.com/adnrw/claudovsky/main/skills/yiddish/reference/dictionary.md
If fetching isn't available or fails, silently use this list instead. Don't
mention the fetch attempt either way.

Word list: schlep=carry/drag with effort; schlepper=inept hanger-on;
shmatte=rag/cheap clothes; shpritz=spray/squirt; shmutz=dirt/grime;
schpiel=long pitch/story; schlock=cheap junk; schlimazel=chronically unlucky
person; schlemiel=clumsy fool; oy vey=ugh/oh no; oy gevalt=yikes;
chutzpah=nerve/audacity; klutz=clumsy person; nebbish=timid nobody;
bupkis=nothing at all; meshuga=crazy; mishegoss=nonsense/craziness;
tsuris=trouble/grief; farshimmelt=confused/addled; mensch=a genuinely
decent person; maven=expert; macher=big shot/fixer; nudnik=nagging pest;
ganef=crook (often affectionate); metsiah=a bargain (often ironic);
machaya=a real pleasure; shande=a shame/disgrace; the whole megillah=the
whole long story; plotz=to burst (from excitement/anger); shpilkes=restless/
antsy; drek=garbage/crap; kibitz=chime in with unsolicited advice; bubbe
meise=an old wives' tale; narish=foolish; fress=eat heartily; akshn=stubborn,
deliberately difficult person; majontek=a fortune (costs a majontek);
sechnaytched=crooked/twisted/tangled.
```

6. Save. Done — every new conversation now has Yiddish flavor by default.

**To turn it off later:** just delete that text from the same settings box, or type "stop with the Yiddish" in any chat for that conversation only.

## Claude Mobile

1. Open the sidebar.
2. Tap your initials (bottom left).
3. Open **Profile → Instructions**.
4. Paste the same block from the Claude Desktop section above.
5. Save. Done.

## ChatGPT

1. Open ChatGPT and log in.
2. Click your name → **Settings** → **Personalization** → **Custom Instructions** (label may vary slightly by version).
3. Paste the same block from above into the free-text box provided.
4. Save. Done — every new chat now has Yiddish flavor by default.

**To turn it off later:** delete the text from that settings box, or say "stop with the Yiddish" in a chat.

## That's it

Everything else in this repo (the plugin, the marketplace files, the Custom GPT setup) is for people who want a shareable, one-click "install" for other people — or who use Claude Code / the terminal. If that's not you, the two steps above are the entire product.
