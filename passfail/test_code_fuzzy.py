import math

# fuzz testing tools
from hypothesis import given, assume
from hypothesis.strategies import floats, integers, text


from .code import mysum


@given(x=integers(), y=integers())
def test_my_sum_integers(x, y):
    print(x, y)      # print outputs for entertainment
    assert x + y == mysum(x, y)


@given(x=floats(), y=floats())
def test_my_sum_floats(x, y):
    print(x, y)
    assume(math.isfinite(x))
    assume(math.isfinite(y))
    assert x + y == mysum(x, y)


@given(x=text(), y=text())
def test_my_sum_string(x, y):
    print(x, y)
    assert x + y == mysum(x, y)
