import json
import time , pytest

from playwright.sync_api import Page, Playwright, expect

from utils.test_api_utils import APIUTILS
from PageObjects.login import LoginPage
from PageObjects.dashboard import DashboardPage
from PageObjects.orderhistory import OrderHistoryPage

#reading data from json file
with open("data/credentials.json") as f:
    data = json.load(f)
    print(data)
    user_credentials_list = data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api_framework_1(playwright: Playwright,browser_Instance, user_credentials) -> None:
    UserEmail = user_credentials["UserEmail"]
    UserPassword = user_credentials["UserPassword"]
   
    # create order and get order id using API
    api_utils = APIUTILS()
    order_id = api_utils.createOrder(playwright,user_credentials)

    #login from PageObjects
    loginPage = LoginPage(browser_Instance)  # object for login page class

    #page.goto("https://rahulshettyacademy.com/client/")    # without page object model simple navigation 
    loginPage.navigate()  # calling navigate method from login page class

    # #page.get_by_role("textbox", name="email@example.com").click()
    # page.get_by_role("textbox", name="email@example.com").fill(user_credentials["UserEmail"])
    # #page.get_by_role("textbox", name="enter your passsword").click()
    # page.get_by_role("textbox", name="enter your passsword").fill(user_credentials["UserPassword"])
    # page.get_by_role("button", name="Login").click()
    loginPage.login(UserEmail,UserPassword)  # calling login method from login page class

    #click on orders button
    #page.get_by_role("button", name="ORDERS").click()
    dashboardPage = DashboardPage(browser_Instance)  # object for dashboard page class
    dashboardPage.selectOrderNavLink()  # calling selectOrderNavLink method from dashboard page

    orderHistoryPage = OrderHistoryPage(browser_Instance)  # object for order history page class
    orderHistoryPage.selectOrder(order_id)  # calling selectOrderById method
    #page.locator("tr", has_text=order_id).get_by_role("button", name="View").click()

    time.sleep(5)

