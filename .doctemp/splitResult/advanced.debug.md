<!-- CHUNK ID: chunk_DDD39913  CHUNK TYPE: paragraph START_LINE:1 -->
[**Advanced**](./introduction.md) > **Advanced** _(current)_

<!-- CHUNK ID: h_rule_7193a0cb  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_D9B293FF  CHUNK TYPE: paragraph START_LINE:5 -->
<h3 id="toc">Table of Contents</h3>

<!-- CHUNK ID: chunk_F0A2B12C  CHUNK TYPE: list START_LINE:7 -->
- [Command Line Args](#command-line-args)
- [Rate Limiting Configuration Guide](#rate-limiting-configuration-guide)
- [Partial translation](#partial-translation)
- [Specify source and target languages](#specify-source-and-target-languages)
- [Translate wih exceptions](#translate-wih-exceptions)
- [Custom prompt](#custom-prompt)
- [Custom configuration](#custom-configuration)
- [Skip clean](#skip-clean)
- [Translation cache](#translation-cache)
- [Deployment as a public services](#deployment-as-a-public-services)
- [Authentication and welcome page](#authentication-and-welcome-page)
- [Glossary Support](#glossary-support)

<!-- CHUNK ID: h_rule_0fe0f941  CHUNK TYPE: h_rule START_LINE:20 -->
---

<!-- CHUNK ID: chunk_3BF1A9B5  CHUNK TYPE: header START_LINE:22 -->
#### Command Line Args

<!-- CHUNK ID: chunk_A2860DDF  CHUNK TYPE: paragraph START_LINE:24 -->
Execute the translation command in the command line to generate the translated document `example-mono.pdf` and the bilingual document `example-dual.pdf` in the current working directory. Use Google as the default translation service. More support translation services can find [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<!-- CHUNK ID: chunk_B6CD1E39  CHUNK TYPE: image START_LINE:26 -->
<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

<!-- CHUNK ID: chunk_B3EB591F  CHUNK TYPE: paragraph START_LINE:28 -->
In the following table, we list all advanced options for reference:

<!-- CHUNK ID: chunk_A2A42E6B  CHUNK TYPE: header START_LINE:30 -->
##### Args

<!-- CHUNK ID: chunk_7A00EE21  CHUNK TYPE: longtable_head START_LINE:32 -->
| Option                          | Function                                                                               | Example                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Local PDF file path                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
<!-- CHUNK ID: chunk_848B1EE1  CHUNK TYPE: longtable_content START_LINE:35 -->
| `links`                         | Online files                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
<!-- CHUNK ID: chunk_8B4991D7  CHUNK TYPE: longtable_content START_LINE:36 -->
| `--output`                      | Output directory for files                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
<!-- CHUNK ID: chunk_D7ED91EE  CHUNK TYPE: longtable_content START_LINE:37 -->
| `--<Services>`                  | Use [**specific service**](./Documentation-of-Translation-Services.md) for translation | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
<!-- CHUNK ID: chunk_00AF4E48  CHUNK TYPE: longtable_content START_LINE:38 -->
| `--help`, `-h`                  | Show help message and exit                                                             | `pdf2zh -h`                                                                                                          |
<!-- CHUNK ID: chunk_B0ABBFCE  CHUNK TYPE: longtable_content START_LINE:39 -->
| `--config-file`                 | Path to the configuration file                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
<!-- CHUNK ID: chunk_634BA748  CHUNK TYPE: longtable_content START_LINE:40 -->
| `--report-interval`             | Progress report interval in seconds                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
<!-- CHUNK ID: chunk_46037BF6  CHUNK TYPE: longtable_content START_LINE:41 -->
| `--debug`                       | Use debug logging level                                                                | `pdf2zh example.pdf --debug`                                                                                         |
<!-- CHUNK ID: chunk_18BA0512  CHUNK TYPE: longtable_content START_LINE:42 -->
| `--gui`                         | Interact with GUI                                                                      | `pdf2zh --gui`                                                                                                       |
<!-- CHUNK ID: chunk_0DA1F9CB  CHUNK TYPE: longtable_content START_LINE:43 -->
| `--warmup`                      | Only download and verify required assets then exit                                     | `pdf2zh example.pdf --warmup`                                                                                        |
<!-- CHUNK ID: chunk_D380BDDD  CHUNK TYPE: longtable_content START_LINE:44 -->
| `--generate-offline-assets`     | Generate offline assets package in the specified directory                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
<!-- CHUNK ID: chunk_F5703109  CHUNK TYPE: longtable_content START_LINE:45 -->
| `--restore-offline-assets`      | Restore offline assets package from the specified directory                            | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
<!-- CHUNK ID: chunk_EB44345E  CHUNK TYPE: longtable_content START_LINE:46 -->
| `--version`                     | Show version then exit                                                                 | `pdf2zh --version`                                                                                                   |
<!-- CHUNK ID: chunk_AD6D96FE  CHUNK TYPE: longtable_content START_LINE:47 -->
| `--pages`                       | Partial document translation                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
<!-- CHUNK ID: chunk_DB35B267  CHUNK TYPE: longtable_content START_LINE:48 -->
| `--lang-in`                     | The code of source language                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
<!-- CHUNK ID: chunk_CAF754AF  CHUNK TYPE: longtable_content START_LINE:49 -->
| `--lang-out`                    | The code of target language                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
<!-- CHUNK ID: chunk_2E1280AA  CHUNK TYPE: longtable_content START_LINE:50 -->
| `--min-text-length`             | Minimum text length to translate                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
<!-- CHUNK ID: chunk_03902660  CHUNK TYPE: longtable_content START_LINE:51 -->
| `--rpc-doclayout`               | RPC service host address for document layout analysis                                  |                                                                                                                      |
<!-- CHUNK ID: chunk_D3C262BD  CHUNK TYPE: longtable_content START_LINE:52 -->
| `--qps`                         | QPS limit for translation service                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
<!-- CHUNK ID: chunk_0F22CD53  CHUNK TYPE: longtable_content START_LINE:53 -->
| `--ignore-cache`                | Ignore translation cache                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
<!-- CHUNK ID: chunk_ED6020AC  CHUNK TYPE: longtable_content START_LINE:54 -->
| `--custom-system-prompt`        | Custom system prompt for translation. Used for `/no_think` in Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
<!-- CHUNK ID: chunk_FC174A78  CHUNK TYPE: longtable_content START_LINE:55 -->
| `--pool-max-worker`             | Maximum number of workers for translation pool. If not set, will use qps as the number of workers | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
<!-- CHUNK ID: chunk_ED9DDA51  CHUNK TYPE: longtable_content START_LINE:56 -->
| `--no-auto-extract-glossary`    | Disable auto extract glossary                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
<!-- CHUNK ID: chunk_3A42A3F8  CHUNK TYPE: longtable_content START_LINE:57 -->
| `--primary-font-family`         | Override primary font family for translated text. Choices: 'serif' for serif fonts, 'sans-serif' for sans-serif fonts, 'script' for script/italic fonts. If not specified, uses automatic font selection based on original text properties. | `pdf2zh example.pdf --primary-font-family serif` |
<!-- CHUNK ID: chunk_D91FDBD2  CHUNK TYPE: longtable_content START_LINE:58 -->
| `--no-dual`                     | Do not output bilingual PDF files                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
<!-- CHUNK ID: chunk_BF3C03E7  CHUNK TYPE: longtable_content START_LINE:59 -->
| `--no-mono`                     | Do not output monolingual PDF files                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
<!-- CHUNK ID: chunk_D70705B4  CHUNK TYPE: longtable_content START_LINE:60 -->
| `--formular-font-pattern`       | Font pattern to identify formula text                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
<!-- CHUNK ID: chunk_BC7944E0  CHUNK TYPE: longtable_content START_LINE:61 -->
| `--formular-char-pattern`       | Character pattern to identify formula text                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
<!-- CHUNK ID: chunk_73F7BC27  CHUNK TYPE: longtable_content START_LINE:62 -->
| `--split-short-line`            | Force split short line into different paragraphs                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
<!-- CHUNK ID: chunk_17ED68F1  CHUNK TYPE: longtable_content START_LINE:63 -->
| `--short-line-split-factor`     | Split threshold factor for short lines                                                 |                                                                                                                      |
<!-- CHUNK ID: chunk_B4E886EC  CHUNK TYPE: longtable_content START_LINE:64 -->
| `--skip-clean`                  | Skip PDF cleaning step                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
<!-- CHUNK ID: chunk_857F16B2  CHUNK TYPE: longtable_content START_LINE:65 -->
| `--dual-translate-first`        | 在双 PDF 模式下优先放置翻译页                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
<!-- CHUNK ID: chunk_A04861D5  CHUNK TYPE: longtable_content START_LINE:66 -->
| `--disable-rich-text-translate` | Disable rich text translation                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
<!-- CHUNK ID: chunk_9D02F06D  CHUNK TYPE: longtable_content START_LINE:67 -->
| `--enhance-compatibility`       | Enable all compatibility enhancement options                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
<!-- CHUNK ID: chunk_7EC1028A  CHUNK TYPE: longtable_content START_LINE:68 -->
| `--use-alternating-pages-dual`  | Use alternating pages mode for dual PDF                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
<!-- CHUNK ID: chunk_D6BE0E79  CHUNK TYPE: longtable_content START_LINE:69 -->
| `--watermark-output-mode`       | Watermark output mode for PDF files                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
<!-- CHUNK ID: chunk_D63C027F  CHUNK TYPE: longtable_content START_LINE:70 -->
| `--max-pages-per-part`          | Maximum pages per part for split translation                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
<!-- CHUNK ID: chunk_3F10F28E  CHUNK TYPE: longtable_content START_LINE:71 -->
| `--translate-table-text`        | Translate table text (experimental)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
<!-- CHUNK ID: chunk_8BCCD462  CHUNK TYPE: longtable_content START_LINE:72 -->
| `--skip-scanned-detection`      | Skip scanned detection                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
<!-- CHUNK ID: chunk_75518F89  CHUNK TYPE: longtable_content START_LINE:73 -->
| `--ocr-workaround`              | Force translated text to be black and add white background                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
<!-- CHUNK ID: chunk_E4BD664E  CHUNK TYPE: longtable_content START_LINE:74 -->
| `--auto-enable-ocr-workaround`  | Enable automatic OCR workaround. If a document is detected as heavily scanned, this will attempt to enable OCR processing and skip further scan detection. See documentation for details. (default: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
<!-- CHUNK ID: chunk_6803D13A  CHUNK TYPE: longtable_content START_LINE:75 -->
| `--only-include-translated-page`| Only include translated pages in the output PDF. Effective only when --pages is used. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
<!-- CHUNK ID: chunk_1E404081  CHUNK TYPE: longtable_content START_LINE:76 -->
| `--glossaries`                  | Custom glossary for translation.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
<!-- CHUNK ID: chunk_1B83C5B9  CHUNK TYPE: longtable_content START_LINE:77 -->
| `--save-auto-extracted-glossary`| save automatically extracted glossary.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |
<!-- CHUNK ID: chunk_CE6D9EA3  CHUNK TYPE: longtable_content START_LINE:78 -->
| `--no-merge-alternating-line-numbers` | Disable merging of alternating line numbers and text paragraphs in documents with line numbers | `pdf2zh example.pdf --no-merge-alternating-line-numbers` |
<!-- CHUNK ID: chunk_6ADE00C8  CHUNK TYPE: longtable_content START_LINE:79 -->
| `--no-remove-non-formula-lines` | Disable removal of non-formula lines within paragraph areas                          | `pdf2zh example.pdf --no-remove-non-formula-lines`                                                                    |
<!-- CHUNK ID: chunk_2525055D  CHUNK TYPE: longtable_content START_LINE:80 -->
| `--non-formula-line-iou-threshold` | Set IoU threshold for identifying non-formula lines (0.0-1.0)                     | `pdf2zh example.pdf --non-formula-line-iou-threshold 0.85`                                                            |
<!-- CHUNK ID: chunk_6ACD14AF  CHUNK TYPE: longtable_content START_LINE:81 -->
| `--figure-table-protection-threshold` | Set protection threshold for figures and tables (0.0-1.0). Lines within figures/tables will not be processed | `pdf2zh example.pdf --figure-table-protection-threshold 0.95` |
<!-- CHUNK ID: chunk_1DE32F1F  CHUNK TYPE: longtable_content START_LINE:82 -->
| `--skip-formula-offset-calculation` | Skip formula offset calculation during processing         | `pdf2zh example.pdf --skip-formula-offset-calculation`                                                                |


<!-- CHUNK ID: chunk_140EFE95  CHUNK TYPE: header START_LINE:85 -->
##### GUI Args

<!-- CHUNK ID: chunk_2D086D22  CHUNK TYPE: longtable_head START_LINE:87 -->
| Option                          | Function                               | Example                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Enable sharing mode                    | `pdf2zh --gui --share`                          |
<!-- CHUNK ID: chunk_927CDC03  CHUNK TYPE: longtable_content START_LINE:90 -->
| `--auth-file`                   | Path to the authentication file        | `pdf2zh --gui --auth-file /path`                |
<!-- CHUNK ID: chunk_951E61B3  CHUNK TYPE: longtable_content START_LINE:91 -->
| `--welcome-page`                | Path to the welcome html file          | `pdf2zh --gui --welcome-page /path`             |
<!-- CHUNK ID: chunk_A9F2F2FE  CHUNK TYPE: longtable_content START_LINE:92 -->
| `--enabled-services`            | Enabled translation services           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
<!-- CHUNK ID: chunk_2C863550  CHUNK TYPE: longtable_content START_LINE:93 -->
| `--disable-gui-sensitive-input` | Disable GUI sensitive input            | `pdf2zh --gui --disable-gui-sensitive-input`    |
<!-- CHUNK ID: chunk_0598D53D  CHUNK TYPE: longtable_content START_LINE:94 -->
| `--disable-config-auto-save`    | Disable automatic configuration saving | `pdf2zh --gui --disable-config-auto-save`       |
<!-- CHUNK ID: chunk_99D3B3A8  CHUNK TYPE: longtable_content START_LINE:95 -->
| `--server-port`                 | WebUI Port                             | `pdf2zh --gui --server-port 7860`               |

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:97 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_a29d8049  CHUNK TYPE: h_rule START_LINE:99 -->
---

<!-- CHUNK ID: chunk_E0DC0651  CHUNK TYPE: header START_LINE:101 -->
#### Rate Limiting Configuration Guide

<!-- CHUNK ID: chunk_23D405EC  CHUNK TYPE: paragraph START_LINE:103 -->
When using translation services, proper rate limiting configuration is crucial to avoid API errors and optimize performance. This guide explains how to configure `--qps` and `--pool-max-worker` parameters based on different upstream service limitations.

<!-- CHUNK ID: chunk_742CD289  CHUNK TYPE: blockquote START_LINE:105 -->
> [!TIP]
>
> It is recommended that the pool_size does not exceed 1000. If the pool_size calculated by the following method exceeds 1000, please use 1000.

<!-- CHUNK ID: chunk_F9E5B2E2  CHUNK TYPE: header START_LINE:109 -->
##### RPM (Requests Per Minute) Rate Limiting

<!-- CHUNK ID: chunk_CDE1A5D3  CHUNK TYPE: paragraph START_LINE:111 -->
When the upstream service has RPM limitations, use the following calculation:

**Calculation Formula:**
<!-- CHUNK ID: chunk_D293CCA3  CHUNK TYPE: list START_LINE:114 -->
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

<!-- CHUNK ID: chunk_1C383BEE  CHUNK TYPE: blockquote START_LINE:117 -->
> [!NOTE]
> The factor of 10 is an empirical coefficient that generally works well for most scenarios.

<!-- CHUNK ID: chunk_AB49073F  CHUNK TYPE: paragraph START_LINE:120 -->
**Example:**
If your translation service has a limit of 600 RPM:
<!-- CHUNK ID: chunk_131B05E6  CHUNK TYPE: list START_LINE:122 -->
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

<!-- CHUNK ID: chunk_D4EF62BC  CHUNK TYPE: code_block START_LINE:125 -->
```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

<!-- CHUNK ID: chunk_C7673CDB  CHUNK TYPE: header START_LINE:129 -->
##### Concurrent Connection Limiting

<!-- CHUNK ID: chunk_62AE5A6C  CHUNK TYPE: paragraph START_LINE:131 -->
When the upstream service has concurrent connection limitations (like GLM official service), use this approach:

**Calculation Formula:**
<!-- CHUNK ID: chunk_B095EF50  CHUNK TYPE: list START_LINE:134 -->
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

<!-- CHUNK ID: chunk_1616A330  CHUNK TYPE: paragraph START_LINE:137 -->
**Example:**
If your translation service allows 50 concurrent connections:
<!-- CHUNK ID: chunk_1D19FB94  CHUNK TYPE: list START_LINE:139 -->
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

<!-- CHUNK ID: chunk_DB872698  CHUNK TYPE: code_block START_LINE:142 -->
```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

<!-- CHUNK ID: chunk_4C0D79DD  CHUNK TYPE: header START_LINE:146 -->
##### Best Practices

<!-- CHUNK ID: chunk_60A6D664  CHUNK TYPE: blockquote START_LINE:148 -->
> [!TIP]
> - Always start with conservative values and gradually increase if needed
> - Monitor your service's response times and error rates
> - Different services may require different optimization strategies
> - Consider your specific use case and document size when setting these parameters


<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:155 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_722c0d79  CHUNK TYPE: h_rule START_LINE:157 -->
---

<!-- CHUNK ID: chunk_ADC018D0  CHUNK TYPE: header START_LINE:159 -->
#### Partial translation

<!-- CHUNK ID: chunk_A7D2451C  CHUNK TYPE: paragraph START_LINE:161 -->
Use the `--pages` parameter to translate a portion of a document.

<!-- CHUNK ID: chunk_C04AFE09  CHUNK TYPE: list START_LINE:163 -->
- If the page numbers are consecutive, you can write it like this:

<!-- CHUNK ID: chunk_037196E3  CHUNK TYPE: code_block START_LINE:165 -->
```bash
pdf2zh_next example.pdf --pages 1-3
```

<!-- CHUNK ID: chunk_02CC256B  CHUNK TYPE: code_block START_LINE:169 -->
```bash
pdf2zh_next example.pdf --pages 25-
```

<!-- CHUNK ID: chunk_773EEC89  CHUNK TYPE: blockquote START_LINE:173 -->
> [!TIP]
> `25-` includes all pages after page 25. If your document has 100 pages, this is equivalent to `25-100`.
> 
> Similarly, `-25` includes all pages before page 25, which is equivalent to `1-25`.

<!-- CHUNK ID: chunk_1A89F075  CHUNK TYPE: list START_LINE:178 -->
- If the pages are not consecutive, you can use a comma `,` to separate them.

<!-- CHUNK ID: chunk_046E7E79  CHUNK TYPE: paragraph START_LINE:180 -->
For example, if you want to translate the first and third pages, you can use the following command:

<!-- CHUNK ID: chunk_7FBB71F3  CHUNK TYPE: code_block START_LINE:182 -->
```bash
pdf2zh_next example.pdf --pages "1,3"
```

<!-- CHUNK ID: chunk_376C9855  CHUNK TYPE: list START_LINE:186 -->
- If the pages include both consecutive and non-consecutive ranges, you can also connect them with a comma, like this:

<!-- CHUNK ID: chunk_DE0F06A2  CHUNK TYPE: code_block START_LINE:188 -->
```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

<!-- CHUNK ID: chunk_16D6BA70  CHUNK TYPE: paragraph START_LINE:192 -->
This command will translate the first page, the third page, pages 10-20, and all pages from 25 to the end.


[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_44986cd7  CHUNK TYPE: h_rule START_LINE:197 -->
---

<!-- CHUNK ID: chunk_482C5F18  CHUNK TYPE: header START_LINE:199 -->
#### Specify source and target languages

<!-- CHUNK ID: chunk_3E16227B  CHUNK TYPE: paragraph START_LINE:201 -->
See [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

<!-- CHUNK ID: chunk_CE426311  CHUNK TYPE: code_block START_LINE:203 -->
```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:207 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_1216eb18  CHUNK TYPE: h_rule START_LINE:209 -->
---

<!-- CHUNK ID: chunk_EA41DE52  CHUNK TYPE: header START_LINE:211 -->
#### Translate wih exceptions

<!-- CHUNK ID: chunk_6BAF2E56  CHUNK TYPE: paragraph START_LINE:213 -->
Use regex to specify formula fonts and characters that need to be preserved:

<!-- CHUNK ID: chunk_8D6F2147  CHUNK TYPE: code_block START_LINE:215 -->
```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

<!-- CHUNK ID: chunk_8FEF09F4  CHUNK TYPE: paragraph START_LINE:219 -->
Preserve `Latex`, `Mono`, `Code`, `Italic`, `Symbol` and `Math` fonts by default:

<!-- CHUNK ID: chunk_ACAC9383  CHUNK TYPE: code_block START_LINE:221 -->
```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:225 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_56986cf4  CHUNK TYPE: h_rule START_LINE:227 -->
---

<!-- CHUNK ID: chunk_37A13558  CHUNK TYPE: header START_LINE:229 -->
#### Custom prompt

<!-- CHUNK ID: chunk_54E57534  CHUNK TYPE: html_comment START_LINE:231 -->
<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

<!-- CHUNK ID: chunk_5F141742  CHUNK TYPE: paragraph START_LINE:233 -->
Custom system prompt for translation. It is mainly used to add the '/no_think' instruction of Qwen 3 in the prompt.

<!-- CHUNK ID: chunk_4E347A0E  CHUNK TYPE: code_block START_LINE:235 -->
```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:239 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_f644669a  CHUNK TYPE: h_rule START_LINE:241 -->
---

<!-- CHUNK ID: chunk_1EC5A9B5  CHUNK TYPE: header START_LINE:243 -->
#### Custom configuration

<!-- CHUNK ID: chunk_754794E1  CHUNK TYPE: paragraph START_LINE:245 -->
There are multiple ways to modify and import the configuration file.

<!-- CHUNK ID: chunk_B9BF8271  CHUNK TYPE: blockquote START_LINE:247 -->
> [!NOTE]
> **Configuration File Hierarchy**
>
> When modifying the same parameter using different methods, the software will apply changes according to the priority order below. 
>
> Higher-ranked modifications will override lower-ranked ones.
>
> **cli/gui > env > user config file > default config file**

<!-- CHUNK ID: chunk_06B261DE  CHUNK TYPE: list START_LINE:256 -->
- Modifying Configuration via **Command Line Arguments**

<!-- CHUNK ID: chunk_4579F74D  CHUNK TYPE: paragraph START_LINE:258 -->
For most cases, you can directly pass your desired settings through command line arguments. Please refer to [Command Line Args](#cmd) for more information.

For example, if you want to enable a GUI window, you can use the following command:

<!-- CHUNK ID: chunk_9668B90D  CHUNK TYPE: code_block START_LINE:262 -->
```bash
pdf2zh_next --gui
```

<!-- CHUNK ID: chunk_85CC4581  CHUNK TYPE: list START_LINE:266 -->
- Modifying Configuration via **Environment Variables**

<!-- CHUNK ID: chunk_A3573A4C  CHUNK TYPE: paragraph START_LINE:268 -->
You can replace the `--` in command line arguments with `PDF2ZH_`, connect parameters using `=`, and replace `-` with `_` as environment variables.

For example, if you want to enable a GUI window, you can use the following command:

<!-- CHUNK ID: chunk_5A8D89BB  CHUNK TYPE: code_block START_LINE:272 -->
```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<!-- CHUNK ID: chunk_9DD1EEE0  CHUNK TYPE: image START_LINE:276 -->
<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

<!-- CHUNK ID: chunk_11A0D60E  CHUNK TYPE: list START_LINE:278 -->
- User-Specified **Configuration File**

<!-- CHUNK ID: chunk_9EE9DFB5  CHUNK TYPE: paragraph START_LINE:280 -->
You can specify a configuration file using the command line argument below:

<!-- CHUNK ID: chunk_3B8259C7  CHUNK TYPE: code_block START_LINE:282 -->
```bash
pdf2zh_next --config-file '/path/config.toml'
```

<!-- CHUNK ID: chunk_FC4FBE9E  CHUNK TYPE: paragraph START_LINE:286 -->
If you are unsure about the config file format, please refer to the default configuration file described below.

<!-- CHUNK ID: chunk_A4C0C077  CHUNK TYPE: list START_LINE:288 -->
- **Default Configuration File**

<!-- CHUNK ID: chunk_B17D9FE3  CHUNK TYPE: paragraph START_LINE:290 -->
The default configuration file is located at `~/.config/pdf2zh`. 
Please do not modify the configuration files in the `default` directory. 
It is strongly recommended to refer to this configuration file's content and use **User-Specified Configuration File** to implement your own configuration file.

<!-- CHUNK ID: chunk_15DFB8EE  CHUNK TYPE: blockquote START_LINE:294 -->
> [!TIP]
> - By default, pdf2zh 2.0 automatically saves the current configuration to `~/.config/pdf2zh/config.v3.toml` each time you click the translate button in the GUI. This configuration file will be loaded by default on the next startup.
> - The configuration files in the `default` directory are automatically generated by the program. You can copy them for modification, but please do not modify them directly.
> - Configuration files may include version numbers such as "v2", "v3", etc. These are **configuration file version numbers**, **not** the version number of pdf2zh itself.


<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:300 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_b12bc520  CHUNK TYPE: h_rule START_LINE:302 -->
---

<!-- CHUNK ID: chunk_870EBD0C  CHUNK TYPE: header START_LINE:304 -->
#### Skip clean

<!-- CHUNK ID: chunk_012D63A3  CHUNK TYPE: paragraph START_LINE:306 -->
When this parameter is set to True, the PDF cleaning step will be skipped, which can improve compatibility and avoid some font processing issues.

Usage:

<!-- CHUNK ID: chunk_56748FCD  CHUNK TYPE: code_block START_LINE:310 -->
```bash
pdf2zh_next example.pdf --skip-clean
```

<!-- CHUNK ID: chunk_1078AA87  CHUNK TYPE: paragraph START_LINE:314 -->
Or using environment variables:

<!-- CHUNK ID: chunk_C147F788  CHUNK TYPE: code_block START_LINE:316 -->
```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

<!-- CHUNK ID: chunk_E510ADDB  CHUNK TYPE: blockquote START_LINE:320 -->
> [!TIP]
> When `--enhance-compatibility` is enabled, Skip clean is automatically enabled.

<!-- CHUNK ID: h_rule_ff06cc0b  CHUNK TYPE: h_rule START_LINE:323 -->
---

<!-- CHUNK ID: chunk_A35603CF  CHUNK TYPE: header START_LINE:325 -->
#### Translation cache

<!-- CHUNK ID: chunk_F8D49E02  CHUNK TYPE: paragraph START_LINE:327 -->
PDFMathTranslate caches translated texts to increase speed and avoid unnecessary API calls for same contents. You can use `--ignore-cache` option to ignore translation cache and force retranslation.

<!-- CHUNK ID: chunk_D7B6C013  CHUNK TYPE: code_block START_LINE:329 -->
```bash
pdf2zh_next example.pdf --ignore-cache
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:333 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_f7a74231  CHUNK TYPE: h_rule START_LINE:335 -->
---

<!-- CHUNK ID: chunk_05080CDF  CHUNK TYPE: header START_LINE:337 -->
#### Deployment as a public services

<!-- CHUNK ID: chunk_A72BDF82  CHUNK TYPE: paragraph START_LINE:339 -->
When deploying a pdf2zh GUI on public services, you should modify the configuration file as described below.

<!-- CHUNK ID: chunk_41166DB8  CHUNK TYPE: blockquote START_LINE:341 -->
> [!WARNING]
>
> This project has not been professionally audited for security, and may contain security vulnerabilities. Please evaluate the risks and take necessary security measures before deploying on public networks.


> [!TIP]
> - When deploying publicly, both disable_gui_sensitive_input and disable_config_auto_save should be enabled.
> - Separate different available services with *English commas* <kbd>,</kbd> .

<!-- CHUNK ID: chunk_F2D0AEC1  CHUNK TYPE: paragraph START_LINE:350 -->
A usable configuration is as follows:

<!-- CHUNK ID: chunk_12A9803B  CHUNK TYPE: code_block START_LINE:352 -->
```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:362 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_fe5ed082  CHUNK TYPE: h_rule START_LINE:364 -->
---

<!-- CHUNK ID: chunk_E255AB78  CHUNK TYPE: header START_LINE:366 -->
#### Authentication and welcome page

<!-- CHUNK ID: chunk_1A5EEA9C  CHUNK TYPE: paragraph START_LINE:368 -->
When using Authentication and welcome page to specify which user to use Web UI and custom the login page:

example auth.txt
Each line contains two elements, username, and password, separated by a comma.

<!-- CHUNK ID: chunk_B865D3B8  CHUNK TYPE: code_block START_LINE:373 -->
```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

<!-- CHUNK ID: chunk_0CEA118C  CHUNK TYPE: paragraph START_LINE:381 -->
example welcome.html

<!-- CHUNK ID: chunk_0FC66A15  CHUNK TYPE: code_block START_LINE:383 -->
```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my simple HTML page.</p>
</body>
</html>
```

<!-- CHUNK ID: chunk_40E12FA3  CHUNK TYPE: blockquote START_LINE:396 -->
> [!NOTE]
> welcome page will work if only authentication file is not blank.
> If authentication file is blank, there will be no authentication. :)

<!-- CHUNK ID: chunk_F2D0AEC1  CHUNK TYPE: paragraph START_LINE:400 -->
A usable configuration is as follows:

<!-- CHUNK ID: chunk_39D7C203  CHUNK TYPE: code_block START_LINE:402 -->
```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:411 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_9463b830  CHUNK TYPE: h_rule START_LINE:413 -->
---

<!-- CHUNK ID: chunk_4A9C44BF  CHUNK TYPE: header START_LINE:415 -->
#### Glossary Support

<!-- CHUNK ID: chunk_65580DD5  CHUNK TYPE: paragraph START_LINE:417 -->
PDFMathTranslate supports the glossary table. The glossary tables file should be `csv` file.
There are three columns in file. Here is a demo glossary file:

<!-- CHUNK ID: chunk_2403CA4A  CHUNK TYPE: table START_LINE:420 -->
| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


<!-- CHUNK ID: chunk_598725B0  CHUNK TYPE: paragraph START_LINE:427 -->
For CLI user:
You can use multiple files for glossary. And different files should be split by `,`.

<!-- CHUNK ID: chunk_332A0BF8  CHUNK TYPE: code_block START_LINE:430 -->
```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

<!-- CHUNK ID: chunk_B3174CBC  CHUNK TYPE: paragraph START_LINE:434 -->
For WebUI user:

You can upload your own glossary file now. After you uploaded the file, you can check them by click their name and the content shows below.

[⬆️ Back to top](#toc)
