[**Advanced**](./introduction.md) > **Documentation of Translation Services** _(current)_

---

### Viewing Available Translate Services via Command Line

You can confirm the available translate services and their usage by printing the help message in the command line.

```bash
pdf2zh_next -h
```

At the end of the help message, you can view detailed information about the different translation services.

### DeepSeek translation with academic review

Select **DeepSeekReview** in the WebUI, or use `--deepseekreview` in the CLI,
to translate with DeepSeek and then review the draft against the source before
BabelDOC typesets it. This is an opt-in, two-pass engine using the official
DeepSeek API. The existing **DeepSeek** engine still performs one pass.
The review uses DeepSeek's [JSON output](https://api-docs.deepseek.com/guides/json_mode/)
API; the default model follows its [official model documentation](https://api-docs.deepseek.com/quick_start/pricing/).

Set `PDF2ZH_DEEPSEEK_REVIEW_API_KEY` in your environment rather than passing a
secret on the command line. Then run:

```bash
pdf2zh_next paper.pdf --deepseekreview \
  --deepseek-review-domain "reinforcement learning" \
  --deepseek-review-context "DreamerV3; keep Dreamer as a proper name; use consistent actor/critic terminology."
```

| Option | Default | Purpose |
| --- | --- | --- |
| `--deepseek-review-api-key` | Unset | DeepSeek API key; masked in the WebUI. Prefer the environment variable above. |
| `--deepseek-review-model` | `deepseek-flash` | Model for both translation and review. |
| `--deepseek-review-domain` | Empty | Optional subject area; inferred from available context when omitted. |
| `--deepseek-review-context` | Empty | Optional document background or terminology guidance. |

The reviewer receives the complete original translation request, including any
document/section titles, paragraph batch and glossary supplied by BabelDOC, plus
the draft and your domain/background. It checks technical terminology, omissions,
negation and exceptions, numbers and units, then returns corrected translated
text. This does not give the reviewer access to the entire PDF or external
references. Use a [glossary](./advanced.md) for consistent terminology throughout
a document.

Both passes use the same API key and model. Expect roughly twice as many API
requests and increased latency and token costs; review also includes the draft
and the original request. Both passes count toward the configured QPS limit and
token totals. If this engine is also used for automatic term extraction, those
LLM requests are reviewed too; select a separate term-extraction engine to avoid
that additional pass.

Only the final reviewed response is cached, separately from single-pass
translations and from other review prompts, models, domains and backgrounds.
Invalid, empty or incomplete review responses, changed batch IDs/schema, or
changed formula/style placeholders raise an error and are not cached as reviewed
translations. BabelDOC may retry or fall back according to its own translation
rules. These checks protect structure, but cannot guarantee scientific accuracy;
review important claims against the source.


---

### Translation Engine Support Policy

#### Tier 1 (Official Support)

**Tier 1 translation engines** are directly maintained by the project maintainers. Although the maintainers do **not use this project regularly**, they will rely on GitHub issues to identify problems. When any of these engines encounter issues, the maintainers will fix them as soon as possible to ensure stability and reliability.


Currently supported Tier 1 translation engines include:
1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible

#### Tier 2 (Community Support)

**Tier 2 translation engines** are maintained and supported by the community.  
When these engines encounter issues, the project maintainers will not provide direct fixes. Instead, they will label the related issues with `help wanted` and welcome pull requests from contributors to help resolve them.

All engines that are supported by the program but not explicitly listed under Tier 1 are considered Tier 2 translation engines.

#### Deprecated Engines

The following translation engines have been **deprecated** and will no longer be maintained or supported:

1. Bing
2. Google
