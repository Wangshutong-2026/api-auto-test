import pytest
from datetime import datetime
from selenium import webdriver

@pytest.fixture(scope="session")
def ff():
    print('我被使用')
@pytest.fixture(autouse=True,scope="session")   #自动使用（适合全文件都用fixture的情况）
# #统一处理，位置不重要
def f(ff):#名字不能说明身份，加上一个装饰器
    #不能依赖自己
    print(datetime.now(),'用例开始执行')
    #前置操作
    yield 123 #开始执行用例
    #pytest要求只能有一个结果
    #后置操作
    print(datetime.now(), '用例执行完毕')

    # 从python的语法来看，函数中可以有多个yield


# 如果没有selenium插件该怎么做

# @pytest.fixture()
# def selenium():
#     d = webdriver.Chrome()
#     yield d
#
#     d.quit()