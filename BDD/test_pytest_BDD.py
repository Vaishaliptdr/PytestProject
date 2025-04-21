import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from Framework.pageObjects.LoginPage import Login_Page
from Framework.utils.apiBase import APIUtils

scenarios("Feature/OrderTransaction.feature")
@pytest.fixture
def shared_data():
    return {}
#shared data is fixture returning empty dictionary

# parsers.parse is a class which will parse the string and execute the code as a variable
# which is enclosed in {} and attach the value of it
@given(parsers.parse("place the item order with {username} and {password}"))
def place_item_order(playwright,username,password,shared_data):
    credentials={}
    credentials["User_Email"]=username
    credentials["User_Password"]=password
    api_utils = APIUtils()
    orderid = api_utils.createOrder(playwright, credentials)
    shared_data["OrderID"]=orderid

@given("the user is on landing page")
def user_on_landing_page(browserInstance, shared_data):  #Passing fixture as an argument
    login_Page = Login_Page(browserInstance)  # Created object of Login_Page class
    login_Page.navigat()
    shared_data["LoginPage"]=login_Page
#Setting dictionary's key value pair
# Here dictionary works like bucket to carry value of "login_Page" object
#We have done this as variable from 1 method can not be used in another
# method but using dictionary we can use it

@when(parsers.parse("User will login to portal with {username} and {password}"))
def login_to_portal(username,password,shared_data):
    login_Page=shared_data["LoginPage"]
    dashboard = login_Page.login(username,password)
    shared_data["dashboard_page"]=dashboard

@when("navigate to orders page")
def navigate_order_page(shared_data):
    dashboard=shared_data["dashboard_page"]
    orderHistory = dashboard.navigateOrderLink()
    shared_data["Order_History"]=orderHistory

@when("select the order id")
def select_orderId(shared_data):
    orderid=shared_data["OrderID"]
    orderHistory=shared_data["Order_History"]
    order_Details_Page = orderHistory.selectOrder(orderid)
    shared_data["OrderDetailsPage"]=order_Details_Page

@then("order message will successfully displayed")
def verify_success_message(shared_data):
    orderid = shared_data["OrderID"]
    order_Details_Page=shared_data["OrderDetailsPage"]
    order_Details_Page.verifySuccessMessage(orderid)
