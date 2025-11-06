[**Começar**](./getting-started.md) > **Instalação** > **WebUI** _(atual)_

---

### Usar PDFMathTranslate via Webui

#### Como abrir a página WebUI:

Existem vários métodos para abrir a interface WebUI. Se você estiver usando **Windows**, consulte [este artigo](./INSTALLATION_winexe.md);

1. Python instalado (versão entre 3.10 e 3.12)

2. Instale nosso pacote:

3. Comece a usar no navegador:

    ```bash
    pdf2zh_next --gui
    ```

4. Se o seu navegador não foi iniciado automaticamente, acesse

    ```bash
    http://localhost:7860/
    ```

    Arraste o arquivo PDF para a janela e clique em `Translate`.

5. Se você implantar o PDFMathTranslate com docker e estiver usando o ollama como o LLM de backend do PDFMathTranslate, você deve preencher "Ollama host" com

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### Variáveis de Ambiente

Você pode definir os idiomas de origem e destino usando variáveis de ambiente:

- `PDF2ZH_LANG_FROM`: Define o idioma de origem. O padrão é "English".
- `PDF2ZH_LANG_TO`: Define o idioma de destino. O padrão é "Simplified Chinese".

## Visualização

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## Manutenção

GUI mantido por [Rongxin](https://github.com/reycn)

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>