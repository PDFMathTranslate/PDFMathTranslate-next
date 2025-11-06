请你出一个设计稿/调研。核心是给本项目提供 http API.

### 要求

1. 不可以有 `redis` 等第三方独立服务依赖。可以 import 包；

2. `fastapi` 实现 http api；

3. 直接传递 `SettingsModel` 来配置参数；

4. 通过 http post body 来上传要处理的目标 pdf；

5. https://github.com/gradio-app/gradio/issues/1608#issuecomment-1247038215 使用类似的方法，在 GUI 启动时自动启动对应的 API 服务。以下是其详细内容：

    Hi @sciai-ai I took a dive into FastAPI and it turns out that it is actually possible to serve your Gradio app within another FastAPI app quite easily using FastAPI's mount() method. Here's a little demo I put together: 

    ```python

    """
    How to launch your Gradio app within another FastAPI app. 

    Run this from the terminal as you would normally start a FastAPI app: `uvicorn run:app`
    and navigate to http://localhost:8000/gradio in your browser to see the Gradio app.
    """
    from fastapi import FastAPI
    import gradio as gr

    CUSTOM_PATH = "/gradio"

    app = FastAPI()

    @app.get("/")
    def read_main():
        return {"message": "This is your main app"}

    io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
    gradio_app = gr.routes.App.create_app(io)

    app.mount(CUSTOM_PATH, gradio_app)

    ```

    This serves the main app on `localhost:8000`, which could be an API endpoint, and it serves the Gradio app on `http://localhost:8000/gradio` and allows you to create a Gradio app within another FastAPI app. This should allow you to do what you're looking for, so I'll go ahead and (finally!) close this issue. If not, feel free to reopen with more details.

6. 提供一个简易队列功能，允许排队。

### 需要提供的 API

1. 使用 `Settingsmodel` + 上传 PDF 来创建任务，并返回任务 id。任务 id 使用 `pdf2zh_next.4位随机16进制.uuid` 格式。其中 "pdf2zh_next"固定前缀，`uuid` 是随机生成的一个 `uuid`。例如：`pdf2zh_next.3E87.uuid`；

2. 仅上传 PDF，使用**默认配置**创建任务；

    **默认配置**指 `gui.py` 第 214 行：    
    
    ```python
    settings = config_manager.initialize_cli_config()
    ```

3. 使用任务 ID 查询任务；

4. 下载结果文件；

5. 取消任务。

- 任务信息仅保存在内存中。重启后原先所有任务丢失，原有任务 id 失效。

- 内存中最多允许排队 `10` 个任务，超出则报错。(排队任务数可在配置中修改)

- 内存中最多保存最新的 `1000` 个任务的进度信息，超出的自动删除。（先进先出）(保存任务数可在配置中修改)


- 使用 GUI 进行的翻译也要归到这个队列里。