# YYYY-MM-DD LeetCode 刷题复习笔记：49. Group Anagrams

## 题目信息

- 题目：49. Group Anagrams
- 链接：https://leetcode.com/problems/group-anagrams/
- 难度：Medium
- 所属计划位置：A 区，第 5 题
- 计划分组：A. 必刷核心：数组、字符串、哈希
- 模式：Hash Key
- 面试验收：能设计稳定 key
- 状态：`pass` / `review` / `redo` / `pattern-gap`
- 下次复刷日期：6.11

## 题目复述

用自己的话重写题意，不复制原题：

- 输入是什么：字符串
- 输出是什么：列表
- 关键限制：相同的key为一组
- 一个例子：`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`


## 模式判断

这题为什么属于 `Hash Key`：

- 看到哪些关键词 / 条件：分组、异位词
- 应该想到的数据结构：list，set
- 不能用或不适合的方法：set不能看出顺序的不同

## 我的第一反应

- 我最开始想到的解法：无
- 这个解法的问题：
- 我卡住的地方：

## 最终思路

用 3-5 句话写清楚核心逻辑：

1. 先将defaultdict创建出来
2. 先遍历整个列表
3. 通过排序字符串的方式，把顺序不同的统一变成同一个key，然后value为原始值

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	d = defaultdict(list)
	
	for s in strs:
		sorted_s = "".join(sorted(s))
		d[sorted_s].append(s)
		
	return list(d.values())
```

## 复杂度

- 时间复杂度：$O(N∗MLogM)$
- 空间复杂度：$O(N)$
- 为什么：额外容器dict

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
