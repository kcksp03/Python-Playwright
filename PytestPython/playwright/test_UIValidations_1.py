import pytest
from playwright.sync_api import Page, expect

@pytest.mark.testlogin
def test_UIValidationDynamicScript(page:Page):

    #Login
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_hidden()

    # iphone X, Nokia edge -> verify 2 items are showing in cart.
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button", name="Add ").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button", name="Add ").click()

    # goto cart page and check for the items
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-body").filter(has_text="iphone X")).to_be_visible()
    expect(page.locator(".media-body").filter(has_text="Nokia Edge")).to_be_visible()


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click() #new page
        childPage = newPage_info.value

        text = childPage.locator(".red").text_content()
        print(text)

        assert "mentor@rahulshettyacademy.com" in text

        # to use if text is constant but email changes

        # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        # index 0 -> Please email us
        # index 1 ->  mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")

        # index 0 -> mentor@rahulshettyacademy.com
        # index 1 -> with below template to receive response
        email = words[1].strip().split(" ")[0]

        print(email)

        assert email == "mentor@rahulshettyacademy.com"

