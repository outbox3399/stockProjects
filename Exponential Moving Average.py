# 1 - Collect Data about Relative Strength Index (RSI) and Exponential Moving Average (EMA) 34, 89,200 Indicators
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# 2 - Store the data
file_read = pd.read_csv('F:/PythonStockProjects/stockProjects/Data/BTC-USD.csv')
# 3 - Set the date as the index
data_frame = file_read.set_index(pd.DatetimeIndex(file_read['Date'].values))


# 4 - Create functions to calculate Exponential Moving Average (EMA)
def EMA34(data, period=34, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()


def EMA89(data, period=89, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()


def EMA200(data, period=200, column='Close'):
    return data[column].ewm(span=period, adjust=False).mean()


# 5 - Create functions to calculate Relative Strength Index (RSI)
'''diff for calculating the nth discrete difference along the given axis. 
If 'x' is the input array, then the first difference is given by out[i]=x[i+1]-a[i]. 
We can calculate the higher difference by using diff recursively.'''

'''def RSI(data, period=14, column='close'):
    delta = data[column].diff(1)
    delta = delta[1:]  # Get rid of the first column
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    data['up'] = up
    data['down'] = down
    AVG_Gain = SMA(data, period, column='up')
    AVG_Loss = abs(SMA(data, period, column='up'))
    RS = AVG_Gain / AVG_Loss
    RSI = 100.0 - (100.0/(1.0 + RS))

    data['RSI'] = RSI
    return data'''

# 6 - Create or Add to the data set
data_frame['EMA_34'] = EMA34(data_frame)
data_frame['EMA_89'] = EMA89(data_frame)
data_frame['EMA_200'] = EMA200(data_frame)

# 7 - Show the data
print(data_frame)
