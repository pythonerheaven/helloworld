from sinanews import Sinanews
from mongodbutil import Mongodbutil
import time
import random
import re
import requests
import pandas as pd
import datetime

sinanews = Sinanews()
mongodbutil = Mongodbutil('10.173.32.123',27017,'sinanews')

MARKET = ['US','HK','SZ','SH']

def read_file(market):
    data = pd.read_csv("../src/futuqant/examples/all_stocks/ALL_" + market + ".txt", sep=' ', names=['code'])
    return data

def generate_url(market,code):
    if market == 'US' :
        return 'http://stock.finance.sina.com.cn/usstock/quotes/' + code + '.html'
    if market == 'HK' :
        return 'http://stock.finance.sina.com.cn/hkstock/quotes/' + code + '.html'
    if market == 'SH' :
        return 'http://finance.sina.com.cn/realstock/company/' + str.lower(market) + code + '/nc.shtml'
    if market == 'SZ' :
        return 'http://finance.sina.com.cn/realstock/company/' + str.lower(market) + code + '/nc.shtml'
    else :
        return "url not found"

print('Starting time: {}'.format(datetime.datetime.now()))

for market in MARKET:
    data = read_file(market)
    for indexs in data.index:
        code = data.loc[indexs].values[0][3:]
        url = generate_url(market,code)
        print('Current Time:{}, code:{}, url:{}'.format(datetime.datetime.now(),code,url))

        try:
            sinanews.get_page(code,url)
            items = sinanews.get_item_array()
            mongodbutil.insertItems(items)

            time.sleep(4*random.random())
        except Exception as err:
            time.sleep(4 * random.random())
            print(err)

print('Ending time: {}'.format(datetime.datetime.now()))
#sinanews.get_content('http://www.capitalcube.com/blog/index.php/etfs-with-exposure-to-agilent-technologies-inc-december-26-2017/?yptr=yahoo')