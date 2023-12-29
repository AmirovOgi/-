import requests
import pytest
from pydantic import BaseModel
import allure

base_url = "https://petstore.swagger.io/v2/"

class UserData(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str

class OrderData(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str

class AnswerUserData(BaseModel):
    code: int
    type: str
    message: str

@allure.feature("Pet Users")
class TestPetUsersApi:

    @allure.title("Retrieve User")
    def test_fetch_user(self):
        response = requests.get(base_url + "user/string")
        assert response.status_code == 200
        user_data = response.json()
        UserData(**user_data)

    @allure.title("Create User")
    def test_create_user(self):
        data = {"id": 1, "username": "new_user", "firstname": "string", "lastname": "string",
                "email": "user@example.com", "password": "string", "phone": "79096895085", "userStatus": 0}
        response = requests.post(base_url + "user", json=data)
        assert response.status_code == 200
        user_data = response.json()
        AnswerUserData(**user_data)

@allure.feature("Pet Store")
class TestPetStoreApi:

    @allure.title("Retrieve Store Inventory")
    def test_fetch_store_inventory(self):
        response = requests.get(base_url + "store/inventory")
        assert response.status_code == 200
        store_data = response.json()

    @allure.title("Create Order")
    def test_create_order(self):
        data = {"id": 0, "petId": 0, "quantity": 0, "shipDate": "2023-11-17T08:03:55.254Z", "status": "placed"}
        response = requests.post(base_url + "store/order", json=data)
        assert response.status_code == 200
        order_data = response.json()
        OrderData(**order_data)
