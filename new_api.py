from pprint import pprint
from datetime import datetime
from math import trunc
import asyncio
import aiohttp
from aiohttp.helpers import BasicAuth
import hmac
import hashlib
from typing import Dict
# import time
clientId = "0PcnK9Pe"
clientSecret = "4eUfqsfvcsec6VKbK3MUYo1ONqD1Yp9Q2IVW2iD-wEg"
timestamp = round(datetime.now().timestamp() * 1000)
nonce = "abcd"
data = ""
signature = hmac.new(
    bytes(clientSecret, "latin-1"),
    msg=bytes('{}\n{}\n{}'.format(timestamp, nonce, data), "latin-1"),
    digestmod=hashlib.sha256
).hexdigest().lower()


async def fetch_data(endpoint, params=None, private='no', payload = {}):
    if private.lower() == 'yes':
        base_url = 'https://test.deribit.com/api/v2/private/'            
    else:
        base_url = 'https://test.deribit.com/api/v2/public/'
    session = aiohttp.ClientSession()
    url = f'{base_url}{endpoint}'
    print(url)
    if endpoint.lower() != 'buy':
        async with session.get(url, params=params) as response:
            print(await response.json())
            if response.status == 200:
                return await response.json()
            else:
                print("Error fetching data")
                return None 
    else:
        async with session.post(url=url, auth=BasicAuth(clientId, clientSecret), json=payload) as response:
            print(await response.json())
            if response.status == 200:
                return await response.json()
            else:
                print("Error fetching data")
                return None 

async def auth():
        order_endpoint = 'auth'
        params = {'grant_type': 'client_credentials',
                  'client_id': clientId,
                  'client_secret': clientSecret,
                  'signature': signature,
                  'timestamp': timestamp,
                  'nonce': nonce}
        data = await fetch_data(endpoint=order_endpoint, params=params)
        if data != "Error fetching data":
            return data
        else:
            return "Error fetching data"
        
def buy(instrument_name, amount=10,price=66800):
    order_endpoint = 'buy'
    payload: Dict = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "private/buy",
                    "params": {
                        "instrument_name": "BTC-PERPETUAL",
                        "amount": 10,
                        "type": "market",
                        "label": "tester"
                        }
                    }
    # params = {'instrument_name': instrument_name,
    #           'amount': amount,
    #           'price': price}
    data = asyncio.run(fetch_data(endpoint=order_endpoint, payload=payload, private='yes'))
    return data

async def get_time():
    order_endpoint = 'get_time'
    data = await fetch_data(endpoint=order_endpoint)
    if data != "Error fetching data":
        return f'Time: {trunc(data['result']/1000)}'
    else:
        return "Error fetching data"

auth_data = asyncio.run(auth())
print(buy('BTC-PERPETUAL'))
# pprint(asyncio.get_event_loop().run_until_complete(get_time()))

# async def fetch_data(endpoint, params={}, private='no'):
#     if private.lower() == 'yes':
#         base_url = 'wss://test.deribit.com/api/v2'
#         endpoint = 'private/'+endpoint            
#     else:
#         base_url = 'wss://test.deribit.com/api/v2'
#         endpoint = 'public/'+endpoint 
#     # session = aiohttp.ClientSession()
#     url = f'{base_url}{endpoint}'
#     msg = {"jsonrpc" : "2.0",
#            "id" : 7365,
#            'method': endpoint,
#            'params': params}
#     print(base_url)
#     async with websockets.connect(uri=base_url) as websocket:
#         await websocket.send(msg)
#         while websocket.open:
#             response = await websocket.recv()
#         # if response.status == 200:
#         #     return await response.json()
#         # else:
#         #     print("Error fetching data")
#         #     return None 
#             print(response)
