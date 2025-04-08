# We can fetch value from fixture in test

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


def test_returnValue(returnValue):
    if returnValue==5:
        print("Fixture returns 5")

