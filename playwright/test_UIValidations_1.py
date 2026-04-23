from playwright.sync_api import Page, expect

def test_UIValidations(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2se")  # incorrect password
    page.get_by_role("combobox").select_option("teach")
    page.check("#terms")
    page.click("#signInBtn")
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()