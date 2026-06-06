




## 一句话解释
pyproject.toml是一个告诉包管理器应该去下载什么的一个工具，同时也被代码检查工具，类型检查工具和其他工具所利用

用自己的话解释这个概念是什么。

## 为什么重要
`pyproject.toml`是现代python项目中推荐写的一种配置文件，相比于requirements.txt更加全面；在我们的项目中是需要写这个的，方便日后项目的版本管理、更新、下载或删除依赖等操作的进行

说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。


## 概念及代码

```TOML
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_project"
version = "0.1.0"
description = "A sample Python project"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28",
    "pandas>=2.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "black", "mypy"]

[tool.black]
line-length = 88

[tool.mypy]
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```


### 使用poetry进行配置

Poetry是现在最流行的Python包管理工具之一，用Poetry可以为我们的项目配置节省下大量的时间

```Bash
# 安装 Poetry
curl -sSL https://install.python-poetry.org | python3 -

# 初始化项目
poetry init
# 会交互式问你项目名称、版本、依赖等
# 最后会生成 pyproject.toml

# 添加依赖
poetry add requests pandas
# 自动更新 pyproject.toml
```

优点：

- 不用自己手写 TOML。
- 自动管理依赖和虚拟环境。
- 可选依赖、开发依赖都很方便。
- 可以直接发布到 PyPI。

---

## 2️⃣

## 常见错误

-

## 我今天的理解
**Q: `pyproject.toml` 是否替代 `requirements.txt`？**
A: 它通常用于项目元数据和可选依赖，你仍可用它管理依赖，不必单独写 `requirements.txt`

**Q: 为什么要用 TOML？**
A: TOML 是易读、结构清晰的配置格式，被 Python 社区采纳为标准。



## 后续问题

- 无
