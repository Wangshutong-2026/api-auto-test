import pytest
import time


@pytest.mark.web
def test_web(selenium):
    selenium.get('http://www.baidu.com')
    # print(selenium.url)
    print(selenium.title)
    # 元素定位、交互
    # 截图、文件上传
    time.sleep(1)