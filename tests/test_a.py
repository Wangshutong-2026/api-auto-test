import time
# from datetime import datetime
#注意一下
#文件太多时，pytest后面加上要执行的文件名
import pytest
# @pytest.fixture(scope="session")
# def ff():
#     print('我被使用')
# @pytest.fixture(autouse=True,scope="session")   #自动使用（适合全文件都用fixture的情况）
# # #统一处理，位置不重要
# def f(ff):#名字不能说明身份，加上一个装饰器
#     #不能依赖自己
#     print(datetime.now(),'用例开始执行')
#     #前置操作
#     yield 123 #开始执行用例
#     #pytest要求只能有一个结果
#     #后置操作
#     print(datetime.now(), '用例执行完毕')
#
#     # 从python的语法来看，函数中可以有多个yield

#-vs 是-v 和 -s 的连写
# def test_1(f):  #更方便
#     pass
# @pytest.mark.usefixtures("f")  #第二种加一个标记，usefixtures()可以加多个fixture
# 这是给用例用的
# def test_2():
#     pass
def test_1(f):
    #必须写参数f，自动使用不会返回值
    print('收到fixture传递的数据',f)  #不能加括号
    pass
    time.sleep(5)
def test_2():
    pass
    time.sleep(5)
#用例没有结果

# 共享范围的默认值：function 函数
# 全局共享：session  #依赖的fixture也要改
        # 所有文件里的用例都能使用 把fixture放进  conftest.py  必须严格按照这个命名
        # 不一定放在根目录，但最好放在根目录
# 同时满足两个条件才能完全全局共享

