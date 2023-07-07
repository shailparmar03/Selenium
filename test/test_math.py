import pytest


def add_two_numbers(a,b):
    return a+b


@pytest.mark.math
def test_samll_numbers():
    assert add_two_numbers(1,2)==3, "The sum of 1 and 2 must be 3"
@pytest.mark.math
def test_add_large_numbers():
    assert add_two_numbers(100,200), "The sum of 100 and 200 must be 300"
