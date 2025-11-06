<!-- CHUNK ID: chunk_1C59CC51  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Usage** > **Command Line** _(current)_

<!-- CHUNK ID: h_rule_4a861785  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_9C810511  CHUNK TYPE: header START_LINE:5 -->
### Use PDFMathTranslate via command line

<!-- CHUNK ID: chunk_30052F3A  CHUNK TYPE: header START_LINE:7 -->
#### Basic Usage

<!-- CHUNK ID: chunk_ACC119CF  CHUNK TYPE: paragraph START_LINE:9 -->
After Installation, please enter this command to translate your PDF.

<!-- CHUNK ID: chunk_0D415785  CHUNK TYPE: code_block START_LINE:11 -->
```bash
pdf2zh_next document.pdf
```

<!-- CHUNK ID: chunk_744BFC94  CHUNK TYPE: blockquote START_LINE:15 -->
> [!NOTE]
> 
> If your pathname contains spaces, please enclose it in quotation marks.
> 
> ```bash
> pdf2zh_next "path with spaces/document.pdf"
> ```

<!-- CHUNK ID: chunk_6375D505  CHUNK TYPE: paragraph START_LINE:23 -->
After execute translation, files generated in **current working directory**.

<!-- CHUNK ID: chunk_1E0F4B41  CHUNK TYPE: blockquote START_LINE:25 -->
> [!TIP]
> **Where is my "Current Working Directory" ?**
> Before entering a command in the terminal, you might see a pathname displayed in your terminal:
> 
> ```powershell
> PS C:\Users\XXX>
> ```
> 
> This directory is the "*Current working directory*."
> 
> If there is no pathname, try running this command in the terminal:
> 
> ```bash
> pwd
> ```
> 
> After executing this command, a pathname will be output. This pathname is the "**Current working directory**". The translated files will appear here.

<!-- CHUNK ID: h_rule_487433fb  CHUNK TYPE: h_rule START_LINE:43 -->
---

<!-- CHUNK ID: chunk_67DBD505  CHUNK TYPE: header START_LINE:45 -->
#### Advance Usage

<!-- CHUNK ID: chunk_98AF19D9  CHUNK TYPE: paragraph START_LINE:47 -->
For detailed explanations of additional command line parameters, please refer to [advanced usage](./../advanced/advanced.md).
