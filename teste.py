import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    return stock_info['regularMarketPrice']

print(get_stock_price('AAPL'))