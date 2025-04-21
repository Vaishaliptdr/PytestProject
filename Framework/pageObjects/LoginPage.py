from Framework.pageObjects.DashboardPage import Dashboard


class Login_Page:

    def __init__(self,page):
        self.page=page

    def navigat(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,email,password):
        self.page.locator("#userEmail").fill(email)
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="Login").click()

        dashboard = Dashboard(self.page)
        return dashboard
