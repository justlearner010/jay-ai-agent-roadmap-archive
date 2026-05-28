# 第 7 周：接入真实 LLM API

时间：2026-07-06 到 2026-07-12

主交付物：AI 学习助手可以调用真实 LLM 生成总结；Java 副线完成 Spring Boot Hello API。

科班基础嵌入：环境变量、API key 安全、网络请求失败处理；把 Next.js / Python 服务端 API 经验过渡成 Spring Boot Controller 和 JSON 响应。

## 本周源码阅读

主线阅读：继续看 [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)。

只看：

- 环境变量或配置相关文件。
- 一个 API 调用失败时如何返回错误。

迁移点：确认自己的 LLM API key 不进前端、不进 GitHub，并在 README 写清配置方式。

Java 后端对照：阅读 [spring-guides/gs-rest-service](https://github.com/spring-guides/gs-rest-service)。

只看：

- README。
- `GreetingController` 或同等最小 Controller 文件。

迁移点：写一个 Spring Boot Hello JSON API 或请求记录。

## 每日入口

- [2026-07-06 周一：环境变量和密钥边界](./day-01.md)
- [2026-07-07 周二：服务端 LLM 调用](./day-02.md)
- [2026-07-08 周三：结构化输出设计](./day-03.md)
- [2026-07-09 周四：调用日志](./day-04.md)
- [2026-07-10 周五：失败处理](./day-05.md)
- [2026-07-11 周六：真实调用手动测试](./day-06.md)
- [2026-07-12 周日：第七周复盘](./day-07.md)

## 本周最低验收

- AI 学习助手可以调用真实 LLM 生成总结。
- Java 副线只做 2 个触点：Hello API + 请求记录或最小 Controller 测试。
- 至少一次 Codex 作业批改。
- 至少更新一次学习日志和追踪表。
- 周日写周复盘。
