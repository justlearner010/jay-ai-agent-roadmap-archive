



## 一句话解释

用自己的话解释这个概念是什么。
`@dataclass` 会根据类里的类型标注，自动生成一些方法，比如 `__init__`、`__repr__`、`__eq__` 等

## 为什么重要

说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。
节省写__init__的时间


## 概念及代码
### init = True
是否自动生成 `__init__()`构造方法

默认是True

```python
@dataclass(init=True)
class Student:
	name:str
	age:int
s= Student("Tom",18)
print(s.name)# Tom

```
等价于自动帮你写
```python
def __init__(self,name,age):
	self.name = name
	self.age = age
```

### repr=True
是否自动生成`__repr__()`,也就是打印对象是否显示的更加清楚
```python
@dataclass(repr=False)
class Student:
    name: str
    age: int

s = Student("Tom", 18)
print(s)
```


## 总结表

| 参数                | 作用                       | 默认值     |
| ----------------- | ------------------------ | ------- |
| `init`            | 自动生成 `__init__()`        | `True`  |
| `repr`            | 打印对象时显示字段内容              | `True`  |
| `eq`              | 支持用 `==` 比较对象内容          | `True`  |
| `order`           | 支持 `<`、`>` 等大小比较         | `False` |
| `frozen`          | 创建后禁止修改字段                | `False` |
| `slots`           | 限制动态属性，节省内存              | `False` |
| `kw_only`         | 必须用关键字传参                 | `False` |
| `default_factory` | 给 list/dict/set 等创建独立默认值 | 无默认     |


## 常见错误

- 

## 我今天的理解



## 后续问题

- 

