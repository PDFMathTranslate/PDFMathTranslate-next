[**Iniziare**](./getting-started.md) > **Installazione** > **WebUI** _(current)_

---

### Utilizzo di PDFMathTranslate tramite Webui

#### Come aprire la pagina WebUI:

Esistono diversi metodi per aprire l'interfaccia WebUI. Se stai utilizzando **Windows**, consulta [questo articolo](./INSTALLATION_winexe.md);

1. Python installato (versione 3.10 <= versione <= 3.12)

2. Installa il nostro pacchetto:

3. Inizia a utilizzare nel browser:

    ```bash
    pdf2zh_next --gui
    ```

4. Se il tuo browser non si è avviato automaticamente, vai a

    ```bash
    http://localhost:7860/
    ```

    Trascina il file PDF nella finestra e clicca `Translate`.

5. Se distribuisci PDFMathTranslate con docker e stai utilizzando ollama come backend LLM di PDFMathTranslate, dovresti inserire "Ollama host" con

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### Variabili d'ambiente

Puoi impostare le lingue di origine e di destinazione utilizzando le variabili d'ambiente:

- `PDF2ZH_LANG_FROM`: Imposta la lingua di origine. Il valore predefinito è "English".
- `PDF2ZH_LANG_TO`: Imposta la lingua di destinazione. Il valore predefinito è "Simplified Chinese".

## Anteprima

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## Manutenzione

GUI mantenuta da [Rongxin](https://github.com/reycn)

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>