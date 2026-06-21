# 第 8 周：LLM 接口加固

> 定位：按卡点调用的任务库，不是日程。参考窗口属于滚动 4 周，可根据上周证据调整。

主交付物：总结功能 v2，包含输入校验、结构化结果和基础成本意识；Java 副线完成 Spring Boot 参数校验。

科班基础嵌入：数据校验、错误分类、日志与可观测性；把 Python / Pydantic 校验思路过渡成 Java Bean Validation 和错误响应。

## 本周源码阅读

主线阅读：阅读 [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) 中和 Pydantic schema / API 输入校验相关的文件。

只看：

- 一个 request / response schema。
- 一个 API 路由如何调用 schema。

迁移点：给自己的总结接口写清输入长度限制和错误提示。

Java 后端对照：阅读 [spring-guides/gs-validating-form-input](https://github.com/spring-guides/gs-validating-form-input)。

只看：

- 一个带校验注解的 model。
- 一个 Controller 如何处理校验结果。

迁移点：给 Java 请求 DTO 写一个字段校验或写出校验计划。

## 任务库索引

校验与错误：

- [输入长度限制](./day-01.md)
- [结构化输出校验](./day-02.md)
- [错误分类](./day-03.md)

证据与说明：

- [日志整理](./day-04.md)
- [5 个手动测试样例](./day-05.md)
- [README 限制说明](./day-06.md)
- [接口加固复盘](./day-07.md)

## 本周最低验收

- 总结功能 v2，包含输入校验、结构化结果和基础成本意识。
- Java 副线只做 2 个触点：请求体校验 + 3 个请求样例。
- 一次周中无评分诊断。
- 至少更新一次学习日志和追踪表。
- 一次周末验收并选择继续、转向或暂存。
