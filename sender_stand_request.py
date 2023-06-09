import configuration
import requests
import data

def post_new_orders(body):
    return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDERS,
                         json=body)

def get_new_track():
    order_responce = post_new_orders(data.order_body)
    track = order_responce.json()["track"]
    return track

def get_order():
    track = get_new_track()
    params = data.order_params
    params['t'] = track
    return requests.get(configuration.URL_SERVER + configuration.GET_ORDERS,
                        params=params)



