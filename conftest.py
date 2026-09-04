import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Run tests in respective Browser")
    parser.addoption("--url_name", action="store", default="https://rahulshettyacademy.com/client", help="Run tests with base url")

@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser_name")

@pytest.fixture
def user_credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright, request):
    # Setup
    browser_name = request.config.getoption("--browser_name")
    url_name = request.config.getoption("--url_name")
    
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name=="safari":
        browser = playwright.webkit.launch(headless=False)
    else:
        print("Browser not found")
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Pause and save state
    yield page

    # Resume and teardown
    page.close()
    context.close()
    browser.close()