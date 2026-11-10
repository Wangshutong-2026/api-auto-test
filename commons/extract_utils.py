import jsonpath

# data = {
#     'a' : 1,
#     'b' : [-1,-2,-3]
# }
#
# # print(jsonpath.jsonpath(data,'$.b'))   #[[1, 2, 3]]
# print(jsonpath.jsonpath(data,'$.b')[0][1])   #-2


import re
import jsonpath

def extract(resp, attr_name, exp):
    # 先拿到属性值
    attr = getattr(resp, attr_name)  #拿到json这个字典(反射)

    if attr_name == "json":
        # jsonpath分支，只用于接口返回json
        try:
            json_data = resp.json()
        except Exception:
            json_data = {}  #jsonpath看不懂字符串所以要转字典
        res = jsonpath.jsonpath(json_data, exp)
        if res:
            return res[0]
        return None
    else:
        # status_code / text 这类，走正则匹配
        raw = str(attr)
        match = re.search(exp, raw)
        if match:
            return match.group(1)
        return None
