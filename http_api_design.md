### 背景与目标

- **目标**: 为 PDFMathTranslate-next 提供基于 FastAPI 的 HTTP API，实现任务化翻译、上传 PDF、按 `SettingsModel` 配置翻译参数、查询与下载结果、取消任务，以及一个内存级队列以限制并发与排队；并在 GUI 启动时自动挂载和联动同一套队列/任务系统。
- **约束**:
  - 不依赖 Redis 等独立服务（可用内存结构与 `asyncio`/线程/进程，并可用 Python 包）。
  - 使用 FastAPI 提供 HTTP 服务。
  - 任务态与历史进度仅驻留内存，进程重启即丢失。
  - 队列默认最多排队 10 个任务；最多保存 1000 条最新任务进度（均可配置）。
  - GUI 内发起的翻译也纳入同一队列/并发控制。

### 现状复用点

- `pdf2zh_next.config`：`ConfigManager.initialize_cli_config()` 可提供默认配置；`SettingsModel`（及其子模型）是唯一权威配置模型；具备校验、转译（引擎 transform）与字段约束。
- `pdf2zh_next.high_level`：
  - `do_translate_async_stream(settings, file)` 产出结构化事件（progress_start/update/end、finish、error），是最可靠的“翻译引擎异步流接口”。
  - 子进程隔离执行，支持取消、错误回传、结构化异常。
- `pdf2zh_next.gui.translate_file(...)`：展示了如何从 UI 入参组装 `SettingsModel`（包含速率限制、PDF 输出选项、高阶参数等），可复用其参数映射逻辑为 API 层输入校验/映射的参考。

### 总体架构

- 采用单进程 FastAPI 应用（可多 worker 部署但内存任务不共享，见“部署建议”），组件：
  - TaskManager（内存任务与队列管理）
  - Worker 执行器（消费队列，调用 `do_translate_async_stream`）
  - Storage（仅内存，结果文件路径落到本地磁盘 `pdf2zh_files/<taskId>/...`）
  - API 层（FastAPI 路由定义）
  - GUI 集成（用 `app.mount('/gradio', gradio_app)`；GUI 产生的作业也走 TaskManager）

### 任务模型

- 任务 ID 规范：`pdf2zh_next.<4位随机16进制>.uuid`（如 `pdf2zh_next.3E87.uuid`）。
- Task 字段（内存保存）：
  - id、status（queued/running/succeeded/failed/cancelled）、createTime、updateTime
  - inputFilePath、resultMonoPath、resultDualPath、glossaryPath
  - progress（0.0~1.0）、progressDesc、parts(total/idx)、stage(stage_current/total)
  - error（message、type、details）
  - settings（`SettingsModel` 的简化快照，避免敏感字段外泄）

### 队列与并发控制

- 限制：
  - `max_queue_size` 默认 10（可通过环境或 API 启动参数覆盖）
  - `max_history_progress` 默认 1000，用环形缓冲或 FIFO 列表维护最近任务信息
  - `max_concurrency` 默认 1（可配置），决定并行运行任务数
- 数据结构：
  - `collections.deque` 作为等待队列
  - `dict[str, Task]` 作为任务表；另有 `OrderedDict` 维护进度历史的裁剪
- 取消：设置 task.cancel_flag，调用 `AsyncCallback`/管道触发取消；worker 感知后停止并更新状态

### API 设计

- 路径前缀：`/api/v1`

1) 创建任务（带 SettingsModel）
- `POST /api/v1/tasks`
  - Content-Type: `multipart/form-data`
    - `file`: PDF（二进制）或 `link`: URL（二选一）
    - `settings`: JSON（`SettingsModel` 结构，若省略则使用默认）
  - 响应：`{ task_id }`

2) 创建任务（仅上传 PDF，使用默认配置）
- `POST /api/v1/tasks/default`
  - multipart form：`file` 或 `link`
  - 响应：`{ task_id }`

3) 查询任务
- `GET /api/v1/tasks/{task_id}`
  - 响应：任务元信息（status、progress、文件可用性、错误信息、创建/更新时间等）

4) 下载结果
- `GET /api/v1/tasks/{task_id}/result`（聚合）
  - 响应：`{ mono_url, dual_url, glossary_url }`（如可访问则返回 URL；或 404）
- `GET /api/v1/tasks/{task_id}/files/mono|dual|glossary`
  - 以 `FileResponse` 方式直传下载

5) 取消任务
- `POST /api/v1/tasks/{task_id}/cancel`
  - 响应：`{ ok: true }`（若处于 queued/running 则尝试取消；终态返回 409）

