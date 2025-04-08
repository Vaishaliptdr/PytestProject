# We can tag the test like smoke, sanity, regression and run it through
# pytest -m smoke or pytest -m regression
import pytest


def test_firstCheck(fixtureFuction):
    print("This is my first test")

@pytest.mark.smoke1
def test_secondCheck():
    print("This is my second test")