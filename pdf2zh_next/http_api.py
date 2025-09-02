from fastapi import FastAPI, Response, UploadFile, File, Form, HTTPException
from celery import Celery, Task
from pdf2zh_next.config.model import SettingsModel
from pdf2zh_next.high_level import do_translate_async_stream
import tempfile, asyncio, json, os
from pathlib import Path
from urllib.parse import quote as urlquote
import uvicorn



celery_app = Celery("pdf2zh-next")
celery_app.conf.update(
    broker_url = "redis://127.0.0.1:6379/0",
    result_backend = "redis://127.0.0.1:6379/0",
    task_ignore_result = False,

)

app = FastAPI(
    title="PDFMathTranslate-next",
    description="PDF scientific paper translation",
    version="1.0.0",
    )

@celery_app.task(bind=True, name='pdf2zh-next.translate_task')
def translate_task(self: Task, stream: bytes, settings_dict: dict, original_filename: str | None = None):
    settings = SettingsModel.model_validate(settings_dict)

    async def async_translate():
        # Create a temp directory and store the uploaded file using its original name
        temp_dir = Path(tempfile.mkdtemp())
        safe_name = os.path.basename(original_filename) if original_filename else "uploaded.pdf"
        if not safe_name.lower().endswith(".pdf"):
            safe_name = f"{safe_name}.pdf"
        temp_file_path = temp_dir / safe_name
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(stream)

        try:
            async for event in do_translate_async_stream(settings, temp_file_path):
                if event["type"] in ("progress_start", "progress_update", "progress_end"):
                    self.update_state(
                        state="PROGRESS",
                    )
                elif event["type"] == "finish":
                    result = event["translate_result"]
                    return {
                        "mono_pdf_path": str(result.mono_pdf_path) if result.mono_pdf_path else None,
                        "dual_pdf_path": str(result.dual_pdf_path) if result.dual_pdf_path else None,
                        "glossary_path": str(result.auto_extracted_glossary_path) if result.auto_extracted_glossary_path else None,
                        "total_seconds": result.total_seconds,
                        "status": "completed",
                    }
                elif event["type"] == "error":
                    raise Exception(event.get("error", "Unknown error"))
        finally:
            try:
                temp_file_path.unlink(missing_ok=True)
            except Exception:
                pass
            try:
                temp_dir.rmdir()
            except Exception:
                pass

    return asyncio.run(async_translate())


@app.post("/v1/translate")
async def create_translate_tasks(
    file: UploadFile = File(...),  
    settings: str = Form(...),    #settings 
):
    # read bytes
    stream = await file.read()
    if not stream:
        raise HTTPException(400, "Empty file")

    # parse JSON
    try:
        args = json.loads(settings)
    except Exception as e:
        raise HTTPException(400, f"Invalid 'data' JSON: {e}")

    # Pass the original filename through to the worker so output names keep the base name
    task = translate_task.delay(stream, args, file.filename)
    return {"id": task.id}


@app.get("/v1/translate/{id}")
def get_translate_task(id: str):
    res = celery_app.AsyncResult(id)
    return {"state": str(res.state)}

@app.delete("/v1/translate/{id}")
def delete_translate_task(id: str):
    res = celery_app.AsyncResult(id)
    res.revoke(terminate=True)   # sends revoke signal to worker
    return {"state": str(res.state)}

@app.get("/v1/translate/{id}/{format}")
def get_translate_result(id: str, format: str):
    if format not in ("mono", "dual"):
        raise HTTPException(400, "format must be 'mono' or 'dual'")

    res = celery_app.AsyncResult(id)

    if not res.ready():
        raise HTTPException(400, "task not finished")
    if not res.successful():
        raise HTTPException(400, "task failed")

    result = res.get() 

    path = result.get("mono_pdf_path" if format == "mono" else "dual_pdf_path")
    if not path:
        raise HTTPException(404, f"{format} PDF path not available")
    if not os.path.exists(path):
        raise HTTPException(404, f"{format} PDF not found on disk")

    with open(path, "rb") as f:
        pdf_bytes = f.read()

    # Propose a filename to the client based on the actual file on disk
    filename = os.path.basename(path)
    headers = {
        "Content-Disposition": f"attachment; filename*=UTF-8''{urlquote(filename)}"
    }
    return Response(content=pdf_bytes, media_type="application/pdf", headers=headers)


if __name__ == "__main__":
    uvicorn.run("pdf2zh_next.http_api:app", host="0.0.0.0", port=8000, reload=True)