[**Erste Schritte**](./getting-started.md) > **Installation** > **WebUI** _(aktuell)_

---

### Verwendung von PDFMathTranslate über Webui

#### So öffnen Sie die WebUI-Seite:

Es gibt mehrere Methoden, um die WebUI-Oberfläche zu öffnen. Wenn Sie **Windows** verwenden, lesen Sie bitte [diesen Artikel](./INSTALLATION_winexe.md);

1. Python installiert (3.10 <= Version <= 3.12)

2. Installieren Sie unser Paket:

3. Beginnen Sie mit der Verwendung im Browser:

    ```bash
    pdf2zh_next --gui
    ```

4. Falls Ihr Browser nicht automatisch gestartet wurde, gehen Sie zu

    ```bash
    http://localhost:7860/
    ```

    Ziehen Sie die PDF-Datei in das Fenster und klicken Sie auf `Translate`.

5. Wenn Sie PDFMathTranslate mit Docker bereitstellen und ollama als Backend-LLM für PDFMathTranslate verwenden, sollten Sie "Ollama host" mit folgendem Wert ausfüllen:

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### Umgebungsvariablen

Sie können die Quell- und Zielsprachen mit Umgebungsvariablen festlegen:

- `PDF2ZH_LANG_FROM`: Legt die Ausgangssprache fest. Standardmäßig "English".
- `PDF2ZH_LANG_TO`: Legt die Zielsprache fest. Standardmäßig "Simplified Chinese".

## Vorschau

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## Wartung

GUI wird von [Rongxin](https://github.com/reycn) gepflegt

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>