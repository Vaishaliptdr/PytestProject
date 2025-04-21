# Create order from API>> Login with UI>>Check order is created or not>>Validate order Details
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Above 3 lines code will programmatically add the parent directory to your path — only for that run.

import json

import pytest
from playwright.sync_api import Playwright, expect


from Framework.pageObjects.LoginPage import Login_Page

from Framework.pageObjects.DashboardPage import Dashboard
from Framework.utils.apiBase import APIUtils
#json>>utils>>Access input data
with open('Data/credentials.json')as f:    #Open json file as f object
    test_data=json.load(f)                 #Storing json file from f object to test_data object
    print(f"Our test data is: {test_data}")  #Printing Test Data as list

# Storing the json dictionaries in to python list format
   # test_data={'UserCredentials': [{'User_Email': 'vaishalidusane@gmail.com', 'User_Password': 'Learning@123'}, {'User_Email': 'rahulshetty@gmail.com', 'User_Password': 'Iamking@000'}, {'User_Email': 'anshika@gmail.com', 'User_Password': 'Iamking@000'}]}
    user_credential_list=test_data['UserCredentials'] #Accessing from json file (key)




@pytest.mark.parametrize("credentials",user_credential_list)  #credentials is parameter of "credentials" fixture
def test_e2e_Web_API(playwright:Playwright,browserInstance,credentials):   #credentials is fixture written in "conftext" file
# Fixture returns parameter value

    UserName=credentials["User_Email"]
    Password=credentials["User_Password"]

#Create Order from API (mentioned in file apiBase.py)
    api_utils=APIUtils()
    orderid=api_utils.createOrder(playwright,credentials)

#Login
    login_Page=Login_Page(browserInstance)  #Created object of Login_Page class
    login_Page.navigat()

# As "login" method returns dashboard object we need to store it in dashboard object here,
# then call dashboard page methods by using that object
# Here we are avoiding to create object of Dashboard class here in test file
    dashboard=login_Page.login(UserName,Password)
#In same way "navigateOrderLink" returns orderHistory object
    orderHistory=dashboard.navigateOrderLink()
    order_Details_Page=orderHistory.selectOrder(orderid)
    order_Details_Page.verifySuccessMessage(orderid)


#Order history page>>Validating on UI, that order created from API is present on UI
    # row=page.locator("tr").filter(has_text=orderid)
    # row.get_by_role("button", name="View").click()





