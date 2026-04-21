import time

import pytest
from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    # chromium engine - chrome, edge and playwright
    # invoking the chromium engine
    # default headless mode - faster
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # do some operations, login ->
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")

# page fixture only works for chromium in headless mode,  single context
def test_playwrightShortCut(page:Page):
    page.goto("https://www.rahulshettyacademy.com")

# CSS selector-- #<id> or .<class> or .<tagname>
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    # page.get_by_label("Password:").fill("Learning")
    page.get_by_role("radio", name="user").click()
    page.get_by_role("button", name="Okay").click()
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect username/password.  -- assertion
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

@pytest.mark.skip(reason="we are using chrome to test")
def test_firefoxBrowser(playwright:Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    # page.get_by_label("Password:").fill("Learning")
    page.get_by_role("radio", name="user").click()
    page.get_by_role("button", name="Okay").click()
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
