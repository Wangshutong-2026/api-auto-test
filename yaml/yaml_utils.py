import yaml

def read_yaml(filename):
    with open(filename,encoding='utf-8') as f:  #打开文件
        s = f.read()  #读取文件内容
    data = yaml.safe_load(s)
    return data
print(read_yaml('no1.yaml'))