import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from playwright.sync_api import Playwright, expect
from pages.login_page import LoginPage
from utils.api import APIUtils

scenarios('../features/order_transaction.feature')


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_item_order_with_username_and_password(playwright: Playwright, username, password, shared_data):
    user_credentials = {'userEmail': username, 'userPassword': password}
    print(f'place the item order with {username} and {password}')
    api_utils = APIUtils()
    order_id = api_utils.create_order_api(playwright, user_credentials)
    shared_data['order_id'] = order_id


@given('the user is on landing page')
def the_user_is_on_landing_page(browser_instance, shared_data):
    print('the user is on landing page')
    login_page = LoginPage(browser_instance)
    login_page.navigate_to_login_page()
    shared_data['login_page'] = login_page


@when(parsers.parse('I login to portal with {username} and {password}'))
def i_login_to_portal_with_username_and_password(username, password, shared_data):
    print(f'i login to portal with {username} and {password}')
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page


@when('Navigate to orders page')
def i_navigate_to_orders_page(shared_data):
    print('Navigate to orders page')
    dashboard_page = shared_data['dashboard_page']
    order_list_page = dashboard_page.navigate_to_orders()
    shared_data['order_list_page'] = order_list_page


@when('Select the order id')
def select_order_id(shared_data):
    print('Select the order id')
    order_list_page = shared_data['order_list_page']
    order_details_page = order_list_page.view_order(shared_data['order_id'])
    shared_data['order_details_page'] = order_details_page


@then('order message is successfully displayed')
def order_message_is_successfully_displayed(shared_data):
    print('order message is successfully displayed')
    order_details_page = shared_data['order_details_page']
    expect(order_details_page.thankyou_message).to_be_visible()