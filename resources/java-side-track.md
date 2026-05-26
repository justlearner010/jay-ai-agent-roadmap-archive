# Java 后端副线语法过渡资源

这个文件只服务于 30% Java 后端副线。目标不是系统学完整 Java，而是把已经用 Python 做过的文本处理、测试、API、持久化和 AI 调用记录，逐步迁移成 Java / Spring Boot 后端能力。

## 使用原则

- 先从 Python 已经做过的练习迁移，不从全新业务开始。
- 每次只学一个 Java 语法点，并立刻绑定一个小产出。
- 第 5-8 周只补语法、Maven、JUnit、最小 Spring Boot API。
- 第 9-12 周才进入 CRUD、数据库、任务模型和 AI 服务调用。
- 不在前 12 周学习 Spring Cloud、JVM 调优、高并发、Kubernetes。

## 语法过渡表

| Python / 主线经验 | Java 过渡点 | 放进每日作业的位置 | 最小产出 |
| --- | --- | --- | --- |
| Python 字符串、list、dict 文本处理 | Java `String`、`List`、`Map`、方法签名 | Week 5 Day 1 | 一个文本处理函数 |
| pytest 测纯函数 | JUnit 断言和测试命名 | Week 5 Day 6 | 一个 JUnit 测试 |
| Python 函数边界 | Java class、method、service 类 | Week 6 Day 2 | 一个 service 类 |
| Python exception | Java exception、正常/异常路径测试 | Week 6 Day 7 | 正常/异常测试各一个 |
| Next.js API route / FastAPI route | Spring Boot Controller、JSON 响应 | Week 7 Day 3 | Hello JSON API |
| API README 和手动请求记录 | Spring Boot 启动、请求路径、响应示例 | Week 7 Day 7 | README 或 Controller 测试 |
| Pydantic model / 输入校验 | DTO、Bean Validation、错误响应 | Week 8 Day 3 | 一个 DTO 和一个字段校验 |
| 手动测试空输入、超长输入 | Java 请求样例和校验边界 | Week 8 Day 7 | 三个请求样例 |
| AI 学习助手文本、摘要、历史记录 | `documents` 资源模型 | Week 9 Day 2 | 文档模型和接口草稿 |
| 内存 mock / API 闭环 | 文档 metadata 创建和查询 API | Week 9 Day 5 | 创建/查询样例 |
| JSON 文件或 SQLite 持久化 | PostgreSQL / MySQL 表设计 | Week 10 Day 1 | `documents` 表结构草稿 |
| Python 保存/读取逻辑 | Repository / Mapper | Week 10 Day 3 | 写入和查询验证 |
| LLM 调用日志 | `ai_tasks` 任务模型 | Week 11 Day 2 | 任务模型和调用链 |
| mock LLM 调用失败 | Java mock 调用 Python AI 服务 | Week 11 Day 4 | 成功/失败任务样例 |
| 项目简历 bullet | AI Agent 版和 Java 后端版表达 | Week 12 Day 3 | 两条不同版本 bullet |

## 语法学习顺序

### 1. Java 基础函数

先学：

- `String`
- `List`
- `Map`
- `for` 循环
- 方法参数和返回值

对应 Python 经验：

- 字符串切分
- 词频统计
- 空字符串过滤
- 文本长度统计

验收：能把一个 Python 文本处理函数改写成 Java 方法，并解释输入、输出和边界情况。

### 2. Maven 和 JUnit

先学：

- Maven 项目目录
- `pom.xml`
- JUnit `@Test`
- `assertEquals`、`assertTrue`

对应 Python 经验：

- `pytest`
- 测纯函数
- 测边界输入

验收：能运行一个 Java 测试，并说明它和 pytest 的一个相同点、一个不同点。

### 3. Class、Service 和异常

先学：

- class
- constructor
- method
- `IllegalArgumentException`
- 正常路径和异常路径测试

对应 Python 经验：

- 函数拆分
- 类型标注
- exception
- service 边界

验收：能把一个 Java 函数封装进 service 类，并测试正常输入和异常输入。

### 4. Spring Boot Controller

先学：

- `@RestController`
- `@GetMapping`
- `@PostMapping`
- JSON 响应
- 手动请求记录

对应 Python / TypeScript 经验：

- FastAPI route
- Next.js API route
- request / response shape

验收：能启动一个 Spring Boot API，返回固定 JSON，并写出请求路径和响应示例。

### 5. DTO 和参数校验

先学：

- request DTO
- required field
- Bean Validation
- 用户可读错误响应

对应 Python 经验：

- Pydantic model
- 输入校验
- 空输入和超长输入处理

验收：能解释一个字段如何从请求体进入 DTO，再进入校验逻辑。

### 6. CRUD 和数据库

先学：

- REST resource
- table schema
- primary key
- Repository / Mapper
- create / read

对应 Python 经验：

- JSON 文件保存
- SQLite 持久化
- 历史记录查询

验收：能创建并查询一条文档 metadata，并说明 Controller / Service / Repository 的边界。

### 7. AI 任务网关

先学：

- task status
- success / failure record
- Java 调用 Python AI 服务的 HTTP 边界
- error message 和 latency

对应 AI 主线经验：

- LLM 调用日志
- API 失败处理
- RAG / Agent 服务边界

验收：能讲清 Java 负责业务后端，Python 负责 RAG / Agent 推理。

## 官方资源

- Java Learn: https://dev.java/learn/
- Java Classes and Objects: https://dev.java/learn/classes-objects/
- Java Defining Methods: https://dev.java/learn/classes-objects/defining-methods/
- Java Exceptions: https://dev.java/learn/exceptions/
- Maven Getting Started: https://maven.apache.org/guides/index.html
- JUnit 5 User Guide: https://junit.org/junit5/docs/current/user-guide/
- Spring Boot Getting Started: https://spring.io/guides/gs/spring-boot
- Spring Boot Reference: https://docs.spring.io/spring-boot/
- Spring Validation: https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html
