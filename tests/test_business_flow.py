import re

import pytest
import requests

from public.yaml_util import read_case, read_yaml, write_yaml


class TestLogin:
    @pytest.mark.parametrize("login_password",read_case("tests/login_data.yaml"))
    def test_login(self, sess,login_password):
        #导入数据
        method = login_password["request"]["method"]
        url = login_password["request"]["url"]
        params = login_password["request"]["params"]
        headers = login_password["request"]["headers"]
        data = login_password["request"]["data"]
        url1 = login_password["request"]["url1"]
        method1 = login_password["request"]["method1"]

        # 获取"csrf_token"
        ret = sess.request(url=url1,method=method1)
        # print("获取token返回：", ret.text)
        ret_token = re.search(r'name="csrf_token" value="(.*?)"', ret.text)
        assert ret is not None, "未提取到csrf_token"
        token = ret_token.group(1)
        write_yaml({"csrf_token": token})

        data["csrf_token"] = read_yaml("csrf_token")

        #用户输入密码
        pwd = input("Please input your password:")
        try:
            assert pwd == data["password"]
            print("恭喜登录成功")
        except:
            print("密码错误，请重试！")

        res = requests.post(url=url, data=data, headers=headers,params=params)
        print("首页状态码：", res.status_code)
        assert res.status_code == 200




            # if resp.json()["password"] == login_password["request"]["data"]["password"] :
            #     print("登录成功！")
            #     break
            # else:
            #     print("密码错误，请重新输入！")
            #     raise