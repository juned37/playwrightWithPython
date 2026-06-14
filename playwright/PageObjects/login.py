class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self,useremail,userpassword):
        #page.get_by_role("textbox", name="email@example.com").click()
        self.page.get_by_role("textbox", name="email@example.com").fill(useremail)
        #page.get_by_role("textbox", name="enter your passsword").click()
        self.page.get_by_role("textbox", name="enter your passsword").fill(userpassword)
        self.page.get_by_role("button", name="Login").click()