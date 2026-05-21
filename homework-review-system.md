# 每日作业批改系统

目标：让每天的学习形成闭环。不是只“学了”，而是每天都有作业、批改、修改、复查和 GitHub 证据。

## 每日流程

1. 当天完成学习任务和代码练习。
2. 用 `templates/daily-learning-log-template.md` 写学习日志。
3. 用 `templates/daily-homework-submission-template.md` 整理作业提交信息。
4. 对 Codex 说：`codex，批改今天作业`。
5. Codex 按 `templates/homework-review-template.md` 批改。
6. 第二天优先修改“必改项”。
7. 修改后再次提交给 Codex 复查。
8. 通过后再推送到 GitHub，或由 Codex 帮你提交并推送。

## 批改范围

每天批改这些内容：

- 代码文件。
- 测试或运行结果。
- 学习日志。
- 截图或 demo。
- commit 或准备提交的改动。
- 是否符合本周计划。

## 评分标准

总分 100 分：

- 功能完成度：25 分。
- 代码质量：20 分。
- 测试/运行证据：20 分。
- 学习日志质量：20 分。
- 计划匹配度：15 分。

## 批改等级

- 90-100：优秀，可以直接进入下一个任务。
- 75-89：合格，有少量修改项。
- 60-74：勉强合格，第二天必须先修改。
- 60 以下：当天作业没有形成有效闭环，需要重做关键部分。

## 必改项和建议项

批改时分两类：

- 必改项：影响正确性、可运行性、测试、理解或后续项目复用的问题。
- 建议项：代码风格、命名、README、日志表达、额外测试等。

第二天优先做必改项。建议项可以在本周内逐步补。

## 复查规则

复查只看三件事：

1. 必改项是否完成。
2. 是否产生新的问题。
3. 是否可以上传 GitHub。

复查通过后，在 `trackers/homework-review-log.csv` 里更新状态。

## 你每天提交给 Codex 的推荐格式

```text
codex，批改今天作业。

今天的代码：
- python-foundations/xxx.py
- python-foundations/tests/test_xxx.py

学习日志：
- learning-log/YYYY-MM-DD.md

我希望你重点看：
- 代码是否正确
- 是否适合写测试
- 明天应该怎么改
```

