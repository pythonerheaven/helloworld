from crawler import Crawler
from mongodbutil import Mongodbutil
import time
import random


# https://finviz.com/screener.ashx?v=152&r=7101

crawler = Crawler('/Users/hujiabao/Downloads/fv.txt','##')
mongodbutil = Mongodbutil('10.173.32.123',27017,'fiv')
pos = 0
while pos < 7101:
    print(pos)
    url = 'http://finviz.com/screener.ashx?v=152&r='+str(pos)+'&c=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70'

    crawler.get_page(url)
    crawler.writeToFile()
    time.sleep(2*random.random())
    pos += 21
    jsonArray = crawler.toJsons()
    mongodbutil.insertItems(jsonArray)
