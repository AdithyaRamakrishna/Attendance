import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 20, 30),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def add(a,b):
    return a+b
