import requests
from pprint import pprint
from datetime import datetime
from math import trunc
import asyncio
import aiohttp
# import time

class DebritTrade:
    def __init__(self):
        self.base_url = 'https://www.deribit.com/api/v2/public/'
        self.params = {}
        self.session = aiohttp.ClientSession()
    
    async def fetch_data(self, endpoint, params=None):
        url = f'{self.base_url}{endpoint}'
        async with self.session.get(url, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                print("Error fetching data")
                return None 

    async def get_time(self):
        order_endpoint = 'get_time'
        data = await self.fetch_data(endpoint=order_endpoint)
        if data != "Error fetching data":
            return f'Time: {trunc(data['result']/1000)}'
        else:
            return "Error fetching data"

    async def get_currencies(self):
        order_endpoint = 'get_currencies'
        data = await self.fetch_data(endpoint=order_endpoint)
        if data != "Error fetching data":
            return f'Currencies available: {[data['currency'] for data in data['result']]}'
        else:
            return "Error fetching data"        

    async def get_index_price(self, index_name):
        order_endpoint = 'get_index_price'
        params = {'index_name': index_name}
        data = await self.fetch_data(endpoint=order_endpoint, params=params)
        if data != "Error fetching data":               
            return f'Index price for {index_name}: {data['result']['index_price']}'
        else:
            return "Error fetching data"

    async def get_index_price_names(self):
        order_endpoint = 'get_index_price_names'
        data = await self.fetch_data(endpoint=order_endpoint)
        if data != "Error fetching data":
            return f'List of index names: {data['result']}'
        else:
            return "Error fetching data"   
        

    async def get_order_book(self, instrument_name):
        order_endpoint = 'get_order_book'
        params = {'instrument_name': instrument_name}
        data = await self.fetch_data(endpoint=order_endpoint, params=params)
        if data != "Error fetching data":
            best_ask_price = data['result']['best_ask_price']
            best_bid_price = data['result']['best_bid_price']
            index_price = data['result']['index_price']
            instrument_name = data['result']['instrument_name']
            data = {"best_ask_price": best_ask_price,
                    "best_bid_price": best_bid_price,
                    "index_price": index_price,
                    "instrument_name": instrument_name}
            return f'Order book details: {data}'
        else:
            return "Error fetching data"

    async def ticker(self, instrument_name):
        order_endpoint = 'ticker'
        params = {'instrument_name': instrument_name}
        data = await self.fetch_data(endpoint=order_endpoint, params=params)
        if data != "Error fetching data":
            best_ask_price = data['result']['best_ask_price']
            best_bid_price = data['result']['best_bid_price']
            index_price = data['result']['index_price']
            instrument_name = data['result']['instrument_name']
            data = {"best_ask_price": best_ask_price,
                    "best_bid_price": best_bid_price,
                    "index_price": index_price,
                    "instrument_name": instrument_name}
            return f'Details from ticker: {data}'
        else:
            return "Error fetching data"
        
    async def status(self):
        order_endpoint = 'status'
        data = await self.fetch_data(endpoint=order_endpoint)
        if data != "Error fetching data":
            return data
        else:
            return "Error fetching data"
        
    async def get_contract_size(self, instrument_name):
        order_endpoint = 'get_contract_size'
        params = {'instrument_name': instrument_name}
        data = await self.fetch_data(endpoint=order_endpoint, params=params)
        if data != "Error fetching data":
            return f'Contract size for {instrument_name}: {data['result']['contract_size']}'
        else:
            return "Error fetching data"
    
    async def auth(self):
        order_endpoint = 'auth'
        data = await self.fetch_data(endpoint=order_endpoint)
        if data != "Error fetching data":
            return data
        else:
            return "Error fetching data"

# async def ticker(instrument_name):
#         base_url = 'https://www.deribit.com/api/v2/public/'
#         order_endpoint = 'ticker'
#         params = {'instrument_name': instrument_name}
#         url = f'{base_url}{order_endpoint}'
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, params=params) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     return data
#                 else:
#                     print("Error fetching data")
#                     return None
# start = datetime.now()
# data = asyncio.run(ticker('BTC-PERPETUAL'))
# best_ask_price = data['result']['best_ask_price']
# best_bid_price = data['result']['best_bid_price']
# index_price = data['result']['index_price']
# instrument_name = data['result']['instrument_name']
# timestamp = data['result']['timestamp']
# print(f"Instrument Name: {instrument_name}\nIndex price: {index_price}\nAsk price: {best_ask_price} \
#         \nBid Price: {best_bid_price}\nTimestamp: {timestamp}")

# end = datetime.now()
# print(end - start)

# request_type = {'get_order_book': get_order_book, 
#                 'ticker': ticker}
# for request_name,request in request_type.items():
#     print(request_name)
#     data = request('BTC-PERPETUAL').json()
#     best_ask_price = data['result']['best_ask_price']
#     best_bid_price = data['result']['best_bid_price']
#     index_price = data['result']['index_price']
#     instrument_name = data['result']['instrument_name']
#     timestamp = data['result']['timestamp']
#     print(f"Instrument Name: {instrument_name}\nIndex price: {index_price}\nAsk price: {best_ask_price} \
#           \nBid Price: {best_bid_price}\nTimestamp: {timestamp}")

# index_names = get_index_price_names().json()['result']

# for index_name in index_names:
#     print(f'{index_name}: {get_index_price(index_name).json()['result']['index_price']}')

# pprint(ticker('BTC-PERPETUAL').json())
# print([currency['currency'] for currency in get_currencies().json()['result']])
async def main():
    start = datetime.now()
    # trade = DebritTrade()
    # trades = [
    #     trade.get_currencies(),
    #     trade.get_time(),
    #     trade.get_index_price_names(),
    #     trade.get_index_price('usd_usdt'),
    #     trade.get_order_book('BTC-PERPETUAL'),
    #     trade.ticker('BTC-PERPETUAL')
    # ]
    # ut = await asyncio.gather(*trades)
# ut = trunc(obj.get_time().json()['result']/1000)
    obj = DebritTrade()
    ut = await asyncio.gather(obj.auth())
    print(ut)
    end = datetime.now()
    print(f'Time Taken: {end - start}')
# time.sleep(10)
# dt = datetime.now()
# dt = trunc(datetime.timestamp(dt))
# print(f"Diff: {abs(ut-dt)}")

if __name__ == '__main__':
    asyncio.run(main())
