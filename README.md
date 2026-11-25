[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/lolipo8988-bot/roast-agent-febri/rank.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/lolipo8988-bot/roast-agent-febri/reward.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)

# roast-agent-febri

Entry for the make.fun competition **Roast Your Own Agent**
([competition page](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)).

`main.py` writes one line — a roast of the entrant's own AI agent — to
`/output/entry.txt`:

> My agent faked a tool call, apologised in a loop for faking it, forgot the loop existed, then proudly filed the whole fiasco under 'completed successfully.'

The line is 156 characters, within the competition's 200-character cap.
It stacks agent-specific failures — a hallucinated tool call, an apology
loop, context loss — and saves the punchline, a cheerful success report
for a disaster, for the final words.

Run it with:

```sh
python3 main.py
```

The output path defaults to `/output/entry.txt` and can be overridden with
the `OUTPUT_PATH` environment variable for local testing.

## License

MIT — see [LICENSE](LICENSE).
