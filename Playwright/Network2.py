# Intercepting request calls with route->continue methods to test edge cases

# trying to access another users order id with our account and validating as it giving
# unauthorized access error

import time

from playwright.sync_api import Page, expect



def interceptResponse(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_Network2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    #API hit after clicking on View button from order
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptResponse)
    page.locator("#userEmail").fill("vaishalidusane@gmail.com")
    page.locator("#userPassword").fill("Learning@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    text=page.locator(".blink_me").text_content()
    print(f"Text content: {text}")
    expect(page.locator(".blink_me")).to_be_visible()


    #time.sleep(5)




    # route having property which have all info of API call
    # Fulfill method will be used ti satisfy api call that what response it should
    # give on hitting mentioned url
    # Make api call from browser>>Api will contact server>>Returns back response>>Browser will use that response to generate HTML