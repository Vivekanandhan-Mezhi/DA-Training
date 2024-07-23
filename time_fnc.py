import datetime as dt
from math import trunc
import time
# import asyncio
# import aiohttp
import requests

def fetch_data(endpoint, params=None):
    base_url = 'https://test.deribit.com/api/v2/public/'
    url = f'{base_url}{endpoint}'
    response = requests.get(url, params=params)
    return response.json()
            
def get_order_book(instrument_name):
    order_endpoint = 'get_order_book'
    params = {'instrument_name': instrument_name}
    data = fetch_data(endpoint=order_endpoint, params=params)
    best_ask_price = data['result']['best_ask_price']
    best_bid_price = data['result']['best_bid_price']
    index_price = data['result']['index_price']
    instrument_name = data['result']['instrument_name']
    data = {"best_ask_price": best_ask_price,
            "best_bid_price": best_bid_price,
            "index_price": index_price,
            "instrument_name": instrument_name}
    return f'Order book details: {data}'
    # if data != "Error fetching data":               
    #     return f'Index price for {index_name}: {data['result']['index_price']}'
    # else:
    #     return "Error fetching data"
    
start = dt.datetime.now()
end = start + dt.timedelta(minutes=30)
while(start < end):
    print(get_order_book('BTC-PERPETUAL'))
    time.sleep(5)
    start += dt.timedelta(seconds=5)