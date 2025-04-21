from email.policy import default

import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome", help="chrome or firefox")
#For real world project we send url from terminal for that use this,
    #parser.addoption("--url_name", action="store", default="defaultURL", help="URL selection")
    #Run using: test_framework_Web_And_API.py --browser_name chrome url_name "url"-s


@pytest.fixture(scope="session")
def credentials(request):   #request : global parameter to access global or local variables
    #Need not define request, directly use it, can be used to access global env variables or
    # local function variables
    return request.param  #will find is there any parameter tied to test where the fixture is mentioned


@pytest.fixture
def browserInstance(playwright:Playwright,request):
    Browser_Name=request.config.getoption("browser_name")
    #URL_Name = request.config.getoption("url_name")
    if Browser_Name=="chrome":
        browser=playwright.chromium.launch(headless=False)
    elif Browser_Name=="firefox":
        browser=playwright.firefox.launch(headless=False)

    context=browser.new_context()
    page=context.new_page()
    #page.goto(URL_Name)
    yield page
    context.close()
    browser.close()