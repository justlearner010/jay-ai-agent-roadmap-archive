# 项目 3：AI Agent Web App

## 目标

做一个可交互的 Web 应用，把真实的 RAG 或 Agent 流程包装成用户能直接使用的产品。

## 必做功能

- Next.js 前端，包含输入、加载、输出、错误、历史记录等状态。
- Python FastAPI 后端，或结构清楚的 API 层。
- UI 背后必须是真实 RAG 或 LangGraph 流程，不能只是普通聊天接口。
- 如果涉及用户数据，要有基础认证或明确的本地使用边界。
- 部署到一个公开 URL。
- 准备 demo 视频和项目 README。

## 推荐技术栈

- Next.js
- TypeScript
- FastAPI
- LangGraph 或 RAG 后端
- Chroma/FAISS 或 SQLite
- 前端部署：Vercel 或 Netlify
- 后端部署：Render、Fly.io 或 Railway

## 验收标准

- 用户可以在浏览器里完成主流程。
- UI 能显示引用、日志或执行摘要。
- 后端核心逻辑有测试。
- 环境变量说明完整。
- 部署步骤可以复现。

## 加分项

- 支持流式输出。
- 加用户反馈按钮。
- 加评估看板。
- 加公开 demo 数据模式。
