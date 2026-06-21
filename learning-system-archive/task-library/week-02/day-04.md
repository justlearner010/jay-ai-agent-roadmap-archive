# 第 2 周 Day 4：异常处理和文件读写边界

日期：2026-06-04（周四）

本周主题：Python 基础补齐：函数、类、异常、类型标注

今日目标：让代码遇到常见错误时能给出可理解反馈。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 给文件读取函数加入 FileNotFoundError 处理。
2. 给 JSON 保存函数加入输出目录不存在的处理。
3. 写 3 个异常练习：数字转换失败、空输入、无效路径。
4. 不要吞掉所有异常，记录你捕获了哪类异常。
5. 在学习日志里解释 try/except/raise 的区别。

## 推荐阅读材料

- Python Tutorial - Errors and Exceptions：https://docs.python.org/3/tutorial/errors.html
- Python Docs - Built-in Exceptions：https://docs.python.org/3/library/exceptions.html
- CS50P Week 3 - Exceptions：https://cs50.harvard.edu/python/weeks/3/

## 提交物

- 带异常处理的文件读写函数
- 3 个异常练习
- 至少 1 条错误输入运行结果

## 验收标准

- 错误信息对使用者可读。
- 没有用裸 except 直接忽略错误。
- 你能解释什么时候应该 raise，什么时候应该返回错误提示。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
