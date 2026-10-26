def test_ok():
    open('main.py')
    assert 1 == 1

def test_fail():
    assert False