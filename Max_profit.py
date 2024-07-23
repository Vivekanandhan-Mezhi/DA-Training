# You are given an integer array prices where prices[i] is the price of a given
# stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. However, you can buy it then 
# immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def max_profit(stock_price):
    maximum_profit = 0
    # buy_price = 0
    # sell_price = 0
    for pos in range(0, len(stock_price)-1):
        if stock_price[pos] < stock_price[pos+1]:
            maximum_profit += (stock_price[pos+1] - stock_price[pos])
        # if stock_price[pos] > stock_price[pos+1]:
        #     if buy_price == 0:
        #         continue
        #     else:
        #         sell_price = stock_price[pos]
        #         maximum_profit += (sell_price - buy_price)
        #         buy_price = 0
        #         sell_price = 0
        # elif stock_price[pos] < stock_price[pos+1]:
        #     continue
        # else:
        #     if buy_price == 0:
        #         buy_price = stock_price[pos]
        #     else:
        #         continue
    return maximum_profit

prices = [7,6,4,3,1]
print(max_profit(prices))