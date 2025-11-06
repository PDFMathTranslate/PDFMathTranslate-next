<!-- CHUNK ID: chunk_F3B96F2D  CHUNK TYPE: paragraph START_LINE:1 -->
[**Getting Started**](./getting-started.md) > **Installation** > **Docker** _(current)_

<!-- CHUNK ID: h_rule_d44cb6ef  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_3EBE8361  CHUNK TYPE: header START_LINE:5 -->
### Install PDFMathTranslate via docker

<!-- CHUNK ID: chunk_760A6888  CHUNK TYPE: header START_LINE:7 -->
#### What is docker?

<!-- CHUNK ID: chunk_41775DAE  CHUNK TYPE: paragraph START_LINE:9 -->
[Docker](https://docs.docker.com/get-started/docker-overview/) is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production.

<!-- CHUNK ID: chunk_6EBC627B  CHUNK TYPE: header START_LINE:11 -->
#### Installation

<!-- CHUNK ID: chunk_BA8550C2  CHUNK TYPE: paragraph START_LINE:13 -->
<h4>1. Pull and run:</h4>

<!-- CHUNK ID: chunk_D49885F5  CHUNK TYPE: code_block START_LINE:15 -->
```bash
docker pull awwaawwa/pdfmathtranslate-next
docker run -d -p 7860:7860 awwaawwa/pdfmathtranslate-next
```

<!-- CHUNK ID: chunk_B1F3E7B5  CHUNK TYPE: blockquote START_LINE:20 -->
> [!NOTE]
> 
> - If you cannot access Docker Hub, please try the image on [GitHub Container Registry](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pkgs/container/pdfmathtranslate).
> 
> ```bash
> docker pull ghcr.io/PDFMathTranslate/PDFMathTranslate-next
> docker run -d -p 7860:7860 ghcr.io/PDFMathTranslate/PDFMathTranslate-next
> ```

<!-- CHUNK ID: chunk_0222B95B  CHUNK TYPE: paragraph START_LINE:29 -->
<h4>2. Enter this URL in your default browser to open the WebUI page:</h4>

<!-- CHUNK ID: chunk_29F610F5  CHUNK TYPE: code_block START_LINE:31 -->
```
http://localhost:7860/
```

<!-- CHUNK ID: chunk_B5C49A1E  CHUNK TYPE: blockquote START_LINE:35 -->
> [!NOTE]
> If you encounter any issues during use WebUI, please refer to [Usage --> WebUI](./USAGE_webui.md).

> [!NOTE]
> If you encounter any issues during use command line, please refer to [Usage --> Command Line](./USAGE_commandline.md).
<!-- CHUNK ID: chunk_0B40829E  CHUNK TYPE: html_comment START_LINE:40 -->
<!-- 
#### For docker deployment on cloud service:

<div>
<a href="https://www.heroku.com/deploy?template=https://github.com/PDFMathTranslate/PDFMathTranslate-next">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" height="26"></a>
<a href="https://render.com/deploy">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Koyeb" height="26"></a>
<a href="https://zeabur.com/templates/5FQIGX?referralCode=reycn">
  <img src="https://zeabur.com/button.svg" alt="Deploy on Zeabur" height="26"></a>
<a href="https://app.koyeb.com/deploy?type=git&builder=buildpack&repository=github.com/PDFMathTranslate/PDFMathTranslate-next&branch=main&name=pdf-math-translate">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb" height="26"></a>
</div>

-->