# Week 06：AI 学习助手 Next.js 前端雏形

日期：2026-06-22 至 2026-06-28

唯一主交付物：完成可输入文本、选择 summary mode、提交 typed mock，并显示四种状态的 Next.js 页面。

## 每日节奏

### 周一：契约与验收

- 回顾 `SummarizeRequest`、`SummarizeResponse` 和 validator 的边界。
- 创建页面最小结构，画出标题、输入区、模式选择、按钮和结果区。
- 写下本周验收命令和两个证据位置。

### 周二：输入与模式

- 完成文本输入和 `brief` / `bullets` 选择。
- 确保两个模式与 `SummaryMode` 一致，不使用任意 `string` 代替。

### 周三：页面状态

- 实现 `idle`、`loading`、`success`、`error` 状态。
- 按钮提交后使用 typed mock 模拟返回，不接真实 API。

### 周四：错误路径

- 空输入时进入 `error`。
- 对一个缺字段或错误 mode 的 mock 运行 validator，不展示为成功结果。

### 周五：测试与复查

- 运行 TypeScript check 和 Next.js build，修复真实报错。
- 至少验证成功路径和一个错误路径。
- 复查是否把运行时校验错误地交给了 `as`。

### 周六：集成与文档

- 补 README 安装、启动、验证命令和 mock 边界。
- 保存四种状态的截图或可替代的测试证据。

### 周日：验收与追踪

- 从安装、启动到主流程重跑一次。
- 整理真实 commit，更新周日复盘和 tracker。
- 写下下周 mock API route 的第一步，不在本周提前实现。

## Java 副线（2 小时上限）

- 只完成一个 Java 小函数和一个运行或 JUnit 证据。
- 超时则停止，不影响 Next.js 主交付物。

## 删减顺序

主线超时时，依次删掉：开源阅读、自由探索、长笔记、算法 AC 要求。保留主功能、一个证据和三行日志。
