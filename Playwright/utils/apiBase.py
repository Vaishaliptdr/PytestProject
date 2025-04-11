from multiprocessing.managers import Token

from playwright.sync_api import Playwright
orders_Payload={"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}
LoginData={"userEmail": "vaishalidusane@gmail.com", "userPassword": "Learning@123"}


class APIUtils:

    def getToken(self,playwright:Playwright):
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=api_request_context.post("/api/ecom/auth/login",
                                            data=LoginData)
        assert response.ok
        print(response.json())
        responseBody=response.json()  #Python reads json as dictionary
        return responseBody["token"]  #Returning value of token keyword from dictionary


    def createOrder(self, playwright:Playwright):
        Token=self.getToken(playwright)
        api_Request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=api_Request_context.post("/api/ecom/order/create-order",
                                          data=orders_Payload,
                                          headers={"authorization":Token,"Content-type":"application/json"}
                                          )
        print(f"Create order response: {response.json()}")
        responseBody=response.json()
        return responseBody["orders"][0]   #As orders are stored as list we need to provide index