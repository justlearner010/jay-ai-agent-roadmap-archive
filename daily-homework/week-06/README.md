# 第 6 周：Next.js API route 与前后端连接

> 定位：按卡点调用的任务库，不是日程。参考窗口属于滚动 4 周，可根据上周证据调整。

主交付物：AI 学习助手 mock 全流程：前端提交到 API route，再返回总结；Java 副线把练习整理成可测试 service。

科班基础嵌入：HTTP 方法、状态码、JSON、CORS 基础概念；把 Python 函数边界过渡成 Java 类、异常和 service 边界。

## 本周源码阅读

主线阅读：阅读 [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)。

只看：

- 后端 README。
- 一个 API 路由文件或配置文件。

迁移点：给自己的 API route 写清请求体、响应体和错误返回。

Java 后端对照：阅读 [spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)。

只看：

- README。
- 一个 service 或 model 文件，不看完整业务。

迁移点：理解 Controller / Service / Model 不是同一层，给自己的 Java service 写一句职责说明。

## 任务库索引

API 契约与连接：

- [创建 summarize API route](./day-01.md)
- [请求和响应结构](./day-02.md)
- [前端 fetch 接 API](./day-04.md)

校验、理解与测试：

- [输入校验和错误状态码](./day-03.md)
- [画 HTTP 数据流](./day-05.md)
- [手动测试和小修](./day-06.md)
- [mock 全流程复盘](./day-07.md)

## 本周最低验收

- AI 学习助手 mock 全流程：前端提交到 API route，再返回总结。
- Java 副线只做 2 个触点：service 封装 + JUnit 正常/异常测试。
- 一次周中无评分诊断。
- 至少更新一次学习日志和追踪表。
- 一次周末验收并选择继续、转向或暂存。
