from playwright.sync_api import Page, expect
import re
class OrderDetailsPage:
    def __init__(self, page:Page, product_name:str):
        self.page = page
        self.message=self.page.get_by_text("Thankyou for your order")

        """String locators"""
        self.product_name_text=f"self.page.get_by_role('heading', name=re.compile(r'{product_name}', re.IGNORECASE))"

    def verify_order_message(self):
        expect(self.message).to_be_visible()
    
    def verify_product_is_present(self, product_name):
        product_name_locator=self.product_name_text.replace("{product_name}", product_name)
        expect(product_name_locator).to_be_visible()
        