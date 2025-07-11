[**Начало работы**](./начало-работы.md) > **Использование** > **Командная строка** _(current)_

---

### Использование PDFMathTranslate через командную строку

#### Основное использование

После установки введите эту команду для перевода вашего PDF.

```bash
pdf2zh_next document.pdf
```

> [!NOTE]
> 
> Если путь содержит пробелы, заключите его в кавычки.
> 
> ```bash
> pdf2zh_next "path with spaces/document.pdf"
> ```

После выполнения перевода файлы создаются в **текущей рабочей директории**.

> [!TIP]
> **Где находится моя "Текущая рабочая директория"?**
> Перед вводом команды в терминале вы можете увидеть путь, отображаемый в вашем терминале:
> 
> ```powershell
> PS C:\Users\XXX>
> ```
> 
> Эта директория является "*Текущей рабочей директорией*."
> 
> Если путь не отображается, попробуйте выполнить эту команду в терминале:
> 
> ```bash
> pwd
> ```
> 
> После выполнения этой команды будет выведен путь. Этот путь является "**Текущей рабочей директорией**". Переведенные файлы будут появляться здесь.

---

#### Расширенные параметры

Для подробного объяснения дополнительных параметров командной строки обратитесь к [расширенным параметрам](./../advanced/advanced.md).

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>