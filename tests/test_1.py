import pytest

# 1.创建test_ 开头的文件

# 2.创建test_ 开头的函数

# 3.在函数中使用断言  1.IF  2.assert

def test_abc():
    assert False

# 4.用例可以放在类中，类名字必须 Test 开头

class TestLei:

    @pytest.mark.first
    def test_abc(self):  #实例方法的绑定参数self
        assert False

# 5.用例文件可位于任意一个目录