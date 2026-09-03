from playwright.sync_api import Page, expect
import re
class OrderDetailsPage:
    def __init__(self, page:Page):
        self.page = page
        self.thankyou_message=self.page.get_by_text("Thank you for Shopping With Us")

        """String locators"""

    def verify_order_thankyou_message(self):
        return (self.thankyou_message).is_visible()
    
    def verify_product_is_present(self, product_name):
        product_name_locator=self.product_name_text.replace("{product_name}", product_name)
        return (product_name_locator).is_visible()
    
    def verify_order_id_is_present(self, order_id):
        order_id_locator=self.page.get_by_text("{order_id}")
        return (order_id_locator).is_visible()