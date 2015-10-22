import pytest

from .code import mysum


def test_1():
    """ what does this test do? """
    ret_val = mysum(1, 3)
    assert ret_val == 4


def test_2():
    assert mysum("Hello", "World") == "HelloWorld"


def test_an_exception():
    with pytest.raises(TypeError):
        mysum("Hello", 42)
