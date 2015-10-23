import math
import sys

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

    # math.isfinite was introduced in python 3.2
    if sys.version_info[0:3] > (3, 2, 0):
        assume(math.isfinite(x))
        assume(math.isfinite(y))
    else:
        assume(not math.isnan(x) and not math.isinf(x))
        assume(not math.isnan(y) and not math.isinf(y))
    assert x + y == mysum(x, y)


@given(x=text(), y=text())
def test_my_sum_string(x, y):
    print(x, y)
    assert x + y == mysum(x, y)
