import requests
import bs4
import sys


class Sinanews(object):
    def __init__(self):
        self.itemArray = []

    def get_page(self,url):
        self.itemArray = []
        res = requests.get(url)
        res.encoding = "gbk"
        res.raise_for_status()
        if res.status_code == 200 :
            contentSoup = bs4.BeautifulSoup(res.text,'lxml')
            elems = contentSoup.select('.xb_list > li')
            for elem in elems:
                json = {}
                ele = elem.select('.xb_list_r')
                json['date'] = ele[0].getText().split('|')[1]
                s = json['date']
                print(s)
                ele = elem.select('a')
                json['title'] = ele[len(ele)-1].getText()
                print(json['title'])
                json['href'] = ele[len(ele)-1].attrs['href']
                json['content'] = self.get_content(json['href'])
                self.itemArray.append(json)


    def get_content(self,url):
        content = ''
        res = requests.get(url)
        res.encoding = "utf-8"
        res.raise_for_status()
        if res.status_code == 200:
            soup = bs4.BeautifulSoup(res.text,'lxml')
            elems = soup.select('#artibody')
            if len(elems) > 0 :
                content = elems[0].getText()
        return content


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