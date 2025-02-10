import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print('Hello')


@pytest.mark.xfail
def test_secondRegression(setup):
    print("Wassup")
