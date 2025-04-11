# Save and inject the session cookies into browser at run time with playwright
import time

from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from Playwright.utils.apiBase import APIUtils


def test_Session_Storage(playwright:Playwright):
    api_Utils= APIUtils()
    getToken=api_Utils.getToken(playwright)
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

#Script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_role("button",name="  ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
    time.sleep(5)

