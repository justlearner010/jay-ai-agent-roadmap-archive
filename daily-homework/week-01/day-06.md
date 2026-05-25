# 第 1 周 Day 6：给两个练习加 pytest

日期：2026-05-30（周六）

本周主题：环境搭建与 Python 文本处理起步

今日目标：用测试固定核心逻辑，开始形成工程化习惯。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 选择文本统计和文本切块两个函数作为测试对象。
2. 为每个函数写至少 2 个测试：正常输入和边界输入。
3. 运行 pytest，保存通过或失败输出。
4. 如果测试失败，先改代码再改测试，记录原因。
5. 整理本周代码，把明显重复的逻辑提成函数。

## 推荐阅读材料

- pytest - Get Started：https://docs.pytest.org/en/stable/getting-started.html
- pytest - How to write and report assertions：https://docs.pytest.org/en/stable/how-to/assert.html
- CS50P Week 5 - Unit Tests：https://cs50.harvard.edu/python/weeks/5/
- 本仓库：templates/homework-review-template.md。

## 提交物

- 至少 2 个 pytest 测试文件或测试函数
- pytest 运行结果
- 本周准备提交的 git diff 摘要

## 验收标准

- 至少 2 个测试通过。
- 测试覆盖正常输入和一个边界情况。
- 你能解释测试为什么能防止以后改坏代码。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
