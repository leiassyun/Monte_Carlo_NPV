import yfinance as yf

import requests
import requests_html
import pandas as pd
import numpy

def fetch_data(ticker):
    try:
        company = yf.Ticker(ticker)
        return company
    except Exception as e:
        print(f"Error fetching company data for {ticker}: {e}")
        return None

def fetch_cashflow(ticker):
    company = fetch_data(ticker)
    data = company.get_cash_flow()
    cashflows = data.loc['FreeCashFlow'].values
    return cashflows[:4]
    
def fetch_capm(ticker):
    company = fetch_data(ticker)
    if company is None:
        return None

    try:
        risk_free_rate = [3.90, 3.84, 1.49, 0.93] # 2023-12-31, 2022-12-31, 2021-12-31, 2020-12-31
        beta = company.info.get("beta", 1)  # Default beta to 1 if not available
        market_return =  [24.23, -19.44, 26.89, 16.26] #2023, 2022, 2021, 2020 | historical average of S&P 500
    
        print(f"Beta value is: {beta}")
        
        if beta is None:
            print(f"Could not fetch beta for {ticker}")
            return None

        capm = calculate_capm(risk_free_rate, beta, market_return)

        return capm
    except Exception as e:
        print(f"Error fetching CAPM for {ticker}: {e}")
        return None
    
def calculate_capm(risk_free_rate, beta, market_return):
    expected_return = []
    for i in range(len(risk_free_rate)):
        yearly_expected = risk_free_rate[i] + beta * (market_return[i] - risk_free_rate[i])  
        expected_return.append(yearly_expected) 
    return expected_return

