import pytest
def test_pass():   #passed
    pass
def test_fail():   #failed
    assert False

@pytest.fixture
def f():   #error
    1+'1'
def test_error(f):
    pass

@pytest.mark.skip
def test_skip():   # skipped
    pass

@pytest.mark.xfail
def test_xfail(): #xfailed
    assert False

@pytest.mark.xfail
def test_xpass():
    assert 1 == 1  #xpassed