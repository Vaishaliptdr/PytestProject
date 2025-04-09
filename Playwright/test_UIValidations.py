# Adding iPhone X and Nokia Edge to cart and validate cart count
# updated to 2 using assertions
# Using filter to get exact element

import time

import playwright
from playwright.sync_api import Page, expect


def test_UIValidationsScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")

# Using name filter
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()  # we can use click also
    page.get_by_role("button", name="Sign In").click()

# As "app-card" tag will return 4 products we need to filter out according to text
    iPhoneProduct=page.locator("app-card").filter(has_text="iphone X") #Using CSS by tagname
    iPhoneProduct.get_by_role("button",name="Add ").click()
    print("iPhone X added to cart")
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")  # Using CSS by tagname
    NokiaProduct.get_by_role("button", name="Add ").click()
    print("Nokia Edge added to cart")


    page.get_by_text("Checkout").click()

# Adding assertion to count the products in cart using css locator having
#common class name for both product
    expect(page.locator(".media-body")).to_have_count(2)

    time.sleep(5)