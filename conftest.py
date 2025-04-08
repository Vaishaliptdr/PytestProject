# We can store fixture in conftest.py file and use that fixture in functions
# mentioned in other files.

# To run multiple files at a time we need to run command "pytest" but for that
# we need to rename the files to start with test_
# Means pytest only identifies files start with "test_" names

# If scope="session" then fixture will run only once though multiple files are run
# Though mentioned it multiple time....


import pytest


@pytest.fixture(scope="session")
def fixtureFuction():
    print("I am code setup")