# 项目 4：Java + AI 后端网关

## 目标

做一个面向 Java 后端实习投递的 AI 应用后端。Java / Spring Boot 负责业务接口、数据库和任务管理，Python RAG / Agent 服务负责 AI 推理能力。

这个项目不是替代个人 RAG 知识库，而是把 RAG / Agent 能力包装成更接近真实业务系统的后端服务。

## 适合投递的定位

- 投 Java 后端实习：放在第一或第二项目，突出 Spring Boot、数据库、REST API、测试和服务调用。
- 投 AI Agent 实习：作为后端工程化加分项目，说明你能把 RAG / Agent 落到业务服务里。

## 必做功能

- 文档元数据管理：创建、查询、更新文档标题、摘要、来源和创建时间。
- AI 任务创建：用户提交文档或问题后，Java 后端创建任务记录。
- 调用 Python AI 服务：Java 后端通过 HTTP 调用 Python RAG / Agent 服务。
- 保存执行结果：保存任务状态、结果摘要、错误信息、耗时和创建时间。
- 查询历史记录：按任务 ID 或文档 ID 查询历史执行记录。
- 错误日志：记录 AI 服务超时、返回错误、参数错误和数据库写入失败。
- 基础测试：至少覆盖 service 层、controller 层或 repository 层中的两个关键路径。

## 推荐技术栈

- Java
- Spring Boot
- Spring Web
- Spring Validation
- Spring Data JPA 或 MyBatis 二选一
- PostgreSQL 或 MySQL
- JUnit
- Python FastAPI RAG / Agent 服务

## 建议接口

- `POST /documents`：创建文档 metadata。
- `GET /documents/{id}`：查询文档 metadata。
- `POST /ai-tasks`：创建 AI 任务，并触发 Python AI 服务调用。
- `GET /ai-tasks/{id}`：查询任务状态和结果。
- `GET /documents/{id}/ai-tasks`：查询某个文档的 AI 任务历史。

## 数据表建议

### `documents`

- `id`
- `title`
- `source`
- `summary`
- `created_at`
- `updated_at`

### `ai_tasks`

- `id`
- `document_id`
- `question`
- `status`
- `result_summary`
- `error_message`
- `latency_ms`
- `created_at`
- `updated_at`

## 验收标准

- Spring Boot 服务可以启动，并能返回 JSON。
- 可以创建并查询文档 metadata。
- 可以创建 AI 任务，并保存 mock 或真实 Python AI 服务返回结果。
- Python AI 服务失败时，Java 后端能保存失败状态和错误信息。
- 数据库重启后，文档和任务记录仍可查询。
- README 写清楚架构、启动步骤、接口样例、数据库表和已知限制。
- 至少有 2 个自动化测试或清晰的手动验证记录。

## 加分项

- 使用 Redis 缓存最近查询的任务结果。
- 增加任务状态机：`PENDING`、`RUNNING`、`SUCCEEDED`、`FAILED`。
- 增加接口文档，例如 OpenAPI / Swagger。
- 增加 Docker Compose，启动 Java 后端、数据库和 Python AI 服务。
- 增加简单前端页面展示文档和 AI 任务历史。

## 简历表达示例

AI Agent 版：

> 构建 Java + Python 双服务 AI 后端，使用 Spring Boot 管理文档、任务和执行记录，并调用 Python RAG 服务完成文档问答，支持任务状态追踪和失败日志。

Java 后端版：

> 基于 Spring Boot 实现文档问答系统后端网关，设计文档和任务表结构，完成 REST API、数据库持久化、参数校验、异常处理和外部 AI 服务调用。
