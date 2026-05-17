import time

from playwright.sync_api import Page, Playwright, Route, expect

from utils.test_api_utils import APIUTILS


def intercept_response(route : Route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/?id=6a09941a965c23b43b20bae3")

def test_e2e_web_api(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_response)
    #page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("3737junedbagban@gmail.com")
    #page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Juned@123")
    page.get_by_role("button", name="Login").click()
    #click on orders button
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(10)


def test_session_storage(playwright: Playwright):
    api_uitls = APIUTILS()
    token = api_uitls.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token' , '{token}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(10)
