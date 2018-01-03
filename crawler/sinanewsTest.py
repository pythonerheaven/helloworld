from sinanews import Sinanews
from mongodbutil import Mongodbutil
import time
import random
import re
import requests
import pandas as pd

sinanews = Sinanews()
mongodbutil = Mongodbutil('10.173.32.123',27017,'sinanews')

data = pd.read_csv("../src/futuqant/examples/all_stocks/ALL_US.txt", sep=' ', names=['code'])

for indexs in data.index:
    print(data.loc[indexs].values[0][3:])

    code = data.loc[indexs].values[0][3:]
    url = 'http://biz.finance.sina.com.cn/usstock/usstock_news.php?symbol=' + code
    print(url)

    try:
        sinanews.get_page(code,url)
        items = sinanews.get_item_array()
        mongodbutil.insertItems(items)

        time.sleep(2*random.random())
    except Exception as err:
        time.sleep(2 * random.random())
        print(err)


#sinanews.get_content('http://www.capitalcube.com/blog/index.php/etfs-with-exposure-to-agilent-technologies-inc-december-26-2017/?yptr=yahoo')