[**Commencer**](./getting-started.md) > **Installation** > **WebUI** _(current)_

---

### Utiliser PDFMathTranslate via Webui

#### Comment ouvrir la page WebUI :

Il existe plusieurs méthodes pour ouvrir l'interface WebUI. Si vous utilisez **Windows**, veuillez consulter [cet article](./INSTALLATION_winexe.md);

1. Python installé (version 3.10 <= version <= 3.12)

2. Installez notre package :

3. Commencez à utiliser dans le navigateur :

    ```bash
    pdf2zh_next --gui
    ```

4. Si votre navigateur ne s'est pas lancé automatiquement, allez à

    ```bash
    http://localhost:7860/
    ```

    Déposez le fichier PDF dans la fenêtre et cliquez sur `Translate`.

5. Si vous déployez PDFMathTranslate avec docker, et que vous utilisez ollama comme backend LLM de PDFMathTranslate, vous devez remplir "Ollama host" avec

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### Variables d'environnement

Vous pouvez définir les langues source et cible en utilisant des variables d'environnement :

- `PDF2ZH_LANG_FROM`: Définit la langue source. Par défaut, "English".
- `PDF2ZH_LANG_TO`: Définit la langue cible. Par défaut, "Simplified Chinese".

## Aperçu

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## Maintenance

GUI maintenu par [Rongxin](https://github.com/reycn)

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>