from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
    
        self.email_textbox=self.page.get_by_role("textbox", name="email@example.com")
        self.password_textbox=self.page.get_by_placeholder("enter your passsword")
        self.login_button=self.page.get_by_role("button", name="Login")


    def navigate_to_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client/")
    
    def login(self,userEmail,userPassword):
        self.email_textbox.fill(userEmail)
        self.password_textbox.fill(userPassword)
        self.login_button.click()
        from pages.dashboard_page import DashboardPage
        dashboard_page = DashboardPage(self.page)
        return dashboard_page
        
