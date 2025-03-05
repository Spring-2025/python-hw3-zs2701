import yfinance as yf
import pandas as pd
import numpy as np  # 确保 NumPy 导入

def YahooData2returns(data):
    """
    兼容老师的测试代码：
    - 如果 `data` 是字符串（股票代码），则从 Yahoo Finance 下载数据。
    - 如果 `data` 是 DataFrame，则直接使用它（用于测试）。
    """
    if isinstance(data, str):
        data = yf.download(data, auto_adjust=0)  # 仅当传入的是股票代码时才下载数据

    # 确保数据包含 'Adj Close' 列
    if 'Adj Close' not in data:
        raise ValueError("Input data must contain 'Adj Close' column")

    # 获取调整收盘价
    prices = data['Adj Close'].values

    # 计算收益率
    returns = get_returns(prices)
    return returns

def get_returns(pricevec):
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1
    return returns
