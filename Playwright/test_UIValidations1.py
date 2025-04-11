# Handling Alerts, popups, frames, Mouse Hover

import time

from playwright.sync_api import Page, expect



def test_UIValidations1(page:Page):
#Hide / Show Assertions, Placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect (page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect (page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

# Alerts and popups
# Here for on function first argument is event: dialog
# Second argument is function but we only require one line in function so no need to write
# its name (Anonymous function) and for this type of functions we can write "Lambda" before code
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm")


#Handling mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


# Handling Frames
# Store new frame in new page object and access frame element using that object
    framePage=page.frame_locator("#courses-iframe")
    framePage.get_by_role("link",name="All Access plan").click()
    expect(framePage.locator("body")).to_contain_text("Happy Subscibers")
    time.sleep(5)
