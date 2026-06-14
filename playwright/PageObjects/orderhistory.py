class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,order_id):
        self.page.locator("tr", has_text=order_id).get_by_role("button", name="View").click()