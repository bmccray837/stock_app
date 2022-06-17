import yfinance as yf
import operator
from collections import Counter

stock_picks = []
stock_ranking = {}
ey_rank = {}
roe_rank = {}

while True:
    try:
        num_stocks = int(input("Please enter # of stocks to analyze: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue


i = 0
while i < num_stocks:
    try:
        stock_pick = str(input("Please enter stock selection: "))
        stock_picks.append(stock_pick)
        i += 1
    except ValueError:
        print("Please input a valid stock ticker.")

for stock in stock_picks:
    try:
        stock_data = yf.Ticker(stock).info
        stock_price = stock_data['regularMarketPrice']
        earnings_yield = stock_data['operatingMargins'] * stock_data['totalRevenue'] / stock_data['enterpriseValue'] * 100
        roe = stock_data['returnOnEquity']
        ey_rank[stock] = round(earnings_yield, 2)
        roe_rank[stock] = round(roe * 100, 2)
        print("{stock} is currently trading at ${price} with an earnings yield of {r}\"%\" and ROE of {s}%.".format(stock = stock, price = round(stock_price, 2), r = round(earnings_yield, 2), s = round(roe, 2)))
    except KeyError:
        continue

sorted_ey = {stock: ey for stock, ey in sorted(ey_rank.items(), key=lambda item: item[1], reverse=True)}

i = 1
for key, val in sorted_ey.items():
    sorted_ey[key] = i
    i += 1

sorted_roe = {k: v for k, v in sorted(roe_rank.items(), key=lambda item: item[1], reverse=True )}

v = 1
for key, val in sorted_roe.items():
    sorted_roe[key] = v
    v += 1

total_rank = dict(Counter(sorted_ey)+Counter(sorted_roe))
sorted_tr = {k: v for k, v in sorted(total_rank.items(), key=lambda item: item[1], reverse=False)}
# print(sorted_tr)

print("Your top ranked stocks based on ROE and Earnings Yield metrics are:")
i = 1
for k in sorted_tr.keys():
    print(i, "-", k)
    i += 1



