# Run test on firefox browser

import time


from playwright.sync_api import Playwright, expect

# No shortcut for firefox browser
def test_LoginPage(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()

# CSS Selector can be created from id and class name
# From id: #id
# From Class Name: .class_name
    page.locator("#terms").check()     #we can use click also

# For button we can identify by its attribute name and value="Sign In"
    page.get_by_role("button",name="Sign In").click()

# Playwright provides auto wait concept, no need to provide wait implicitly /explicitly
# Adding assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
# This test will fail as we have provided correct credentials
    time.sleep(5)
