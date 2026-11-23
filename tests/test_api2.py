"""
@FileName: test_api2.py
"""
import re
import jsonpath
import pytest
import requests

from public.yaml_util import read_yaml, read_case
from public.request_util import RequestUtil

# fixture，整个测试类共用同一个session，cookie互通

class TestApi:

    # 声明：本用例依赖 test_phpwind_start，必须等它跑完才执行
    # @pytest.mark.dependency(depends=["test_phpwind_start"])
    # 用例2：登录
    @pytest.mark.parametrize("args_name",read_case("tests/test_login.yaml"))
    def test_login(self, sess,args_name):
        print(args_name)
        method=args_name["request"]["method"]
        url=args_name["request"]["url"]
        headers=args_name["request"]["headers"]
        params=args_name["request"]["params"]
        data=args_name["request"]["data"]
        data["csrf_token"]=read_yaml("csrf_token")
        print(data)


        # # # 第一步：访问登录表单页面，拿csrf_token
        # # form_url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
        # # form_res = sess.get(url=form_url)
        # # # 正则提取token
        # # ret = re.search(r'name="csrf_token" value="(.*?)"', form_res.text)
        # # assert ret is not None, "未捕获到csrf_token！"
        # # token = ret.group(1)
        # # print("提取到的csrf_token：", token)
        # token = read_yaml("csrf_token")
        # assert token is not None, "yaml中未读取到csrf_token"
        #
        # # 第二步：提交登录
        # method = "post"
        # url = "http://47.107.116.139/phpwind/index.php"
        # params = {
        #     "m": "u",
        #     "c": "login",
        #     "a": "dorun"
        # }
        # headers = {
        #     "Accept": "application/json, text/javascript, */*; q=0.01",
        #     "X-Requested-With": "XMLHttpRequest"
        # }
        # data = {
        #     "username": "ShuTong",
        #     "password": "123qwe@@@",
        #     "csrf_token": read_yaml("csrf_token"),
        #     "backurl": "http://47.107.116.139/phpwind/",
        #     "invite": ""
        # }
        res = sess.request(method=method, url=url, params=params, data=data, headers=headers)
        # print("登录返回内容：", res.text)
        # assert "CSRF verification failed" not in res.text



