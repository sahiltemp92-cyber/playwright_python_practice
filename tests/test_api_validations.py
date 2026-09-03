from pages import order_details_page
from conftest import user_credentials
from utils.api import APIUtils
from pages.login_page import LoginPage
from playwright.sync_api import Playwright, expect

def test_e2e_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Create order via API
    api_util = APIUtils()
    order_id=api_util.create_order_api(playwright)
    
    # Login with credentials from JSON
    user_credentials = {
        "userEmail": "sahil.khenat.career@gmail.com",
        "userPassword": "Rahul@12345"
    }
    login_page=LoginPage(page)
    login_page.navigate_to_login_page()
    dashboard_page=login_page.login(user_credentials['userEmail'], user_credentials['userPassword'])

    # Go to Orders page  and Verify Order ID exists
    order_list_page=dashboard_page.navigate_to_orders()
    order_details_page=order_list_page.view_order(order_id)
    assert f"/client/#/dashboard/order-details/{order_id}" in page.url
    expect(order_details_page.thankyou_message).to_be_visible()
    