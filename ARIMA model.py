import warnings
warnings.filterwarnings('ignore')
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
import yfinance as yf

stocks = ["SPY"]

endDate = dt.date.today()
startDate = dt.date.today() - dt.timedelta(days=365)

def auto_arima_Model(train_data):
    model_autoARIMA = auto_arima(train_data, start_p=0, start_q=0,
                          test='adf',       # use adftest to find             optimal 'd'
                          max_p=5, max_q=5, # maximum p and q
                          m=1,              # frequency of series
                          d=None,           # let model determine 'd'
                          seasonal=True,   # No Seasonality
                          start_P=0,
                          D=0,
                          trace=True,
                          error_action='ignore',
                          suppress_warnings=True,
                          stepwise=True)
    print(model_autoARIMA)
    return model_autoARIMA

stockData = yf.download(stocks,startDate,endDate)['Close']
auto_arima_Model(stockData)
