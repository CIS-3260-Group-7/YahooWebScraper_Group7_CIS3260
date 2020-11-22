'''
pandas: helps convert the data in a tabular structure, and can 
        manipulate the data with numerous functions that have been
        efficiently developed
'''
import pandas as pd

# Ask user for the stock ticker of interest
stock_ticker = input('Enter stock ticker: ')

# Concatenate the url with the stock ticker and apply upper() to automatically uppercase user input
link = 'https://finance.yahoo.com/quote/'+ stock_ticker.upper() + '/history?p=' + stock_ticker.upper()
print(link)

# use pandas read_html() function to read HTL tables into a list of DataFrames objects
df_list = pd.read_html(link)[0].head()

print(df_list)