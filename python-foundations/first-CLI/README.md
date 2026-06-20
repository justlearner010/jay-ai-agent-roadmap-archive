# 文本处理 CLI 工具

这个工具可以在命令行读取文本文件，并完成基础文本处理：文本统计、词频统计、文本切块、JSON 输出和 mock summary。

## 功能

- 读取文本，统计行数、单词数、空格数、数字数。
- 统计词频，并输出词频最高的 10 个单词。
- 按指定长度切分文本。
- 把 summary、mode、input_chars 等结果保存为 JSON。
- 使用 mock summary 模拟后续 LLM 总结能力。

## 项目结构

```text
first-CLI/
├── src/
│   ├── cli.py
│   ├── create_json.py
│   ├── main.py
│   ├── summarize.py
│   ├── text_status.py
│   ├── word_chunk.py
│   └── word_freq.py
├── tests/
│   ├── test_createjson.py
│   ├── test_summarize.py
│   ├── test_text_status.py
│   ├── test_word_chunk.py
│   └── test_word_freq.py
├── pytest.ini
└── requirements.txt
```

## 技术栈

- Python
- pytest
- argparse
- pathlib
- json
- logging

## 我具体做了什么

- `word_freq.py`：统计词频。
- `text_status.py`：统计文本的基础信息。
- `word_chunk.py`：实现文本分块。
- `create_json.py`：实现 JSON 文件创建。
- `summarize.py`：实现 mock summary，并预留真实 LLM provider 接口。
- `tests/`：为主要模块补 pytest 测试。

## 安装和运行

进入项目目录：

```bash
cd python-foundations/first-CLI
```

安装依赖：

```bash
./.venv/bin/python -m pip install -r requirements.txt
```

查看 CLI 参数：

```bash
./.venv/bin/python src/main.py --help
```

运行文本统计：

```bash
./.venv/bin/python src/main.py test1.txt --status
```

运行词频统计：

```bash
./.venv/bin/python src/main.py test1.txt --freq
```

运行 mock summary：

```bash
./.venv/bin/python src/main.py test1.txt --summary
```

生成 JSON：

```bash
./.venv/bin/python src/main.py test1.txt --createjson
```

## pytest 使用方法

测试目录是 `tests/`。

运行全部测试：

```bash
./.venv/bin/python -m pytest
```

只运行某个测试文件：

```bash
./.venv/bin/python -m pytest tests/test_summarize.py
```

只运行某个测试函数：

```bash
./.venv/bin/python -m pytest tests/test_summarize.py::test_summarize_brief
```

当前测试结果：

```text
30 passed, 1 xfailed
```

## 已知限制

- 中文分词还没有实现，所以没有空格的中文文本词数统计不准确。
- `OpenAILLM` 只是预留真实 LLM 接口，普通单元测试不会调用真实 OpenAI API。
- README 里的示例主要用于本地复现，还不是完整产品文档。

## 下一步改进

- 为 Next.js 前端整理 `/api/summarize` 的 request / response 数据结构。
- 给 CLI 错误路径补更完整的测试或手动运行证据。
- 后续支持按段落、句子或语义切块。
