import allure
import pytest

@allure.epic('王小彤自动化测试')   #史诗  项目
@allure.feature('pytest框架训练')  #主题  模块
@allure.story('mark标记和筛选')  #故事  功能
@allure.title('实现筛选的用例')  #标题  用例
@pytest.mark.ut
def test_a():
    pass

@allure.epic('王小彤自动化测试')   #史诗  项目
@allure.feature('pytest框架训练')  #主题  模块
@allure.story("fixture前置和后置")  #故事  功能
@allure.title('使用fixture的用例')
@pytest.mark.ut
def test_b():
    pass