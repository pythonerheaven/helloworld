import requests
import bs4
import sys


class Sinanews(object):
    def __init__(self):
        self.itemArray = []

    def get_page(self,code,url):
        self.itemArray = []
        res = requests.get(url)
        res.encoding = "gbk"
        res.raise_for_status()
        if res.status_code == 200 :
            contentSoup = bs4.BeautifulSoup(res.text,'lxml')
            elems = contentSoup.select('.xb_list > li')
            for elem in elems:
                json = {}
                json['code'] = code
                ele = elem.select('.xb_list_r')
                json['date'] = ele[0].getText().split('|')[1]
                s = json['date']
                print(s)
                ele = elem.select('a')
                json['title'] = ele[len(ele)-1].getText()
                print(json['title'])
                json['href'] = ele[len(ele)-1].attrs['href']
                ret,content = self.get_content(json['href'])
                if ret == 0 :
                    json['content'] = content
                    self.itemArray.append(json)


    def get_content(self,url):
        content = ''
        ret = 1
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        res = requests.get(url,headers=header)
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