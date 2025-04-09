# Handling child window
# Python string methods to retrieve the values from string

import time

from playwright.sync_api import Page


def test_HandlingChildWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

# If we expect any child window, before that use this code and store the info in any
# variable >>then by using value attribute of that variable get the access of Child window
# here "expect_popup()" is listener event

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
        childPage = new_page_info.value
        text= childPage.locator(".red").text_content()
        print(text)
#O/P=Please email us at mentor@rahulshettyacademy.com with below template to receive response
        word=text.split("at")
#word[0]="Please email us "
#word[1]= " mentor@rahulshettyacademy.com with below template to receive response"

        print("word[0]: "+word[0])
        print("word[1]: "+word[1])

        email=(word[1]).split(" ")
#email[0]= " "
#email[1]= "mentor@rahulshettyacademy.com"
        print("email[0]: "+email[0])
        print("email[1]: "+email[1])
        assert (email[1])=="mentor@rahulshettyacademy.com"

    time.sleep(5)


# Use of split() and strip() method from string class
# split() method splits the sentence according to provided splitting point and stores it
# in indexed structure starting with 0
# strip() method removes spaces from start and end of the string

def test_HandlingStrings(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
        childPage = new_page_info.value
        text= childPage.locator(".red").text_content()
        print(text)
#O/P=Please email us at mentor@rahulshettyacademy.com with below template to receive response
        word=text.split("at")

#word[0]= "Please email us "
#word[1]= " mentor@rahulshettyacademy.com with below templ"
#word[2]= "e to receive response"

        print("word[0]: "+word[0])
        print("word[1]: "+word[1])
        print("word[2]: "+word[2])

        email=(word[1]).strip().split(" ")  # strip method will remove initial and last spaces from string if any
# email[0]= "mentor@rahulshettyacademy.com"
# email[1]= "with"
# email[2]= "below"
# email[3]= "templ"

        print("email[0]: "+email[0])
        print("email[1]: "+email[1])
        print("email[2]: "+email[2])
        print("email[3]: "+email[3])
        assert (email[0])=="mentor@rahulshettyacademy.com"

    time.sleep(5)