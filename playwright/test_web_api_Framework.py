import json
import time

from playwright.sync_api import Page, Playwright, expect

from utils.test_api_utils import APIUTILS

def test_e2e_web_api_Framework(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #reading data from json file
    with open("data/credentials.json") as f:
        data = json.load(f)
        print(data)

    # create order and get order id using API
    api_utils = APIUTILS()
    order_id = api_utils.createOrder(playwright)

    page.goto("https://rahulshettyacademy.com/client/")
    #page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill(data["user_credentials"][0]["UserEmail"])
    #page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill(data["user_credentials"][0]["UserPassword"])
    page.get_by_role("button", name="Login").click()

    #click on orders button
    page.get_by_role("button", name="ORDERS").click()
    page.locator("tr", has_text=order_id).get_by_role("button", name="View").click()
    time.sleep(5)

