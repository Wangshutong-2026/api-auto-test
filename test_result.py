import pytest
def test_pass():
    pass
def test_fail():
    assert False

@pytest.fixture
def f():
    1+'1'
def test_error(f):
    pass

@pytest.mark.skip
def test_skip():
    pass

@pytest.mark.xfail
def test_xfail():
    assert False

@pytest.mark.xfail
def test_xfass():
    assert 1 == 1