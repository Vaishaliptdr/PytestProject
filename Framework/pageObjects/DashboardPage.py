from pydoc import pager

from Framework.pageObjects.OrderHistoryPage import OrderHistoryPage


class Dashboard:

    def __init__(self,page):
        self.page=page

    def navigateOrderLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_History=OrderHistoryPage(self.page)
        return order_History