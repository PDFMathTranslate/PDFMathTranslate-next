[**开始使用**](./getting-started.md) > **如何安装** > **WebUI** _(当前)_

---

### 通过 Webui 使用 PDFMathTranslate

#### 如何打开 WebUI 页面：

有多种方法可以打开 WebUI 界面。如果您使用的是 **Windows**，请参考 [这篇文章](./INSTALLATION_winexe.md)；

1. 已安装 Python（3.10 <= 版本 <= 3.12）

2. 安装我们的软件包：

3. 在浏览器中开始使用：

    ```bash
    pdf2zh_next --gui
    ```

4. 如果浏览器未自动启动，请访问

    ```bash
    http://localhost:7860/
    ```

    将 `PDF` 文件拖入窗口并点击 `Translate`。

5. 如果您通过 docker 部署 PDFMathTranslate，并使用 ollama 作为 PDFMathTranslate 的后端 `LLM`，则应在 "Ollama host" 中填写

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### 环境变量

您可以通过环境变量设置源语言和目标语言：

- `PDF2ZH_LANG_FROM`: 设置源语言。默认为 "English"。
- `PDF2ZH_LANG_TO`: 设置目标语言。默认为 "Simplified Chinese"。

## 预览

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## 维护

由 [Rongxin](https://github.com/reycn) 维护的 GUI

<div align="right"> 
<h6><small>本页面的部分内容由 GPT 翻译，可能包含错误。</small></h6>