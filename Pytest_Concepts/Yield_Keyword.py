# "yield" keyword separates setup tests from tear down steps
# We can pass more than one fixtures to functions as an argument

import pytest

@pytest.fixture()

def preWork():
    print("Setting up Browsers")
    yield
    print("Closing all connections")

@pytest.fixture()

def teamWork():
    print("Working")

def test_check(preWork, teamWork):
    print("Hello!!!!!!")


# Yield_Keyword.py::test_check Setting up Browsers
# Working
# PASSED                                      [100%]Hello!!!!!!
# Closing all connections