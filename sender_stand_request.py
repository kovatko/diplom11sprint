import requests
import configuration
import data

url1 = configuration.URL_SERVICE + configuration.CREATE_USER_ORDER
url2 = configuration.URL_SERVICE + configuration.ORDER_NUMBER


def create_order():
    response_order = requests.post(url1, headers=data.headers, json=data.order_body)
    if response_order.status_code == 201:
        return response_order.json()['track']
    else:
        raise ValueError("Ошибка при создании заказа, код ответа: {}".format(response_order))


def get_order_by_track(track_number):
    params = data.params_orders.copy()
    params['t'] = track_number
    return requests.get(url2, headers=data.headers, params=params)

