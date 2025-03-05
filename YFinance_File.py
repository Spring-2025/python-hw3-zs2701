#GetReturns
import yfinance as yf
import pandas as pd

def YahooData2returns(symbol='GS'):
  data=yf.download(symbol,auto_adjust=0)
  prices=data['Adj Close'].values
  returns=get_returns(prices)

  return returns

def get_returns(pricevec):
  n=len(pricevec)
  ratiovec=pricevec[1:n]/pricevec[:n-1]
  returns=ratiovec-1
  return returns

returns_GS=YahooData2returns('GS')

returns_df=pd.DataFrame(returns_GS,columns=["Daily Return"])
print(returns_df.head())
