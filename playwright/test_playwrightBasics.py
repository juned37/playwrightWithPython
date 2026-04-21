from playwright.sync_api import Page

def test_playwrightBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


def test_playwrightshortcut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    #page.fill("input[name='username']", "rahulshettyacademy") # css selector
    #page.fill("#username", "rahulshettyacademy")   # id selector
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    #page.select_option("select.form-control", "teach")
    page.check("#terms")
    page.click("#signInBtn")
    #page.click("input[value='Sign In']")
    #page.click("text=Sign In")
    #page.click("input[name='signin']")
    page.inner_text("text=Shop Name")