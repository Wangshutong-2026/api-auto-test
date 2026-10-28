import pytest
import st
def add(a,b):
    return a+b
#用类来整合
class TestAdd:  #用例的类，不能有__init__()函数
    @pytest.mark.skip
    @pytest.mark.api
    def test_int(self):  #用例中不能自己添加参数，self是方法自带的
        res = add(1,3)
        assert res == 4

    @pytest.mark.skipif(1==2,reason ='不想干了')  #用skipif要有reason
    @pytest.mark.ul
    def test_str(self):
        res =add('1','3')
        assert res == '13'  #没有跳过

    @pytest.mark.xfail
    @pytest.mark.pay
    def test_list(self):
        res = add([1,2,3],[4,5,6])
        assert res == [1,2,3,4,5,6]

    @pytest.mark.xfail
    @pytest.mark.pay
    def test_li(self):
        res = add([1, 2, 3], [4, 5, 6])
        assert res != [1, 2, 3, 4, 5, 6]

    #数据驱动
    @pytest.mark.ddt
    @pytest.mark.parametrize(
        "a,b,c",
        st.read_csv('data.csv')   #方法里要有return
    )
    def test_ddt(self,a,b,c):  #这个abc参数是parametrize赋予的，所以还是不能自己传参
        res = add(int(a),int(b))
        assert res == int(c)

# 所有配置方式可以一键获取：pytest -h
# 输入输出会被拦截 -s可以获取到
def test_input():
    a = input('请输入手机号：')
def test_print():
    print('123')
# -x：快速退出，当遇到失败的用例停止执行
# -m：用力筛选
#
# 框架内置标记：
# 不需要注册，可以直接使用
# 不仅可以筛选，还可以增加特殊效果
# 不同的标记，增加不同的特殊效果
# skip 无条件跳过
# skipif 有条件跳过 （满足条件后才可以跳过）
# xfail 预期失败
# parametrize 参数化
# usefixture 使用fixture

# 数据驱动测试
