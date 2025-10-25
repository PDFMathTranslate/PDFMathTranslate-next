[**Начало работы**](./getting-started.md) > **Установка** > **WebUI** _(текущая)_

---

### Использование PDFMathTranslate через Webui

#### Как открыть страницу WebUI:

Существует несколько способов открытия интерфейса WebUI. Если вы используете **Windows**, обратитесь к [этой статье](./INSTALLATION_winexe.md);

1. Установленный Python (версия от 3.10 до 3.12)

2. Установите наш пакет:

3. Начните использование в браузере:

    ```bash
    pdf2zh_next --gui
    ```

4. Если ваш браузер не запустился автоматически, перейдите по адресу:

    ```bash
    http://localhost:7860/
    ```

    Перетащите `PDF` файл в окно и нажмите `Translate`.

5. Если вы развертываете PDFMathTranslate с помощью docker и используете ollama в качестве бэкенд LLM для PDFMathTranslate, вам следует указать "Ollama host" как:

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### Переменные среды

Вы можете установить исходный и целевой языки с помощью переменных среды:

- `PDF2ZH_LANG_FROM`: Устанавливает исходный язык. По умолчанию "English".
- `PDF2ZH_LANG_TO`: Устанавливает целевой язык. По умолчанию "Simplified Chinese".

## Предпросмотр

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## Обслуживание

GUI поддерживается [Rongxin](https://github.com/reycn)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>