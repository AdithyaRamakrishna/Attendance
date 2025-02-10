import pytest


@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print("i am executing at the last")


@pytest.fixture()
def dataLoad():
    print("this is from the dataLoad")
    return ["Adithya", "Testing"]
