"""
Zhilin Zhou
Class: CS677 - SUMMER
Date: 06/06/2022
Homework Problem # Preliminary task2
Description of problem:
1.to download daily stock data (5-years from Jan 1, 2014 to Dec 31, 2019) for your ticker as a CSV file
2.computes additional fields for time (week, day, month) and prices (daily returns, 14- and 50-day moving price averages).
"""
# Preliminary Task 2

# run this  !pip install pandas_datareader
# in line 24 may need to use day_name not weekday_name

import pip
pip.main(['install', 'pandas_datareader'])

# run this  !pip install pandas_datareader
# in line 24 may need to use day_name not weekday_name
from pandas_datareader import data as web
import os
import pandas as pd

def get_stock(ticker, start_date, end_date, s_window, l_window):
    try:
        df = web.get_data_yahoo(ticker, start=start_date, end=end_date)
        df['Return'] = df['Adj Close'].pct_change()
        df['Return'].fillna(0, inplace = True)
        df['Date'] = df.index
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['Day'] = df['Date'].dt.day
        for col in ['Open', 'High', 'Low', 'Close', 'Adj Close']:
            df[col] = df[col].round(2)
        df['Weekday'] = df['Date'].dt.strftime('%A')
        df['Week_Number'] = df['Date'].dt.strftime('%U')
        df['Year_Week'] = df['Date'].dt.strftime('%Y-%U')
        df['Short_MA'] = df['Adj Close'].rolling(window=s_window, min_periods=1).mean()
        df['Long_MA'] = df['Adj Close'].rolling(window=l_window, min_periods=1).mean()
        col_list = ['Date', 'Year', 'Month', 'Day', 'Weekday',
                    'Week_Number', 'Year_Week', 'Open',
                    'High', 'Low', 'Close', 'Volume', 'Adj Close',
                    'Return', 'Short_MA', 'Long_MA']
        num_lines = len(df)
        df = df[col_list]
        print('read ', num_lines, ' lines of data for ticker: ' , ticker)
        return df
    except Exception as error:
        print(error)
        return None

try:
    ticker='ZIONL'
    input_dir = r'/Users/jolenezhou/PycharmProjects/cs677——A2'
    output_file = os.path.join(input_dir, ticker + '.csv')
    df = get_stock(ticker, start_date='2015-01-01', end_date='2019-12-31',
               s_window=14, l_window=50)
    df.to_csv(output_file, index=False)
    print('wrote ' + str(len(df)) + ' lines to file: ' + output_file)
except Exception as e:
    print(e)
    print('failed to get Yahoo stock data for ticker: ', ticker)

