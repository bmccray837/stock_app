import yfinance as yf
import operator

stock_picks = []
stock_ranking = {}
ey_rank = {}
roe_rank = {}

while True:
    try:
        num_stocks = int(input("Enter number of stocks you would like to research: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue


i = 0
while i < num_stocks:
    try:
        stock_pick = str(input("Please enter your stock selection: "))
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
        print("{stock} is currently trading at ${price} with an earnings yield of {r}% AND ROE of {s}%.".format(stock = stock, price = round(stock_price, 2), r = round(earnings_yield, 2), s = round(roe, 2)))
    except KeyError:
        continue

sorted_ey = {stock: ey for stock, ey in sorted(ey_rank.items(), key=lambda item: item[1])}
print(sorted_ey)



# for stock in russell3000:
#     stock_data = yf.Ticker(stock).info
#     if stock_data['sector'] == "Financial Services" or stock_data['sector'] == "Utilities":
#         continue
#     else:


