import yaml

def read_yaml(filename):
    with open(filename,encoding='utf-8') as f:
        return yaml.safe_load(f)


# def read_yaml(filename):
#     with open(filename,encoding='utf-8') as f:  #打开文件
#         s = f.read()  #读取文件内容
#     data = yaml.safe_load(s)
#     return data
# print(read_yaml('../data/no1.yaml'))