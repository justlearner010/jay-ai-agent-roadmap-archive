



## 一句话解释

用自己的话解释这个概念是什么。
exception 是python中的异常问题
## 为什么重要

说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。
在出现错误时能找到问题所在之处并进行调试和改错


## 概念及代码

### SyntaxError

#### ValueError

```python
x = int(input("what is x"))
print(f"x is {x}")

>>> what is x? 50
50

>>> what is x? cat
ValueError:invalid literal for int()
```


#### try
```python
try:
	x = int(input("what is x"))
	print(f"x is {x}")
except ValueError:
	print("x is not an integer")
```








# 为什么不要裸 except

David 特别提到：

虽然可以写：

```
except:
```

但是不推荐。

因为：

```
except:
```

会捕获所有错误。

可能把真正的 bug 隐藏起来。

更好的写法：

```
except ValueError:
```

明确说明：

```
我只处理 ValueError
```

---

# 5. NameError

课程里出现了第二种错误：

```
try:    x = int(input("What's x? "))except ValueError:    print("x is not an integer")print(f"x is {x}")
```

如果输入：

```
cat
```

会得到：

```
NameError
```

因为：

```
x = int(...)
```

这里根本没执行成功。

所以：

```
x
```

实际上没有被创建。

---

# 6. try / except / else

为了解决上面的问题，引入：

```
try:    x = int(input("What's x? "))except ValueError:    print("x is not an integer")else:    print(f"x is {x}")
```

逻辑：

```
try 成功    -> 执行 elsetry 失败    -> 执行 except
```

这样就不会出现 NameError。

---

# 7. while True

仅仅报错还不够友好。

更好的方式：

```
while True:    try:        x = int(input("What's x? "))    except ValueError:        print("x is not an integer")    else:        break
```

如果用户输入：

```
catdogbird
```

程序会一直提示：

```
x is not an integer
```

直到输入：

```
50
```

才继续执行。

---

# 8. break

```
break
```

用于跳出循环。

例如：

```
while True:    ...    break
```

一旦执行到：

```
break
```

循环立刻结束。

---

# 最后浓缩成考试笔记

```
Exception（异常）│├── SyntaxError│   └── 代码写错│├── Runtime Error│   ├── ValueError│   └── NameError│├── try│   └── 尝试执行代码│├── except│   └── 处理异常│├── else│   └── try 成功时执行│├── while True│   └── 持续重试│└── break    └── 跳出循环
```

这一讲真正想培养的思维是：

> **不要假设用户一定会正确输入数据。**
> 
> **写程序时要“防御性编程（Defensive Programming）”，提前考虑错误并处理它们。**

## 常见错误

- 

## 我今天的理解



## 后续问题

- 

