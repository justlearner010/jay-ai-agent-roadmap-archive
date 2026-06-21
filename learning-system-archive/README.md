# Jay AI Agent Learning System

> A reusable, question-driven framework for turning AI Agent learning into verifiable project assets. This repository also contains Jay's active workspace as a concrete example.

这是我学习 AI Agent / RAG 应用工程时使用的固定模板与运行框架。它把“阅读和做题”改造成“提出问题、实验、交付、验证、复盘”的循环，也为以后探索学习系统自动化保留稳定的数据与目录边界。

## 谁适合使用

- 希望用项目问题驱动学习，而不是被逐日课表推动的人。
- 需要把代码、测试、README、演示和面试表达连成资产链的人。
- 愿意每周做取舍，并记录“继续 / 转向 / 暂存”决策的人。

## 仓库边界

- `framework/`：可复用的方法、节奏、资产化与验收规则。
- `task-library/`：按真实卡点调用的任务卡，不是必须顺序完成的课程表。
- `templates/`：周计划、周中诊断、周末验收与机会实验模板。
- `automation/`：生成新周、校验工作区的轻量脚本。
- `workspace/jay/`：Jay 的个人运行实例，包含当前周、路线、项目与追踪表。
- `modules/career/`：作品集、JD、简历与面试辅助材料。

### Template Repository 使用提醒

GitHub Template 会连同 `workspace/jay/` 一起复制。该目录是示例实例，不是框架本体。使用模板后，请把它复制或改名为 `workspace/your-name/`，再清理不属于你的个人内容，并同步修改 `learning-system.toml` 中的标准路径。

## 快速开始

要求 Python 3.11 或更高版本，不依赖第三方包。

```bash
git clone https://github.com/justlearner010/jay-ai-agent-learning-system.git
cd jay-ai-agent-learning-system
python -m automation.validate_workspace
python -m automation.new_week --start 2026-06-29 --question "本周主问题"
```

`new_week` 会生成 ISO 周文件，并在目标文件已存在时拒绝覆盖。

## 学习循环

```text
提出真实问题 → 收敛验收 → 项目实验 → 周中诊断
→ 周末交付与复盘 → 继续 / 转向 / 暂存
```

默认每周 20 小时，其中 4 小时保留给相邻自由探索。具体参数记录在 `learning-system.toml`，不是对所有使用者的硬性要求。

## 验证证据

```bash
python -m unittest discover -s tests -v
python -m automation.validate_workspace
```

校验器检查标准目录、周追踪表关键字段，以及仓库内相对 Markdown 链接和图片引用；外部链接只人工抽查。

## 当前状态与限制

- 当前状态：框架已从 Jay 的 12 周 AI Agent 求职路线中抽离，正在用真实学习周持续验证。
- 这是个人实践中的初版系统，不是经过教育学研究验证的通用课程。
- 自动化只处理文件生成与结构校验，不负责替使用者选择问题或评价学习质量。
- `workspace/jay/` 会包含个人目标与历史，不应被误认为空白模板。

## 下一步

- 用连续学习周验证模板字段是否足够。
- 在不增加流程负担的前提下，完善周数据汇总与资产索引。
- 只在真实重复操作出现后增加自动化。

## 关联仓库

- [first-CLI 文本工具](https://github.com/justlearner010/jay-first-cli-text-tool)
- [AI 工程学习笔记](https://github.com/justlearner010/jay-ai-engineering-notes)
- [历史路线归档](https://github.com/justlearner010/jay-ai-agent-roadmap-archive)
