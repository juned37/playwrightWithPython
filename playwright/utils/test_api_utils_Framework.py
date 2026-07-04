from playwright.sync_api import Playwright

userLogin_payload = {"userEmail": "3737junedbagban@gmail.com", "userPassword": "Juned@123"}

createOrder_payload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class APIUTILS:

    def getToken(self , playwright: Playwright,user_credentials):
        user_email = user_credentials["UserEmail"]
        user_password = user_credentials["UserPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response  = api_request_context.post(url="api/ecom/auth/login",
                                             data={"userEmail": user_email, "userPassword": user_password},
                                             headers={"Content-Type": "application/json"})
        assert response.ok
        token = response.json()["token"]
        print(token)
        return token

    def createOrder(self , playwright: Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response  = api_request_context.post(url="api/ecom/order/create-order",
                                 data=createOrder_payload,
                                 headers={"Authorization": token , 
                                          "Content-Type": "application/json"}) 
        assert response.ok
        response_body = response.json()
        print(response_body)
        order_id = response.json()["orders"][0]
        print(order_id)
        return order_id
