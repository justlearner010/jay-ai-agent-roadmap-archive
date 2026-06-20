



## 这是一个非常好的问题。

很多人学 pytest fixture 的时候，直接背：

```python
@pytest.fixture
def db():
    ...
```

然后开始记 scope、autouse、yield。

结果越学越晕。

因为根本没有理解：

> fixture 到底解决了什么问题？

如果从第一性原理出发，其实 fixture 的本质非常简单。

---

# 第一层：测试到底在干什么？

假设你写一个函数：

```python
def add(a, b):
    return a + b
```

测试：

```python
def test_add():
    assert add(1, 2) == 3
```

这里没有 fixture。

因为：

```text
输入很简单
状态很简单
```

直接测就行。

---

但是现实项目不是这样。

例如：

```python
def login(user):
    ...
```

测试：

```python
def test_login():
    user = create_user()
    assert login(user)
```

你发现：

```text
测试之前
必须先创建 user
```

于是有了：

```python
def test_login():
    user = create_user()

    assert login(user)

    delete_user(user)
```

---

这时候你会发现：

测试逻辑只有一行：

```python
assert login(user)
```

剩下全是：

```text
准备数据
清理数据
```

---

于是产生第一个思想：

> 能不能把测试和准备工作分开？

---

# 第二层：把准备工作抽出来

例如：

```python
def create_test_user():
    return User("kris")
```

测试：

```python
def test_login():
    user = create_test_user()

    assert login(user)
```

是不是清爽很多？

---

但是问题来了。

第二个测试：

```python
def test_profile():
    user = create_test_user()

    assert user.profile()
```

第三个测试：

```python
def test_logout():
    user = create_test_user()

    assert logout(user)
```

出现了：

```text
重复
重复
重复
```

---

于是第二个思想出现：

> 让 pytest 自动把 create_test_user() 的结果塞给测试。

---

# 第三层：fixture诞生

于是：

```python
@pytest.fixture
def user():
    return User("kris")
```

测试：

```python
def test_login(user):
    ...
```

这里不要把 fixture 看成魔法。

本质上 pytest 干的事情只是：

```python
user_obj = user()

test_login(user=user_obj)
```

仅此而已。

---

第一性原理总结：

```text
fixture
=
自动生成测试数据的函数
```

---

# 第四层：为什么不用普通函数？

你可能会问：

```python
def user():
    return User("kris")
```

不就完了？

为什么非要：

```python
@pytest.fixture
```

---

因为 pytest 想管理它。

例如：

```python
@pytest.fixture
def user():
    print("创建用户")
    return User("kris")
```

pytest知道：

```text
谁依赖 user
什么时候创建
创建几次
什么时候销毁
```

普通函数做不到。

---

所以：

```text
fixture
=
被pytest接管生命周期的函数
```

---

# 第五层：为什么有scope？

思考：

```python
@pytest.fixture
def db():
    return connect_database()
```

测试：

```python
def test_a(db):
    ...

def test_b(db):
    ...

def test_c(db):
    ...
```

---

如果每次都：

```text
连接数据库
断开数据库

连接数据库
断开数据库

连接数据库
断开数据库
```

太慢了。

---

于是出现：

```python
@pytest.fixture(scope="module")
```

意思：

```text
整个文件共用一个db
```

---

本质：

```text
scope
=
资源活多久
```

---

记忆：

```text
function -> 活一个测试

class -> 活一个类

module -> 活一个文件

session -> 活整个pytest运行
```

---

# 第六层：为什么有yield？

这是最关键的一层。

---

假设：

```python
def create_user():
    ...
```

创建用户后：

```python
test_login()
```

结束了。

---

数据库里留下：

```text
测试用户1
测试用户2
测试用户3
```

垃圾越来越多。

---

所以需要：

```python
创建
↓
测试
↓
删除
```

---

普通写法：

```python
user = create_user()

test()

delete_user(user)
```

---

fixture写法：

```python
@pytest.fixture
def user():
    user = create_user()

    yield user

    delete_user(user)
```

---

把它翻译成人话：

```text
yield前：
准备工作

yield：
把资源交出去

yield后：
清理工作
```

---

所以：

```text
yield
=
setup 和 teardown 的分界线
```

---

# 第七层：为什么fixture能互相依赖？

例如：

```python
@pytest.fixture
def db():
```

数据库连接。

---

然后：

```python
@pytest.fixture
def user(db):
```

创建用户需要数据库。

---

然后：

```python
def test_login(user):
```

登录需要用户。

---

形成：

```text
db
 ↓
user
 ↓
test
```

---

其实这已经不是函数调用了。

而是：

```text
依赖图（Dependency Graph）
```

---

pytest真正厉害的地方：

不是fixture。

而是：

```text
自动分析依赖图
自动排序
自动销毁
```

---

# 第八层：autouse是什么？

正常：

```python
def test_x(user):
```

显式请求：

```text
我要user
```

---

autouse：

```python
@pytest.fixture(autouse=True)
```

变成：

```text
所有测试默认依赖它
```

---

相当于：

```python
def test_x(hidden_fixture):
```

自动加上去了。

---

所以本质：

```text
autouse
=
隐式依赖
```

---

# 最终第一性原理总结

fixture其实只有一句话：

```text
Fixture = 被pytest管理生命周期的资源生成器
```

它负责：

```text
创建资源
↓
提供资源
↓
缓存资源
↓
共享资源
↓
销毁资源
```

对应：

```text
创建资源  -> fixture函数

提供资源  -> 参数注入

缓存资源  -> fixture cache

共享资源  -> scope

销毁资源  -> yield

自动执行  -> autouse
```

如果把 pytest 想象成一个小型操作系统，会更容易理解：

```text
测试函数
    ↑
    │ 请求资源
    │
pytest
    │
    ├── user
    ├── db
    ├── driver
    └── tmp_path
```

测试根本不负责创建资源。

测试只负责声明：

```python
def test_login(user, db):
```

意思其实是：

```text
我需要user
我需要db

至于怎么创建
什么时候销毁

pytest你自己解决
```

这就是 fixture 的本质。