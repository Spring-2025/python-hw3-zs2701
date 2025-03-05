import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(symbol='GS'):
    """
    Downloads data from Yahoo Finance and computes daily returns.
    """
    data = yf.download(symbol, auto_adjust=0)
    prices = data['Adj Close'].values  # Extract adjusted close prices
    
    # Ensure there are enough data points
    if len(prices) < 2:
        raise ValueError("Not enough data to compute returns")

    # Compute returns
    returns = get_returns(prices)
    return returns  # Now returns daily returns instead of prices

def get_returns(pricevec):
    """
    Computes daily log returns.
    """
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1
    return returns

# Test with real Yahoo Finance data
returns = YahooData2returns('GS')
print(type(returns))  # Should be a NumPy array
print(returns[:5])  # Print the first 5 returns for verification
