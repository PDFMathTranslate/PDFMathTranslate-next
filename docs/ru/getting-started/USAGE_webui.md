[**Начало работы**](./getting-started.md) > **Установка** > **WebUI** _(current)_

---

### Использование PDFMathTranslate через Webui

#### Как открыть страницу WebUI:

Есть несколько способов открыть интерфейс WebUI. Если вы используете **Windows**, обратитесь к [этой статье](./INSTALLATION_winexe.md);

1. Установленный Python (версия от 3.10 до 3.12)

2. Установите наш пакет:

3. Начните использование в браузере:

    ```bash
    pdf2zh_next --gui
    ```

4. Если ваш браузер не запустился автоматически, перейдите по адресу

    ```bash
    http://localhost:7860/
    ```

    Перетащите PDF-файл в окно и нажмите `Translate`.

<!-- <img src="./images/gui.gif" width="500"/> -->
<img src='./../images/gui.gif' width="500"/>

### Переменные среды

Вы можете установить исходный и целевой языки с помощью переменных среды:

- `PDF2ZH_LANG_FROM`: Устанавливает исходный язык. По умолчанию "English".
- `PDF2ZH_LANG_TO`: Устанавливает целевой язык. По умолчанию "Simplified Chinese".

## Предпросмотр

<img src="./../images/before.png" width="500"/>
<img src="./../images/after.png" width="500"/>

## Поддержка

GUI поддерживается [Rongxin](https://github.com/reycn)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>