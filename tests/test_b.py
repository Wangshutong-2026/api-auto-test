# 插件分为两类：内置插件、第三方插件
from operator import contains
from pydoc import html

from _pytest import fixtures

# 插件启用管理
# 使用：-p abc
# 禁用： -p no:abc

# 插件使用方式：
# 参数
# 配置文件
# fixture   针对用例
# 标记   针对用例

# pytest-xdist 默认多进程
# 分布式执行
# 使用：-n N     #N几个进程
# 只有任务本身比较慢，调度成本高，才有意义
# 能不能用：分布式执行，有并发问题，资源竞争、乱序


# pytest-html 生成HTML测试报告
# 参数：pytest --html=report.html --self-contained-html
# --self-contained-html  把所有的东西打包成一个html

import time

def test_3(f,ff):
    pass
   #接收了返回值123，但是和test_1复用了
    time.sleep(5)

# pytest-rerunfailures
# 用例失败之后，重新执行
#
# --returns N --reruns-delay T  #N重启次数 T每次的间隔时间

# pytest-result-log   把用例的执行结果记录到日志文件
# 测试报告和日志都会被覆盖

# 企业级测试报告
# allure是一个测试报告框架
# pip install allure-pytest