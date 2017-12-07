from apps.fibonachi import fib
arr_pass = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


def test_count():
    for i in range(10):
        assert fib(i).__len__() == i


def test_list():
    for i in range(10):
        assert fib(i) == arr_pass[0:i]


def test_neg_1():
    assert fib(45.8).__len__() == 0


def test_neg_2():
    assert fib('str').__len__() == 0







