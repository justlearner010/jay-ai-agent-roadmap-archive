# 第 7 周 Day 3：结构化输出设计

日期：2026-07-08（周三）

本周主题：接入真实 LLM API

今日目标：让返回结果稳定可展示。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 设计 summary、keyPoints、followupQuestions 字段。
2. 让前端按字段渲染。
3. 保存一个真实返回样例。
4. 在学习日志里记录今天新增或修改的文件路径、运行命令和实际结果。
5. 整理 1-3 个准备提交给 Codex 批改的具体问题，问题必须指向代码、测试、文档或概念。
6. 写下明天第一步要做什么，必须具体到一个文件、一个函数、一个页面或一个文档段落。

## Java 副线任务

时间上限：45-60 分钟。

1. 创建一个 Spring Boot Hello API，返回固定 JSON；把它理解成 Next.js API route 或 Python FastAPI route 的 Java 版本。
2. JSON 至少包含 `message` 和 `timestamp` 或同等字段。
3. 记录启动命令和一次请求结果。

## 科班基础嵌入

- 今日基础点：客户端 / 服务端边界。
- 对应项目任务：Spring Boot Hello API 和 LLM 结构化输出。
- 最小验收：能画出 browser -> API -> response 的最小链路。

## 推荐阅读材料

- 本仓库：`resources/cs-foundations-side-track.md` 的 Week 7 Day 3
- 本仓库：`resources/java-side-track.md` 的“Spring Boot Controller”
- OpenAI Structured Outputs：https://platform.openai.com/docs/guides/structured-outputs
- TypeScript Handbook - Object Types：https://www.typescriptlang.org/docs/handbook/2/objects.html

## 提交物

- 当天代码、文档或测试文件
- 学习日志 learning-log/YYYY-MM-DD.md
- 运行结果、截图或测试输出
- 需要 Codex 批改的 1-3 个问题

## 验收标准

- 完成今日主功能、主文档或主测试，不用“看了资料”代替交付。
- 留下可检查的证据：运行命令、测试输出、页面截图、README 片段或学习日志。
- 能用自己的话解释今天最关键的概念，以及它和 AI 学习助手项目的关系。
- 明天第一步任务已经写清楚，并且能在 30 分钟内开始执行。
- Spring Boot Hello API 能返回 JSON；如果环境没配好，至少写清缺少哪一步。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
