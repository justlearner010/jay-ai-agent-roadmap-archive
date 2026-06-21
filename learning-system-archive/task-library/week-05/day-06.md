## 任务卡：loading 和 error 状态

> 适用卡点：当本周主问题需要“loading 和 error 状态”相关能力、实验或证据时选择。
> 使用规则：这是一张可选任务卡，没有指定日期或前后顺序；未选择或未完成不形成补债。

本周主题：TypeScript 与 Next.js 页面

任务问题：页面怎样准确表达“尚未请求、正在等待、成功、失败”四种情况？

参考投入上限：2-3 小时。只做到足以推进本周主问题的深度，未选内容不延期、不补做。

## 0. 任务在项目中的位置

- 已知基础：页面可以发起异步 mock 总结，也能制造成功和失败。
- 本任务：让用户看懂等待和失败，并避免状态互相冲突。
- 后续：把类型、状态和异步流程作为一个整体进行综合复盘。

## 1. 先回忆，不看答案（10 分钟）

1. 复述“点击 → Promise → await → 更新结果”的顺序。
2. 微型变式：如果忘记 await，结果 state 可能收到什么？
3. 写出 `[fail]` 分支的目的。

## 2. 真实问题情境

用户点击总结后，两秒内页面毫无变化，可能误以为按钮失效并连续点击；请求失败时旧摘要仍留在页面，用户也无法判断它是否属于本次输入。

## 3. 先预测

1. 请求开始时应清除哪些旧状态？
2. 成功和失败是否应该同时显示？
3. loading 为 true 时按钮应如何处理？
4. `finally` 可能适合负责哪一项收尾？

## 4. 为什么学

loading 和 error 不是装饰文字，而是异步流程对用户的可见状态；明确状态转换能减少重复请求、旧数据误导和无法恢复的错误。

## 5. 最小知识讲解

### 5.1 先用四状态理解页面

```text
idle -> loading -> success
                 -> error
```

- idle：尚未发起请求。
- loading：请求进行中。
- success：有当前请求的有效结果。
- error：当前请求失败，并有可读错误信息。

本任务可以使用多个 state 实现，但必须保证展示逻辑不矛盾。以后再讨论 reducer 或正式状态机。

### 5.2 try/catch/finally 对应流程职责

- `try`：等待可能成功的工作。
- `catch`：把失败转换成用户可理解的信息。
- `finally`：无论成功失败都结束 loading。

### 5.3 边界输入也是测试

正常文本验证 success；`[fail]` 验证 error；连续点击验证 loading 期间的行为。

与 pytest 对照：这仍然是在准备正常路径和异常路径，只是证据来自 UI 状态。

常见误区：只把错误打印到 console，用户界面仍然没有可行动的信息。

## 6. 跟做实验（约 25 分钟）

为已知基础 `loadGreeting` 实验增加 `loading` 和 `error`：

1. 请求前进入 loading 并清理旧错误。
2. 成功后显示结果。
3. 失败后显示可读错误。
4. 无论结果如何都退出 loading。

暂停并解释：为什么新请求开始时要清理旧错误？

## 7. 核心动手任务（约 45-60 分钟）

修改 AI 学习助手页面：

1. 加入 loading 状态和等待提示。
2. 加入 error 状态和用户可读提示。
3. 使用 try/catch/finally 组织异步调用。
4. 在 loading 期间避免重复提交。
5. 用正常文本和 `[fail]` 各验证一次，并留下记录或截图。

验收条件：等待、成功、失败可以被明确区分；失败后页面仍能再次提交并恢复；错误不会和成功结果混成同一次请求结果。

## 8. 迁移挑战（约 20 分钟）

任选一个完成：

- 新请求开始时清除旧结果，避免旧摘要被误认为本次结果。
- 请求失败后保留输入文本，让用户修改后重试。

写下你的选择及理由。

## 9. 卡住时的分级提示

<details>
<summary>提示 1：应该回忆什么</summary>

一次请求需要明确开始、成功、失败和统一收尾；每次状态更新都应能对应其中一个阶段。

</details>

<details>
<summary>提示 2：检查哪个范围</summary>

检查提交函数开头、await 周围、catch、finally，以及按钮 disabled 和条件渲染。

</details>

<details>
<summary>提示 3：半成品伪代码</summary>

```ts
setLoading(true);
setError(______);
try {
  const nextResult = await ______;
  setResult(______);
} catch (caughtError) {
  setError(______);
} finally {
  setLoading(______);
}
```

</details>

## 10. 内化检查

1. idle、loading、success、error 各表示什么？
2. 为什么 loading 期间要防止重复提交？
3. catch 和 finally 的职责有什么不同？
4. 一个正常输入和一个边界/失败输入分别是什么？
5. 如果错误提示一直不消失，你会先检查哪次状态转换？

## 11. Java 副线任务（45-60 分钟）

1. 给本周 Java 小函数补 1 个 JUnit 测试。
2. 记录 JUnit 和 pytest 在写法、断言、运行命令上的一个相同点和一个不同点。
3. 不增加新 Java 功能，只验证已有练习。
4. 至少准备一个正常输入和一个边界输入；主线超时可以只完成测试计划。

## 12. 科班基础、算法与自由探索

- 基础点：测试边界。
- 项目映射：JUnit 测 Java 小函数，主线验证 UI 正常与失败状态。
- 最小验收：能说出一个正常输入和一个边界输入。
- 算法和自由探索按总规则执行。

## 13. 推荐阅读、证据与后续入口

- `resources/cs-foundations-side-track.md` 的 Week 5 Day 6
- `resources/java-side-track.md` 的“Maven 和 JUnit”
- React Docs - Conditional Rendering：https://react.dev/learn/conditional-rendering

记录页面文件、正常/失败运行证据、状态错误及修复、迁移结果、最高提示等级、JUnit 证据或计划和 1-3 个具体问题。

后续自然动作：关闭代码，用纸或 Markdown 画出“输入 → state → async summarize → success/error UI”的完整流程。

## 提交物与验收

- loading、error、成功恢复和重复提交限制。
- 正常路径与失败路径证据。
- Java JUnit 测试或明确计划。
- 本次学习日志。
- 能解释状态转换，而不是只展示两个布尔变量。
