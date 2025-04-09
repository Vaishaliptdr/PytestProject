# First playwright test to open the browser and URL

# pytest-playwright package provide inbuilt global fixture named "playwright"
# pytest-playwright package provide inbuilt global fixture named "page"
# We provide that fixture to our tests
# chromium will be for Google Chrome and Microsoft Edge
# by default playwright will execute all tests in headless mode
# Running in headless will increase execution speed

# For customized requirements

from playwright.sync_api import Page
# Importing Page class from playwright.sync_api package of "pytest-playwright" package

def test_playwrightBasics(playwright):
    browser=playwright.chromium.launch(headless=False)  # Invoked chromium engine

# Opening browser in incognito mode, store that in context object
    context=browser.new_context()

# Soring the new context in page object
    page=context.new_page()
    page.goto("https://www.google.com/")

# For chromium, headless and 1 single context
def test_playwrightShortcut(page):
    page.goto("https://www.google.com/")

# To get suggestions from IDE
# By default it is in headless mode
# To run it in headed mode
# Click on green arrow>>modify run configuration>>in additional argument section add
# "--headed">>Apply>>ok>>It will run in headed mode
def test_playwrightShortcut1(page:Page):  # page:fixture from Page:class
    page.goto("https://www.google.com/")


