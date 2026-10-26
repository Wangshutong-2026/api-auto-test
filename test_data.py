def test_number():
    assert 1 ==2

def test_str():
    a = 'aaaaa'
    b = 'aaabc'
    assert a == b

def test_list():
    a = list('aaaaa')
    b = list('aaabc')
    assert a == b

def test_dict():
    a = {'a':1, 'b':2, 'c':3}
    b = {'a':2, 'b':2, 'c':3}
    assert a == b