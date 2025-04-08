# If we define scope as module then fixture will be checked
# once in the entire test file

import pytest


@pytest.fixture(scope="module")

def fixtureFuction():
    print("I am code setup")

def test_firstCheck(fixtureFuction):
    print("This is my first test")


def test_secondCheck():
    print("This is my second test")
