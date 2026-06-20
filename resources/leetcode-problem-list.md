# LeetCode 面试刷题计划

定位：这是独立于每日作业和项目任务的面试刷题计划。它的目标不是刷题数量，而是在 2027 年 3 月投递窗口前，覆盖后端 / AI 应用实习常见算法模式，做到面试时不因为基础题型欠缺而失分。

它不进入 `this-week.md` 的当前任务清单，也不作为每日作业验收项。主线项目、测试、README、日志和复盘仍然优先。

## 面试目标

到正式投递前，需要达到这 5 个标准：

- 看到 Easy 能在 10-15 分钟内写出正确代码。
- 看到常见 Medium 能在 25-35 分钟内写出可运行解法，至少能讲清暴力解、优化方向和复杂度。
- 能识别数组 / 哈希、双指针、滑动窗口、栈、链表、二分、树、图、堆、区间、DP、回溯这 12 类常见模式。
- 每道做过的题都能说清楚：为什么用这个数据结构、边界条件是什么、时间和空间复杂度是多少。
- 面试前至少完成核心题二刷，错题和卡题三刷。

## 时间线

当前日期基准：2026-06。投递窗口：2027-03 到 2027-06。

| 阶段 | 时间 | 频率 | 目标 | 验收 |
| --- | --- | --- | --- | --- |
| 阶段 1：基础手感 | 2026-06 到 2026-08 | 每周 3-4 题 | 数组、字符串、哈希、双指针、栈 | A/B 区 Easy 基本不卡 |
| 阶段 2：常见模式 | 2026-09 到 2026-11 | 每周 4-5 题 | 链表、二分、树、堆、BFS/DFS | C/D 区 Medium 能讲清思路 |
| 阶段 3：面试补齐 | 2026-12 到 2027-02 | 每周 6-8 题 | 图、区间、贪心、DP、回溯、设计 | 核心题完成一刷，重点题完成二刷 |
| 阶段 4：投递冲刺 | 2027-03 起 | 每周 2 次模拟 + 错题复刷 | 稳定表达和限时完成 | 30 分钟内完成常见 Medium 或讲清可行解 |

如果某周项目任务很重，LeetCode 降级为“读题 + 写思路 + 标记卡点”，不需要硬挤 AC。

## 每周执行方式

每周最多安排 3 次，每次 30-60 分钟：

- 第一次：做 1-2 道新题，优先当前阶段题区。
- 第二次：复刷上周错题或卡题，不新增题。
- 第三次：限时做 1 道面试高频题，写复杂度和边界条件。

每周日只复盘 4 个数字：

- 本周新题数：
- 本周复刷数：
- 超过 35 分钟仍未完成的题：
- 下周必须复刷的题：

## 单题记录模板

每道题只记录必要信息，避免把刷题变成长笔记：

```md
- 题目：
- 模式：
- 一句话思路：
- 复杂度：
- 卡点：
- 下次复刷日期：
```

80 道题的单题笔记已经预先生成在 `leetcode-notes/`。每个文件都填好了题目、链接、难度、计划位置、模式和面试验收；做题后直接补题意、思路、代码、复杂度、边界条件和复刷记录即可。

如果以后新增题目，再复制 `templates/leetcode-review-note-template.md` 新建单题笔记。

## 复刷规则

一刷只要求理解和写出来；二刷才要求速度和稳定性。

| 状态 | 标记 | 下一步 |
| --- | --- | --- |
| 15 分钟内独立完成 Easy / 30 分钟内独立完成 Medium | `pass` | 2-4 周后抽查 |
| 看提示后完成，或边界条件错 | `review` | 3-7 天内二刷 |
| 完全没思路，或只能背答案 | `redo` | 当天写思路，第二天重做 |
| 二刷仍卡住 | `pattern-gap` | 暂停新题，补同模式 2 道基础题 |

## A. 必刷核心：数组、字符串、哈希

