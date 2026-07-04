import pytest
from pytest_bdd import given, scenarios, then, when , parsers

from PageObjects.login import LoginPage
from PageObjects.dashboard import DashboardPage
from PageObjects.orderhistory import OrderHistoryPage
from utils.test_api_utils_Framework import APIUTILS

scenarios('features/OrderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("Place order with {username} and {password}"))
def place_order(playwright, username, password, shared_data):
    user_credentials = {"UserEmail": username, "UserPassword": password}
    api_utils = APIUTILS()
    order_id = api_utils.createOrder(playwright,user_credentials)
    shared_data["order_id"] = order_id

@given("Verify user is on landing page")
def verify_landing_page(browser_Instance, shared_data):
    loginPage = LoginPage(browser_Instance)  # object for login page class
    loginPage.navigate()  # calling navigate method from login page class
    shared_data["loginPage"] = loginPage  # Store the loginPage object in shared_data for later use

@when(parsers.parse("Login with {username} and {password}"))
def login(username, password, shared_data, browser_Instance):
    loginPage = shared_data["loginPage"]  # Retrieve the loginPage object from shared_data
    loginPage.login(username, password)  # calling login method from login page class
    shared_data["dashboard_Page"] = DashboardPage(browser_Instance)  # Store the DashboardPage object in shared_data for later use

@when("Navigate to Order page")
def navigate_to_order_page(shared_data, browser_Instance):  
    dashboardPage = shared_data["dashboard_Page"]  # Retrieve the DashboardPage object from shared_data
    dashboardPage.selectOrderNavLink()  # calling selectOrderNavLink method from dashboard page
    shared_data["orderHistory_Page"] = OrderHistoryPage(browser_Instance)  # Store the OrderHistoryPage object in shared_data for later use
    

@then("select orderid")
def select_orderid(shared_data):
    orderHistoryPage = shared_data["orderHistory_Page"]  # Retrieve the OrderHistoryPage object from shared_data
    order_id = shared_data["order_id"]  # Retrieve the order_id from shared_data
    orderHistoryPage.selectOrder(order_id)  # calling selectOrderById method

    