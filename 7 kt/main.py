from db import add_record
import aiohttp
import pytest
import asyncio
import threading

async def async_resolve():
    return "Value"

@pytest.mark.asyncio
async def test_async_resolve(event_loop):
    assert await async_resolve() == "Value"

async def async_raise_error():
    raise ValueError("Expected error.")

@pytest.mark.asyncio
async def test_async_raise_error(event_loop):
    with pytest.raises(ValueError, match="Expected error."):
        await async_raise_error()

async def async_fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://petstore.swagger.io/v2/user/string") as resp:
            return await resp.json()

@pytest.mark.asyncio
async def test_async_fetch_data(event_loop):
    data = await async_fetch_data()
    assert all(key in data for key in ["id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"])

@pytest.mark.asyncio
async def test_insert_to_db(event_loop):
    data = ("val1", "val2")
    assert await add_record(data) is not None

def run_async_in_thread(async_func, *args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    result = None

    def run():
        nonlocal result
        result = loop.run_until_complete(async_func(*args, **kwargs))
        loop.stop()

    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

    return loop, result

async def async_task():
    await asyncio.sleep(1)
    return "Result"

@pytest.mark.asyncio
async def test_run_async_thread(event_loop):
    loop, res = run_async_in_thread(async_task)
    assert res == "Result"
    loop.close()
