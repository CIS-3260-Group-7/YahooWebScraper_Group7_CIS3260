'''
numpy: makes array operations simple and fast

pandas: helps convert the data in a tabular structure, and can 
        manipulate the data with numerous functions that have been
        efficiently developed

urllib3: HTTP client for Python

certifi: provides Mozilla’s carefully curated collection of 
        Root Certificates for validating the trustworthiness clear
        
        of SSL certificates while verifying the identity of 
        TLS hosts.

BeautifulSoup: This library helps to get the HTML structure 
                of the page that is to be manipulated. 

'''
import numpy as np
import pandas as pd
import urllib3
import certifi

from bs4 import BeautifulSoup

# Ask user for the stock ticker of interest
stock_ticker = input('Enter stock ticker: ')

# Concatenate the url with the stock ticker and apply upper() to automatically uppercase user input
link = 'https://finance.yahoo.com/quote/'+ stock_ticker.upper() + '/history?p=' + stock_ticker.upper()

# Create getHTMLContent function to grab HTML content from the link
def getHTMLContent(link):
    http = urllib3.PoolManager(ca_certs=certifi.where())
    resp = http.request('GET', link)
    soup = BeautifulSoup(resp.data.decode('utf-8'), 'html.parser')
    return soup

'''
Save HTML response in content variable

Use BeautifulSoup's built in find_all() function to target all table HTML tags and iterate through
all the tables on the page and print HTML structure.
'''
content = getHTMLContent(link)
tables = content.find_all('table')
for table in tables:
    print(table.prettify())