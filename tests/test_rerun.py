import random
import pytest

@pytest.mark.ut
def test_rerun():
    x = random.randint(1,10)  #随机数
    assert x >= 9