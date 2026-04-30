from playwright.sync_api import Page, expect

def test_UI_checks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    #page.locator("#hide-textbox").click()
    page.get_by_role("button" , name="Hide").click()
    expect(page.locator("#displayed-text")).to_be_hidden()

    #handle the alert / dailog box
    page.get_by_role("button" , name="Confirm").click()
    #wait_for_dialog = page.wait_for_event("dialog")
    page.on("dialog", lambda dialog: dialog.accept())       #lambda dialog: dialog.accept()  # this is a one liner function to handle the dialog box
                                                            # lambda if wewrite we don't need to write a separate function to handle the dialog box, we can write it in one line

    #handling frames
    PageFrame = page.frame_locator("#courses-iframe")
    PageFrame.get_by_role("link" , name="All Access Plan").click()
    expect(PageFrame.locator("body")).to_contain_text("Happy")

def test_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link" , name="Top").click()

def test_dynamic_tables(page: Page):
    #handling dynamic tables 
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    rice = "Rice"

    # get column index
    col_index = page.locator("table thead th").all_inner_texts().index("Price")

    # get row
    row = page.locator("table tbody tr").filter(
        has=page.locator("td:first-child", has_text=rice)
    )
    # get value
    price = row.locator("td").nth(col_index).inner_text()

    assert price == "37"

