



## 一句话解释

**Monkey Patch（猴子补丁）就是：在程序运行过程中，动态地替换、修改或添加对象的行为，而不修改原始源码。**

你可以理解成：

> 本来这个函数长这样，但我临时把它换成另一个函数，让程序以为自己调用的还是原来的东西。

---

## 为什么重要

### 1. 在 pytest 测试里极其常见

很多时候你不希望测试真的：

- 调用 OpenAI API
- 访问数据库
- 发 HTTP 请求
- 读取真实文件

所以会用 monkey patch 把这些依赖替换成假的实现（mock）。

例如：

```
def call_llm():    return openai.chat(...)
```

测试时：

```
def fake_llm():    return "hello"
```

然后把真正的 `call_llm()` 换掉。

---

### 2. AI Agent 开发中大量使用

Agent 经常依赖：

- LLM
- Search Tool
- Browser Tool
- Database

测试 Agent 时：

```
search()
```

可能真的联网。

你会 monkey patch：

```
search()
```

↓

```
fake_search()
```

这样测试就变得：

- 快
- 稳定
- 免费

---

### 3. RAG 开发经常用

比如：

```
vector_store.search(query)
```

真实情况：

```
ChromaPineconeMilvus
```

测试时：

```
fake_search(query)
```

直接返回固定文档。

这样不用真的启动向量数据库。

---

### 4. 后端工程中的依赖隔离

例如：

```
send_email()
```

生产环境：

```
真的发邮件
```

测试环境：

```
假的send_email()
```

防止：

- 发垃圾邮件
- 扣钱
- 污染数据

---
## 概念及代码

### 最原始的 Monkey Patch

假设有：

```python
class Dog:    def bark(self):        return "wang"
```

正常：

```python
dog = Dog()print(dog.bark())
```

输出：

```python
wang
```

---

运行时修改：

```python
def fake_bark():    return "meow"
```

```python
dog.bark = fake_bark
```

现在：

```python
print(dog.bark())
```

输出：

```
meow
```

这就是 Monkey Patch。

---

### pytest中的MonkeyPatch

假设：

```python
# weather.pydef get_temperature():    return 35
```

业务代码：

```
# service.pyfrom weather import get_temperaturedef need_ac():    return get_temperature() > 30
```

---

测试：

```
def fake_temperature():    return 20
```

```
def test_need_ac(monkeypatch):    monkeypatch.setattr(        "service.get_temperature",        fake_temperature    )    assert need_ac() is False
```

这里：

```
service.get_temperature
```

被替换成：

```
fake_temperature
```

于是：

```
need_ac()
```

执行时得到：

```
20
```

而不是：

```
35
```

---

### Mock LLM 的典型场景

真实代码：

```
def call_llm(text):    return openai.chat(text)
```

测试：

```
def fake_llm(text):    return "summary result"
```

```
monkeypatch.setattr(    "summarizer.call_llm",    fake_llm)
```

然后：

```
summarize("hello")
```

不会真的调用 OpenAI。

---

### 本质是什么

其实就是：

```
old_function
```

↓

```
new_function
```

运行时替换。

画图：

```
原来summarize    │    ▼call_llm    │    ▼OpenAIMonkey Patch后summarize    │    ▼call_llm    │    ▼fake_llm
```

---

## 常见错误

- patch 错位置

```
monkeypatch.setattr(    "weather.get_temperature",    fake)
```

但实际代码：

```
from weather import get_temperature
```

应该 patch：

```
service.get_temperature
```

而不是：

```
weather.get_temperature
```

这是 pytest 新手最容易踩的坑。

---

- fake函数签名不一致

原函数：

```
def call_llm(text):
```

fake：

```
def fake_llm():
```

运行时报错：

```
TypeError
```

参数数量必须一致。

---

- 忘记返回值

```
def fake_llm(text):    pass
```

得到：

```
None
```

测试失败。

---

- 过度使用 Monkey Patch

如果只是传参就能解决：

```
def summarize(text, llm):
```

优先：

```
Dependency Injection（依赖注入）
```

而不是到处 Monkey Patch。
## 常见错误

-

## 我今天的理解



## 后续问题

-
