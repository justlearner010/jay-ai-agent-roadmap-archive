## 任务卡：结构化输出设计

> 适用卡点：当本周主问题需要“结构化输出设计”相关能力、实验或证据时选择。
> 使用规则：这是一张可选任务卡，没有指定日期或前后顺序；未选择或未完成不形成补债。

本周主题：接入真实 LLM API

任务目标：让返回结果稳定可展示。

参考投入上限：2-3 小时。只选择足以验证当前假设的步骤，未选内容不延期、不补做。

## 候选实验

1. 设计 summary、keyPoints、followupQuestions 字段。
2. 让前端按字段渲染。
3. 保存一个真实返回样例。
4. 在学习日志里记录本任务新增或修改的文件路径、运行命令和实际结果。
5. 整理 1-3 个准备在周中诊断时提交给 Codex 的具体问题，问题必须指向代码、测试、文档或概念。
6. 写下后续自然动作要做什么，必须具体到一个文件、一个函数、一个页面或一个文档段落。

## Java 副线任务

时间上限：45-60 分钟。

1. 创建一个 Spring Boot Hello API，返回固定 JSON；把它理解成 Next.js API route 或 Python FastAPI route 的 Java 版本。
2. JSON 至少包含 `message` 和 `timestamp` 或同等字段。
3. 记录启动命令和一次请求结果。

## 科班基础嵌入

- 相关基础点：客户端 / 服务端边界。
- 对应项目任务：Spring Boot Hello API 和 LLM 结构化输出。
- 最小验收：能画出 browser -> API -> response 的最小链路。

## 推荐阅读材料

- 本仓库：`resources/cs-foundations-side-track.md` 的 Week 7 Day 3
- 本仓库：`resources/java-side-track.md` 的“Spring Boot Controller”
- OpenAI Structured Outputs：https://platform.openai.com/docs/guides/structured-outputs
- TypeScript Handbook - Object Types：https://www.typescriptlang.org/docs/handbook/2/objects.html

## 提交物

- 本次代码、文档或测试文件
- 学习日志 learning-log/YYYY-MM-DD.md
- 运行结果、截图或测试输出
- 准备在周中诊断讨论的 1-3 个问题

## 验收标准

- 完成能验证当前假设的主功能、主文档或主测试，不用“看了资料”代替交付。
- 留下可检查的证据：运行命令、测试输出、页面截图、README 片段或学习日志。
- 能用自己的话解释本任务最关键的概念，以及它和 AI 学习助手项目的关系。
- 已写下一个可在 30 分钟内开始的后续自然动作。
- Spring Boot Hello API 能返回 JSON；如果环境没配好，至少写清缺少哪一步。

## 诊断重点

在周中诊断时，重点看：

- 本任务的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 后续第一件事应该修什么。
