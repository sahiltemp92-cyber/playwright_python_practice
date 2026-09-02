
from playwright.sync_api import Page, expect

def test_table_handling(page: Page):
    """
    - Verify price of rice is equal to 37
        - Identify price column
        - Identify rice row
        - Extract price of rice
    """
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Web Table Logic
    number_of_columns = page.locator("th").count()

    # Identify Price Column
    col_value=0
    for index in range(number_of_columns):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            col_value = index
            print(f"Price column value is {col_value}")
            break

    # Identify Rice Row
    rice_row = page.locator("tr").filter(has_text="Rice")

    # Extract Price of rice
    rice_price=rice_row.locator("td").nth(col_value).inner_text()
    print(rice_price)

    assert rice_price == "37"