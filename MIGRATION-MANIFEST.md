# 四仓库迁移清单

迁移日期：2026-06-21

原则：新仓库只复制白名单内容；旧仓库的本地源文件不移动、不删除。三个内容仓库使用精选快照，不携带旧提交历史。

## `jay-ai-agent-learning-system`

| 源路径 | 目标路径 | 说明 |
|---|---|---|
| `weekly-operating-system.md` 等系统文档 | `framework/` | 可复用的周问题制、资产化、验收与基础整合规则 |
| `daily-homework/` | `task-library/` | 第 1-4 周历史材料与第 5-12 周按卡点调用的任务卡 |
| `this-week.md`、`roadmap.md`、`projects/`、精选 tracker | `workspace/jay/` | Jay 的个人运行实例 |
| 周计划、诊断、验收、机会实验模板 | `templates/` | 当前周级流程模板 |
| 作品集、JD、简历、面试材料 | `modules/career/` | 求职辅助模块 |
| 新增轻量脚本与测试 | `automation/`、`tests/` | 生成新周与校验标准结构 |

## `jay-first-cli-text-tool`

| 源路径 | 目标路径 | 说明 |
|---|---|---|
| `python-foundations/first-CLI/src/*.py` | `src/first_cli/` | 保留文本统计、词频、分块、JSON 与摘要逻辑 |
| `python-foundations/first-CLI/tests/test_*.py` | `tests/` | 只调整为包内导入 |
| `test0.txt` 的用途 | `examples/sample.txt` | 重新提供无隐私的公开运行示例 |
| 新增工程文件 | `pyproject.toml`、CI、README、LICENSE | 标准安装、命令入口与持续测试 |

## `jay-ai-engineering-notes`

| 源路径 | 目标路径 | 数量 |
|---|---|---:|
| `notes/**/*.md` | Python、测试、AI 工程、TypeScript 主题目录 | 37 |
| `leetcode-notes/001` 至 `006` | `algorithms/` | 6 |
| `learning-log/weekly_review/*.md` | `journey/weekly-reviews/` | 4 |
| `notes/assets/2026-05-24-json-*.png` | `assets/` | 2 |

计划中的“39 篇知识笔记”是预估值；源仓库实际可确认 37 篇，迁移与索引以实际文件为准。

## 明确排除

| 内容 | 排除原因 |
|---|---|
| 每日学习日志、作业提交、Codex 批改 | 过程性个人记录，不属于公开知识资产 |
| `leetcode-notes/007` 至 `080` | 未跟踪的空白模板，没有可展示内容 |
| 未跟踪空文件和个人编辑器配置 | 不构成迁移资产 |
| `.venv`、缓存、`node_modules` | 构建或依赖产物 |
| `first_cli_demo.mov` 等大视频 | 不进入 Git；后续使用发布页或外部演示链接 |
| 未被迁移内容引用的图片 | 避免无上下文资产堆积 |
| API Key、Token、私钥、私人邮箱 | 禁止公开；发布前执行模式扫描 |

## 验证门槛

- 所有仓库内相对 Markdown 链接和图片引用可解析。
- 学习系统命令、拒绝覆盖行为和 validator 测试通过。
- first-CLI 在干净虚拟环境安装，保持 `30 passed, 1 xfailed`。
- 笔记两个索引覆盖全部 47 个迁移内容文件。
- 新仓库通过排除项和敏感信息检查后，才允许创建远程与处理旧仓库。
