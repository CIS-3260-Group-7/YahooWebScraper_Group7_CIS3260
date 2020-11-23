'''
LIBRARIES: 

urllib3: HTTP client for Python, and is used to send requests and retrieve their response.

certifi: provides Mozilla’s carefully curated collection of 
        Root Certificates for validating the trustworthiness clear
        of SSL certificates while verifying the identity of 
        TLS hosts.

BeautifulSoup: This library helps to get the HTML structure 
                of the page that is to be manipulated. 

'''
import urllib3
import certifi

from bs4 import BeautifulSoup

# Ask user for the stock ticker of interest
stock_ticker = input('Enter stock ticker: ')

# Concatenate the url with the stock ticker and apply upper() to automatically uppercase user input
link = 'https://finance.yahoo.com/quote/'+ stock_ticker.upper() + '/history?p=' + stock_ticker.upper()
print(link)

# Create getHTMLContent function to grab HTML content from the link
def getHTMLContent(link):
    http = urllib3.PoolManager(ca_certs=certifi.where())
    resp = http.request('GET', link, timeout = 5)
    soup = BeautifulSoup(resp.data.decode('utf-8'), 'html.parser')
    return soup

'''
Save HTML response in content variable

Use BeautifulSoup's built in find_all() function to target all table HTML tags and iterate through
all the tables on the page and print HTML structure.
'''
content = getHTMLContent(link)
tables = content.find_all('table')

'''
The <table> tag acts as the parent container, which is stored in the tables variable.

Below, we are traversing the table we retrieved from the HTML Content Tree and retrieving 
the tables headers (th), the tables rows (tr), and the tables data (td)
'''
for table in tables:
    # Use BeautifulSoups find_all() to get all the <th>(Table Headers) from the searching tree
    table_headers = table.find_all('th')  
    print("Table Headers: ")
    for title in table_headers:
        if len(table_headers) > 1:
            headers = title.find('span').get_text()
            print(headers)

    
    # Use BeautifulSoups find_all() to get all the <tr>(Table Rows) from the searching tree
    rows = table.find_all('tr')
    print("Table Row Data: ")
    # Traverse rows and use BeautifulSoups find_all() to get all the <td>(Table Data) from the searching tree
    for row in rows:
            table_data = row.find_all('td')
            if len(table_data) > 1:
                trade_date = table_data[0].find('span').get_text()
                # open_ = table_data[1].find('span').get_text()
                # high = table_data[2].find('span').get_text()
                # low = table_data[3].find('span').get_text()
                # close = table_data[4].find('span').get_text()
                # adj_close = table_data[5].find('span').get_text()
                # volume = table_data[6].find('span').get_text()

                '''Remember to change the variable to retrieve the 
                correct column of table_data'''

                print(trade_date)
