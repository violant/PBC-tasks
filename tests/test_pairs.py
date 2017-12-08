import pytest
from apps.pairs import pair

_empty_set = set([])


@pytest.mark.positive
@pytest.mark.parametrize("test_input,expected", [
    ((4, 5, 6, 7, 3), set([(3, 7), (4, 6)])),
    ((17, 4, 5, 6, 5, 5), set([(4, 6), (5, 5)])),
    ([1, 2, 3, 4, 5], _empty_set)
])
def test1(test_input, expected):
    assert expected == pair(*test_input)


@pytest.mark.negative
@pytest.mark.parametrize("test_input,expected", [
    ([], _empty_set),
    ([765], _empty_set)
])
def test2(test_input, expected):
    assert expected == pair(test_input)
