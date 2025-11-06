[**시작하기**](./getting-started.md) > **설치** > **WebUI** _(현재)_

---

### Webui 를 통해 PDFMathTranslate 사용하기

#### WebUI 페이지를 여는 방법:

WebUI 인터페이스를 여는 방법에는 여러 가지가 있습니다. **Windows**를 사용 중이라면 [이 문서](./INSTALLATION_winexe.md) 를 참조하세요.

1. Python 설치 (3.10 <= 버전 <= 3.12)

2. 패키지 설치:

3. 브라우저에서 사용 시작:

    ```bash
    pdf2zh_next --gui
    ```

4. 브라우저가 자동으로 시작되지 않은 경우 다음으로 이동:

    ```bash
    http://localhost:7860/
    ```

    PDF 파일을 창에 드롭하고 `Translate` 을 클릭하세요.

5. docker 로 PDFMathTranslate 를 배포하고 ollama 를 PDFMathTranslate 의 백엔드 LLM 으로 사용하는 경우 "Ollama host"에 다음을 입력해야 합니다:

   ```bash
   http://host.docker.internal:11434
   ```

<!-- <img src="./../../images/gui.gif" width="500"/> -->
<img src='./../../images/gui.gif' width="500"/>

### 환경 변수

소스 및 대상 언어를 환경 변수를 사용하여 설정할 수 있습니다:

- `PDF2ZH_LANG_FROM`: 소스 언어를 설정합니다. 기본값은 "English"입니다.
- `PDF2ZH_LANG_TO`: 대상 언어를 설정합니다. 기본값은 "Simplified Chinese"입니다.

## 미리보기

<img src="./../../images/before.png" width="500"/>
<img src="./../../images/after.png" width="500"/>

## 유지 관리

[Rongxin](https://github.com/reycn) 이 유지 관리하는 GUI

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>