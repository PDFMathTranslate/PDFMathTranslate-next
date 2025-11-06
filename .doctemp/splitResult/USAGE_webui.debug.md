<!-- CHUNK ID: chunk_03FD0E12  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Installation** > **WebUI** _(current)_

<!-- CHUNK ID: h_rule_cd8270c0  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_EDC72645  CHUNK TYPE: header START_LINE:5 -->
### Use PDFMathTranslate via Webui

<!-- CHUNK ID: chunk_D75BD342  CHUNK TYPE: header START_LINE:7 -->
#### How to open the WebUI page:

<!-- CHUNK ID: chunk_65E65B28  CHUNK TYPE: paragraph START_LINE:9 -->
There are several methods to open the WebUI interface. If you are using **Windows**, please refer to [this article](./INSTALLATION_winexe.md);

<!-- CHUNK ID: chunk_3B3548CA  CHUNK TYPE: list START_LINE:11 -->
1. Python installed (3.10 <= version <= 3.12)

2. Install our package:

3. Start using in browser:

    ```bash
    pdf2zh_next --gui
    ```

4. If your browswer has not been started automatically, goto

    ```bash
    http://localhost:7860/
    ```

    Drop the PDF file into the window and click `Translate`.

5. If you deploy PDFMathTranslate with docker, and you are using ollama as PDFMathTranslate's backend LLM, you should fill "Ollama host" with

   ```bash
   http://host.docker.internal:11434
   ```

<!-- CHUNK ID: chunk_F5A7DD64  CHUNK TYPE: html_comment START_LINE:35 -->
<!-- <img src="./images/gui.gif" width="500"/> -->
<!-- CHUNK ID: chunk_B79CAF04  CHUNK TYPE: image START_LINE:36 -->
<img src='./../../images/gui.gif' width="500"/>

<!-- CHUNK ID: chunk_2FDC0409  CHUNK TYPE: header START_LINE:38 -->
### Environment Variables

<!-- CHUNK ID: chunk_7865A8EB  CHUNK TYPE: paragraph START_LINE:40 -->
You can set the source and target languages using environment variables:

<!-- CHUNK ID: chunk_104D91B6  CHUNK TYPE: list START_LINE:42 -->
- `PDF2ZH_LANG_FROM`: Sets the source language. Defaults to "English".
- `PDF2ZH_LANG_TO`: Sets the target language. Defaults to "Simplified Chinese".

<!-- CHUNK ID: chunk_EEBEC547  CHUNK TYPE: header START_LINE:45 -->
## Preview

<!-- CHUNK ID: chunk_433E69C5  CHUNK TYPE: image START_LINE:47 -->
<img src="./../../images/before.png" width="500"/>
<!-- CHUNK ID: chunk_64A11402  CHUNK TYPE: image START_LINE:48 -->
<img src="./../../images/after.png" width="500"/>

<!-- CHUNK ID: chunk_742C5FE6  CHUNK TYPE: header START_LINE:50 -->
## Maintainance

<!-- CHUNK ID: chunk_7E834869  CHUNK TYPE: paragraph START_LINE:52 -->
GUI maintained by [Rongxin](https://github.com/reycn)
