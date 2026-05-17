import time

from playwright.sync_api import Page, Playwright, Route, expect

fakePayload = {"data":[],"message":"No Orders"}

def intercept_response(route : Route):
    route.fulfill(
        json=fakePayload
    )


def test_e2e_web_api(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    #page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("3737junedbagban@gmail.com")
    #page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Juned@123")
    page.get_by_role("button", name="Login").click()
    #click on orders button
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(10)

