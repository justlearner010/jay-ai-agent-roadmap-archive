# 文本处理CLI工具

一句话说明：这个系统做什么，为谁解决什么问题。
这个工具是可以在命令行读入文本然后对于文本进行初步处理

## Demo

- 在线地址：无
- demo 视频：![[first_cli_demo.mov]]
- 截图：（模块结构）
- ![[Pasted image 20260525155833.png]]
- （json文本）![[Pasted image 20260525155731.png]]


## 问题背景



## 功能

- 功能 1：读取文本记录文本的单词数、空格数、数字数
- 功能 2：记录并给出文本的单词词频，并给出词频最高的10个单词以及其词频数
- 功能 3：将大型文本按照字符串长度进行分块，并生成结构化的.json文件

## 架构

说明或画图展示：

- 前端；
- 后端；
- LLM provider；
- 检索/向量库；
- 数据库；
- 日志/评估。

## 技术栈

- Python：
- TypeScript：
- 框架：
- 数据库/向量库：
- LLM provider：
- 部署：

## 我具体做了什么

清楚说明你的个人贡献。
- word_freq.py:统计词频
- word_status:统计文本的基础信息
- word_chunk.py:实现文本分块
- create_json.py:实现json文本的创建

## 评估

- 测试集规模：
- 检索指标：
- 回答质量指标：
- 已知失败案例：

## 学到的东西
- 使用`with open`语句打开文件，选择操作模式`r`(read) `w`(write)
- 使用`.readline()/.read()语句读取文件
- 使用 `collection counter`对于词频进行读取
- 使用`argparse`在命令行中传递参数
- 使用`json`模块中的`.dumps()`将python对象转化成json格式的文件
- 使用`json`模块中的`.dump()`将读取的内容直接写入json文件中


## 下一步改进
- 实现`word_chunk`模块中支持通过语义semantic和段落/句子进行切块
- 


## pytest使用方法
- first-CLI/src/tests为test文件夹

- ./.venv/bin/python -m pytest
进行所有文件测试

