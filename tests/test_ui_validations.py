from tkinter import dialog

from playwright.sync_api import Page, expect


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

