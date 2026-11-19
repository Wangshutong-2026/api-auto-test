"""
@File: test.py.py
"""
import yaml


# 写入
def write_yaml(data):
    with open('./extract.yaml',encoding="utf-8",mode='a+') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

# 读取:通过key获取value
def read_yaml(key):
    with open('./extract.yaml',encoding="utf-8",mode='r') as f:
        all_value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return all_value[key]

#删除：
def delete_yaml():
    with open('./extract.yaml', encoding="utf-8", mode='w') as f:
        f.truncate()