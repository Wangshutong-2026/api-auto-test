"""
@FileName: test_api2.py
"""
import re
import jsonpath
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

    # 用例3：微信获取access_token + 文件上传
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

        # 第二步：文件上传
        upload_url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        upload_params = {
            "access_token": access_token
        }
        # ⚠️ 改成你电脑上真实图片路径
        files = {
            "media": open("D:\图片\黄.jpg", "rb")
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

# 接口自动化测试框架封装之思路整理

# 1. 新建一个项目，然后安装 requests 库
# 2. 创建模块或类
# 3. 创建用例
# 　请求四要素和响应四要素
# 　记得要使用 session 发请求
# 4. 如果需要接口关联
# 　正则和 JsonPath
# 5. 检查响应数据
#
# 任何一个接口请求四要素和响应四要素的值是不一样的。但是传值的方式和得到响应的方式是一样的。
#
# 请求：
# 请求方式 method,
# 请求地址 url,
# 四种参数：
# 　params=None, 查询字符串参数，在请求地址后面以？传递的参数
# 　data=None, 表单参数，在接口文档中是表格形式，然后不是查询字符串参数
# 　json=None, Json 参数：{"tag":{"name":"广东"}}，由 {} 或 [] 组成的字符串
# 　files=None, Files 参数：一般有说明
# 请求头
# 　headers=None,

# 响应
# print(res.status_code) #响应码
# print(res.headers)     #响应头
# print(res.cookies)     #Cookie登录状态
# print(res.text)        #字符串
# print(res.json())      #字典格式

#
# """
# 踩坑记录：
# - Session大小写写错、混淆类属性与实例属性
# - 局部变量不加self，跨用例拿不到token
# - csrf拼写错误、抓错页面导致token为空
# - pytest用例顺序不确定，跨用例传token不稳定
# """
#
#
# # 错误代码
#
# """
# @FileName: test_api2.py
# """
# import re
#
# import requests
# from jsonpath import jsonpath
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
#      # 用例：3.文件上传
#
#     def test_fileuoload(self):
#         method = "get"
#         url = "http://api.weixin.qq.com/cgi-bin/token"
#         params = {
#             "grant_type":"client_credential",
#             "appid":"wx8a9de038e93f77ab",
#             "aecret":"8326fc915928dee3165720c910effb86"
#         }
#         res = TestApi.sess.request(url=url, params=params, method=method)
#         print(res.json())
#         #提取
#         access_token = jsonpath.jsonpath(res.json(), '$..access_token')[0]
#         print(access_token)
#
#         #文件上传
#         method = "post"
#         url = "http://api.weixin.qq.com/cgi-bin/media/uploadimg"
#         params = {
#             "access_token":access_token
#         }
#         files = {
#             "media":open("D:\图片\黄.jpg",'rb')
#         }
#         res = TestApi.sess.request(url=url, params=params, files=files, method=method)
#         print(res.json())
#         assert "url" in res.text
#
#
#
#
# if __name__ == '__main__':
#     api = TestApi()
#     api.test_phpwind_start()
#     api.test_login()
#     api.test_fileuoload()
#
#
