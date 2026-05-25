# 对话归档：AI 时代技能与 AI Agent 实习路线图

来源会话 ID：`019e45fa-3b5c-71a1-bf70-32f87d4aadb5`  
会话标题：AI时代必学技能  
整理日期：2026-05-21  
归档类型：整理版，不是原始逐字稿。

## 这次对话解决了什么

这次对话把一个宽泛问题：“AI 时代应该学什么技能”，逐步落成了一个可执行的 AI Agent 实习准备工作区。

最后形成的核心方向是：

- 主技术栈：Python + TypeScript。
- 求职方向：AI Agent / GenAI Application / LLM App Engineering。
- 时间范围：2026 年 5 月到 2027 年 6 月。
- 投递窗口：2027 年 3 月到 2027 年 6 月。
- 学习节奏：每周 20 小时以上。
- 最终成果：3 个作品集项目、GitHub 证据链、简历材料、面试准备材料。

## 关键判断

### 1. AI 时代最重要的不是只会用工具

最开始讨论的结论是：真正有价值的能力不是“会用 AI 聊天”，而是：

- 有一个主专业或主方向。
- 会拆问题。
- 会验证 AI 输出。
- 会把 AI 接入真实工作流。
- 能把想法做成可运行、可展示、可复盘的项目。

### 2. 对你当前阶段，AI Agent 实习路线比泛泛学 AI 更合适

对话里把目标聚焦到 AI Agent 实习竞争力，而不是同时追很多方向。

优先补齐：

- Python 工程基础。
- TypeScript / Next.js 基础。
- GitHub 项目展示。
- LLM API 调用。
- RAG。
- LangGraph / Agent 工作流。
- FastAPI 后端。
- 测试、日志、评估、README。

### 3. 第一阶段不要扩太多科目

后来你问 12 周任务是否还需要加内容，结论是：

不要继续加 Java、Spring Boot、Docker、LangGraph 深入、RAG 深入或大量算法刷题。

前 12 周最重要的是建立：

- Python 工程习惯。
- 函数化写法。
- pytest 测试意识。
- 每日学习日志。
- 每周复盘。
- GitHub 可见证据。
- 作业批改和第二天修正循环。

## 已落地到仓库的内容

这次对话中创建或逐步补充了这些核心文件：

- `README.md`：工作区总入口。
- `this-week.md`：第一周执行清单。
- `roadmap.md`：2026-05 到 2027-06 的长期路线图。
- `90-day-start-plan.md`：前 90 天启动计划。
- `weekly-plans/first-12-weeks.md`：前 12 周逐周计划。
- `12-week-execution-discipline.md`：前 12 周执行纪律。
- `cs-foundations-integration.md`：如何把科班基础嵌入项目主线。
- `resources/learning-resources.md`：课程、文档、书目、后端技术栈和语言学习策略。
- `homework-review-system.md`：每日作业批改流程。
- `github-portfolio-checklist.md`：作品集检查清单。
- `job-description-analysis-template.md`：岗位 JD 分析模板。
- `interview/ai-agent-interview-checklist.md`：AI Agent 面试准备清单。
- `projects/01-personal-rag-knowledge-base.md`：个人 RAG 知识库项目规格。
- `projects/02-langgraph-research-agent.md`：LangGraph 研究 Agent 项目规格。
- `projects/03-ai-agent-web-app.md`：AI Agent Web App 项目规格。
- `templates/`：学习日志、学习笔记、作业提交、作业批改、项目 README、简历 bullet 等模板。
- `trackers/`：技能矩阵、周记录、作业批改记录、项目评分、投递、面试复盘等追踪表。

## 资源与书目方向

对话中推荐的学习资源被整理进 `resources/learning-resources.md`。

优先级最高的是官方文档：

- OpenAI Agents SDK / Structured Outputs。
- LangGraph 官方文档。
- FastAPI 官方文档。
- pytest 官方文档。
- MIT Missing Semester。

推荐课程方向：

- CS50P: Python。
- Full Stack LLM Bootcamp。
- DeepLearning.AI 的 RAG、Agentic AI、LangGraph、Agent 评估相关课程。

推荐书目方向：

- 《AI Engineering: Building Applications with Foundation Models》。
- 《Hands-On Large Language Models》。
- 《Designing Data-Intensive Applications》作为后期补充。
- Python、系统基础、软件工程类书目按阶段补。

## 第一周具体执行内容

第一周围绕 Python 文本处理基础展开，目的是为后面的 RAG / Agent 项目打底。

5 个练习是：

1. `text_stats.py`：读取文本，统计行数、非空行数、单词数、字符数。
2. `word_frequency.py`：统计出现频率最高的 10 个词。
3. `text_chunker.py`：把长文本切成固定长度 chunk，支持 overlap。
4. `save_summary.py`：把模拟总结结果保存为 JSON。
5. `cli_tool.py`：用命令行调用前面的功能。

第一周最低测试要求：

- 至少给 `text_stats.py` 写测试。
- 至少给 `text_chunker.py` 写测试。
- 每个练习最终都要函数化、可测试、可解释。

## 每日学习记录约定

每日学习日志放在：

`learning-log/`

建议文件名：

`YYYY-MM-DD.md`

每天控制在 10-20 行，重点回答：

- 今日目标是什么。
- 今天做了什么。
- 学到了什么概念。
- 遇到什么问题。
- 如何解决。
- 明天做什么。
- 证据是什么：代码文件、运行命令、测试结果、commit。

对话中明确不建议只写：

“今天学习了 Python，感觉还可以，但是还有很多不会。”

更好的写法是：

“今天实现了 `count_text_stats(path)`，返回行数、非空行数、单词数、字符数。测试发现空文件时 `split()` 返回空列表，统计结果符合预期。”

## 作业批改系统

后续你提出希望每天作业可以被批改，然后第二天修改再复查。

因此仓库增加了每日作业批改流程：

1. 你每天完成代码、日志、截图或运行结果。
2. 你发起批改请求。
3. Codex 按模板检查功能、代码质量、测试证据、学习日志、计划匹配度。
4. Codex 给出总评分、必改项、建议改进项、明日修改任务、是否建议上传 GitHub。
5. 第二天你先修必改项，再推进新任务。

评分维度是 100 分：

- 功能完成度：25。
- 代码质量：20。
- 测试/运行证据：20。
- 学习日志质量：20。
- 计划匹配度：15。

## 当前最近一次作业反馈

2026-05-21 的作业批改结论：

- 总分：82/100。
- 等级：合格，有明确进步空间。
- 主要问题：最初 `txt_check.py` 更像课堂脚本，函数化和测试意识还需要加强。
- 已经改成工程化方向：新增 `text_stats.py`，保留 `txt_check.py` 作为兼容入口，新增测试文件和 README。
- 下一步：安装并运行 pytest，读懂 `count_text_stats(path)`、`format_text_stats(stats)`、`argparse`，然后开始 `word_frequency.py`。

## 后续使用方式

以后如果你想继续沿着这次对话的路线推进，可以按这个顺序看：

1. `README.md`
2. `this-week.md`
3. `weekly-plans/first-12-weeks.md`
4. `12-week-execution-discipline.md`
5. `homework-review-system.md`
6. `learning-log/`
7. `python-foundations/`

每天最小闭环是：

功能 / 日志 / commit 三选二。

理想闭环是：

一个小功能 + 一到两个测试 + 一篇学习日志 + 一次 commit。

