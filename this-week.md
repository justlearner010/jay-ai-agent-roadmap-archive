# 本周从这里开始

校准日期：2026-06-21

执行周期：2026-06-22 至 2026-06-28

## 当前定位

- 主线不变：70% AI Agent / RAG / LLM 应用工程，30% Java 后端兼容。
- 当前阶段：把 `first-CLI` 的 Python 逻辑转换为可供 Next.js 前端使用的类型契约和页面状态。
- 当前项目：AI 学习助手。`python-foundations/first-CLI` 是后端原型，本周开始前端雏形。
- 资产化标准：学习过的 TypeScript 概念必须进入真实页面契约或运行证据，不另起新仓库。

## 发布门槛状态

- [x] 6 月 18 日 `keywords` 契约必改项已关闭。
- [x] 6 月 19 日 `interface`、`as`、validator 必改项已关闭。
- [x] TypeScript `npm run check` 通过，三组 mock 输出为 `true / false / false`。
- [x] `first-CLI`：`30 passed, 1 xfailed`。
- [x] `practice`：`15 passed`。
- [ ] 当前里程碑完成整理提交并推送 GitHub。

在最后一项完成前，不对外声称里程碑已发布。

## 本周主问题

如何让用户完成文本输入和模式选择，并清楚看到 `idle`、`loading`、`success`、`error` 四种页面状态？

选择原因：这是从 CLI 原型进入可交互 AI 学习助手的最小闭环，也会暴露 TypeScript 契约、异步状态和错误处理中的真实卡点。

周日可演示结果：用户可以输入文本、选择模式、提交 typed mock，并观察成功与失败流程。

## 验收条件

- 用户可以输入文本、选择 `brief` / `bullets` 并提交。
- 页面初始为 `idle`，提交后显示 `loading`，最终进入 `success` 或 `error`。
- typed mock 符合 `SummarizeResponse`，错误 mock 不能进入成功结果。
- 至少保留两个运行、类型检查、构建、测试或截图证据。

## 当前未知点与候选实验

- 输入、模式和请求状态应该分别保存，还是合并管理？
- 如何用 typed mock 模拟延迟与失败？
- 四种状态如何做到互斥且容易解释？
- 卡在类型契约、表单状态或异步流程时，再从第 5 周任务库选择对应任务卡；不按日期补任务。

## 本周主交付物

完成 AI 学习助手 Next.js 前端雏形：

- 文本输入区。
- `brief` / `bullets` 模式选择。
- 提交按钮。
- `idle`、`loading`、`success`、`error` 四种状态。
- 使用 typed mock 显示 summary，本周不调用真实 LLM。

## 本周交付证据

- 证据 1：TypeScript 类型检查或 Next.js build 成功输出。
- 证据 2：四种页面状态的运行截图或自动化测试。
- 资产入口：代码、运行命令和截图统一纳入 AI 学习助手，不拆成独立练习仓库。

## 本周 20 小时

- 10 小时：Next.js 页面与四种状态实验。
- 3 小时：由页面卡点触发的 TypeScript、调试和测试。
- 2 小时：Java 基础小产出。
- 4 小时：相邻自由探索，主题由你选择并提前锁定时间。
- 1 小时：证据整理和周末验收。

## 本周任务池

- 建立最小 Next.js 页面并确认可以运行。
- 实现输入和模式选择。
- 用 typed mock 跑通 `loading → success`。
- 制造一个真实失败场景并进入 `error`。
- 补类型检查、构建、测试或截图证据。

任务池没有固定顺序。每次只选择最有助于回答本周主问题的一项；未选择项不形成补债。

## 本周不做

- 不接真实 LLM API。
- 不提前做 RAG 或 LangGraph。
- 不增加 AI Infra、CUDA、vLLM、Kafka或 Spring Cloud。
- 不追求文章、仓库或算法题数量。
- 不用长笔记替代页面和测试。

## 本周验收

- 用户可以输入文本、选择模式并提交。
- 页面能明确展示 `loading`、`success` 和 `error`，初始为 `idle`。
- typed mock 符合 `SummarizeResponse`，错误 mock 不能被当成有效响应。
- 至少两个运行或测试证据。
- README 说明安装、启动、当前 mock 边界和下周 API route 计划。
- 周日更新 `trackers/weekly-log.csv` 和 `trackers/project-scorecard.csv`。

## 周中诊断与周末决策

- 周中：使用 `templates/midweek-diagnosis.md`，只诊断当前结果和最大卡点，不评分。
- 周末：使用 `templates/weekly-acceptance.md` 验收，并在“继续 / 转向 / 暂存”中选择一个结论。

任务库见 `daily-homework/week-05/README.md`，按卡点选择，不按日期执行。
