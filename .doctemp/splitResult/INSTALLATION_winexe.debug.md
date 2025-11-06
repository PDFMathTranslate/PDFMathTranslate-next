<!-- CHUNK ID: chunk_E5616440  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Installation** > **Windows EXE** _(current)_

<!-- CHUNK ID: h_rule_192aec21  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_F372470F  CHUNK TYPE: header START_LINE:5 -->
### Install PDFMathTranslate via .exe file

<!-- CHUNK ID: chunk_D3A98932  CHUNK TYPE: table START_LINE:7 -->
***Step 1*** | Download `pdf2zh-<version>-with-assets-win64.zip` from [release page](https://github.com/PDFMathTranslate/PDFMathTranslate-next/releases).

<!-- CHUNK ID: chunk_29FE8C1D  CHUNK TYPE: blockquote START_LINE:9 -->
> [!TIP]
> **What is the difference between `pdf2zh-<version>-with-assets-win64.zip` and `pdf2zh-<version>-win64.zip`?**
>
> - If you are downloading and using PDFMathTranslate for the first time, it is recommended to download `pdf2zh-<version>-with-assets-win64.zip`.
> - The `pdf2zh-<version>-with-assets-win64.zip` includes resource files (such as fonts and models) compared to `pdf2zh-<version>-win64.zip`.
> - The version without assets will also dynamically download resources when running, but the download may fail due to network issues.

<!-- CHUNK ID: chunk_17427D5A  CHUNK TYPE: table START_LINE:16 -->
***Step 2*** | Unzip `pdf2zh-<version>-with-assets-win64.zip` and navigate `pdf2zh` folder. It takes a while to decompress, please be patient.

***Step 3*** | Navigate `pdf2zh` folder, then Double-click `pdf2zh.exe`.

<!-- CHUNK ID: chunk_B4068DB4  CHUNK TYPE: blockquote START_LINE:20 -->
> [!TIP]
> **Cannot run the .exe file**
>
> If you have some problems running pdf2zh.exe, please install `https://aka.ms/vs/17/release/vc_redist.x64.exe` and try again.

<!-- CHUNK ID: chunk_68C037E0  CHUNK TYPE: table START_LINE:25 -->
***Step 4*** | A terminal will pop up after double-clicking the exe file. After about half a minute to a minute, a webpage will open in your default browser. If it does not happen, you can try to manually access `http://localhost:7860/`.

<!-- CHUNK ID: chunk_E9C46195  CHUNK TYPE: blockquote START_LINE:27 -->
> [!NOTE]
>
> If you encounter any issues during use WebUI, please refer to [this webpage](./USAGE_webui.md).

<!-- CHUNK ID: chunk_703B946D  CHUNK TYPE: table START_LINE:31 -->
***Step 5*** | Enjoy!

<!-- CHUNK ID: chunk_BF8657F3  CHUNK TYPE: blockquote START_LINE:33 -->
> [!TIP]
> **You can use the .exe file via command line**
>
> Use the .exe file through command line as follows:
>
> - Launch your terminal and navigate to the folder containing the .exe file:
>
> ```bash
> cd /path/pdf2zh_next/build
> ```
>
> - Call the .exe file:
>
> ```bash
> ./pdf2zh_next.exe "document.pdf"
> ```
>
> You can use other command line parameters as normal:
>
> ```bash
> ./pdf2zh_next.exe "document.pdf" --lang-in en --lang-out ja
> ```
>
> If you need more information about command line usage, please refer to this article.
