[**Начало работы**](./getting-started.md) > **Установка** > **uv** _(current)_

---

### Установка PDFMathTranslate через uv

#### Что такое uv? Как его установить?

uv — это чрезвычайно быстрый менеджер пакетов и проектов Python, написанный на Rust.
<br>
Чтобы установить uv на ваш компьютер, обратитесь к [этой статье](https://docs.astral.sh/uv/getting-started/installation/).

---

#### Установка

1. Установленный Python (версия от 3.10 до 3.12);

2. Используйте следующую команду для работы с нашим пакетом:

    ```bash
    pip install uv
    uv tool install --python 3.12 pdf2zh-next
    ```

После установки вы можете начать перевод через **командную строку** или **WebUI**.

!!! Warning

    Если при запуске вы видите ошибку `command not found: pdf2zh_next`, настройте переменные среды следующим образом и попробуйте снова:

    === "macOS и Linux"

        Добавьте следующее в ваш ~/.zshrc:

        ```console
        export PATH="$PATH:/Users/Username/.local/bin"
        ```

        Затем перезапустите терминал

    === "Windows"

        Введите следующее в PowerShell:

        ```powershell
        $env:Path = "C:\Users\Username\.local\bin;$env:Path"
        ```

        Затем перезапустите терминал

> [!NOTE]
> Если у вас возникли проблемы при использовании WebUI, обратитесь к разделу [Использование --> WebUI](./USAGE_webui.md).

> [!NOTE]
> Если у вас возникли проблемы при использовании командной строки, обратитесь к разделу [Использование --> Командная строка](./USAGE_commandline.md).

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>