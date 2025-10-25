<!-- CHUNK ID: chunk_F2495A85  CHUNK TYPE: blockquote START_LINE:1 -->
> [!CAUTION]
>
> This document is outdated, please do not refer to it.

<!-- CHUNK ID: chunk_3CA8722C  CHUNK TYPE: paragraph START_LINE:5 -->
<h2 id="toc">Table of Content</h2>
The present project supports two types of APIs, All methods need the Redis;

<!-- CHUNK ID: chunk_AE8C8A31  CHUNK TYPE: list START_LINE:8 -->
- [Functional calls in Python](#api-python)
- [HTTP protocols](#api-http)

<!-- CHUNK ID: h_rule_d89cf333  CHUNK TYPE: h_rule START_LINE:11 -->
---

<!-- CHUNK ID: chunk_1C2FD3FE  CHUNK TYPE: paragraph START_LINE:13 -->
<h2 id="api-python">Python</h2>

As `pdf2zh` is an installed module in Python, we expose two methods for other programs to call in any Python scripts.

For example, if you want translate a document from English to Chinese using Google Translate, you may use the following code:

<!-- CHUNK ID: chunk_7A13B606  CHUNK TYPE: code_block START_LINE:19 -->
```python
from pdf2zh_next import translate, translate_stream

params = {
    'lang_in': 'en',
    'lang_out': 'zh',
    'service': 'google',
    'thread': 4,
}
```
<!-- CHUNK ID: chunk_2DB09B71  CHUNK TYPE: paragraph START_LINE:29 -->
Translate with files:
<!-- CHUNK ID: chunk_1F8B4E30  CHUNK TYPE: code_block START_LINE:30 -->
```python
(file_mono, file_dual) = translate(files=['example.pdf'], **params)[0]
```
<!-- CHUNK ID: chunk_8C07F04C  CHUNK TYPE: paragraph START_LINE:33 -->
Translate with stream:
<!-- CHUNK ID: chunk_258306A3  CHUNK TYPE: code_block START_LINE:34 -->
```python
with open('example.pdf', 'rb') as f:
    (stream_mono, stream_dual) = translate_stream(stream=f.read(), **params)
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:39 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_712718ea  CHUNK TYPE: h_rule START_LINE:41 -->
---

<!-- CHUNK ID: chunk_F96246D5  CHUNK TYPE: paragraph START_LINE:43 -->
<h2 id="api-http">HTTP</h2>

In a more flexible way, you can communicate with the program using HTTP protocols, if:

<!-- CHUNK ID: chunk_5C9E9558  CHUNK TYPE: list START_LINE:47 -->
1. Install and run backend

   ```bash
   pip install pdf2zh_next[backend]
   pdf2zh_next --flask
   pdf2zh_next --celery worker
   ```

2. Using HTTP protocols as follows:

   - Submit translate task

     ```bash
     curl http://localhost:11008/v1/translate -F "file=@example.pdf" -F "data={\"lang_in\":\"en\",\"lang_out\":\"zh\",\"service\":\"google\",\"thread\":4}"
     {"id":"d9894125-2f4e-45ea-9d93-1a9068d2045a"}
     ```

   - Check Progress

     ```bash
     curl http://localhost:11008/v1/translate/d9894125-2f4e-45ea-9d93-1a9068d2045a
     {"info":{"n":13,"total":506},"state":"PROGRESS"}
     ```

   - Check Progress _(if finished)_

     ```bash
     curl http://localhost:11008/v1/translate/d9894125-2f4e-45ea-9d93-1a9068d2045a
     {"state":"SUCCESS"}
     ```

   - Save monolingual file

     ```bash
     curl http://localhost:11008/v1/translate/d9894125-2f4e-45ea-9d93-1a9068d2045a/mono --output example-mono.pdf
     ```

   - Save bilingual file

     ```bash
     curl http://localhost:11008/v1/translate/d9894125-2f4e-45ea-9d93-1a9068d2045a/dual --output example-dual.pdf
     ```

   - Interrupt if running and delete the task
     ```bash
     curl http://localhost:11008/v1/translate/d9894125-2f4e-45ea-9d93-1a9068d2045a -X DELETE
     ```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:95 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_9dcfa49f  CHUNK TYPE: h_rule START_LINE:97 -->
---
