import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'


def get_user(user_id):
    response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
    pprint.pprint(f'GET {user_id}')
    pprint_response(response)


def create_user(name):
    data = {'name': name}
    response = requests.post(f'{BASE_URL_PETSTORE}/user', json=data)
    dict_text = json.loads(response.text)
    user_id = dict_text['message']
    pprint_response(response)
    return user_id


def delete_user(user_id):
    response = requests.delete(f'{BASE_URL_PETSTORE}/user/{user_id}')
    pprint_response(response)


def update_user(user_id, user_data):
    response = requests.put(f'{BASE_URL_PETSTORE}/user/{user_id}', json=user_data)
    pprint_response(response)


def get_order(order_id):
    response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
    pprint.pprint(f'GET {order_id}')
    pprint_response(response)


def create_order(order_id, status):
    data = {'status': status}
    response = requests.post(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=data)
    pprint_response(response)


def delete_order(order_id):
    response = requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
    pprint_response(response)


def update_order(order_id, order_data):
    response = requests.put(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=order_data)
    pprint_response(response)


def pprint_response(response):
    pprint.pprint(response.status_code)
    pprint.pprint(response.reason)
    pprint.pprint(response.text)


if __name__ == "__main__":
    # Пример использования:
    user_id = create_user('Leonard')
    get_user(user_id)
    
    order_id = 2
    create_order(order_id, 'placed')
    get_order(order_id)
    
    update_order(order_id, {
        "id": 3,
        "petId": 2,
        "quantity": 0,
        "shipDate": "2200-02-03T12:35:20.885+0000",
        "status": "placed"
    })
    get_order(order_id)
