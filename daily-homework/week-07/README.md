# 第 7 周：接入真实 LLM API

> 定位：按卡点调用的任务库，不是日程。参考窗口属于滚动 4 周，可根据上周证据调整。

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

## 任务库索引

真实调用与契约：

- [环境变量和密钥边界](./day-01.md)
- [服务端 LLM 调用](./day-02.md)
- [结构化输出设计](./day-03.md)

可观测性与失败：

- [调用日志](./day-04.md)
- [失败处理](./day-05.md)
- [真实调用手动测试](./day-06.md)
- [真实 LLM 闭环复盘](./day-07.md)

## 本周最低验收

- AI 学习助手可以调用真实 LLM 生成总结。
- Java 副线只做 2 个触点：Hello API + 请求记录或最小 Controller 测试。
- 一次周中无评分诊断。
- 至少更新一次学习日志和追踪表。
- 一次周末验收并选择继续、转向或暂存。
