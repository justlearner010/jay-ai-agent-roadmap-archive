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

## 必须掌握的主题

- Python 包管理和虚拟环境。
- Python 异步基础。
- Pydantic model 和数据校验。
- HTTP API 和状态码。
- embedding 和向量相似度。
- RAG 评估和幻觉检查。
- Agent 状态机和工具调用。
- 日志与可复现调试。

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

## 编程语言学习策略

主线不要摇摆：

- Python：AI、RAG、Agent、FastAPI、数据处理的主语言。
- TypeScript：Next.js 前端、Web App、API 调用和作品集展示。
- SQL：数据库和后端项目必须掌握。
- C/C++：保留已有基础，用来支持算法和系统理解，不作为当前主线。

Java 的处理方式：

- 不建议现在抢主线时间系统学 Java。
- 建议 2027 年寒假用 2-3 周补 Java + Spring Boot CRUD。
- 补到能看懂企业后端项目、能写简单 API、能连 PostgreSQL、能写基础测试即可。
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

以后按岗位补：

- Redis 深入
- Celery / RQ
- Kafka
- Kubernetes
- 微服务架构
- 高并发优化
- 云服务体系
- 复杂权限系统
- Go / Java 后端栈

判断标准：

- 能直接帮助你把 RAG/Agent 项目做成可用服务的，现在学。
- 主要服务大规模生产系统的，以后根据岗位 JD 补。

## 阶段阅读安排

- 2026-05 到 2026-07：CS50P、MIT Missing Semester、FastAPI、pytest、Effective Python 选读。
- 2026-08 到 2026-10：《AI Engineering》、《Hands-On Large Language Models》、RAG 相关官方文档。
- 2026-11 到 2027-01：LangGraph 文档、OpenAI Agents SDK 文档、Agent 安全和工具调用资料。
- 2027-02 到 2027-04：《Designing Machine Learning Systems》选读，重点转向项目讲解、评估和面试。
- 2027 寒假或投递前：根据 JD 决定是否补 Java + Spring Boot。

## 英文阅读习惯

每周读一篇英文技术文章或文档页面，并写下：

- 一句话总结；
- 三个有用术语；
- 一个可以用到项目里的点；
- 一个还没搞懂的问题。
