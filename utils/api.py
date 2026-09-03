from pyee import base
from playwright.sync_api import Playwright

orders_payload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "6960eac0c941646b7a8b3e68"
        }
    ]
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2YTk3MmE3ZDIxMDU0YmE0NjUwNGFjNzIiLCJ1c2VyRW1haWwiOiJzYWhpbC5raGVuYXQuY2FyZWVyQGdtYWlsLmNvbSIsInVzZXJNb2JpbGUiOjg3Njc5NDc2NDcsInVzZXJSb2xlIjoiY3VzdG9tZXIiLCJpYXQiOjE3ODg0MjExNjAsImV4cCI6MTgxOTk3ODc2MH0.AKokHf6zrPOsYa4KruSVnafo8AON2r-7x50K17q4QR0"

class APIUtils:

    def generate_token(self,playwright:Playwright):
       api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
       response = api_request_context.post("/api/ecom/auth/login",
       data={"userEmail":"sahil.khenat.career@gmail.com",
       "userPassword":"Rahul@12345"}
       )
       assert response.ok
       response_json=response.json()
       token=response_json['token']
       return token

    def create_order_api(self,playwright:Playwright):
        token = self.generate_token(playwright)

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post(url="/api/ecom/order/create-order", 
        data=orders_payload,
        headers={
            "Authorization": token
        })

        response_json=response.json()
        order_id = response_json['orders'][0]
        return order_id