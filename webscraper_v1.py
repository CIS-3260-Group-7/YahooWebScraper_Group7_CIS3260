'''
LIBRARIES: 

BeautifulSoup: This library helps to get the HTML structure 
                of the page that is to be manipulated. 

Requests: This library allows you to send HTTP request
'''

# First we have to let python know that which libraries to use
# Good practice to structure the file where all of your imports are on top
from bs4 import BeautifulSoup
import requests

# Ask user for the stock ticker of interest
stock_ticker = input('Enter stock ticker: ')

# Concatenate the url with the stock ticker and apply upper() to automatically uppercase user input
url = 'https://finance.yahoo.com/quote/'+ stock_ticker.upper() + '/history?p=' + stock_ticker.upper()

print(url)

# Store the response from the request sent to the website server
response = requests.get(url, timeout = 5)

# Store formatted HTML Content Tree 
content = BeautifulSoup(response.content, "html.parser")

# print (content.prettify())
print (content.find('table', attrs={"data-test": "historical-prices"}).text.encode('utf-8'))