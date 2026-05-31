
假设你有一本书：

100 万字符

你不可能：

一次性丢给 embedding model

因为：

1）上下文窗口有限

例如：

模型	token限制
`GPT-4o mini	几十万`
embedding model	通常更小
`2）检索粒度太粗`

如果整本书只生成：

`一个 embedding`

那：

无法精确定位内容

例如：

用户问：

`“牛顿第二定律是什么？”`

系统只知道：

`“这本物理书可能相关”`

但不知道：

具体在哪
2. 所以 RAG 的核心思路

不是：

`“检索整本书”`

而是：

`“检索书中的片段”`

即：

chunks
`3. RAG 的经典数据流`

真正 RAG 基本都是：

```
Document
↓
Chunking
↓
Embedding
↓
Vector Database
↓
Similarity Search
↓
Top-K Chunks
↓
LLM
```
你现在已经在做：

`Chunking`

这一步。

`4. 为什么 chunk size 很重要`

这其实是：

`信息密度 vs 检索精度`

的 tradeoff。

`5. chunk 太大`

例如：

`5000 tokens
`
问题：

`embedding 会“平均化”`

一个 chunk 里面：

```
数学
历史
编程
哲学

全混在一起。
```

embedding 会失去语义聚焦。

`检索不精准`

用户问：

Python dict

结果整个 chunk 都被塞进去。

大量无关内容。

`6. chunk 太小`

例如：

`10 tokens`

问题：

`上下文断裂`

例如：

`He invented it.`

这里：

`He`

`是谁？`

`丢失上下文。`

`语义不完整`

`embedding 效果会变差。`

7. `所以 RAG 里的 chunking 本质是：
找到“语义完整”的最小单元

这是核心。`

8. `最原始的方法：固定长度切块`

你现在做的：

`text[i:i+chunk_size]`

属于：

`Fixed-size Chunking
`
```
优点：

简单
快
易实现

缺点：

可能切断语义
```
例如：

`Newton's second law states that`
`Force equals mass times acceleration`

可能从中间断开。

`9. 更高级的 chunking`

真实 RAG 常见：

`1）Sentence Chunking
`
```
按句子切：

.
?!
2）Paragraph Chunking
```
按段落切：

`split("\n\n")`
3）Semantic Chunking（高级）

```
按：

语义边界

切。

例如：

一整段都在讲牛顿力学

就保持一起。
```
10. overlap（非常重要）

真实 RAG 非常常见：

```
overlapping chunks

例如：

0-500
400-900
800-1300
```
11. 为什么 overlap 很重要

因为：

`信息经常跨 chunk 边界`

例如：

Chunk A：

The company was founded in 1998.

Chunk B：

Its CEO later became...

如果没 overlap：

`上下文断裂`
12. 你现在的 metadata 很有价值

你现在存：

start
end
index

这其实已经是：

retrieval metadata

了。

以后：

还能存：

source
"source": "physics_book.txt"
page

PDF 中：

"page": 12
title
embedding id
13. embedding 为什么依赖 chunk

`embedding 本质：`

把文本映射成向量

例如：

“苹果”
→
[0.12, -0.44, ...]

如果 chunk 不合理：

embedding 质量会直接下降
14. RAG 的本质其实是：
“先找相关知识，再让LLM生成”

所以：

`chunking`

决定：

`能不能找到正确知识`

`embedding`

决定：

相似度质量
`retrieval`

决定：

`给LLM喂什么上下文`