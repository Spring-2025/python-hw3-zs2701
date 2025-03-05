import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(data_or_symbol):
    """
    Convert Yahoo Finance stock data or a provided DataFrame to lagged returns.
    
    Parameters:
        data_or_symbol (str or DataFrame): Stock ticker symbol (e.g., 'GS') or a DataFrame containing stock data.
    
    Returns:
        numpy array: Lagged daily returns.
    """
    # 1. 判断输入类型
    if isinstance(data_or_symbol, str):  # 如果输入是股票代码，先下载数据
        data = yf.download(data_or_symbol, progress=False)
    else:  # 如果输入是 DataFrame，直接使用
        data = data_or_symbol

    # 2. 提取 'Adj Close' 列
    prices = data['Adj Close'].values

    # 3. 计算收益率
    returns = get_returns(prices)

    return returns

def get_returns(pricevec):
    """
    Compute daily returns from price data.
    
    Parameters:
        pricevec (numpy array): Array of stock prices.
    
    Returns:
        numpy array: Daily returns.
    """
    # 计算收益率 (price_t / price_t-1) - 1
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns
