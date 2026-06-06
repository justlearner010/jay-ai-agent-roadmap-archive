# 第二周周中总结批改

日期：2026-06-03

归档文件：

- `homework-reviews/2026-06-03-week-02-summary-review.md`

批改对象：

- `learning-log/weekly_review/第二周复盘.md`

说明：今天是 2026-06-03，第二周还没结束。本次按“周中总结”批改，不按周日最终复盘标准扣满。

## 总评

评分：74/100
等级：合格，但需要补证据和结构

一句话评价：这份总结能看出你本周确实在推进 Python 基础、pytest、异常处理和数据结构练习；但它现在更像“文件列表 + 感受”，还没有把计划、证据、测试结果、遗留问题和下周动作连成闭环。

## 分项评分

- 计划对齐：17/25
- 证据完整度：18/25
- 复盘深度：17/25
- 下步可执行性：17/25

## 做得好的地方

1. 实际交付物列出了主要代码文件和测试文件，说明你开始用文件证据说话，而不是只写“我学习了 Python”。
2. “本周进步”能抓住几个真实能力变化：类、封装、pytest、类型错误、工程化意识。
3. “自由探索”写得不错，尤其是没有把 `AI Engineering from Scratch` 直接变成主线，而是判断为阶段性参考，这符合当前计划。
4. 当前我实际运行 `python-foundations/practice/.venv/bin/python -m pytest python-foundations -q`，结果是 `23 passed`，说明代码测试状态比 6 月 2 日批改时更好了。

## 必改项

1. 把“原计划交付物”写具体。当前只写了“python练习与测试”，太泛。应该对齐第 2 周计划：`完成 20 个 Python 小练习，其中至少 5 个有 pytest 测试`。
2. 补上缺失的模板字段：`本周嵌入的科班基础`、`本周算法微练习`、`证据链接` 现在没有写。
3. 把实际交付物从“文件名列表”升级成“文件 + 作用 + 测试结果”。例如：`two_sum.py：用 dict 实现查找；test_two_sum.py 覆盖找到、空列表、负数场景`。

## 具体问题

- 第 19 行写的是 `test_groups_word.py`，实际文件是 `python-foundations/practice/tests/test_group_words.py`，文件名不一致。
- “测试结果”没有写进总结。当前实际可写成：`python-foundations 全量：23 passed`。
- “本周困难”写得真实，但还缺对应策略。你写“有时候想不到怎么得到正确答案”，下一步应该写成规则：先写输入输出样例，再写伪代码，再问 AI 要策略，不直接要答案。
- “下周计划”里的 `first-CLI-V2` 是好方向，但太大。需要拆成 2-3 个最小动作，例如：整理参数解析、增加 mock summary 函数、保存 JSON 输出。
- 当前仍有代码问题没有反映在总结里：`list_max([])` 的测试函数还没有被 pytest 收集，`main.py` 仍有尾随空格，`git diff --check` 会失败。

## 建议改法

可以直接补这几段：

```md
## 本周嵌入的科班基础

项目卡点：去重、分组、两数之和、按字段排序。
对应基础：list 顺序遍历、dict 快速查找、哈希表、异常边界。
如何用到项目中：用 dict 降低重复查找，用 pytest 固定输入输出。

## 本周算法微练习

完成题数：2-3 个小练习。
主要题型：去重、分组、两数之和。
最常卡住的数据结构或思路：dict 的 key/value 设计，以及异常测试。
下周算法练习是否需要调整：继续每天 1 题以内，不做题海。

## 证据链接

- `python-foundations/practice/src/two_sum.py`
- `python-foundations/practice/tests/test_two_sum.py`
- `python-foundations/practice/src/groups_words.py`
- `python-foundations/practice/tests/test_group_words.py`
- pytest：`23 passed`
```

## 是否建议上传 GitHub

- [ ] 可以上传
- [x] 修改后再上传
- [ ] 暂不上传，需要重做关键部分

说明：总结值得保留，但建议先补齐模板字段、修正文件名、写入测试结果，再和本周代码一起提交。

## 明日修改任务

1. 修正 `learning-log/weekly_review/第二周复盘.md` 的文件名、证据链接和缺失字段。
2. 把 `list_max` 的空列表测试改成会被 pytest 收集，并修掉 `main.py` 尾随空格。
3. 把 `first-CLI-V2` 拆成 3 个最小任务，写进下周计划。
