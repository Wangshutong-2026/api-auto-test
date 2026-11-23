import pytest
import requests

from public.yaml_util import read_case, read_yaml, write_yaml


class TestLogin:
    @pytest.mark.parametrize("login_password",read_case("tests/login_data.yaml"))
    def test_login(self, sess,login_password):
        method = login_password["request"]["method"]
        url = login_password["request"]["url"]
        params = login_password["request"]["params"]
        headers = login_password["request"]["headers"]
        data = login_password["request"]["data"]
        data["csrf_token"] = read_yaml("csrf_token")
        pwd = input("Please input your password:")
        data["password"] = pwd
        write_yaml({"password": pwd})
        resp = requests.post(url, data=data, headers=headers,params=params)
        print("响应文本",resp.text)
            # if resp.json()["password"] == login_password["request"]["data"]["password"] :
            #     print("登录成功！")
            #     break
            # else:
            #     print("密码错误，请重新输入！")
            #     raise