from calculator import *

def test_add():
    actual = add(2, 2)
    expected = 4
    assert actual == expected

def test_subtract():
    actual= subtract(5, 4)
    expected = 1
    assert actual == expected
# def test_sub_default():
#     assert  subtract() == 1