<!-- CHUNK ID: chunk_03FD0E12  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Installation** > **WebUI** _(current)_

<!-- CHUNK ID: h_rule_b8e7019d  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_EDC72645  CHUNK TYPE: header START_LINE:5 -->
### Use PDFMathTranslate via Webui

<!-- CHUNK ID: chunk_D75BD342  CHUNK TYPE: header START_LINE:7 -->
#### How to open the WebUI page:

<!-- CHUNK ID: chunk_65E65B28  CHUNK TYPE: paragraph START_LINE:9 -->
There are several methods to open the WebUI interface. If you are using **Windows**, please refer to [this article](./INSTALLATION_winexe.md);

<!-- CHUNK ID: chunk_2A12C8AD  CHUNK TYPE: list START_LINE:11 -->
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

<!-- CHUNK ID: chunk_F5A7DD64  CHUNK TYPE: html_comment START_LINE:29 -->
<!-- <img src="./images/gui.gif" width="500"/> -->
<!-- CHUNK ID: chunk_FFA0F1F7  CHUNK TYPE: image START_LINE:30 -->
<img src='./../images/gui.gif' width="500"/>

<!-- CHUNK ID: chunk_2FDC0409  CHUNK TYPE: header START_LINE:32 -->
### Environment Variables

<!-- CHUNK ID: chunk_7865A8EB  CHUNK TYPE: paragraph START_LINE:34 -->
You can set the source and target languages using environment variables:

<!-- CHUNK ID: chunk_104D91B6  CHUNK TYPE: list START_LINE:36 -->
- `PDF2ZH_LANG_FROM`: Sets the source language. Defaults to "English".
- `PDF2ZH_LANG_TO`: Sets the target language. Defaults to "Simplified Chinese".

<!-- CHUNK ID: chunk_EEBEC547  CHUNK TYPE: header START_LINE:39 -->
## Preview

<!-- CHUNK ID: chunk_D7787657  CHUNK TYPE: image START_LINE:41 -->
<img src="./../images/before.png" width="500"/>
<!-- CHUNK ID: chunk_4685028B  CHUNK TYPE: image START_LINE:42 -->
<img src="./../images/after.png" width="500"/>

<!-- CHUNK ID: chunk_742C5FE6  CHUNK TYPE: header START_LINE:44 -->
## Maintainance

<!-- CHUNK ID: chunk_3D5EA421  CHUNK TYPE: paragraph START_LINE:46 -->
GUI maintained by [Rongxin](https://github.com/reycn)