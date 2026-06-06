# AI Agent 实习准备路线图

这个文件夹是你的 AI Agent 实习准备工作区。它把长期学习计划拆成路线图、每周执行系统、项目规格、求职追踪表和面试清单。

## 目标

- 时间范围：2026 年 5 月到 2027 年 6 月。
- 投递窗口：2027 年 3 月到 2027 年 6 月。
- 每周投入：20 小时以上。
- 主技术栈：Python + TypeScript + Java / Spring Boot。
- 路线权重：70% AI Agent / RAG / LLM 应用工程，30% Java 后端实习兼容。
- 最终成果：3 个 AI Agent 作品集项目、1 个 Java + AI 后端网关项目、GitHub 展示页、中文/英文简历、面试准备材料、投递追踪表。

## 使用顺序

1. 先看 `daily-homework/README.md`，进入当前周和当天作业。
2. 如果只做本周 Python 任务，再看 `this-week.md`。
3. 用 `daily-homework/week-xx/day-xx.md` 执行前 12 周每日作业。
4. 看 `cs-foundations-integration.md`，把科班基础嵌入项目主线。
5. 用 `resources/learning-resources.md` 选择课程和阅读书目。
6. 每周用 `weekly-operating-system.md` 做计划和复盘。
7. 按顺序完成 `projects/` 里的作品集项目，其中 Java + AI 后端网关用于兼容普通后端实习。
8. 每周日更新 `trackers/` 里的表格。
9. 从 2027 年 2 月开始，用 `interview/ai-agent-interview-checklist.md` 准备面试。

## 每周最低产出

每周至少交付一个可见成果：

- 一个功能；
- 一次重构；
- 一篇项目笔记；
- 一个评估脚本；
- 一次部署；
- 一个 demo 视频；
- 一条简历 bullet；
- 或一次 GitHub issue/PR。

## 每日文件生成

创建今天的学习日志：

```bash
python3 scripts/new_daily_entry.py log
```

创建今天的学习笔记：

```bash
python3 scripts/new_daily_entry.py note --topic "collections.Counter"
```

脚本会自动把模板里的 `YYYY-MM-DD` 替换成今天日期，并生成到 `learning-log/` 或 `study-notes/`。如果同名文件已经存在，脚本只提示路径，不会覆盖已有内容。

## 作品集项目

1. 个人 RAG 知识库
2. LangGraph 研究 Agent
3. AI Agent Web App
4. Java + AI 后端网关

每个项目最终都应该有 README、架构图、demo、测试和失败案例分析。

## 资源入口

- `daily-homework/README.md`：前 12 周每日作业要求和推荐阅读材料入口。
- `conversation-archive/2026-05-20-ai-era-skills-roadmap.md`：本工作区来源对话整理版，记录从“AI 时代应该学什么”到当前路线图的关键决策。
- `cs-foundations-integration.md`：如何把数据结构、网络、数据库、操作系统等科班基础嵌入 AI Agent 项目。
- `daily-homework/week-xx/day-xx.md`：前 12 周每天的作业要求、推荐阅读、提交物和验收标准。
- `weekly-operating-system.md`：每周计划、时间分配和复盘方式。
- `resources/learning-resources.md`：课程、官方文档、推荐书目、后端技术栈、语言学习策略。
- `templates/open-source-reading-note-template.md`：每周阅读开源项目时使用的记录模板。
- `templates/daily-learning-log-template.md`：轻量每日学习日志模板，只保留今日三行和可选证据。
- `templates/daily-study-note-template.md`：每日学习笔记模板，整理一个具体概念或知识点。
- `homework-review-system.md`：每日作业提交、批改、修改、复查流程。
- `templates/daily-homework-submission-template.md`：每天请求作业批改时使用的提交模板。
- `templates/homework-review-template.md`：Codex 批改作业时使用的评分模板。
- `trackers/homework-review-log.csv`：记录每日作业评分、复查和推送状态。
- `trackers/open-source-reading-log.csv`：记录每周开源项目阅读、迁移点和后续动作。
- `job-description-analysis-template.md`：分析具体岗位需要补哪些技能。
- `github-portfolio-checklist.md`：检查项目是否达到可投递标准。
