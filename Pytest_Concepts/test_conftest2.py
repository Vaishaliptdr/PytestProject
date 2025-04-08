import pytest


@pytest.mark.smoke
def test_thirdCheck(fixtureFuction):
    print("This is my third test")


def test_fourthCheck():
    print("This is my fourth test")
