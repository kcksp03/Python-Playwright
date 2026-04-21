import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #hide/display and placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(4)

    #mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    #Frame handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name = "All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    #webtables
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #check the price of rice is equal to 37.
    #identify the price column
    priceColValue = 0

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index;
            print(f"Price column value is {priceColValue}.")
            break

    #identify rice column
    riceRow = page.locator("tr").filter(has_text="Rice")

    #extract the price of the rice
    expect(riceRow.locator("td").nth(priceColValue)).to_contain_text("37")

