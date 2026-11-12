# fixture : 夹具，实现用例前置、后置自动化操作
import doctest

import pytest


# 1.他是一个函数
# 2.装饰器：@pytest.fixrure
# 3.用yield区分前后置

## 1. 创建fixture
@pytest.fixture(scope="function")
def shutong():
    print('用例前置操作：链接数据库、启动浏览器、生成测试数据')
    print('用例开始执行')

    yield

    print('用例执行结束')
    print('用例后置操作：关闭数据库、退出浏览器、删除测试数据')

## 2.使用fixture
@pytest.fixture

def test_abc(shutong,doctest_namespace):
    name = '姝彤'
    doctest_namespace['name'] = name
    assert 1 + 1 == 3

@pytest.fixture

def test_bbq(shutong,doctest_namespace):
    name = doctest_namespace['name']
    print(name)
    assert 1 + 1 == 3

## 3. 共享fixture
# 共享的好处:
# 1. 复用fixture，减少前置、后置操作时间
# 2. 在用例之间传递数据

# 共享的弊端：在共享范围内内容，fixture不会重复执行

# fixture的作用范围:
# 1. function，默认，在函数范围，进行共享
# 2. class，在同一类的范围，进行共享
# 3. module，在同一模块（文件）的范围，进行共享
# 4. package，在同一包（目录）的范围，进行共享
# 5. session，在同一次执行用例所有用例，进行共享
