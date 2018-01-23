import requests
import bs4
import sys
import random
import time
from eth_bloom import BloomFilter

class Sinanews(object):
    def __init__(self):
        self.itemArray = []
        originalBloom = self.readBloomValueFromFile()
        if originalBloom == '' :
            self.b = BloomFilter()
        else:
            self.b = BloomFilter(int.from_bytes(originalBloom,byteorder='big'))
        self.urlExist = False

    def get_page(self,code,url):
        self.itemArray = []
        res = requests.get(url,timeout=10)
        res.encoding = "gbk"
        res.raise_for_status()
        if res.status_code == 200 :
            contentSoup = bs4.BeautifulSoup(res.text,'lxml')
            elems = contentSoup.select('#js_ggzx > li,.li_point > ul > li,.col02_22 > ul > li')
            for elem in elems:
                json = {}
                json['code'] = code
                ele = elem.select('span')
                json['date'] = ele[0].getText()[1:-1]
                s = json['date']
                ele = elem.select('a')
                json['title'] = ele[len(ele)-1].getText()
                print("date:{},title:{}".format(s,json['title']))
                json['href'] = ele[len(ele)-1].attrs['href']
                ret,content = self.get_content(json['href'])
                time.sleep(4 * random.random())
                if ret == 0 :
                    json['content'] = content
                    self.itemArray.append(json)


    def get_content(self,url):
        content = ''
        ret = 1

        self.urlExist = bytes(url.encode('utf-8')) in self.b
        if self.urlExist:
            print('This url:{} has existed'.format(url))
            return ret, content
        else:
            self.b.add(bytes(url.encode('utf-8')))

        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        res = requests.get(url,headers=header,timeout=10)
        res.encoding = "utf-8"
        try:
            res.raise_for_status()
        except Exception as err:
            print(err)

        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text,'lxml')
            elems = soup.select('#artibody,.entry-content')
            if len(elems) > 0 :
                content = elems[0].getText()
                ret = 0
        return ret, content


    def get_item_array(self):
        return self.itemArray

    def writeToFile(self,content):
        file = open('/Users/hujiabao/Downloads/text.html', 'a')
        file.write(content)
        file.close()

    def readFile(self):
        file = open('/Users/hujiabao/Downloads/test2.html')
        content = file.read()
        print(content)
        file.close()

    def writeBloomValueToFile(self):
        file = open('./bloom.txt','wb')
        file.write(bytes(bin(self.b).encode('utf-8')))
        file.close()

    def readBloomValueFromFile(self):
        file = None
        content = ''
        try:
            file = open('./bloom.txt','rb')
            content = file.read()
            print(content)
            file.close()
        except Exception as err:
            print(err)

        return content