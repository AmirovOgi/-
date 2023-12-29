import pytest
import allure
from fetcher import get_json_data

async def verify_data_presence(url):
    data = await get_json_data(url)
    assert data is not None
    return data

@pytest.mark.asyncio
@allure.feature("Data Fetching")
@allure.severity(allure.severity_level.NORMAL)
async def test_petstore_fetch(event_loop):
    data = await verify_data_presence("https://petstore.swagger.io/v2/store/order/10")
    assert "id" in data and "petId" in data and "quantity" in data

@pytest.mark.asyncio
@allure.feature("Data Fetching")
@allure.severity(allure.severity_level.NORMAL)
async def test_json_placeholder_fetch(event_loop):
    data = await verify_data_presence("https://jsonplaceholder.typicode.com/todos/1")
    assert "title" in data

@pytest.mark.asyncio
@allure.feature("Data Fetching")
@allure.severity(allure.severity_level.NORMAL)
async def test_dog_api_fetch(event_loop):
    data = await verify_data_presence("https://dog.ceo/api/breeds/image/random")
    assert "message" in data and "status" in data
