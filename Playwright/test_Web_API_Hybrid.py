# Create order from API>> Login with UI>>Check order is created or not>>Validate order Details

from playwright.sync_api import Playwright, expect

from Playwright.utils.apiBase import APIUtils


def test_e2e_Web_API(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

#Create Order from API (mentioned in file apiBase.py)
    api_utils=APIUtils()
    orderid=api_utils.createOrder(playwright)


#Login
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("vaishalidusane@gmail.com")
    page.locator("#userPassword").fill("Learning@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button",name="  ORDERS").click()

#Order history page>>Validating on UI, that order created from API is present on UI
    row=page.locator("tr").filter(has_text=orderid)
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print(f"Order {orderid} created successfully")



