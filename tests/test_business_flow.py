import re

import pytest
import requests

from public.request_util import RequestUtil
from public.yaml_util import read_case, read_yaml, write_yaml


class TestLogin:
    @pytest.mark.parametrize("login_password",read_case("tests/login_data.yaml"))
    def test_login(self,login_password):
        #导入数据
        method = login_password["request"]["method"]
        url = login_password["request"]["url"]
        params = login_password["request"]["params"]
        headers = login_password["request"]["headers"]
        data = login_password["request"]["data"]
        url1 = login_password["request"]["url1"]
        method1 = login_password["request"]["method1"]

        # 获取"csrf_token"
        req = RequestUtil()
        ret = req.send_all_request(url=url1,method=method1)
        # print("获取token返回：", ret.text)
        ret_token = re.search(r'name="csrf_token" value="(.*?)"', ret.text)
        assert ret is not None, "未提取到csrf_token"
        token = ret_token.group(1)
        write_yaml({"csrf_token": token})

        data["csrf_token"] = read_yaml("csrf_token")

        res = req.send_all_request(url=url, method=method, data=data, headers=headers,params=params)
        print("登录接口返回内容：", res.text)
        res_json = res.json()
        print(login_password)
        expected_state = login_password["expected"]["state"]
        assert res_json["state"] == expected_state
