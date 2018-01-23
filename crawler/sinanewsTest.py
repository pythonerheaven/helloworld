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
    sinanews.writeBloomValueToFile()

print('Ending time: {}'.format(datetime.datetime.now()))
#sinanews.get_content('http://www.capitalcube.com/blog/index.php/etfs-with-exposure-to-agilent-technologies-inc-december-26-2017/?yptr=yahoo')



#
# print(b'a value' in b)
#
# b.add(b'a value')
# print(b'a value' in b)
# print(int(b))
# print(len(bin(b)))
#
# c = BloomFilter(3458628712844765018311492773359360516229024449585949240367644166080576879632652362184119765613545163153674691520749911733485693171622325900647078772681584616740134230153806267998022370194756399579977294154062696916779055028045657302214591620589415314367270329881298073237757853875497241510733954508399863880080986777555986663988492288946856978031023631618215522505971170427986911575695114157059398791122395379400594948096)
# print(b'b value'  in b)
