# 学习资源与推荐书目

优先看官方文档。只有文档看不懂、需要项目演示，或者需要系统梳理时，再看课程和书。

学习原则：不要囤资源。每个阶段只选 1-2 个主资源，并且必须和当前项目绑定。

## 核心文档

- Python: https://docs.python.org/3/
- pytest: https://docs.pytest.org/
- FastAPI: https://fastapi.tiangolo.com/
- TypeScript: https://www.typescriptlang.org/docs/
- Next.js: https://nextjs.org/docs
- OpenAI API 文档: https://platform.openai.com/docs/
- OpenAI Structured Outputs: https://platform.openai.com/docs/guides/structured-outputs
- OpenAI Agents SDK: https://openai.github.io/openai-agents-js/guides/agents/
- LangGraph: https://langchain-ai.github.io/langgraph/
- LangChain: https://python.langchain.com/docs/
- Chroma: https://docs.trychroma.com/
- FAISS: https://faiss.ai/
- PostgreSQL: https://www.postgresql.org/docs/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Java 官方教程: https://dev.java/learn/
- Spring Boot: https://docs.spring.io/spring-boot/
- Spring Web: https://docs.spring.io/spring-framework/reference/web/webmvc.html
- Spring Data JPA: https://spring.io/projects/spring-data-jpa
- MyBatis: https://mybatis.org/mybatis-3/
- Redis: https://redis.io/docs/
- 本仓库 Java 副线语法过渡：`resources/java-side-track.md`

## 必须掌握的主题

- Python 包管理和虚拟环境。
- Python 异步基础。
- Pydantic model 和数据校验。
- HTTP API 和状态码。
- embedding 和向量相似度。
- RAG 评估和幻觉检查。
- Agent 状态机和工具调用。
- 日志与可复现调试。
- Java 集合、异常、Maven 和 JUnit。
- Spring Boot REST API、参数校验和数据库 CRUD。
- Java 后端调用 Python RAG / Agent 服务的基本模式。

## 推荐课程

按顺序学，不要同时开太多课程。

1. CS50P: Python
   链接：https://cs50.harvard.edu/python/
   用途：补 Python 基础。你学过 C/C++，可以快速过，但练习要亲自写。

2. MIT Missing Semester
   链接：https://missing.csail.mit.edu/
   用途：补 shell、Git、命令行、调试、编辑器、脚本化等工程基本功。

3. Full Stack LLM Bootcamp
   链接：https://fullstackdeeplearning.com/llm-bootcamp/
   用途：理解 LLM 应用从原型到产品的完整链路。

4. DeepLearning.AI: LangChain Chat with Your Data
   链接：https://www.deeplearning.ai/courses/langchain-chat-with-your-data/
   用途：入门 RAG。学完后要立刻做自己的文档问答项目。

5. DeepLearning.AI 课程库
   链接：https://www.deeplearning.ai/courses/
   用途：只挑和 `RAG`、`Agentic AI`、`Evaluating AI Agents`、`LangGraph` 直接相关的短课。

6. Java 官方教程
   链接：https://dev.java/learn/
   用途：只补语法、集合、类、异常、Maven / Gradle 基本概念，不系统刷完整 Java 课程。

7. Spring Boot 官方文档
   链接：https://docs.spring.io/spring-boot/
   用途：从 Spring Web REST API、配置、测试开始，配合 Java + AI 后端网关项目学习。

## 推荐阅读书目

1. 《AI Engineering: Building Applications with Foundation Models》- Chip Huyen
   优先级最高。重点看 AI 应用开发、评估、RAG、Agent、部署和维护。
   建议时间：2026-08 到 2026-10，配合 RAG 项目读。

2. 《Hands-On Large Language Models》- Jay Alammar, Maarten Grootendorst
   用来建立 LLM、embedding、transformer、RAG 的直觉。
   建议时间：2026-08 到 2026-10，遇到概念不清时查读。

3. 《Designing Machine Learning Systems》- Chip Huyen
   偏系统设计、数据、监控和生产化。
   建议时间：做完第一个 RAG 项目后再读，不要一开始就啃。

4. 《Effective Python》- Brett Slatkin
   用来提高 Python 工程代码质量。
   建议时间：2026-05 到 2026-07 选读，重点看函数、类、迭代器、异常、并发和测试相关章节。

5. 《Designing Data-Intensive Applications》- Martin Kleppmann
   不是 AI 书，但能补数据库、数据流、可靠系统的底层理解。
   建议时间：2027 年后期或实习前后选读，不要挤占 RAG/Agent 项目时间。

## 数学基础资源

学习原则：数学只学能直接解释项目的部分。每学一个概念，都要配一个小 Python 文件或项目评估脚本，不单独刷完整教材。

### 线性代数

用途：理解 embedding、向量相似度、向量检索、Top K 排序。

1. 3Blue1Brown: Essence of Linear Algebra
   链接：https://www.3blue1brown.com/topics/linear-algebra
   使用方式：先看，用来建立直觉。重点看向量、线性组合、矩阵变换、点积。

2. MIT 18.06SC Linear Algebra
   链接：https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/
   使用方式：作为正式课程选读。重点看 vectors、matrix multiplication、orthogonality、projection、least squares、eigenvalues。

对应练习：

- 写 `cosine_similarity.py`，手动计算两个向量的余弦相似度。
- 写一个小脚本，对 5 个文本 chunk 的模拟 embedding 做 Top K 排序。

### 概率统计

用途：理解 RAG 评估、Agent 成功率、失败率、抽样、precision、recall、F1。

1. Seeing Theory
   链接：https://seeing-theory.brown.edu/
   使用方式：先看可视化章节，重点看 Basic Probability、Compound Probability、Probability Distributions、Frequentist Inference。

