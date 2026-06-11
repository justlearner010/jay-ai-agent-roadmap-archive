# 2026-06-07 LeetCode 刷题复习笔记：217. Contains Duplicate

## 题目信息

- 题目：217. Contains Duplicate
- 链接：https://leetcode.com/problems/contains-duplicate/
- 难度：Easy
- 所属计划位置：A 区，第 2 题
- 计划分组：A. 必刷核心：数组、字符串、哈希
- 模式：Set
- 面试验收：能解释 set 去重
- 状态：`pass` / `review` / `redo` / `pattern-gap`
- pass
- 下次复刷日期：6.10

## 题目复述

用自己的话重写题意，不复制原题：
这个题是给一个数组，如果这个数组中只要有一个数出现过两次及以上就返回True，否则返回False

- 输入是什么：数组
- 输出是什么：布尔值 True or False
- 关键限制：无
- 一个例子：**输入** nums = [1,1,1,3,3,4,3,2,4,2]

**输出：** True

## 模式判断

这题为什么属于 `Set`：

- 看到哪些关键词 / 条件：出现两次以上
- 应该想到的数据结构：set
- 不能用或不适合的方法：hashmap

## 我的第一反应

- 我最开始想到的解法：用list.dictfromkeys
- 这个解法的问题：无
- 我卡住的地方：

## 最终思路

用 3-5 句话写清楚核心逻辑：

1. 使用set，存放数组中的记录
2. 如果是看见过的直接返回True
3. 如果最后也没看见就返回False

## 代码

```python

  def containsDuplicate(self, nums: List[int]) -> bool:
	seen = set()
	for num in nums:
		if num in seen:
			return True
		seen.add(num)
	return False
		
		

```

## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$
- 为什么：一次for循环是$O(n)$ ，一个额外set，占据空间为$O(n)$

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