目标：这是所有后端和 AI 应用面试的底层题型。必须熟到可以顺手写出 `dict`、`set`、`Counter`、前缀数组和边界条件。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 1 | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Hash Map | 能解释为什么一遍哈希是 O(n) |
| 2 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Set | 能解释 set 去重 |
| 3 | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Counter / Hash | 能处理字符频率 |
| 4 | [383. Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy | Counter / Hash | 能比较两个频率表 |
| 5 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Hash Key | 能设计稳定 key |
| 6 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Counter / Heap | 能讲清 Top K 的堆解法 |
| 7 | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Prefix / Suffix | 能不用除法解决 |
| 8 | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Set | 能从序列起点扩展 |
| 9 | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane | 能解释当前最优和全局最优 |
| 10 | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix Sum + Hash | 能解释前缀和计数 |

## B. 必刷核心：双指针、滑动窗口、栈和队列

目标：覆盖字符串、数组、窗口状态、括号、表达式和单调栈。面试里这些题最容易因为边界条件丢分。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 11 | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | Two Pointers | 能从后往前合并 |
| 12 | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Two Pointers | 能原地维护写入位置 |
| 13 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two Pointers | 能跳过非字母数字字符 |
| 14 | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two Pointers | 能利用有序性质 |
| 15 | [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | Sort + Two Pointers | 能处理去重 |
| 16 | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Two Pointers | 能解释为什么移动短板 |
| 17 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Sliding Window | 能维护无重复窗口 |
| 18 | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Sliding Window | 能维护窗口内最高频字符 |
| 19 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Sliding Window | 只要求能讲清窗口收缩逻辑 |
| 20 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Stack | 能用栈匹配括号 |
| 21 | [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Stack Design | 能同步维护最小值 |
| 22 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Stack | 能用栈执行表达式 |
| 23 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic Stack | 能维护单调栈 |
| 24 | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | Queue / Stack | 能用两个栈模拟队列 |

## C. 必刷核心：链表、二分和排序

目标：链表题练指针和边界；二分题练不变量。Java 后端面试也常用这些题检查基础代码能力。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 25 | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Linked List | 能维护 `prev` / `cur` |
| 26 | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Linked List | 能使用 dummy node |
| 27 | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Fast / Slow Pointers | 能用快慢指针判环 |
| 28 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Two Pointers | 能处理删除头节点 |
| 29 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Linked List | 能处理进位 |
| 30 | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Heap / Linked List | 只要求掌握堆合并思路 |
| 31 | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Binary Search | 能写稳定边界 |
| 32 | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Binary Search | 能返回插入位置 |
| 33 | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | Binary Search | 能把矩阵映射成一维 |
| 34 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Binary Search | 能判断旋转区间 |
| 35 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Binary Search | 能判断哪一半有序 |
| 36 | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | Sort | 能讲清快排或归并 |

## D. 必刷核心：树、图、BFS/DFS 和堆

目标：这部分直接连接 Agent 状态图、任务依赖、Top K、检索排序和后端任务调度。至少要能写 DFS/BFS 模板。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 37 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Tree DFS | 能递归处理左右子树 |
| 38 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Tree DFS | 能写递归终止条件 |
| 39 | [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | Tree DFS | 能同步比较两棵树 |
| 40 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS | 能按层遍历 |
| 41 | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | DFS Bounds | 能传递上下界 |
| 42 | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Inorder | 能利用 BST 中序有序 |
| 43 | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Tree DFS | 能在递归中维护全局答案 |
| 44 | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | Tree DFS | 能拆成 same-tree 子问题 |
| 45 | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | DFS / BFS | 能扩展相邻格子 |
| 46 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | DFS / BFS | 能访问并标记网格 |
| 47 | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Graph + Hash Map | 能用映射保存克隆节点 |
| 48 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Topological Sort | 能检测依赖环 |
| 49 | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS | 能按轮次扩散 |
| 50 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Heap / Quickselect | 能求 Top K |
| 51 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Heap | 能按距离排序或维护堆 |
| 52 | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Two Heaps | 只要求理解双堆维护中位数 |

## E. 面试补齐：区间、贪心、DP、回溯和设计

目标：这些题不需要一开始就刷，但投递前不能空白。DP 和回溯至少要能做基础题，设计题至少能讲清数据结构组合。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 53 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Intervals | 能排序后合并重叠区间 |
| 54 | [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Intervals | 能处理插入前、中、后三段 |
| 55 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Greedy | 能按结束时间贪心 |
| 56 | [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Greedy | 能维护最远可达位置 |
| 57 | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | DP | 能写一维状态转移 |
| 58 | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | DP | 能处理起点选择 |
| 59 | [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | DP | 能处理选 / 不选 |
| 60 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | DP | 能写最小值状态 |
| 61 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | DP / Binary Search | 能理解 O(n^2) 解法和优化方向 |
| 62 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D DP | 能写二维状态表 |
| 63 | [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | Backtracking | 能维护路径和 used |
| 64 | [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | Backtracking | 能做选择 / 不选择 |
| 65 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Backtracking | 能处理重复选择 |
| 66 | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Design | 能解释 Hash Map + 双向链表 |
| 67 | [208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Trie | 能解释前缀树 |

## F. 冲刺加题：只在核心题稳定后做

这些题用于面试前加固，不要求现在开始。判断标准：A-E 至少 80% 能二刷通过，再进入这一组。

| 顺序 | 题目 | 难度 | 模式 | 面试验收 |
| --- | --- | --- | --- | --- |
| 68 | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | One Pass | 能维护历史最小值 |
| 69 | [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | Greedy | 能解释局部利润累加 |
| 70 | [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy | Intervals | 能识别连续区间 |
| 71 | [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Intervals / Greedy | 能按结束位置贪心 |
| 72 | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand Center | 能从中心扩展 |
| 73 | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | Expand Center | 能统计所有回文中心 |
| 74 | [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtracking | 能处理 visited 和回退 |
| 75 | [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | DFS / BFS | 能从边界反向搜索 |
| 76 | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Union Find | 能解释并查集 |
| 77 | [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union Find / DFS | 能合并连通分量 |
| 78 | [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | DP | 能判断前缀状态 |
| 79 | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | DP | 能处理负数翻转 |
| 80 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 Knapsack | 能理解背包状态 |

## 面试前验收清单

投递前用这张清单判断是否还欠缺：

- A/B/C 区 Easy 全部能 15 分钟内独立完成。
- A/B/C/D 区 Medium 至少 80% 能 35 分钟内完成或讲清可行解。
- 每类模式至少有 2 道题能不用看答案复现。
- DP 至少会 `Climbing Stairs`、`House Robber`、`Coin Change`、`LCS` 四类基础转移。
- 图至少会 DFS、BFS、拓扑排序各 1 题。
- 堆至少会 Top K、K Closest、合并 K 链表或数据流中位数中的 2 类。
- 能用中文和英文各讲 3 道题：一道哈希、一道树 / 图、一道 DP 或设计。

## 不建议现在做

- 不追求 Hard 题数量。
- 不按 LeetCode 难度从低到高机械刷。
- 不刷竞赛技巧。
- 不把刷题挤占项目交付。
- 不因为一道 DP 卡住就停掉全部计划；先标记 `pattern-gap`，继续补基础题。

## 可选官方题单

如果核心 80 题完成并二刷稳定，再补官方题单：

- [LeetCode 75](https://leetcode.com/studyplan/leetcode-75/)：适合继续巩固常见模式。
- [Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)：适合 2027 年 2 月之后面试冲刺。

使用规则：只补自己薄弱模式，不从头机械刷完。
