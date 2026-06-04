



Conda体系 VS 官方体系
Conda：独立的生态，多语言支持，依赖管理和虚拟环境
官方：比较乱


## 一句话解释
通过命令来从网上下载自己需要的python package
用自己的话解释这个概念是什么。

## 为什么重要
我们项目要用到外置的包需要学会怎么下载
说明它和当前项目、AI Agent、RAG、后端工程或科班基础有什么关系。


## 概念及代码
- pipi.org:有着许多python包的网站允许自己查找
- anaconda/package

**pip ,venv,requirements.txt** :过时的写法

venv主要是修改了python中sys.path这个变量，sys.path记录了路径
没有虚拟环境会把包装到整个全局环境中，需要虚拟环境避免版本冲突


#### 缺陷
pip freeze分不清需要的直接依赖和间接依赖
项目一旦变得复杂就很麻烦了
pip 在卸载包的时候也分不清要删的间接依赖

`pyproject.toml`:总的配置文件
只需要声明直接依赖的包就行

**venv + pyproject.toml:很麻烦**

### uv 、poetry、PDM
更简单的接口
```python
uv add flask = pip + venv 
uv sync 读取好pyproject.toml安装好环境和依赖

uv run main.py
在虚拟环境中直接执行命令，然后执行完后自动退出这个虚拟环境
```




## 常见错误

- 

## 我今天的理解



## 后续问题

- 

