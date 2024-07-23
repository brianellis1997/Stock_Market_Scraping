import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def real_time_price(stock_code):
    url = ('https://finance.yahoo.com/quote/') + stock_code
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', class_='container yf-mgkamr')
    web_content = web_content.find('span').text

    if web_content == []: # if it's empty, assign default value
        web_content = '99999'

    return web_content

companies = ['TSLA', 'NFLX', 'AMZN', 'META']

for step in range(1, 101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in companies:
        price.append(real_time_price(stock_code))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real time stock data.csv', mode='a', header = False)
    print(col)
    