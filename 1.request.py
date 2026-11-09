import requests

##1. 方法
url = 'http://116.62.63.211/shop/api.php'

#GET方法

requests.get(url)

#POST方法

requests.post(url)

#任意方法
requests.request('MOVE',url)

##2. 头
method = 'post'
url = 'http://116.62.63.211/shop/api.php'

requests.request(
    method,url,
    headers={  #字符串字典
        '1':'1',
        '2':'b',
    }
)

##3. 参数
method = 'post'
url = 'http://116.62.63.211/shop/api.php'
resp = requests.request(
    method,url,
    json={   #data也可以，默认是表单
        'a':1,
        'b':[1,2,3],
        'c':{},
    }
)

#resp 就是响应
#获取响应中的内容
print(resp.status_code) #状态码
print(resp.headers) #响应头
print(resp.text) #响应正文
print(resp.json()) #响应正文转成JSON

assert resp.status_code == 200
assert '美酒' in resp.text
assert resp.json()['data']['banner_list'][0]['name']=='美酒'

# 断言全部的内容
from responses_validator import validator
validator(
    resp,
    status_code=200,
    text = '*美酒*',
    json = {
        'data':{
            'banner_list':[{'name':'美酒'}]
        }
    }
)