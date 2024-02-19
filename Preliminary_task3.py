"""
Zhilin Zhou
Class: CS677 - SUMMER
Date: 06/06/2022
Homework Problem # Preliminary task3
Description of problem:
1.to read your saved CSV file into a list of lines
"""
import os

ticker='ZIONL'
input_dir = r'/Users/jolenezhou/PycharmProjects/cs677——A2'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
