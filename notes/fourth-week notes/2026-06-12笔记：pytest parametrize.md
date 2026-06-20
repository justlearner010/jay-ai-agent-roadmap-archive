




## 一句话解释

用自己的话解释这个概念是什么。
pytest parametrize 是将变量参数化的工具

## 为什么重要

说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。

方便我们将测试逻辑和测试数据给分离开，防止我们浪费大量资源维护测试环境；对于我们做具体项目时的测试有重要作用


## 概念及代码
parametrize的用处是将「测试逻辑」和「测试数据」分离

#### 标准写法
```python
@pytest.mark.parametrize(
	"input,expected",
	[
		(value1,result1),
		(value2,result2),
		(value3,result3)

	],
)

def test_xxx(input,expected):
	assert xxx(input) == expected
```

```python
#实际例子
@pytest.mark.parametrize(
	"test,count",
	[
		("hello world",2),
		("a b c",3),
		("",0)

	],
)

def test_word_count(text,count):
	assert count_words(text) == count
```


#### 标准命名

```python
@pytest.mark.parametrize(
    "value",
    [1, 2, 3],
)

@pytest.mark.parametrize(
    "input,expected",
    [
        (1, 2),
        (3, 4),
    ],
)

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (3, 4, 7),
    ],
)
```
单个参数为 **value** ，两个参数为 **input expected** ，多个参数为 **a b expected**
## 常见错误

- parametrize和fixture不是一个东西
- parametrize负责参数化，fixture负责准备环境
- fixture = 准备东西
- parametrize = 换数据
## 我今天的理解

parametrize可以帮助开发者实现测试数据和测试逻辑的分离，有助于后期的调试和维护

## 后续问题

-
