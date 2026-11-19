import re

import jsonpath
import pytest

from public.request_util import RequestUtil
from public.yaml_util import write_yaml


class TestApi2:
    # 用例1：访问论坛首页
    # 标记：这个用例是前置依赖
    # @pytest.mark.dependency()
    # 强制先提取 token 写 yaml，再执行登录，解决跨文件顺序错乱导致读不到 token 的问题，同时保留文件拆分结构。
    def test_phpwind_start(self, sess):
        method = "get"
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
        res = sess.request(url=url, method=method)

        # sess.request(...)：直接调用requests原生方法
        # RequestUtil().send_all_request(...)：把sess.request包了一层，统一封装请求

        print("首页状态码：", res.status_code)
        assert res.status_code == 200

        ret = re.search(r'name="csrf_token" value="(.*?)"', res.text)
        assert ret is not None, "未提取到csrf_token"
        token = ret.group(1)
        write_yaml({"csrf_token": token})

    # 用例3：获取access_token + 文件上传
    def test_fileupload(self, sess):
        # 第一步：获取鉴权码 access_token
        get_token_url = "https://api.weixin.qq.com/cgi-bin/token"
        token_params = {
            "grant_type": "client_credential",
            "appid": "wx8a9de038e93f77ab",
            "secret": "8326fc915928dee3165720c910effb86"
        }
        res_token = sess.request(method="GET", url=get_token_url, params=token_params)
        print("获取token返回：", res_token.json())

        # jsonpath 提取token，加兜底判断
        token_result = jsonpath.jsonpath(res_token.json(), "$.access_token")
        assert token_result, "access_token 提取失败"
        access_token = token_result[0]
        print("access_token：", access_token)
        data = {"access_token":token_result}
        write_yaml(data)


        # 第二步：文件上传
        upload_url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        upload_params = {
            "access_token": access_token
        }
        files = {
            "media": open(r"D:\图片\黄.jpg", "rb")
        }
        try:
            res_upload = sess.request(
                method="POST",
                url=upload_url,
                params=upload_params,
                files=files
            )
            print("上传返回：", res_upload.json())
            assert "url" in res_upload.text
        finally:
            files["media"].close()