6) 健康检查
- `GET /health`
  - 响应：`{ status: "ok", version: string, queue_size: int, running: int }`
  - 说明：用于探针/监控，默认豁免鉴权（可通过配置修改）。

- 错误码：
  - 400（参数错误/文件非法）、401（未认证/令牌无效）、404（任务不存在）、409（队列满/任务终态不可取消）、429（队列满时也可用）

### SettingsModel 输入映射

- 支持两种输入：
  - 直接传完整 `SettingsModel` JSON；服务端用 `SettingsModel(**payload)` 校验；并进行 `validate_settings()`；敏感字段（如 API Key）按原样使用但不回传
  - 默认配置：通过 `ConfigManager.initialize_cli_config()` 获取基础 `CLIEnvSettingsModel`，再 `to_settings_model()`
- 与 GUI 统一：保留 `gui.py` 中 `_build_translate_settings` 的映射规则作为参考，API 端不必暴露所有 UI 粒度字段；如需精细控制，可接受 `ui_inputs` 风格 JSON 并在服务端复用该构造流程（可选 V2）

### Worker 执行流

- 入队 → 调度器根据并发度唤醒 Worker → 调用 `_prepare_input_file`（文件/链接下载，重用 `gui.py` 的实现思路）→ 根据 settings 生产输出目录 → `async for event in do_translate_async_stream(settings, file)`：
  - progress_* 事件：更新内存任务进度
  - finish：写入 `mono_pdf_path/dual_pdf_path/glossary_path`，置 `succeeded`
  - error：填充错误信息，置 `failed`
- 任务结束后：任务进度记录入历史队列，超出 `max_history_progress` 则丢弃最旧

### 与 GUI 的集成

- 在 FastAPI app 中使用 `app.mount('/gradio', gradio_app)`，GUI 按钮触发时不直接执行 `translate_file`，而是改为调用 TaskManager 的“创建任务”接口（或内部 API 调用），从而保证：
  - GUI 任务与 HTTP 任务共享相同的队列/并发与统计
  - 取消操作亦走同一逻辑
- 方案 A（推荐）：将 `translate_file` 的核心“构建设置 + 提交执行”的部分抽象成 `enqueue_translation(settings, file_or_link)`，GUI 改调用该函数；
- 方案 B：GUI 继续原实现，但由 TaskManager 提供一个“内部队列接入适配器”，在 GUI 创建任务时经由适配器将作业统一登记

### 内存实现要点（无外部依赖）

- 任务表、队列、运行中集合均为内存结构；使用 `asyncio.Queue` 或 `deque` + 自管信号；
- 通过 `max_queue_size` 限制等待队列长度；
- 结果文件落盘路径与 GUI 相同（`pdf2zh_files/<taskId>/`），避免重复实现；
- 取消通过与 `high_level` 一致的管道/事件触发；

### 并发与健壮性

- 限制并发度以避免过载；
- 子进程崩溃由 `high_level` 已捕获并上抛结构化错误；
- 进程重启会丢任务信息与队列，文档中明确声明；
- 大文件上传限制（例如 200MB），并在下载链接模式下增加超时与大小保护（参考 `download_with_limit`）。

### 存储与文件生命周期（当前策略）

- 暂无自动清理：当前版本不内置结果文件自动清理/过期策略，重启不会自动删除历史结果。
- 手动清理建议：
  - 定期清理 `pdf2zh_files` 下的历史任务目录（可按 mtime/完成时间）。
  - 示例（按 7 天过期）：
```bash
find pdf2zh_files -type d -mtime +7 -exec rm -rf {} +
```
- 留足磁盘空间：部署前请评估典型 PDF 规模与并发度，合理预留磁盘（建议 10~20GB 起，根据业务调整）。
- 磁盘空间监控：建议使用外部监控/告警（如 Prometheus node_exporter）或定期 `df/du` 检查；V2 计划提供阈值检查与后台清理器。
- 结果过期策略（V2 规划）：支持基于 TTL 的后台清理与空间阈值触发清理（FIFO/最近最少访问）。

### 监控与健康检查

- 健康检查端点：`GET /health`，返回基础运行态（版本、队列长度、运行中数量）。
- 鉴权：默认免认证，便于负载均衡与容器编排探针；可通过豁免路径配置修改。
- 指标（V2 规划）：提供 Prometheus 指标 `/metrics`（任务耗时、错误率、队列长度、磁盘可用空间等）。

### 安全与鉴权（API 认证）

- 认证要求：除 `/health`、`/docs`、`/openapi.json` 外的所有 API 需通过 Bearer Token 认证。
- 认证方式：
  - 请求头：`Authorization: Bearer <token>`
  - 令牌来源：环境变量 `HTTP_AUTH_TOKEN`（单一 Token，必填）；可选 `HTTP_AUTH_TOKENS`（逗号分隔多 Token）。
  - 校验失败：返回 401，错误码 `UNAUTHORIZED`。
