import yfinance as yf

stock_data = yf.Ticker("AAPL").info

for key, val in stock_data.items():
    print(key, ":", val)

