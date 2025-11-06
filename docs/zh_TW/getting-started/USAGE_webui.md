[**開始使用**](./getting-started.md) > **如何安裝** > **WebUI** _(current)_

---

### 透過 Webui 使用 PDFMathTranslate

#### 如何開啟 WebUI 頁面：

有幾種方法可以開啟 WebUI 介面。如果您使用的是 **Windows**，請參考 [這篇文章](./INSTALLATION_winexe.md)；

1. 已安裝 Python（3.10 <= 版本 <= 3.12）

2. 安裝我們的套件：

3. 在瀏覽器中開始使用：

    ```bash
    pdf2zh_next --gui
    ```

4. 如果瀏覽器未自動啟動，請前往

    ```bash
    http://localhost:7860/
    ```

    將 `PDF` 文件拖入視窗並點擊 `Translate`。

5. 如果您使用 docker 部署 PDFMathTranslate，且使用 ollama 作為 PDFMathTranslate 的後端 LLM，應在「Ollama host」欄位填入

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### 環境變數

您可以使用環境變數來設定來源語言與目標語言：

- `PDF2ZH_LANG_FROM`: 設定來源語言。預設為「English」。
- `PDF2ZH_LANG_TO`: 設定目標語言。預設為「Simplified Chinese」。

## 預覽

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## 維護

由 [Rongxin](https://github.com/reycn) 維護的 GUI

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>