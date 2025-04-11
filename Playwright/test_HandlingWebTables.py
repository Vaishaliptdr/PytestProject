#Handling Web Tables
# Check the price of rice is 37
# Identify rice column
# Identify rice row
# Extract price of the rice

from playwright.sync_api import Page, expect


def test_HandlingWebTable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    ColumnCount=page.locator("th").count()
    for index in range(ColumnCount):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColumnValue = index
            print(f"price column value is: {priceColumnValue}")
            break

    riceRow=page.locator("tr").filter(has_text="rice")
    expect(riceRow.locator("td").nth(priceColumnValue)).to_contain_text("37")
