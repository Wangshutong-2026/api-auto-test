import allure
from commons.yaml_utils import read_yaml
from commons.runner_utils import runner
import pytest

@pytest.mark.web
def test_yaml():
    data = read_yaml('tests/test_api.yaml')
    allure.title(data['name'])
    my_var = {}
    for step in data['steps']:
        for k,v in step.items():
            runner(k,v,my_var)