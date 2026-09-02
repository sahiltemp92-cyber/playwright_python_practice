from tkinter import dialog

from playwright.sync_api import Page, expect

def test_child_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.get_by_text("Free Access to InterviewQues").click()    # new page
        child_page = new_page_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at ")
        print(words)
        email = words[1].split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"

