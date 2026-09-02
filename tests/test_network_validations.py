from playwright.sync_api import Page, expect, Playwright

def test_network_1(page: Page):
    # Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*", intercept_redirect=True)

    page.get_by_placeholder("email@example.com").fill("sahil.khenat.career@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()

