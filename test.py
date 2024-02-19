"""
Zhilin Zhou
Class: CS677 - SUMMER
Date: 05/27/2022
Homework Problem #
Description of problem:


"""
# Q1-1: read files into a pandas frame and add a column ”True Label”
import pandas as pd

my_stock = pd.read_csv('ZIONL.csv')
SPY = pd.read_csv('SPY.csv')
print(my_stock)
print(SPY)


def add_column(file_name):
    True_label = []
    for row in file_name['Return']:
        if row < 0:
            True_label.append('-')
        else:
            True_label.append('+')
    file_name['True_label'] = True_label
    print(file_name)


add_column(my_stock)
add_column(SPY)

# Q1-2: The default probability that the next day with trend 'up'
# For my_data ZIONL.CSV
print("Quetion 1-2")
ZIONL_training = my_stock[(my_stock['Year'] >= 2015) & (my_stock['Year'] <= 2017)]
SPY_training = SPY[(SPY['Year'] >= 2015) & (SPY['Year'] <= 2017)]

# print(my_stock_training)
# print(SPY_training)

# the ratio of ZIONL 'UP' Stock
ratio1 = len(ZIONL_training.loc[ZIONL_training.True_label == '+']) / len(ZIONL_training)
# the ratio of SPY 'UP' Stocks
ratio2 = len(SPY_training.loc[SPY_training.True_label == '+']) / len(SPY_training)

print(f'For ZIONL stock, the default probability that the next day is a "up" day is {ratio1:.2f}.\n'
      f'For SPY stock, the default probability that the next day is a "up" day is {ratio2:.2f}.')
