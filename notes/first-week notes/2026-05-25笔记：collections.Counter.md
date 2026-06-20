# 一句话解释

`Counter` 是 Python 标准库 `collections` 模块中的一个类，本质上是一个“专门用于计数的字典”。

导入方式：

```
from collections import Counter
```

它特别适合：

- 统计词频
- 统计字符出现次数
- Top K 高频元素
- 数据分析中的频率统计
- NLP 文本处理

---

# 1. Counter 的本质

普通字典：

```
word_cnt = {    "apple": 3,    "banana": 2}
```

Counter：

```
Counter({    "apple": 3,    "banana": 2})
```

区别在于：

Counter 自动帮你处理计数逻辑。

---

# 2. 最基本用法

## 统计列表元素出现次数

```
from collections import Counternums = [1,1,1,2,2,3]cnt = Counter(nums)print(cnt)
```

输出：

```
Counter({1: 3, 2: 2, 3: 1})
```

---

# 3. 统计字符串字符频率

```
from collections import Countertext = "hello"cnt = Counter(text)print(cnt)
```

输出：

```
Counter({    'l': 2,    'h': 1,    'e': 1,    'o': 1})
```

---

# 4. 统计单词词频（你现在最需要的）

```
from collections import Countertext = "apple banana apple orange banana apple"words = text.split()cnt = Counter(words)print(cnt)
```

输出：

```
Counter({    'apple': 3,    'banana': 2,    'orange': 1})
```

---

# 5. 与普通 dict 的区别

你之前写的：

```
word_cnt = {}for word in words:    if word in word_cnt:        word_cnt[word] += 1    else:        word_cnt[word] = 1
```

Counter 相当于自动帮你做了这件事。

直接：

```
cnt = Counter(words)
```

即可。

---

# 6. most_common() —— 高频统计核心函数

这是最重要的方法之一。

## 获取出现最多的元素

```
from collections import Counter
words = ["a","b","a","c","a","b"]
cnt = Counter(words)
print(cnt.most_common(2))
```

输出：

```
[('a', 3), ('b', 2)]
```

意思：

- a 出现 3 次
- b 出现 2 次

---

# 7. 做 Top10 词频统计

这就是 NLP 和文本分析里的经典操作。

```
from collections import Counterwith open("test.txt","r") as f:    text = f.read().lower()words = text.split()cnt = Counter(words)top10 = cnt.most_common(10)print(top10)
```

输出类似：

```
[ ('the', 120), ('of', 98), ('and', 76)]
```

---

# 8. Counter 本质上还是 dict

所以：

## 可以像字典一样访问

```
print(cnt["apple"])
```

输出：

```
3
```

---

## 不存在的 key 默认返回 0

这是 Counter 非常方便的地方。

普通 dict：

```
d["x"]
```

会报错。

但 Counter：

```
cnt["x"]
```

输出：

```
0
```

---

# 9. 更新计数：update()

```
from collections import Countercnt = Counter()cnt.update(["a","b","a"])print(cnt)
```

输出：

```
Counter({'a': 2, 'b': 1})
```

可以继续累加：

```
cnt.update(["a","c"])print(cnt)
```

输出：

```
Counter({    'a': 3,    'b': 1,    'c': 1})
```

---

# 10. Counter 的数学操作

这是它比普通 dict 强很多的地方。

## 相加

```
a = Counter("apple")b = Counter("banana")print(a + b)
```

会自动合并计数。

---

## 相减

```
a = Counter(a=4,b=2)b = Counter(a=1,b=1)print(a - b)
```

输出：

```
Counter({'a': 3, 'b': 1})
```

---

# 11. elements()

把计数重新展开。

```
cnt = Counter(a=3,b=2)print(list(cnt.elements()))
```

输出：

```
['a','a','a','b','b']
```

---

# 12. NLP 中最常见的组合

这是你以后做 RAG、文本分析会非常常见的写法：

```
from collections import Counterimport rewith open("test.txt","r") as f:    text = f.read().lower()words = re.findall(r"\b[a-z]+\b", text)cnt = Counter(words)for word,freq in cnt.most_common(10):    print(word,freq)
```

这里：

|部分|作用|
|---|---|
|`lower()`|全转小写|
|`re.findall()`|提取单词|
|`Counter()`|统计词频|
|`most_common()`|Top 高频词|

---

# 13. Counter vs dict 总结

|功能|dict|Counter|
|---|---|---|
|自动计数|❌|✅|
|默认值为0|❌|✅|
|高频统计|❌|✅|
|数学运算|❌|✅|
|NLP词频统计|一般|非常适合|

---

# 14. 你当前阶段最应该掌握的 Counter 用法

你现在重点应该掌握：

```
Counter(words)
```

以及：

```
most_common()
```

因为：

这已经能做：

- 词频统计
- TopK
- 文本分析
- 简单搜索引擎
- RAG preprocessing

了。

---

# 15. 一个完整实战案例

```
from collections import Counterimport refname = "test.txt"with open(fname,"r") as f:    text = f.read().lower()words = re.findall(r"\b[a-z]+\b", text)cnt = Counter(words)print("Top 10 Words:\n")for word,freq in cnt.most_common(10):    print(f"{word}: {freq}")
```

---

# 16. 你之后会发现的一个事实

Python 生态里：

- `dict`
- `set`
- `Counter`
- `defaultdict`

这几个数据结构几乎构成了：

大量文本处理、
爬虫、
数据分析、
NLP、
AI preprocessing

的基础。
