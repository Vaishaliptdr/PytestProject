import pytest


@pytest.fixture()
def preWork():
    print("Setup browser")
    return "PASS"

@pytest.fixture()
def returnValue():
    print("Setup environment")
    return 5


def test_initialWork(preWork):
    print("Working on initial test")
    assert preWork=="PASS"

@pytest.mark.skip("Incomplete test")
#Here pytest will skip the test, we can add reason for skipping
def test_returnValue(returnValue):
    if returnValue==5:
        print("Fixture returns 5")

