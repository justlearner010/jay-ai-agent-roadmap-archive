# YYYY-MM-DD LeetCode 刷题复习笔记：347. Top K Frequent Elements

## 题目信息

- 题目：347. Top K Frequent Elements
- 链接：https://leetcode.com/problems/top-k-frequent-elements/
- 难度：Medium
- 所属计划位置：A 区，第 6 题
- 计划分组：A. 必刷核心：数组、字符串、哈希
- 模式：Counter / Heap
- 面试验收：能讲清 Top K 的堆解法
- 状态：`pass` / `review` / `redo` / `pattern-gap`
- 下次复刷日期：6.11

## 题目复述

用自己的话重写题意，不复制原题：

- 输入是什么：list 和 int
- 输出是什么：list
- 关键限制：
- 一个例子：
- `输入：nums = [1,1,1,2,2,3], k = 2`

`输出：[1,2]`

## 模式判断

这题为什么属于 `Counter / Heap`：

- 看到哪些关键词 / 条件：统计频率
- 应该想到的数据结构：哈希表、堆
- 不能用或不适合的方法：基本的列表

## 我的第一反应

- 我最开始想到的解法：用Counter统计频率，用most_common(k)选取前k个高频的词的列表
- 这个解法的问题：返回的既有key 也有value
- 我卡住的地方：不知道如何只返回key，不返回value

## 最终思路

用 3-5 句话写清楚核心逻辑：

1. Counter 统计列表的频率
2. most_common(k)生成列表
3. 选取key返回

## 代码

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	counter = Counter(nums)
	
	return [num for num,_ in counter.most_common(k)]
```

只关心num不关心后面的变量可以用下划线代替这个变量
## 复杂度

- 时间复杂度：
- 空间复杂度：
- 为什么：

## 边界条件

至少写 3 个需要特别注意的输入：

- 
- 
- 

## 错误记录

这次错在哪里：

- [ ] 题意理解错
- [ ] 数据结构选错
- [ ] 边界条件漏掉
- [ ] 循环条件写错
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

## 关联题

同模式可以一起复习的题：

- 
- 
- 
