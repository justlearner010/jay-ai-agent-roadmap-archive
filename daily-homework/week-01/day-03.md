# 第 1 周 Day 3：词频 Top 10：字典和 Counter

日期：2026-05-27（周三）

本周主题：环境搭建与 Python 文本处理起步

今日目标：用字典或 Counter 统计词频，建立哈希表直觉。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 复用昨天的文本文件，写一个词频统计函数。
2. 先用普通 dict 实现一次，再用 collections.Counter 实现一次。
3. 统一大小写，去掉最基础的标点符号。
4. 输出出现频率最高的 10 个词。
5. 在学习日志里比较 dict 和 Counter 的差异。

## 推荐阅读材料

- Python Tutorial - Data Structures：https://docs.python.org/3/tutorial/datastructures.html
- Python Docs - collections.Counter：https://docs.python.org/3/library/collections.html#collections.Counter
- CS50P Week 4 - Libraries：https://cs50.harvard.edu/python/weeks/4/
- 科班基础：把 dict 理解成“用 key 快速找到 value 的表”。

## 提交物

- python-foundations/word_frequency_count.py
- Top 10 输出结果
- 学习日志里一段 dict vs Counter 的解释

## 验收标准

- 至少能处理英文大小写和常见标点。
- 输出结果按频率从高到低排列。
- 你能解释为什么 dict 适合做词频统计。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
