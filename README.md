# Yahoo! Finance Web Scraper - Group 7 - CIS 3260

**What is Web Scraping?**

> ***Definition:***
>
> Web scraping is a term for various methods user to collect information from across the Internet.



**How will we accomplish this?**

We will need to go through three stages: Fetching HTML, Obtaining HTML Tree, then Extracting information from the tree

1. We will then use the Request library to fetch the HTML code from this URL:

   ```https://finance.yahoo.com/quote/{Stock_Ticker}?p={Stock_Ticker}```

2. We  will use BeautifulSoup to Parse and Extract the HTML tree, and use Python to organize the data.



## Project Setup

**Setup Git On Computer**

[Connecting to GitHub with SSH](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh)

- This will enable a virtual handshake with your computer and this GitHub repository.

**Setup Python Environment and Python VirtualEnv**

[Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)

* This will walk you through installing and using Python packages, as well as explain what the function of pipenv is and how to setup 

***Using Python on Windows?***

[Get started using Python on Windows](https://docs.microsoft.com/en-us/windows/python/web-frameworks)



## Clone Project Repository

1. run ```git clone git@github.com:CIS-3260-Group-7/YahooWebScraper_Group7_CIS3260.git``` in your terminal

2. Change directory to the project folder ```YahooWebScraper_Group7_CIS3260```

3. run ```python3 -m venv .venv``` inside the project folder

4. run ```source .venv/bin/activate```

> run ```deactivate``` when you're finished with your virtual environment

5. run ```pip install -r requirements.txt```
6. run ```python3 webscraper.py``` and type ```tsla``` in terminal to test if it is working

