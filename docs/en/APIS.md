
## Running

You need **two processes**:

1. **Celery worker**
2. **FastAPI server**

### Start the Celery worker

```bash
# Linux / macOS
gelery -A pdf2zh_next.http_api.celery_app worker --loglevel=info

# Windows (solo pool required)
celery -A pdf2zh_next.http_api.celery_app worker --loglevel=info --pool=solo
```

### Run the FastAPI server

```bash
uvicorn pdf2zh_next.http_api:app --host 0.0.0.0 --port 8000 --reload
```

Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


---

## Using the HTTP API

### 1) Submit a translate task

```bash
curl -X POST "http://127.0.0.1:8000/v1/translate" \
  -F "file=@/path/to/input.pdf" \
  -F 'settings={"translation":{"lang_in":"tr","lang_out":"en"},"translate_engine_settings":{"translate_engine_type":"Google"}}'
```

**Response**

```json
{"id": "f8a61b9e-d93f-495c-afce-50b2fe23c90c"}
```

---

### 2) Check the task status

```bash
curl -X GET "http://127.0.0.1:8000/v1/translate/<task-id>" -H 'accept: application/json'
```

**Example**

```json
{"state": "PROGRESS"}
```


---

### 3) Download the translated PDF

```bash
# mono
curl -X GET "http://127.0.0.1:8000/v1/translate/<task-id>/mono" -o output.mono.pdf

# dual
curl -X GET "http://127.0.0.1:8000/v1/translate/<task-id>/dual" -o output.dual.pdf
```

---
