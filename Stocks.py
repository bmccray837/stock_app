import yfinance as yf


while True:
    try:
        num_stocks = int(input("Enter number of stocks you would like to research: "))
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

ten_fav = []
i = 0
while i < num_stocks:
    try:
        stock_pick = str(input("Please enter your stock selection: "))
        ten_fav.append(stock_pick)
        i += 1
    except ValueError:
        print("Please input a valid stock ticker.")

for stock in ten_fav:
    try:
        stock_data = yf.Ticker(stock).info
        stock_price = stock_data['regularMarketPrice']
        print("{stock} is currently trading at ${price}".format(stock = stock, price = stock_price))
    except KeyError:
        continue

# for stock in russell3000:
#     stock_data = yf.Ticker(stock).info
#     if stock_data['sector'] == "Financial Services" or stock_data['sector'] == "Utilities":
#         continue
#     else:


