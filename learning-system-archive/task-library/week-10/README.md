# 第 10 周：历史记录与本地持久化

> 定位：滚动 4 周之外的候选任务库，不绑定日期；只有被周主问题选中后才进入计划。

主交付物：AI 学习助手支持保存和查看历史记录；Java 后端副线把文档 metadata API 接入 PostgreSQL 或 MySQL。

科班基础嵌入：数据库或文件持久化、基础数据建模、CRUD 思维；把 Python / SQLite 或文件持久化经验过渡成 SQL 表设计和 Repository / Mapper。

## 本周源码阅读

主线阅读：阅读 [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template)。

只看：

- 一个 model / CRUD / API 的组合。
- 数据库配置或迁移说明。

迁移点：给自己的历史记录功能写清数据字段和保存/读取边界。

Java 后端对照：继续阅读 [spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)。

只看：

- 一个实体模型。
- 一个 Repository 或数据库相关文件。

迁移点：给 Java 文档 metadata API 写表结构草稿或 Repository 边界说明。

## 任务库索引

数据设计与写入：

- [选择持久化方案](./day-01.md)
- [数据模型设计](./day-02.md)
- [保存会话](./day-03.md)

读取与验证：

- [历史记录列表](./day-04.md)
- [读取详情和问答记录](./day-05.md)
- [持久化测试](./day-06.md)
- [持久化复盘](./day-07.md)

## 本周最低验收

- AI 学习助手支持保存和查看历史记录。
- Java 后端副线只做 3 个触点：数据库方案、写入查询、持久化复盘。
- 一次周中无评分诊断。
- 至少更新一次学习日志和追踪表。
- 一次周末验收并选择继续、转向或暂存。
