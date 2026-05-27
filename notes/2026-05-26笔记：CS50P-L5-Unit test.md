
# Unit Tests（单元测试）

也就是：

> 用代码测试代码。

课程主要围绕：

- 为什么要测试
- 如何手动测试
- assert
- pytest
- 测试设计思想

展开。

---

# 一、为什么需要 Unit Test

以前你测试代码：

```
python calculator.py
```

然后手动输入：

```
23
```

看看结果对不对。

这种方式的问题：

- 很慢
- 不系统
- 容易漏掉边界情况
- 每次都要人工操作

所以工程里会：

> 专门写“测试代码”去验证主程序。

---

# 二、测试的对象：函数（Function）

课程里强调：

> Unit（单元）通常指函数。

例如：

```
def square(n):    return n * n
```

这个函数：

- 输入明确
- 输出明确

因此特别适合测试。

---

# 三、`if __name__ == "__main__"`

这是为了：

> 防止 import 时自动执行 main()

比如：

```
if __name__ == "__main__":    main()
```

意义：

- 直接运行文件 → 执行 main
- 被别的文件 import → 不执行 main

因为测试文件需要：

```
from calculator import square
```

所以必须避免 import 时程序自己跑起来。

---

# 四、测试文件命名规范

课程采用：

```
test_calculator.py
```

规则：

```
test_ + 被测试模块名
```

pytest 会自动识别这种文件。

---

# 五、导入待测试函数

```
from calculator import square
```

这样测试代码就能调用：

```
square(2)
```

了。

---

# 六、最原始的测试方式

David 先写：

```
if square(2) != 4:    print("2 squared was not 4")
```

本质：

```
如果结果不符合预期 → 报错
```

这已经是测试思想了。

---

# 七、Corner Case（边界情况）

这是本节课特别重要的思想。

不能只测：

```
23
```

还应该测：

- 0
- 负数
- 特殊值

因为：

> bug 往往出现在边界情况。

---

# 八、为什么多个测试很重要

David 故意把：

```
return n * n
```

改成：

```
return n + n
```

这时：

```
2 + 2 == 4
```

居然还能通过。

但：

```
3 + 3 != 9
```

失败了。

说明：

> 一个测试通过 ≠ 程序正确。

---

# 九、`assert`

这是本节最核心的新语法。

```
assert square(2) == 4
```

意思：

> 我断言这件事必须成立。

如果成立：

- 什么都不发生

如果失败：

- 抛出 AssertionError

---

你可以理解成：

```
if 条件不成立:    报错
```

但更简洁。

---

# 十、AssertionError

assert 失败后：

```
AssertionError
```

会出现 traceback。

这是一种：

> 测试失败信号。

课程这里其实是在告诉你：

> 测试代码本身也是程序。

---

# 十一、try / except 捕获测试失败

David 后来写：

```
try:    assert square(2) == 4except AssertionError:    print("2 squared was not 4")
```

这是：

- assert 负责检测
- except 负责友好提示

但问题：

> 太啰嗦了。

---

# 十二、测试设计思想

课程强调：

不要只测：

- 正常输入

还要测：

- 正数
- 负数
- 0

这是：

```
Representative Inputs
```

代表性输入。

---

# 十三、pytest

这是本节最大重点。

David 引入：

```
pip install pytest
```

pytest 是：

> 第三方测试框架。

---

# 十四、pytest 的核心优势

用了 pytest 后：

你只需要：

```
def test_square():    assert square(2) == 4    assert square(3) == 9
```

不需要：

- main
- print
- try
- except

pytest 自动：

- 运行测试
- 捕获错误
- 输出报告

---

这是现代 Python 工程最常用方式之一。

---

# 十五、运行 pytest

不是：

```
python test_calculator.py
```

而是：

```
pytest test_calculator.py
```

pytest 会自动：

- 找 test 开头函数
- 自动运行
- 自动报告结果

---

# 十六、pytest 输出怎么看

失败：

```
F
```

成功：

```
.
```

绿色：

- 通过

红色：

- 失败

pytest 会显示：

- 哪个 assert 失败
- 实际值
- 预期值

例如：

```
assert 6 == 9
```

说明：

```
square(3)
```

返回了 6。

---

# 十七、测试应该“拆分”

不要：

```
def test_square():
```

里面塞几十个 assert。

更好的方式：

```
def test_positive():def test_negative():def test_zero():
```

因为：

> 一个测试失败后，后面的 assert 不会继续执行。

拆分后：

- 能看到更多错误
- 更容易定位 bug

---

# 十八、函数化的重要性

这节课其实还隐藏讲了：

> 为什么工程里强调函数拆分。

因为：

```
square(n)
```

容易测试。

但：

```
input()print()
```

这种直接和用户交互的代码难测。

所以：

工程里会：

- 把逻辑写成纯函数
- 输入输出放 main()

这是非常核心的软件工程思想。

---

# 十九、本节课真正的核心思想

不是 pytest。

而是：

# “程序应该可验证”

也就是：

- 不靠感觉
- 不靠手点
- 不靠“我觉得没问题”

而是：

```
代码自动验证代码
```

这才是现代工程开发。