2. Think Stats 2e
   链接：https://greenteapress.com/wp/think-stats-2e/
   使用方式：适合 Python 程序员。重点看分布、均值、方差、抽样、估计、相关性。

对应练习：

- 写 `rag_eval.py`，计算命中率、正确率、失败案例比例。
- 用 20-50 个测试问题统计 RAG 的 Top K 命中情况。

### 信息检索

用途：理解关键词检索、向量空间模型、tf-idf、Precision@K、Recall@K、MRR、NDCG。

1. Introduction to Information Retrieval
   链接：https://nlp.stanford.edu/IR-book/html/htmledition/irbook.html
   使用方式：做 RAG 项目时选读。先看 Boolean retrieval、term vocabulary、tf-idf、vector space model、evaluation in information retrieval。

对应练习：

- 在个人 RAG 知识库项目里记录 `Precision@3`、`Recall@5`。
- 比较关键词检索、向量检索、混合检索的失败案例。

### 离散数学和图论

用途：理解 LangGraph、Agent 状态机、任务拆解、BFS/DFS、失败重试循环。

1. MIT 6.042J Mathematics for Computer Science
   链接：https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/
   使用方式：做 Agent 项目前选读。重点看 sets、relations、graphs、trees、state machines、probability。

对应练习：

- 画一个 Agent workflow 图，标出节点、边、状态字段。
- 写一个小型状态机 demo，模拟 plan -> tool call -> retry -> final answer。

### 总览参考书

1. Mathematics for Machine Learning
   链接：https://mml-book.github.io/
   使用方式：长期参考书，不作为每日主线。优先看第 2 章 Linear Algebra、第 6 章 Probability and Distribution。第 7 章 Optimization 先了解即可。

## 数学学习阶段安排

- 2026-05 到 2026-07：只补数据结构、复杂度、排序、Top K。配合 Python 词频统计、文本切块、CLI 练习。
- 2026-08 到 2026-10：补线性代数和信息检索。配合 RAG 项目学习 embedding、cosine similarity、Precision@K、Recall@K。
- 2026-11 到 2027-01：补图论、状态机和基础概率统计。配合 LangGraph Agent 学节点、边、状态转移、失败率和成功率。
- 2027-02 到 2027-04：复习复杂度、概率统计和 RAG/Agent 评估指标，用于项目讲解和面试。

## 编程语言学习策略

主线不要摇摆：

- Python：AI、RAG、Agent、FastAPI、数据处理的主语言。
- TypeScript：Next.js 前端、Web App、API 调用和作品集展示。
- SQL：数据库和后端项目必须掌握。
- C/C++：保留已有基础，用来支持算法和系统理解，不作为当前主线。

Java 的处理方式：

- 不建议抢主线时间系统学 Java，但需要从第 5 周开始作为 30% 副线进入。
- 每次 Java 学习都先查 `resources/java-side-track.md`，确认它对应哪个 Python / AI 主线经验。
- 第 1-4 周不加 Java，先跑通 Python、pytest、CLI 和 GitHub 证据链。
- 第 5-8 周每周 2 小时补 Java 基础：语法、集合、类、异常、Maven、JUnit。
- 第 9-12 周每周 3-4 小时补 Spring Boot：REST API、JSON、参数校验、基础 CRUD、数据库连接。
- 2026-08 到 2026-10，把 Java 作为 RAG 项目的 API Gateway 或业务后端：Java 管理用户、文档、任务和数据库，Python 负责 RAG 推理。
- 补到能看懂企业后端项目、能写简单 API、能连 PostgreSQL / MySQL、能写基础测试即可。
- Spring Cloud、JVM 调优、复杂微服务、高并发深入，等岗位 JD 明确要求时再补。

## 后端技术栈优先级

现在就学：

- FastAPI
- Pydantic
- pytest
- 基础 SQL
- PostgreSQL 基础
- API 设计
- 环境变量
- 日志
- 简单部署
- Docker 基础
- Java 基础
- Spring Boot REST API
- JUnit 基础
- PostgreSQL / MySQL CRUD
- MyBatis 或 Spring Data JPA 二选一
- Java 后端调用 Python AI 服务

以后按岗位补：

- Redis 深入
- Celery / RQ
- Kafka
- Kubernetes
- 微服务架构
- 高并发优化
- 云服务体系
- 复杂权限系统
- Go 后端栈

判断标准：

- 能直接帮助你把 RAG/Agent 项目做成可用服务的，现在学。
- 主要服务大规模生产系统的，以后根据岗位 JD 补。

## 阶段阅读安排

- 2026-05 到 2026-07：CS50P、MIT Missing Semester、FastAPI、pytest、Effective Python 选读。
- 2026-06-22 到 2026-07-19：每周 2 小时 Java 官方教程、Maven、JUnit，只做小练习。
- 2026-07-20 到 2026-08-16：每周 3-4 小时 Spring Boot REST API、参数校验、CRUD 和数据库连接。
- 2026-08 到 2026-10：《AI Engineering》、《Hands-On Large Language Models》、RAG 相关官方文档、线性代数和信息检索选读；Java 后端用于 RAG API Gateway。
- 2026-11 到 2027-01：LangGraph 文档、OpenAI Agents SDK 文档、Agent 安全和工具调用资料、图论和状态机选读；Java 后端用于任务、日志和执行记录 API。
- 2027-02 到 2027-04：《Designing Machine Learning Systems》选读，重点转向项目讲解、评估、数学指标、Java 后端面试和简历分版。

## 英文阅读习惯

每周读一篇英文技术文章或文档页面，并写下：

- 一句话总结；
- 三个有用术语；
- 一个可以用到项目里的点；
- 一个还没搞懂的问题。
