from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page:Page):
        self.page = page
        self.checkout_button=self.page.get_by_text("Checkout")
        self.orders_button = self.page.get_by_role("button", name="ORDERS")
        self.cart_button=self.page.get_by_text("Cart")
        self.product_cards=self.page.locator(".card-body")
        
    
    def add_product_to_cart(self,product_name):
        self.product_cards.filter(has_text=product_name).get_by_role("button", name=" Add To Cart").click()

    def verify_cart_items(self,expected_item_count):
        expect(self.cart_items).to_have_count(expected_item_count)

    def verify_product_links(self,product_name):
        expect(self.page.get_by_role("link", name=product_name)).to_be_visible()

    def checkout(self):
        self.checkout_button.click()
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.page)
        
    def navigate_to_orders(self):
        self.orders_button.click()
        from pages.orders_list_page import OrderListPage
        order_list_page = OrderListPage(self.page)
        return order_list_page
    
    def navigate_to_cart(self):
        self.cart_button.click()
        from pages.cart_page import CartPage
        return CartPage(self.page)
