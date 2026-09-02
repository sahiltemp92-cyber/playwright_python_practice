
from playwright.sync_api import Page, expect

def test_alert_box_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Confirm Dialog Boxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    # Alert Dialog Boxes
    page.get_by_role("button", name="Alert").click()
