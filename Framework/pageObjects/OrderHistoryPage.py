from Framework.pageObjects.OrderDetailsPage import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self,page):
        self.page=page

    def selectOrder(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()
        order_Details_Page=OrderDetailsPage(self.page)
        return order_Details_Page