- 输入安全：
  - 文件扩展名与 MIME 检查，仅允许 PDF；
  - 上传大小限制：由 `HTTP_FILE_SIZE_LIMIT_MB` 控制；
  - CORS：按需配置允许域；
  - 结果文件路径白名单 `allowed_paths` 与 GUI 一致。

### 部署建议

- 单实例：最简，内存任务即有效；
- 多实例（多 worker / 多 Pod）：因任务保存在内存，不共享；建议：
  - 通过入口做粘性会话/实例亲和，或
  - 显式声明“不可水平扩展共享队列”；需要水平扩展时再演进外部持久化（见“演进计划”）

### 目录与文件变更（实施建议）

- 新增：`pdf2zh_next/http_api.py`（若无则创建）
  - 定义 FastAPI `app`，路由、模型、异常处理器、CORS；
  - 实现 TaskManager（单例）与 Worker（后台任务/线程）；
  - 提供 `create_app(mount_gui=True)`，在 GUI 启动时复用同一进程并 `app.mount('/gradio', gradio_app)`。
- GUI 侧调整：将按钮触发改为排队提交（方案 A）或接入适配器（方案 B）。

### 示例接口定义（伪代码）

```python
# Pydantic models
class CreateTaskResponse(BaseModel):
    task_id: str

class TaskState(BaseModel):
    id: str
    status: Literal['queued','running','succeeded','failed','cancelled']
    progress: float | None
    progress_desc: str | None
    mono: bool
    dual: bool
    glossary: bool
    error: dict | None
    created_at: float
    updated_at: float

# FastAPI routes
@router.post('/tasks', response_model=CreateTaskResponse)
async def create_task(file: UploadFile | None = File(None), link: str | None = Form(None), settings: str | None = Form(None)):
    # 校验 + 反序列化 settings
    # 生成 task_id, 入队
    return {"task_id": task_id}

@router.get('/tasks/{task_id}', response_model=TaskState)
async def get_task(task_id: str):
    # 返回任务状态

@router.get('/tasks/{task_id}/result')
async def get_result(task_id: str):
    # 返回文件可用性与下载链接

@router.get('/tasks/{task_id}/files/{kind}')
async def download(task_id: str, kind: Literal['mono','dual','glossary']):
    # FileResponse

@router.post('/tasks/{task_id}/cancel')
async def cancel_task(task_id: str):
    # 尝试取消

@router.get('/health')
async def health():
    return {"status": "ok"}
```

### 错误与返回规范

- 统一错误响应：`{"error": {"code": str, "message": str}}`
- 典型：
  - 队列已满 → 409/429 + `QUEUE_FULL`
  - 非法文件/链接 → 400 + `INVALID_INPUT`
  - 未认证/令牌无效 → 401 + `UNAUTHORIZED`
  - 不存在的任务 → 404 + `NOT_FOUND`
  - 终态取消 → 409 + `INVALID_STATE`

### 配置项（环境变量）

- `HTTP_MAX_QUEUE_SIZE`（默认 10）
- `HTTP_MAX_HISTORY_PROGRESS`（默认 1000）
- `HTTP_MAX_CONCURRENCY`（默认 1）
- `HTTP_FILE_SIZE_LIMIT_MB`（默认 200）
- `HTTP_AUTH_TOKEN`（必填，单 Token）
- `HTTP_AUTH_TOKENS`（可选，逗号分隔多 Token）
- `HTTP_AUTH_EXEMPT_PATHS`（可选，默认 `/health,/docs,/openapi.json`）
- `HTTP_HEALTH_ENABLED`（可选，默认 true）

### 演进计划

- V1：单实例、内存队列、GUI 共用队列、REST API 完成。
- V2（可选）：
  - API 端支持 `ui_inputs` 风格 payload，服务端复用 `_build_translate_settings` 逻辑。
  - SSE/WebSocket 推送任务进度（实时）。
  - 灰度引入外部存储（如 SQLite + 文件系统）以提供重启恢复与水平扩展（保留“无 Redis”选项）。
  - 内置后台清理器（TTL/空间阈值）、磁盘空间阈值监测与指标暴露。

### 风险与权衡

- 进程重启丢任务/进度：已在文档与 API 明确说明；
- 多实例不共享队列：需要时通过演进引入持久层；
- 大文件上传与磁盘占用：建议定期清理 `pdf2zh_files`；
- API Key 等敏感信息：仅入参使用，不回传，不持久化。
