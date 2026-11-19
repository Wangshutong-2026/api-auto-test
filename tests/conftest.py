"""
@FileName: conftest.py
"""
import pytest
import requests

from public.yaml_util import delete_yaml


# 专文用来管理fixture固件的

@pytest.fixture(scope='session',autouse=True)
def exe_sql():
    print("前置操作")
    delete_yaml()
    yield "success"
    print("后置操作")


@pytest.fixture(scope="session")
def sess():
    s = requests.Session()
    yield s
    s.close()
