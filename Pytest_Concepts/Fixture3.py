# Fixture scope="class"
# Every class name and function name should start with Test/test
import pytest

@pytest.fixture(scope="class")
def fixture():
    print("I am fixture")

@pytest.mark.usefixtures("fixture")

class TestCheckFixtureScope:
    def test_check1(self):
        print("first check")

    def test_check2(self):
        print("Second check")

@pytest.mark.usefixtures("fixture")

class TestCheckFixtureScope1:

    def test_check3(self):
        print("third check")

    def test_check4(self):
        print("Fourth check")

# a=CheckFixtureScope()
# b=CheckFixtureScope1()
# a.test_check1()
# a.test_check2()
# b.test_check3()
# b.test_check4()