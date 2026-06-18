# 第 5 周 Day 1：TypeScript 基础类型

日期：2026-06-22（周一）

本周主题：TypeScript 与 Next.js 页面

今日主问题：怎样在程序运行前发现摘要数据中的类型错误？

预计投入：2-3 小时。理解和讲解约 40%，编码、验证和迁移约 60%。时间不足时，优先完成核心动手任务、类型检查和学习日志。

## 0. 今天在项目中的位置

- 昨天：你为 `/api/summarize` 设计了 request、success response 和 error response。
- 今天：把 JSON 草稿变成 TypeScript 能检查的数据契约。
- 明天：把一个结果类型扩展为完整的 request/response interface，并讨论运行时校验。

## 1. 先回忆，不看答案（10 分钟）

关闭第四周复盘，凭记忆写出 `/api/summarize` 成功响应中至少 3 个字段，并标注每个字段应该保存文本、数字还是布尔值。

再回答：如果 `inputChars` 收到的是 `"54"` 而不是 `54`，程序可能在哪里暴露问题？先写预测，不搜索。

## 2. 真实问题情境

后端返回了一份看起来像摘要结果的数据：

```json
{
  "summary": "TypeScript 可以提前发现一部分数据错误。",
  "mode": "short",
  "inputChars": "54"
}
```

页面需要显示摘要、判断模式并比较输入长度。字段都有值，但其中一些值不符合项目约定。只靠肉眼检查，错误很容易进入后续页面代码。

## 3. 先预测

在学习日志中先写下：

1. 上面三个字段中，哪些值可能有问题？
2. JavaScript 会在创建这个对象时立即报错吗？
3. 你希望编辑器在什么时候提醒你？

## 4. 今天为什么学

TypeScript 基础类型用于把“我们认为数据应该长什么样”写成编译器可检查的约定，减少错误数据继续流入页面、状态和 API 调用。

## 5. 最小知识讲解

### 5.1 今天只学五类类型

```ts
const title: string = "学习助手";
const inputChars: number = 54;
const loading: boolean = false;
const keywords: string[] = ["TypeScript", "类型"];
const mode: "brief" | "bullets" = "brief";
```

- `string`、`number`、`boolean` 描述单个基础值。
- `string[]` 表示元素都应是字符串的数组。
- `"brief" | "bullets"` 是 union，表示值只能二选一；普通 `string` 则允许任意文本。

### 5.2 object type 是一份数据形状约定

```ts
type ReadingProgress = {
  bookTitle: string;
  pagesRead: number;
  finished: boolean;
};
```

它描述每个字段是否存在以及字段值的类型。TypeScript 检查代码，不会改变对象在运行时的实际内容。

### 5.3 和 Python 的联系

- Python `list[str]` 与 TypeScript `string[]` 都表达“字符串列表”。
- Python `dict` 可以保存动态键值；TypeScript object type 常用来描述字段固定的业务对象。
- Python 和 TypeScript 的类型提示都帮助阅读与检查代码，但 TypeScript 前端项目通常会在构建阶段强制检查。

常见误区：类型不是为了多写代码，而是为了让字段改名、缺失或类型错误尽早暴露。

## 6. 跟做实验（约 30 分钟）

创建练习文件 `week-05/types-practice.ts`。如果本地暂时没有 TypeScript 环境，可以先在 TypeScript Playground 运行，但仍要保存本地文件。

1. 定义 `ReadingProgress`，字段使用上面的示例。
2. 创建一个符合类型的对象。
3. 把 `pagesRead` 故意改成字符串，观察编辑器或类型检查结果。
4. 修正错误，并记录报错中最关键的一句话。

本地有 TypeScript 时运行：

```bash
npx tsc --noEmit week-05/types-practice.ts
```

暂停并解释：为什么 `pagesRead: "20"` 看起来有数字，却仍不属于 `number`？

## 7. 核心动手任务（约 45-60 分钟）

在同一个练习文件中独立完成：

1. 定义 `SummaryMode`，只允许 `brief` 和 `bullets`。
2. 定义 `SummaryResult`，包含 `summary`、`mode`、`inputChars`。
3. 创建一个 `mockSummary` typed object。
4. 故意让一个字段类型错误，运行检查后再修复。

验收条件：

- `mockSummary` 缺字段、字段类型错误或 mode 越界时，类型检查能够提醒。
- 修复后类型检查不再报告该错误。
- 你能指出类型约束的是哪一个字段，而不是只说“代码红了”。

## 8. 迁移挑战（约 20 分钟）

产品希望摘要结果增加 `keywords`，它必须是一个字符串数组。

独立修改类型和 mock 数据，并验证：

- 多个字符串可以通过检查。
- 混入数字时会出现类型错误。

## 9. 卡住时的分级提示

按顺序展开，能继续就不要看下一级。

<details>
<summary>提示 1：应该回忆什么</summary>

对象中的每个字段都需要“字段名 + 对应类型”；多个允许值使用 union，多个同类元素使用数组类型。

</details>

<details>
<summary>提示 2：检查哪个范围</summary>

先检查 `SummaryMode` 是否限制了两个字符串值，再检查 `SummaryResult` 中三个字段是否分别引用了正确类型。

</details>

<details>
<summary>提示 3：半成品结构</summary>

```ts
type SummaryMode = "brief" | ______;

type SummaryResult = {
  summary: ______;
  mode: ______;
  inputChars: ______;
};
```

</details>

## 10. 内化检查

不看代码回答：

1. TypeScript 类型在什么时候帮助我们发现错误？
2. `mode: string` 和 `mode: "brief" | "bullets"` 有什么区别？
3. `string[]` 解决了什么约束问题？
4. 你的初始预测哪里正确，哪里需要修正？
5. 如果删除文件，你会按什么顺序重写 `SummaryResult`？

## 11. Java 副线任务（30-45 分钟）

1. 创建或规划一个最小 Maven 练习目录。
2. 从第 1-2 周 Python 文本处理练习中选一个，用 Java 重写最小函数，例如统计字符串长度、拆分单词或过滤空字符串。
3. 写下 Python `list` / `dict`、Java `List` / `Map`、TypeScript array / object 的用途区别。
4. 今天不要求 Spring Boot；主线超时时可以只完成目录规划和方法签名。

## 12. 科班基础、算法与自由探索

- 基础点：字符串、数组、哈希表。
- 项目映射：TypeScript 类型和 Java 文本处理函数。
- 最小验收：能解释三种语言中列表、映射和固定业务对象的用途区别。
- 算法：按总规则进行 20-30 分钟 Easy 微练习，主线超时可只写伪代码。
- 自由探索：可选，不能替代核心动手任务。

## 13. 推荐阅读、证据与明日入口

推荐材料：

- `resources/cs-foundations-side-track.md` 的 Week 5 Day 1
- `resources/java-side-track.md` 的“Java 基础函数”
- TypeScript Handbook - Everyday Types：https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

学习日志必须记录：

- 新增或修改的文件路径。
- 运行命令和实际结果。
- 故意制造并修复的类型错误。
- 迁移挑战结果。
- 最高提示等级：0 / 1 / 2 / 3。
- 1-3 个准备提交给 Codex 的具体问题。
- 明天第一步：打开今天的类型文件，在不看答案的情况下写出 request 和 response 的字段草稿。

## 提交物与验收

- `SummaryResult`、typed mock 和 `keywords` 迁移结果。
- 一次类型检查证据或 Playground 检查结果。
- 当天学习日志。
- 能解释类型与 AI 学习助手数据契约的关系；只交代码但不能解释，不算完整掌握。
