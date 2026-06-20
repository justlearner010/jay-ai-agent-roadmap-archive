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

## 本周唯一主交付物

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

- 10 小时：Next.js 页面与四种状态。
- 3 小时：TypeScript 契约、调试和测试。
- 2 小时：Java 基础小产出。
- 2 小时：项目卡点对应的 HTTP/状态机基础或算法微练习。
- 2 小时：复查、README、证据与里程碑整理。
- 1 小时：JD、英文文档或一个开源项目分析。

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

详细日程见 `week-06/README.md`。
