# YYYY-MM-DD LeetCode 刷题复习笔记：1. Two Sum

## 题目信息

- 题目：1. Two Sum
- 链接：https://leetcode.com/problems/two-sum/
- 难度：Easy
- 所属计划位置：A 区，第 1 题
- 计划分组：A. 必刷核心：数组、字符串、哈希
- 模式：Hash Map
- 面试验收：能解释为什么一遍哈希是 O(n)
- 状态：`pass` / `review` / `redo` / `pattern-gap`
- pass：6.07
- 下次复刷日期：6.10

## 题目复述

用自己的话重写题意，不复制原题：给一个数组，和target值，返回满足target值的两数之和的数的对应下标

- 输入是什么：输入数组和target
- 输出是什么：数组下标，以列表形式返回
- 关键限制：？
- 一个例子：[2,7,11,12,3] target = 9
- 输出：[0,1]

## 模式判断

这题为什么属于 `Hash Map`：要查询，哈希表用空间换时间

- 看到哪些关键词 / 条件：查询元素是否在集合之中
- 应该想到的数据结构：哈希表（字典）数组
- 不能用或不适合的方法：不清楚

## 我的第一反应

- 我最开始想到的解法：二重循环暴力解
- 这个解法的问题：时间复杂度太高
- 我卡住的地方：对于python语法遍历不熟悉

## 最终思路

用 3-5 句话写清楚核心逻辑：

1. 建立哈希表，用于查词是否出现
2. 建立result数组，用于返回答案
3. 遍历数组，判断需要的数出现没，出现就把他加入result数组中，没出现就让哈希表对应的value 等于这个数的下标

## 代码

```python
class Solution:
	def twoSum(self,nums:List[int],target:int)->List[int]:
		seen = {}
		result = []
		for i,num in enumerate(nums):
			need = target - num
			if need in seen:
				result.append(i)
				result.append(seen[need])
			seen[num] = i
			
		return result
```

## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$
- 为什么：使用了哈希表这个额外的数据结构，耗费$O(n)$ 的复杂度，时间复杂度看一次for 循环，是$O(n)$的复杂度

## 边界条件

至少写 3 个需要特别注意的输入：

- 
- 
- 

## 错误记录

这次错在哪里：

- [ ] 题意理解错
- [ ] 数据结构选错
- [x] 边界条件漏掉 ✅ 2026-06-07
- [x] 循环条件写错 ✅ 2026-06-07
- [ ] 指针移动错
- [ ] 复杂度不达标
- [ ] 只能背答案，不能解释

具体错误：

- 

## 面试表达

如果面试官问这题，我会这样讲：

> 

## 可迁移模板

这题以后可以复用的套路：

```python

```

## 复刷记录

| 日期 | 用时 | 是否独立完成 | 状态 | 备注 |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD |  |  |  |  |


## 补充知识点

`enumerate()` 是 Python 里的一个内置函数，用来**在遍历序列时同时获得下标和值**。

例如：

```
nums = [2, 7, 11, 15]for i, num in enumerate(nums):    print(i, num)
```

输出：

```
0 21 72 113 15
```

这里：

- `i` 是索引（index）
- `num` 是元素值（value）

等价于你以前可能写的：

```
nums = [2, 7, 11, 15]for i in range(len(nums)):    num = nums[i]    print(i, num)
```

但 `enumerate()` 更 Pythonic，也更不容易出错。

---

### 你刚才这道 Two Sum 里的用法

你代码里有：

```
for i, num in enumerate(nums):    need = target - num
```

假设：

```
nums = [2,7,11,15]target = 9
```

执行过程：

|i|num|need|
|---|---|---|
|0|2|7|
|1|7|2|
|2|11|-2|
|3|15|-6|

所以：

```
i
```

表示当前位置下标。

```
num
```

表示当前位置的数字。

---

### enumerate 的返回值是什么？

实际上：

```
enumerate(nums)
```

产生的是：

```
(0, 2)(1, 7)(2, 11)(3, 15)
```

因此：

```
for item in enumerate(nums):    print(item)
```

输出：

```
(0, 2)(1, 7)(2, 11)(3, 15)
```

而：

```
for i, num in enumerate(nums):
```

其实是把元组自动拆包：

```
(i, num) = (0, 2)(i, num) = (1, 7)...
```

---

### 指定起始下标

默认从 0 开始：

```
for i, num in enumerate(nums):
```

如果想从 1 开始：

```
for i, num in enumerate(nums, start=1):    print(i, num)
```

输出：

```
1 22 73 114 15
```

---

对于刷 LeetCode 来说，你几乎可以记住一个固定模板：

```
for i, x in enumerate(nums):    pass
```

以后看到：

```
for i, node in enumerate(nodes):for i, ch in enumerate(s):for i, val in enumerate(arr):
```

本质都是：

> 遍历序列，同时拿到「下标 i」和「元素值」。
## 关联题

同模式可以一起复习的题：

- 
- 
- 
