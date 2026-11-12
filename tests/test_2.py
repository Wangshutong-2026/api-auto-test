# 用力筛选
# mark标记，用来筛选用例
# 使用：
# 1.注册（可选） ：配置文件 pytest.ini
# 2.使用 : 装饰器 @pytest.mark.first
# 3.筛选 : 命令行参数 -m
import pytest


@pytest.mark.xfail #预期失败，如果用例失败，反而符合预期
def test_abc():
    assert True

class TestLei:

    @pytest.mark.parametrize('n',[1,2,3])    #增加用例数量，不会去重
    def test_abc(self,n):  #实例方法的绑定参数self
        assert False

# 内置标记
# 特点：
# 1. 不需要注册
# 2. 不仅用例筛选，还有特殊效果
# 3. 不同的内置标记，产生不同执行效果
# - skip： 无条件跳过（不执行）
# - skipif： 有条件跳过（当判断为真的的适合跳过）
# - xfail： 预期失败
# - parametrize： 参数化测试:  动态生成用例
# - usefixture： 自动使用fixture
