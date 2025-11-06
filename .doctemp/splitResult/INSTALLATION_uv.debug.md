<!-- CHUNK ID: chunk_23005398  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Installation** > **uv** _(current)_

<!-- CHUNK ID: h_rule_db71edfa  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_D43EE31C  CHUNK TYPE: header START_LINE:5 -->
### Install PDFMathTranslate via uv

<!-- CHUNK ID: chunk_1BF9C99B  CHUNK TYPE: header START_LINE:7 -->
#### What is uv? How to install it?

<!-- CHUNK ID: chunk_8963BEA0  CHUNK TYPE: paragraph START_LINE:9 -->
uv is an extremely fast Python package and project manager, written in Rust.
<br>
To install uv on your computer, please refer to [this article](https://docs.astral.sh/uv/getting-started/installation/).

<!-- CHUNK ID: h_rule_a20d0d6e  CHUNK TYPE: h_rule START_LINE:13 -->
---

<!-- CHUNK ID: chunk_6EBC627B  CHUNK TYPE: header START_LINE:15 -->
#### Installation

<!-- CHUNK ID: chunk_05BD0E93  CHUNK TYPE: list START_LINE:17 -->
1. Python installed (3.10 <= version <= 3.12);

2. Use the following command to use our package:

    ```bash
    pip install uv
    uv tool install --python 3.12 pdf2zh-next
    ```

<!-- CHUNK ID: chunk_74F9EC5E  CHUNK TYPE: paragraph START_LINE:26 -->
After installation, you can start translation via the **command line** or **WebUI**.

<!-- CHUNK ID: chunk_747DC3A8  CHUNK TYPE: callout_mkdocs START_LINE:28 -->
!!! Warning

    If you see the error `command not found: pdf2zh_next` when running, please configure the environment variables as follows and try again:

    === "macOS and Linux"

        Add the following to your ~/.zshrc:

        ```console
        export PATH="$PATH:/Users/Username/.local/bin"
        ```

        Then restart your terminal

    === "Windows"

        Enter the following in PowerShell:

        ```powershell
        $env:Path = "C:\Users\Username\.local\bin;$env:Path"
        ```

        Then restart your terminal

<!-- CHUNK ID: chunk_C86DFF6A  CHUNK TYPE: blockquote START_LINE:52 -->
> [!NOTE]
> If you encounter any issues during use WebUI, please refer to [Usage --> WebUI](./USAGE_webui.md).

> [!NOTE]
> If you encounter any issues during use command line, please refer to [Usage --> Command Line](./USAGE_commandline.md).
