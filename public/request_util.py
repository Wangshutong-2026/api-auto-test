"""
@FileName: request_util.py
"""
import requests

class RequestUtil:
    def __init__(self):
        self.sess = requests.Session()

    # 发送所有请求，统一请求封装
    #参数不定长，类型字典
    def send_all_request(self,**kwargs):
        res = self.sess.request(**kwargs)
        return res