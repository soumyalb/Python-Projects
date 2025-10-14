# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. 
# The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

# Question:
# What is the process to extract data from the wikipedia website using Beautiful Soup in Python? 
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth,
# Headquarters for the top US companies by Revenue?

import pandas as pd
import requests
from bs4 import BeautifulSoup

url= "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

response_data = requests.get(url,headers=headers).text

soup_data = BeautifulSoup(response_data,'html.parser')

tables=soup_data.find_all('table')
df = pd.read_html(str(tables[0]))[0]
print(df)