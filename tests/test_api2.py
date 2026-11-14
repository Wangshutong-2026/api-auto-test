
"""
@FileName: test_api2.py
"""
import re
import pytest
import requests

# fixture，整个测试类共用同一个session，cookie互通
@pytest.fixture(scope="class")
def sess():
    return requests.Session()


class TestApi:
    # 用例1：访问论坛首页
    def test_phpwind_start(self, sess):
        method = "get"
        url = "http://47.107.116.139/phpwind/"
        res = sess.request(url=url, method=method)
        print("首页状态码：", res.status_code)
        assert res.status_code == 200
        assert "phpwind" in res.text

    # 用例2：登录
    def test_login(self, sess):
        # 第一步：访问登录表单页面，拿csrf_token
        form_url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
        form_res = sess.get(url=form_url)
        # 正则提取token
        ret = re.search(r'name="csrf_token" value="(.*?)"', form_res.text)
        assert ret is not None, "未捕获到csrf_token！"
        token = ret.group(1)
        print("提取到的csrf_token：", token)

        # 第二步：提交登录
        method = "post"
        url = "http://47.107.116.139/phpwind/index.php"
        params = {
            "m": "u",
            "c": "login",
            "a": "dorun"
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        data = {
            "username": "ShuTong",
            "password": "123qwe@@@",
            "csrf_token": token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        res = sess.request(method=method, url=url, params=params, data=data, headers=headers)
        print("登录返回内容：", res.text)
        assert "CSRF verification failed" not in res.text




"""
踩坑记录：
- Session大小写写错、混淆类属性与实例属性
- 局部变量不加self，跨用例拿不到token
- csrf拼写错误、抓错页面导致token为空
- pytest用例顺序不确定，跨用例传token不稳定
"""


# 错误代码

# """
# @FileName: test_api2.py
# """
# import re
#
# import requests
#
#
# class TestApi:
#     def __init__(self):
#         self.sess = requests.session()
#         self.csrf_token = ""
#     # 用例：1.访问phpwind论坛首页接口
#     def test_phpwind_start(self):
#         method = "get"
#         url = "http://47.107.116.139/phpwind/"
#         res = TestApi.sess.request(url=url, method=method)
#         print(res.status_code)
#         print(res.text)
#         self.csrf_token = re.search(r'name="csrf_token" value "(.*?)"', res.text).group(1)
#         print(self.csrf_token)
#     # 用例：2.登录接口
#     def test_login(self):
#         method = "post"
#         url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
#         params = {
#             "m":"u",
#             "c":"login",
#             "a":"dorun"
#         }
#         headers = {
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "X-Requested-With": "XMLHttpRequest",
#         }
#         data = {
#             "username":"ShuTong",
#             "password":"123qwe@@@",
#             "csrf_token":self.csrf_token,
#             "backurl":"http://47.107.116.139/phpwind/",
#             "invite":""
#         }
#         res = TestApi.sess.post(url=url, data=data, headers=headers, params=params,method=method)
#         print(res.json())
#
# if __name__ == '__main__':
#     api = TestApi()
#     api.test_phpwind_start()
#     api.test_login()


