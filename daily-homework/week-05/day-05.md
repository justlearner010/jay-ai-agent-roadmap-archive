## 任务卡：async/fetch mock 流程

> 适用卡点：当本周主问题需要“async/fetch mock 流程”相关能力、实验或证据时选择。
> 使用规则：这是一张可选任务卡，没有指定日期或前后顺序；未选择或未完成不形成补债。

本周主题：TypeScript 与 Next.js 页面

任务问题：结果不能立刻返回时，页面怎样继续运行并在稍后接收结果？

参考投入上限：2-3 小时。只做到足以推进本周主问题的深度，未选内容不延期、不补做。

## 0. 任务在项目中的位置

- 已知基础：页面已经能保存用户输入并判断它是否有效。
- 本任务：把输入交给异步 mock summarize 函数，并在结果返回后展示。
- 后续：在等待和失败期间给用户明确状态。

## 1. 先回忆，不看答案（10 分钟）

1. 画出“用户输入 → state → 页面重渲染”的链路。
2. 微型变式：说明只有空格的输入为什么不能提交。
3. 写下输入文本与字符数中，哪个是 state，哪个是派生值。

## 2. 真实问题情境

真实 LLM 请求可能需要几秒钟。如果代码把“发出请求”和“拿到结果”当成同一时刻，页面会读取到尚未完成的结果，或者无法在等待时继续响应用户。

## 3. 先预测

1. 一个延迟两秒返回的函数，调用后立即得到的是最终摘要吗？
2. `await` 前后的代码执行顺序可能怎样变化？
3. 如果请求失败，函数应该返回假摘要还是抛出错误？

## 4. 为什么学

`Promise`、`async` 和 `await` 用来表达“工作现在开始，结果未来到达”，是页面连接 API 和 LLM 的必要基础。

## 5. 最小知识讲解

### 5.1 Promise 表示未来的结果

Promise 常见状态可以先理解为：等待中、已成功、已失败。异步函数会返回 Promise，即使代码看起来返回的是普通对象。

### 5.2 await 只暂停当前 async 函数

`await` 等待 Promise 成功结果。它不是让整个浏览器停止，而是让当前异步流程在结果到达后继续。

### 5.3 mock 延迟的价值

同步返回的 mock 无法暴露等待期间的 UI 问题。加入 Promise 延迟，可以在不调用真实 API 的情况下练习真实控制流。

与 Python 对照：概念上类似 `async def` 和 `await`，但本任务只要求理解 JavaScript/TypeScript 的 Promise 流程。

常见误区：忘记 `await` 时拿到的是 Promise，不是其中的摘要对象。

## 6. 跟做实验（约 30 分钟）

先写一个与摘要无关的 `loadGreeting(name)`：延迟一秒后返回问候文本。

1. 调用函数但不加 await，观察输出是什么。
2. 在 async 函数中使用 await，再观察输出。
3. 在等待前后打印日志，记录实际顺序。

暂停并解释：为什么两次输出不同？哪一个值代表“未来结果”？

## 7. 核心动手任务（约 50-60 分钟）

1. 写 typed async `summarize(text, mode)` 函数。
2. 使用 Promise 延迟模拟请求。
3. 返回符合 `SummarizeResponse` 的摘要、模式和字符数。
4. 点击按钮时传入当前输入并等待结果。
5. 用 state 保存结果并显示摘要和要点。

验收条件：点击后不是立即得到同步常量；结果符合既有类型；重复输入不同文本时字符数或摘要展示能够对应变化。

故意删除一次 `await` 或给函数错误返回类型，观察提示后修复。

## 8. 迁移挑战（约 20 分钟）

让 mock 函数在文本包含 `[fail]` 时拒绝 Promise 或抛出错误。本任务只需确认错误确实发生并能被调用方捕获，UI 错误展示留到后续。

## 9. 卡住时的分级提示

<details>
<summary>提示 1：应该回忆什么</summary>

异步函数返回 Promise；调用方需要在 async 上下文中等待结果，再更新结果 state。

</details>

<details>
<summary>提示 2：检查哪个范围</summary>

分开检查 mock 函数的参数/返回类型、按钮事件是否 async、await 的位置和结果 state。

</details>

<details>
<summary>提示 3：半成品伪代码</summary>

```ts
async function summarize(text: string, mode: SummaryMode): Promise<______> {
  await new Promise((resolve) => setTimeout(resolve, ______));
  if (text.includes("[fail]")) ______;
  return { /* 使用参数生成结果 */ };
}
```

</details>

## 10. 内化检查

1. Promise 表达的是什么？
2. async 函数为什么不能声明成直接返回 `SummaryResult`？
3. 忘记 await 时，调用方拿到什么？
4. mock 延迟为后续暴露了什么 UI 问题？
5. 用自己的话复述“点击 → 调用 → 等待 → 更新结果”。

## 11. 科班基础、算法与自由探索

- 基础点：同步流程与异步流程。
- 项目映射：mock 请求模拟未来真实 API 调用。
- 最小验收：能按时间顺序解释 await 前后的行为。
- 算法和自由探索按总规则执行。

## 12. 推荐阅读、证据与后续入口

- TypeScript Handbook - More on Functions：https://www.typescriptlang.org/docs/handbook/2/functions.html
- MDN - Using promises：https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises
- MDN - Fetch API：https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

记录文件路径、启动命令、日志顺序、成功与 `[fail]` 结果、最高提示等级、迁移结果和 1-3 个具体问题。

后续自然动作：写出请求等待期间用户至少需要看到什么，以及失败后不能继续保留什么状态。

## 提交物与验收

- typed async summarize 函数和 Promise 延迟。
- 页面调用与结果展示。
- 可触发的失败分支。
- 运行证据和学习日志。
- 能解释异步控制流，而不是只会套用 `async/await`。
