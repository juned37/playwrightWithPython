from playwright.sync_api import Page, expect

nokia = "Nokia"
samsung = "Samsung"

def test_UIValidations(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.check("#terms")
    page.click("#signInBtn")
    page.inner_text("text=Shop Name")
    # MY WAY OF DOING IT
    # page.locator(f"//div[contains(@class,'card')]//h4/a[contains(normalize-space(), '{nokia}')]/ancestor::div[contains(@class,'card')]//button").click()
    # page.locator(f"//div[contains(@class,'card')]//h4/a[contains(normalize-space(), '{samsung}')]/ancestor::div[contains(@class,'card')]//button").click()
    # page.click("text=Checkout")
    # TEACHER'S WAY OF DOING IT
    page.locator("app-card").filter(has_text=nokia).get_by_role("button").click()
    page.locator("app-card").filter(has_text=samsung).get_by_role("button").click()
    page.click("text=Checkout")
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page = newPage_info.value
        child_page.wait_for_load_state()
        print(child_page.title())