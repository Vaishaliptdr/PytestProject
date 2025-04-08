# Fixture
# If we provide fixture name as an argument to test then
# first fixture is executed then test will execute
# If we do not pass fixture as an argument then only test will execute

import pytest


@pytest.fixture

def fixtureFuction():
    print("I am code setup")

def test_firstCheck(fixtureFuction):
    print("This is my first test")
