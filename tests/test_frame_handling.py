from playwright.sync_api import Page, expect

def test_frame_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")
