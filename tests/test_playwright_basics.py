from time import time

import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.mark.smoke
def test_playwright_browser_launch(playwright):
    browser=playwright.chromium.launch(headless=False)
    context = browser.new_context() # do some operations, login ->
    page = context.new_page()
    page.goto("https://courses.rahulshettyacademy.com/")


def test_playwright_shortcut_launch(page:Page):
    page.goto("https://courses.rahulshettyacademy.com/")


def test_playwright_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("link",name="ProtoCommerce Home")).to_be_visible()

def test_firefox_browser(playwright: Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    page=firefox_browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_role("link", name="ProtoCommerce Home")).to_be_visible()

def test_playwright_more_locators(page: Page):

    # Hide/Show using placeholder locator
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.wait_for_timeout(4000)
