import pytest


@pytest.mark.usefixtures("dataLoad","setup")
class TestFixtures:

    def test_fixturedataLoad(self, dataLoad):
        print(dataLoad)
