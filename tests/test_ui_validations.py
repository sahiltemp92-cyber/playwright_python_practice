from tkinter import dialog
from playwright.sync_api import Playwright, Page, expect
import pytest
import json

# JSON file -> util -> access to test
with open("data/credentials.json") as f:
    test_data = json.load(f)
    print(test_data)

user_credentials_list = test_data['user_credentials']


def test_ui_validations_dynamic_script(page:Page):
    """Verify that 2 items are shown in cart. -> IphoneX and Nokia Edge"""

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").check()
    page.get_by_role("button", name="Sign In").click()

    # Click Add for Iphone X
    iphonex_product=page.locator("app-card").filter(has_text="iphone X")
    iphonex_product.get_by_role("button", name="Add ").click()

    # Click Add for Iphone X
    nokia_edge_product=page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge_product.get_by_role("button", name="Add ").click()

    # Checkout
    page.get_by_text("Checkout").click()

    # Verify Checkout has 2 items
    expect(page.locator(".media-body")).to_have_count(2)

    # Verify the link for respective phones of Nokia Edge and Iphone X are visible
    expect(page.get_by_role("link", name="Nokia Edge")).to_be_visible()
    expect(page.get_by_role("link", name="iphone X")).to_be_visible()


@pytest.mark.api
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://rahulshettyacademy.com/client/#/")
    page.fill("#userEmail", user_credentials['userEmail'])
    page.fill("#userPassword", user_credentials['userPassword'])
    page.click("#login")
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash", timeout=10000)
