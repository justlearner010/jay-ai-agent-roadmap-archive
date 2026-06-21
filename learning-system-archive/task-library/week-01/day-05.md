# 第 1 周 Day 5：组合成 CLI：输入文件到输出文件

日期：2026-05-29（周五）

本周主题：环境搭建与 Python 文本处理起步

今日目标：把前几天的函数串成一个可以从命令行运行的小工具。

预计投入：2-3 小时。如果当天时间少，优先完成“作业要求”的前 3 项，并在学习日志里说明延期项。

## 作业要求

1. 写 CLI 参数：input path、output path、mode。
2. mode 至少支持 stats 和 chunks 两种。
3. 把统计结果或切块结果保存到输出文件。
4. 对输入路径不存在、输出目录不存在给出清楚错误。
5. 记录 2 条可复制运行命令。

## 推荐阅读材料

- Python Docs - argparse：https://docs.python.org/3/library/argparse.html
- Python Docs - sys：https://docs.python.org/3/library/sys.html
- MIT Missing Semester - Shell Tools and Scripting：https://missing.csail.mit.edu/2020/shell-tools/
- CS50P Week 3 - Exceptions：https://cs50.harvard.edu/python/weeks/3/

## 提交物

- CLI Python 文件
- 两条运行命令和输出文件
- 学习日志里记录一个错误处理例子

## 验收标准

- 别人复制你的命令可以运行。
- 错误输入不会直接输出一堆看不懂的 traceback。
- 你能画出 CLI 参数进入程序后的数据流。

## 批改重点

提交给 Codex 批改时，重点看：

- 今天的代码或文档是否完成了核心要求。
- 你是否能用自己的话解释关键代码和概念。
- 是否有清楚的运行结果、截图、测试结果或日志证据。
- 明天第一件事应该修什么。
