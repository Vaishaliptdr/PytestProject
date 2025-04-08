# Fixture has by default scope as function
# means every time function runs it will check for fixture
# Default scope of fixture is "function"

import pytest


@pytest.fixture(scope='function')

def fixtureFuction():
    print("I am code setup")

def test_firstCheck(fixtureFuction):
    print("This is my first test")


def test_secondCheck(fixtureFuction):
    print("This is my second test")
