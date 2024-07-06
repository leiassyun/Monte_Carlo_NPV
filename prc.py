
from yahoo_fin import stock_info as si
import yfinance as yf
from yahoo_fin.stock_info import get_cash_flow
import requests
import requests_html

ticker = yf.Ticker("SE")
print(ticker.get_cash_flow())
