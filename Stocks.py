import yfinance as yf

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
        print("{stock} is currently trading at ${price} and has an earnings yield of {r}%.".format(stock = stock, price = stock_price, r = round(earnings_yield, 2)))
    except KeyError:
        continue

for stock, ey in ey_rank.items():
    

# for stock in russell3000:
#     stock_data = yf.Ticker(stock).info
#     if stock_data['sector'] == "Financial Services" or stock_data['sector'] == "Utilities":
#         continue
#     else:


