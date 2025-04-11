# Intercepting response calls with route->fulfil methods to test edge cases

# Validating case where no orders are present on user's account without deleting the
# actual orders
# route having property which have all info of API call
# Fulfill method will be used ti satisfy api call that what response it should
# give on hitting mentioned url
# Make api call from browser>>Api will contact server>>Returns back response>>Browser will use
# that response to generate HTML


from playwright.sync_api import Page, expect

fakeOrderResponse={"data":[],"message":"No Orders"}


def interceptResponse(route):
    route.fulfill(json=fakeOrderResponse)


def test_Network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",interceptResponse)
    page.locator("#userEmail").fill("vaishalidusane@gmail.com")
    page.locator("#userPassword").fill("Learning@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="  ORDERS").click()
    order_text=page.locator(".mt-4").text_content()
    print(f"Order text: {order_text}")

