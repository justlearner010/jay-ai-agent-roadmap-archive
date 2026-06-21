# 第 1 周 Day 4：文本切块和 JSON 保存

日期：2026-05-28（周四）

本周主题：环境搭建与 Python 文本处理起步

今日目标：把长文本拆成固定大小块，并保存成可复用的数据格式。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 写函数把一段长文本按 500 字符切成多个 chunk。
2. 每个 chunk 保存 index、start、end、text。
3. 把 chunks 保存成 JSON 文件。
4. 写一个小样例验证最后一个 chunk 可以少于 500 字符。
5. 在学习日志里写：为什么 RAG 以后也需要文本切块。

## 推荐阅读材料

- Python Docs - json：https://docs.python.org/3/library/json.html
- Python Docs - String methods：https://docs.python.org/3/library/stdtypes.html#string-methods
- Full Stack LLM Bootcamp - 先浏览课程目录，了解 LLM app 会涉及哪些模块：https://fullstackdeeplearning.com/llm-bootcamp/
- 本仓库：cs-foundations-integration.md 中“阶段 1”部分。

## 提交物

- 文本切块函数文件
- 生成的 JSON 样例
- 学习日志里的 RAG 切块解释

## 验收标准

- chunk index 连续，从 0 或 1 开始都可以，但要一致。
- JSON 能被 Python 重新读取。
- 你能解释 start/end/text 三个字段的用途。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
