# 路线图：AI Agent 实习竞争力

## 总体定位

主线仍然是 AI Agent / RAG / LLM 应用工程，占整体投入约 70%。Java + Spring Boot 后端作为 30% 副线，用来兼容普通后端实习和“后端 + AI 应用”岗位。

原则：

- 前 4 周不加 Java，先把 Python、pytest、CLI 和 GitHub 证据链跑稳。
- 第 5 周开始低强度补 Java 基础，但每周都必须有小产出。
- RAG 阶段开始让 Java 进入项目：Java 负责业务后端和 API 网关，Python 负责 RAG / Agent 推理服务。
- 不把路线改成普通 Java 培训路线；Java 是后端工程化能力和投递兼容层。

## 阶段 1：AI 工程基础

时间：2026-05 到 2026-07

重点：

- Python 基础：函数、类、类型标注、异步基础、虚拟环境、包管理、pytest。
- TypeScript 和 Next.js 基础：组件、表单、API routes、fetch、简单部署。
- 第 5-8 周加入 Java 基础：语法、集合、面向对象、异常、Maven、JUnit 入门。
- Git/GitHub：分支、提交、README、issue、PR。
- AI 辅助编程习惯：可以用 AI 加速，但必须自己读懂、调试、解释每一处关键代码。
- 嵌入科班基础：数组、字符串、哈希表、栈、队列、文件系统、命令行、调试。

推荐资源：

- CS50P: Python。
- MIT Missing Semester。
- FastAPI 和 pytest 官方文档。
- Java 官方教程和 Spring Boot 官方文档按需查读。
- 《Effective Python》选读。

阶段成果：

- 做一个“AI 学习助手”，支持输入文本、总结、提问和保存历史。
- 做一个最小 Java / Spring Boot 练习服务，能返回 JSON、做参数校验，并有基础测试。

## 阶段 2：LLM 应用与 RAG

时间：2026-08 到 2026-10

重点：

- LLM API 调用、流式输出、结构化输出、工具调用。
- RAG：文本切块、embedding、向量检索、来源引用、回答验证。
- 向量数据库：优先从 Chroma 或 FAISS 开始。
- FastAPI：路由、Pydantic、错误处理、日志、环境变量。
- Java Spring Boot API Gateway：Java 负责用户、文档、任务、数据库接口；Python / FastAPI 负责 RAG 推理服务。
- 嵌入科班基础：SQL、表设计、索引、事务、HTTP、状态码、CORS、DNS、HTTPS。

推荐资源：

- OpenAI API 和 Structured Outputs 文档。
- DeepLearning.AI: LangChain Chat with Your Data。
- Full Stack LLM Bootcamp。
- Spring Boot、Spring Web、Spring Data JPA 或 MyBatis 官方文档。
- 《AI Engineering: Building Applications with Foundation Models》。
- 《Hands-On Large Language Models》。

阶段成果：

- 做一个“个人 RAG 知识库”，支持文档导入、语义搜索、带来源回答和基础评估集。
- 做一个 Java + AI 后端网关雏形，能管理文档元数据、创建 AI 任务、调用 Python RAG 服务并保存结果。

## 阶段 3：Agent 工作流

时间：2026-11 到 2027-01

重点：

- 主攻 LangGraph。
- Agent 状态管理、工具调用、规划、重试、反思、人工确认。
- 做 2-3 个真实工具：网页搜索、文件访问、任务管理、代码执行或数据库查询。
- 安全边界：权限、工具白名单、成本控制、超时、日志、用户确认。
- 后端工程要求：任务状态、执行日志、工具调用记录、超时和重试可以通过 Spring Boot 或 FastAPI 暴露 API。
- 嵌入科班基础：进程、线程、并发、文件、环境变量、图搜索、BFS/DFS。

推荐资源：

- LangGraph 官方文档。
- OpenAI Agents SDK 文档。
- DeepLearning.AI 中和 Agentic AI / Evaluating AI Agents / LangGraph 直接相关的短课。

阶段成果：

- 做一个“研究 Agent”或“求职 Agent”，能拆解任务、收集信息、生成结构化结果，并保存执行日志。
- 让 Agent 项目具备后端可讲性：任务表、执行日志、错误处理、API 设计和基础监控意识。

## 阶段 4：作品集与求职准备

时间：2027-02 到 2027-04

重点：

- 把项目收敛成 2-3 个高质量 GitHub 仓库。
- 补齐 README、架构图、测试、部署和 demo 视频。
- 准备两版简历：AI Agent 应用后端版、Java 后端版。
- 准备面试：Python、Java、API、数据库、RAG、Agent、基础系统设计。
- 根据 JD 决定是否继续加强 Spring Boot、MySQL / PostgreSQL、Redis 和 Java 单元测试；不要牺牲 RAG/Agent 主线。
- 嵌入科班基础：算法刷题、API 设计、数据库设计、缓存、队列、日志、监控。

推荐资源：

- 《Designing Machine Learning Systems》选读。
- PostgreSQL、SQLAlchemy、Spring Boot、Docker 文档按项目需要查读。

阶段成果：

- GitHub 主页有可展示的 pinned projects，项目 README 能让面试官快速看懂你的能力。
- 同一套项目能支持两种投递叙事：AI Agent / RAG 工程能力，以及 Java 后端工程能力。

## 阶段 5：投递与迭代

时间：2027-05 到 2027-06

重点：

- 每周投递 10-20 个 AI Agent / AI Engineer Intern / GenAI Intern / LLM App Intern 岗位。
- 追踪每一次投递。
- 复盘每一次面试。
- 根据 JD 和面试反馈更新项目、简历和学习重点。

阶段成果：

- 有稳定投递管线、面试复盘记录，以及能针对不同岗位讲清楚的项目故事。
