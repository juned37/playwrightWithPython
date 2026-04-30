import time

from playwright.sync_api import Page, Playwright, expect

def test_codegen_generatedFlow(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("3737junedbagban@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Juned@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Add To Cart").nth(1).click()
    page.locator(".btn.btn-custom", has_text="Cart").click()
    page.get_by_role("button", name="Checkout❯").click()
    page.get_by_role("textbox", name="Select Country").click()
    page.get_by_role("textbox", name="Select Country").type("ind")
    page.get_by_text("India", exact=True).click()
    #page.set_viewport_size({"width": 500, "height": 500})
    page.get_by_text("Place Order").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="Delete").click()

################ to generate code using playwright codegen command in terminal ##################
# playwright codegen https://rahulshettyacademy.com/client/#/auth/login
# do the steps in the browser and then copy the generated code and paste it in the file to check the flow and update the locators if needed and then run the test to check the flow