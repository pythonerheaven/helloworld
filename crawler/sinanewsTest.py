from sinanews import Sinanews
from mongodbutil import Mongodbutil
import time
import random
import re
import requests

sinanews = Sinanews()
mongodbutil = Mongodbutil('10.173.32.123',27017,'sinanews')

url = 'http://biz.finance.sina.com.cn/usstock/usstock_news.php?symbol=NTES'
sinanews.get_page(url)
items = sinanews.get_item_array()
mongodbutil.insertItems(items)

time.sleep(2*random.random())
