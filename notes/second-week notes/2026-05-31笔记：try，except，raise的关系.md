
## `raise` —— 抛出异常

`raise` 用来告诉 Python **程序出现了问题，需要跳出当前流程**。

示例：

```
def divide(a, b):    if b == 0:        raise ZeroDivisionError("不能除以0")    return a / b
```

- 当 `b==0` 时，`raise` 抛出异常
- 程序会立刻停止当前函数的执行
- 如果没有捕获这个异常，程序就会崩掉

---

## 2️⃣ `try` —— 尝试执行可能报错的代码

`try` 块里写 **可能出现异常的代码**，Python 会监控它。

```
try:    result = divide(10, 0)except ZeroDivisionError:    print("捕获到除零错误")
```

- Python 进入 `try` 执行
- 如果没有异常，`except` 块不执行
- 如果出现异常，Python 会停止 `try` 中后续语句，跳到匹配的 `except` 块

---

## 3️⃣ `except` —— 捕获异常

`except` 用来处理 `try` 中抛出的异常。

```
try:    result = divide(10, 0)except ZeroDivisionError as e:    print(f"错误信息：{e}")
```

- `as e` 可以拿到异常对象
- `except` 块里可以决定如何响应：打印、忽略、重新 `raise` 等
- 只捕获指定类型的异常，其他异常会继续向上抛

---

## 4️⃣ 三者关系总结

流程图可以这样理解：

```
[执行程序]      │     ▼[try块]      │     ├── 如果没有异常 → 跳过 except → 继续执行后续     │     └── 如果有异常 → 停止 try，查找匹配 except                     │                     ├─ 匹配成功 → 执行 except → 继续执行 try 后面的代码或 finally                     └─ 匹配失败 → 异常继续向上抛
```

而 `raise` 就是 **触发异常的动作**：

- 可以在函数内部抛出异常
- 可以在 except 内部重新抛出异常

示例：

```
try:    x = int(input("请输入一个整数: "))    if x < 0:        raise ValueError("不能输入负数")except ValueError as e:    print(f"捕获到错误：{e}")
```

---

## 5️⃣ 额外补充：finally 和 else

```
try:    # 尝试执行    result = 10 / xexcept ZeroDivisionError:    # 异常处理    print("除零")else:    # 没有异常才执行    print("运算成功")finally:    # 不管有没有异常都会执行    print("结束")
```

- `else`：try 成功时执行
- `finally`：无论如何执行，常用于释放资源

---

**总结一句话**：

- `raise` → 主动抛异常
- `try` → 尝试执行可能报错的代码
- `except` → 捕获和处理异常

你可以把它想成 **“报警器 + 防护网”**：

- `raise` 是报警器
- `try` 是防护网
- `except` 是防护网上的缓冲区，让程序不会崩掉