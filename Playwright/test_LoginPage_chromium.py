# Handling textbox, Check box, Radio button, Dropdown, link
# Use expect for assertion as it will have auto wait : Playwright Assertion
# Playwright assertion using "expect" keyword
# Pytest assertion using "assert" keyword
# This test will fail as we have added assertion for failing cases,
# to make it pass remove assertion or add wrong credentials

import time

from playwright.sync_api import Page, expect


def test_LoginPage(page:Page):
    # browser=playwright.chromium.launch(headless=False)
    # context=browser.new_context()
    # page=context.new_page()

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")   #Textbox
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")       #Dropdown
    page.get_by_role("link", name="terms and conditions").click()  #Link

# CSS Selector can be created from id and class name and Tagname
# From id: #id
# From Class Name: .class_name
# From Tagname: tagname

    page.locator("input[value='user']").check()  #Radio Button

# Wait for the modal and click "Okay"
    page.locator("#okayBtn").click()

# You can verify it's selected
    expect(page.locator("input[value='user']")).to_be_checked()

    page.locator("#terms").check()     #Checkbox , we can use click also

# For button we can identify by its attribute name and value="Sign In"
    page.get_by_role("button",name="Sign In").click()    #button

# Playwright provides auto wait concept, no need to provide wait implicitly /explicitly
# Adding assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
# This test will fail as we have provided correct credentials
    time.sleep(5)
