## 任务卡：interface 和数据形状

> 适用卡点：当本周主问题需要“interface 和数据形状”相关能力、实验或证据时选择。
> 使用规则：这是一张可选任务卡，没有指定日期或前后顺序；未选择或未完成不形成补债。

本周主题：TypeScript 与 Next.js 页面

任务问题：TypeScript 已经写了类型，为什么真实 API 数据仍然需要校验？

参考投入上限：2-3 小时。只做到足以推进本周主问题的深度，未选内容不延期、不补做。

## 0. 任务在项目中的位置

- 已知基础：使用基础类型、union 和 object type 描述摘要结果。
- 本任务：把请求和响应结构写完整，并区分编译期检查与运行时校验。
- 后续：在 Next.js 页面中真正使用这些数据形状。

## 1. 先回忆，不看答案（10 分钟）

1. 不看基础类型任务卡，重写 `SummaryMode` 和 `SummaryResult` 的字段草稿。
2. 微型变式：增加一个 `success: boolean` 字段。
3. 写下 `type` 是否会自动阻止服务器返回错误 JSON。

完成后再打开已知基础文件核对，不要求一字不差。

## 2. 真实问题情境

你在代码中声明响应包含 `summary` 和 `inputChars`，但服务端实际返回：

```json
{
  "summary": "一段摘要"
}
```

网络返回的数据来自程序外部。即使本地类型写得正确，服务器仍可能缺字段、返回旧版本数据或返回错误页面。

## 3. 先预测

1. TypeScript 会在网络响应到达时自动补上 `inputChars` 吗？
2. `as SummarizeResponse` 是检查数据，还是告诉编译器“相信我”？
3. 运行时最少应该检查哪些字段？

## 4. 为什么学

interface 用来统一前后端代码中的数据形状；运行时校验用来检查外部数据是否真的符合这份形状，两者解决不同阶段的问题。

## 5. 最小知识讲解

### 5.1 interface 描述对象应有的字段

```ts
interface UserProfile {
  name: string;
  level: number;
}
```

本任务可以先把 `interface` 理解为“对象结构说明书”。它和 object `type` 在本任务的场景中都能描述固定字段，不需要深入争论全部差异。

### 5.2 类型检查只发生在开发和构建阶段

TypeScript 编译后，interface 不会跟着进入浏览器运行。来自 `fetch`、文件或用户输入的数据仍需要运行时代码检查。

### 5.3 `unknown` 迫使我们先检查

当一个值来源不可信时，使用 `unknown` 表示“当前不知道它是什么”。在读取字段前先用 `typeof`、空值判断和属性检查逐步缩小范围。

与 Python 对照：类型标注描述预期；真正读取 JSON 时仍可能需要检查字典是否存在键、值是否属于正确类型。

常见误区：`value as SummarizeResponse` 不会验证 value，只会绕过一部分编译器怀疑。

## 6. 跟做实验（约 35 分钟）

在 `week-05/interface-practice.ts` 中定义一个与摘要无关的 `UserProfile`，再写 `validateUserProfile(value: unknown): boolean`。

至少检查：

- value 不是 `null`。
- value 是 object。
- `name` 是 string。
- `level` 是 number。

分别传入正确对象、缺少 level 的对象和 level 为字符串的对象，记录结果。

暂停并解释：为什么定义了 `UserProfile` 后，还要写 `validateUserProfile`？

## 7. 核心动手任务（约 45-60 分钟）

在已知基础练习基础上完成：

1. 定义 `SummarizeRequest` interface：包含文本和摘要模式。
2. 定义 `SummarizeResponse` interface：包含摘要、模式和输入字符数。
3. 在注释或学习日志中记录每个字段的含义。
4. 写 `validateMockResponse(value: unknown): boolean`，检查核心字段是否存在且类型正确。
5. 使用一个有效 mock 和至少一个无效 mock 验证函数。

验收条件：有效对象返回 `true`；缺字段或字段类型错误的对象返回 `false`；不能只用类型断言假装完成校验。

## 8. 迁移挑战（约 20 分钟）

准备两份新数据：

- 缺少 `inputChars`。
- `mode` 为 `"short"`。

让校验函数都能拒绝它们，并解释这两个错误分别违反了哪条契约。

## 9. 卡住时的分级提示

<details>
<summary>提示 1：应该回忆什么</summary>

先确认 value 是非空对象，再逐个检查属性。字符串 union 的运行时校验需要显式比较允许值。

</details>

<details>
<summary>提示 2：检查哪个范围</summary>

校验顺序可以是：对象本身、summary、mode、inputChars。每一步都应产生 boolean 条件。

</details>

<details>
<summary>提示 3：半成品伪代码</summary>

```ts
function validateMockResponse(value: unknown): boolean {
  if (typeof value !== "object" || value === null) return false;
  // 检查 summary
  // 检查 mode 是否属于两个允许值
  // 检查 inputChars
  return true;
}
```

</details>

## 10. 内化检查

1. interface 解决的是哪个阶段的问题？
2. 运行时校验解决的是哪个阶段的问题？
3. 为什么 `as` 不能替代校验？
4. 初始预测哪里需要修正？
5. 后续页面拿到 mock 数据时，哪些代码可以直接复用？

## 11. 科班基础、算法与自由探索

- 基础点：固定数据结构与外部输入校验。
- 项目映射：request/response interface 和 mock 响应校验。
- 最小验收：能解释“预期的数据形状”和“实际收到的数据”为什么可能不同。
- 算法和自由探索按总规则执行，不能挤占核心任务。

## 12. 推荐阅读、证据与后续入口

- TypeScript Handbook - Object Types：https://www.typescriptlang.org/docs/handbook/2/objects.html
- TypeScript Handbook - Narrowing：https://www.typescriptlang.org/docs/handbook/2/narrowing.html

学习日志必须记录文件路径、命令、有效/无效 mock 的实际结果、最高提示等级、迁移结果和 1-3 个具体问题。

后续自然动作：画出页面需要的四个区域，并标出哪个区域读取 `SummarizeResponse`。

## 提交物与验收

- request/response interface。
- `validateMockResponse` 和至少三份验证数据。
- 字段含义与运行结果。
- 本次学习日志。
- 能解释静态类型与运行时校验的边界。
