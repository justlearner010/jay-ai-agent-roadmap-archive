# 第 4 周 Day 2：参数化测试

日期：2026-06-12（周五）

本周主题：pytest 与后端前置能力

今日目标：把已经开始的 `pytest.mark.parametrize` 学习落到 `summarize_text()` 测试里，用少量测试代码覆盖多组输入。

预计投入：2-3 小时。如果当天时间少，只完成“必做”的前 3 项，并在学习日志里说明延期项。

## 作业要求

### 必做

1. 复查今天已经改过的测试文件：
   - `python-foundations/first-CLI/tests/test_summarize.py`
2. 确认参数化测试覆盖了至少 3 类输入：
   - 英文文本
   - 中文带空格文本
   - 空文本
3. 保留并解释 1 个预期失败用例，例如中文不带空格分词尚未实现时使用 `pytest.mark.xfail`。
4. 运行 `test_summarize.py` 的定向 pytest，并把命令和结果写进学习日志。
5. 在学习日志里用自己的话解释：什么时候适合用 `parametrize`，什么时候不适合。
6. 整理 1-3 个准备提交给 Codex 批改的问题，问题必须指向具体测试、参数列表、`xfail` 或概念。
7. 写下明天第一步：继续改哪一个测试文件，具体到文件名。

### 选做

1. 清理 `test_summarize.py` 顶部已经注释掉的旧测试代码，避免文件噪音影响阅读。
2. 选择一个旧测试文件尝试参数化：
   - `python-foundations/first-CLI/tests/test_word_freq.py`
   - `python-foundations/first-CLI/tests/test_word_chunk.py`
3. 如果时间够，运行项目全量测试，确认参数化改造没有破坏其他测试。

## 推荐阅读材料

- pytest - Parametrizing tests：https://docs.pytest.org/en/stable/how-to/parametrize.html

## 提交物

提交批改时，按 `templates/daily-homework-submission-template.md` 整理，至少包含这些项：

代码文件：

- `python-foundations/first-CLI/tests/test_summarize.py`
- 选做改动到的其他测试文件

测试文件：

- `python-foundations/first-CLI/tests/test_summarize.py`

学习日志：

- `learning-log/fourth-week-log/2026-06-12日志.md`

学习笔记：

- 如果今天新增了参数化测试笔记，列出对应 `notes/` 文件。
- 如果没有新增笔记，说明今天只更新学习日志。

运行证据：

- 定向 pytest 命令和结果。
- 如果跑了全量测试，也记录全量 pytest 命令和结果。

希望 Codex 重点批改：

- `parametrize` 是否真的减少重复测试代码。
- 参数列表是否覆盖英文、中文、空文本和非法 mode。
- `xfail` 是否用在“已知未实现但值得记录”的场景，而不是掩盖普通失败。
- 明天应该优先继续改哪个测试文件。

当前是否已经上传 GitHub：

- [ ] 已上传
- [ ] 还没上传，等批改后再上传

## 验收标准

Codex 会按 `templates/homework-review-template.md` 批改，评分映射如下：

- 当前阶段完成度 30 分：是否完成 `test_summarize.py` 的参数化改造；是否符合第 4 周“pytest 与后端前置能力”的阶段目标。
- 正确性和可运行性 25 分：定向 pytest 是否通过；`xfail` 是否是预期失败，不是普通错误。
- 代码可读性 15 分：参数列表是否清楚；测试函数命名是否准确；旧注释代码是否影响阅读。
- 学习日志和证据 20 分：学习日志是否记录修改文件、运行命令、实际结果、parametrize 的适用场景和卡点。
- 明日可执行性 10 分：明天第一步是否具体到一个测试文件和一个动作。

## 批改重点

提交给 Codex 批改时，重点看：

- 学习阶段：工程化练习。
- 当前阶段完成度：今天是否形成“参数化测试 + 运行证据 + 学习日志”的闭环。
- 正确性和可运行性：`test_summarize.py` 定向测试是否通过；失败用例是否清楚标记为 `xfail`。
- 代码可读性：参数化是否让测试更集中，而不是让参数表难读。
- 学习日志和证据：是否能用自己的话解释 `parametrize` 解决的是“同一逻辑多组输入”的问题。
- 明日可执行性：明天第一件事应该修什么，必须具体到文件。

## 批改后归档要求

Codex 批改时必须把结果保存到：

- `homework-reviews/2026-06-12-review.md`

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
