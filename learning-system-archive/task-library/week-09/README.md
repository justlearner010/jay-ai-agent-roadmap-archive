# 第 9 周：基于当前文本的问答

> 定位：滚动 4 周之外的候选任务库，不绑定日期；只有被周主问题选中后才进入计划。

主交付物：AI 学习助手支持“对当前文本提问”；Java 后端副线设计并实现文档 metadata 创建/查询雏形。

科班基础嵌入：上下文窗口、简单检索直觉、字符串匹配和输入约束；把 AI 学习助手里的文本和问答对象过渡成 Java REST 资源建模和 CRUD 思维。

## 本周源码阅读

主线阅读：浏览 [langchain-ai/rag-from-scratch](https://github.com/langchain-ai/rag-from-scratch)。

只看：

- retrieval 或 question answering 相关的一个 notebook。
- 文档、问题、回答之间的数据流。

迁移点：在自己的问答功能里写清“回答必须基于当前文本”的边界。

Java 后端对照：阅读 [spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)。

只看：

- 一个 Controller。
- 一个 Model 或 Repository。

迁移点：为 Java 后端副线写 `documents` 资源的字段和创建/查询接口草稿。

## 任务库索引

问答功能：

- [问题输入 UI](./day-01.md)
- [问答 API 结构](./day-02.md)
- [基于原文回答 prompt](./day-03.md)
- [连续提问流程](./day-06.md)

边界与评估：

- [无关问题拒答策略](./day-04.md)
- [问答测试样例](./day-05.md)
- [文本问答复盘](./day-07.md)

## 本周最低验收

- AI 学习助手支持“对当前文本提问”。
- Java 后端副线只做 3 个触点：`documents` 模型、创建/查询 API、周复盘说明。
- 一次周中无评分诊断。
- 至少更新一次学习日志和追踪表。
- 一次周末验收并选择继续、转向或暂存。
