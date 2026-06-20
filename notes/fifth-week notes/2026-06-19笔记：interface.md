`interface` 是 TypeScript 用来**描述对象结构（形状）**的语法。

如果你学过 Python，可以把它理解成：

> “只规定这个对象应该长什么样，不负责创建对象。”

类似于一种**契约（contract）**。

---

## 最基础的例子

```ts
interface User {
    name: string
    age: number
}

const user: User = {
    name: "Kris",
    age: 19
}
```

这里：

```ts
interface User {
    name: string
    age: number
}
```

规定：

- 必须有 `name`

- 必须有 `age`

- name 必须是 string

- age 必须是 number


---

## 和 type 的区别

你之前问过 type。

很多时候：

```ts
type User = {
    name: string
    age: number
}
```

和

```ts
interface User {
    name: string
    age: number
}
```

效果完全一样。

---

## interface 最常见用途

### 1. 给对象定义结构

```ts
interface Book {
    title: string
    author: string
    pages: number
}
```

---

### 2. 给函数参数定义结构

比如 Python：

```python
def print_user(user):
    print(user["name"])
```

TS：

```ts
interface User {
    name: string
    age: number
}

function printUser(user: User) {
    console.log(user.name)
}
```

调用：

```ts
printUser({
    name: "Tom",
    age: 20
})
```

---

### 3. 给 API 返回值定义结构

这个在 AI 工程里特别常见。

例如：

```json
{
  "id": 1,
  "title": "Hello",
  "completed": false
}
```

定义：

```ts
interface Todo {
    id: number
    title: string
    completed: boolean
}
```

然后：

```ts
const todo: Todo = await fetch(...)
```

IDE 就知道有哪些字段。

---

# 可选属性

有些字段可能不存在。

```ts
interface User {
    name: string
    age?: number
}
```

这里：

```ts
age?
```

表示：

```ts
{
    name: "Tom"
}
```

也是合法的。

---

# 只读属性

```ts
interface User {
    readonly id: number
    name: string
}
```

创建：

```ts
const user: User = {
    id: 1,
    name: "Tom"
}
```

之后：

```ts
user.id = 2
```

会报错。

---

# 描述函数

interface 不仅能描述对象。

还能描述函数长什么样。

```ts
interface AddFunc {
    (a: number, b: number): number
}
```

实现：

```ts
const add: AddFunc = (a, b) => {
    return a + b
}
```

---

# interface 继承

类似 Python 类继承。

```ts
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}
```

最终：

```ts
const dog: Dog = {
    name: "Buddy",
    breed: "Golden Retriever"
}
```

相当于：

```ts
{
    name: string
    breed: string
}
```

---

# TypeScript 项目里最常见的用法

假设你以后做 AI Agent：

```ts
interface Message {
    role: "user" | "assistant"
    content: string
}
```

```ts
interface SummaryRequest {
    text: string
    mode: "brief" | "bullet"
}
```

```ts
interface SummaryResponse {
    summary: string
}
```

然后：

```ts
async function summarize(
    req: SummaryRequest
): Promise<SummaryResponse> {
    ...
}
```

整个项目会非常清晰。

---

对于你目前的阶段，可以先记一句话：

> `type` 和 `interface` 都能定义类型；`interface` 更偏向描述对象结构，尤其用于 API、配置、数据模型；`type` 更灵活，可以定义联合类型、字面量类型、元组等。

以后你学 React、Next.js、AI Agent SDK 时，会看到大量：

```ts
interface User {}
interface Message {}
interface Config {}
interface AgentState {}
```

它们本质上都在做同一件事：

**告诉 TypeScript：这个对象应该长什么样。**