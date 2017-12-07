# content of test_expectation.py
import pytest
from apps.fibonachi import fib

arr_pass = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


@pytest.mark.parametrize("test_input,expected", [
    (1, arr_pass[0:1]),
    (10, arr_pass[0:10]),
    (20, arr_pass[0:20])
])
def test_list(test_input, expected):
    assert fib(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (1, 1),
    (10, 10),
    (20, 20)
])
def test_count(test_input, expected):
    assert fib(test_input).__len__() == expected









