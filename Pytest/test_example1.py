import pytest


@pytest.mark.skip
@pytest.mark.smoke
def test_firstprograms():
    num = 1
    assert num == 1, "Number doesnt match"


def test_firstRegression(setup):
    print("This is regression")
