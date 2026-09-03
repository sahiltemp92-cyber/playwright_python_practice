from playwright.sync_api import Page, expect
class OrderListPage:
    def __init__(self, page:Page):
        self.page = page
        self.orders_table=self.page.get_by_role("table",name="Order ID")
        self.home_button=self.page.get_by_role("button", name="HOME")
        self.no_orders_message=self.page.locator(".mt-4")
        

    def navigate_to_dashboard(self):
        self.home_button.click()
        from pages.dashboard_page import DashboardPage
        dashboard_page = DashboardPage(self.page)
        return dashboard_page

    def view_order(self,order_id:str):
       row=self.page.locator("tr").filter(has_text=order_id)
       row.get_by_role("button", name="View").click()
       expect(self.page).to_have_url(f"/client/#/dashboard/orders/{order_id}")
       from pages.order_details_page import OrderDetailsPage
       order_details_page = OrderDetailsPage(self.page)
       return order_details_page

    def delete_order(self,order_id:str):
       row=self.page.locator("tr").filter(has_text=order_id)
       row.get_by_role("button", name="Delete").click()
