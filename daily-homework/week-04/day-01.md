# 第 4 周 Day 1：pytest fixture

日期：2026-06-11（周四）

本周主题：pytest 与后端前置能力

今日目标：把已经开始的 fixture 学习落到 `first-CLI` 测试里，减少重复测试准备工作。

预计投入：2-3 小时。如果当天时间少，只完成“必做”的前 3 项，并在学习日志里说明延期项。

## 作业要求

### 必做

1. 复查今天已经改过的两个测试文件：
   - `python-foundations/first-CLI/tests/test_text_status.py`
   - `python-foundations/first-CLI/tests/test_createjson.py`
2. 确认 fixture 只负责“准备测试数据 / 临时文件 / 公共输入”，不要把断言逻辑塞进 fixture。
3. 针对这两个测试文件运行定向测试，并把命令和结果写进学习日志。
4. 在学习日志里用自己的话解释：fixture 和普通 helper 函数的区别是什么。
5. 整理 1-3 个准备提交给 Codex 批改的问题，问题必须指向具体文件、测试或概念。
6. 写下明天第一步：继续改哪一个测试文件，具体到文件名。

### 选做

1. 再选择一个旧测试文件改成 fixture 写法：
   - `python-foundations/first-CLI/tests/test_word_freq.py`
   - `python-foundations/first-CLI/tests/test_word_chunk.py`
   - `python-foundations/first-CLI/tests/test_summarize.py`
2. 如果时间够，运行 `python -m pytest` 或项目当前等价测试命令，确认全量测试没有被 fixture 改坏。
3. 在 `notes/fourth-week notes/2026-06-11笔记：pytest fixture.md` 里补一个来自本项目的真实 fixture 例子。

## 推荐阅读材料

- pytest - Fixtures：https://docs.pytest.org/en/stable/how-to/fixtures.html

## 提交物

提交批改时，按 `templates/daily-homework-submission-template.md` 整理，至少包含这些项：

代码文件：

- `python-foundations/first-CLI/tests/test_text_status.py`
- `python-foundations/first-CLI/tests/test_createjson.py`
- 选做改动到的其他测试文件

测试文件：

- `python-foundations/first-CLI/tests/test_text_status.py`
- `python-foundations/first-CLI/tests/test_createjson.py`

学习日志：

- `learning-log/fourth-week-log/2026-06-11日志.md`

学习笔记：

- `notes/fourth-week notes/2026-06-11笔记：pytest fixture.md`

运行证据：

- 定向 pytest 命令和结果。
- 如果跑了全量测试，也记录全量 pytest 命令和结果。

希望 Codex 重点批改：

- fixture 是否真的减少了重复准备工作。
- fixture、helper 函数、`tmp_path` 的理解是否准确。
- 两个测试文件是否仍然清楚、可读、可维护。
- 明天应该优先继续改哪个测试文件。

当前是否已经上传 GitHub：

- [ ] 已上传
- [ ] 还没上传，等批改后再上传

## 验收标准

Codex 会按 `templates/homework-review-template.md` 批改，评分映射如下：

- 当前阶段完成度 30 分：是否完成 2 个测试文件的 fixture 改造或复查；是否符合第 4 周“pytest 与后端前置能力”的阶段目标。
- 正确性和可运行性 25 分：定向 pytest 是否通过；fixture 改造后是否没有破坏原测试含义。
- 代码可读性 15 分：fixture 命名是否清楚；测试逻辑和准备数据是否分开；没有把断言塞进 fixture。
- 学习日志和证据 20 分：学习日志是否记录修改文件、运行命令、实际结果、fixture 和 helper 的区别。
- 明日可执行性 10 分：明天第一步是否具体到一个测试文件和一个动作。

## 批改重点

提交给 Codex 批改时，重点看：

- 学习阶段：工程化练习。
- 当前阶段完成度：今天是否形成“测试改造 + 运行证据 + 学习日志”的闭环。
- 正确性和可运行性：定向测试和可选全量测试是否通过；失败时是否记录失败命令和原因。
- 代码可读性：fixture 是否服务于测试准备，不制造新的理解成本。
- 学习日志和证据：是否能用自己的话解释 fixture、helper 函数、`tmp_path` 的关系。
- 明日可执行性：明天第一件事应该修什么，必须具体到文件。

## 批改后归档要求

Codex 批改时必须把结果保存到：

- `homework-reviews/2026-06-11-review.md`

批改文件必须使用 `templates/homework-review-template.md` 的结构，包括：

- 总评
- 分项评分
- 必改项
- 建议改进项
- 代码反馈
- 学习日志反馈
- 明日修改任务
- 是否建议上传 GitHub
- 复查结果
