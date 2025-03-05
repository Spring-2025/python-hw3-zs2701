#GetReturns
import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(symbol='GS'):
  data=yf.download(symbol,auto_adjust=0)
  prices=data['Adj Close'].values
  return prices

prices = YahooData2returns('GS')
print(type(prices))
pricevec = prices

def get_returns(pricevec):
  n=len(pricevec)
  ratiovec=pricevec[1:n]/pricevec[:n-1]
  returns=ratiovec-1
  return returns

returns=get_returns(pricevec)
print(returns)
