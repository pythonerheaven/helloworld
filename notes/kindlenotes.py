#!/usr/bin/python
#coding:utf-8

import bs4
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class KindleNotes(object):
    def __init__(self,uri):
        self.uri = uri
        self.uriMd = uri.replace('.html','.md')
        self.notes = []

    def readNotes(self):
        content = self.readFile()
        soup = bs4.BeautifulSoup(content, 'html5lib')
        applyFor = self.parseSingleNode(soup,'.notebookFor')
        title = self.parseSingleNode(soup,'.bookTitle')
        authors = self.parseSingleNode(soup,'.authors')
        self.notes.append('# 简介')
        self.notes.append( applyFor + '\n' + title + '\n' + 'authors:' + authors + '\n')

        notes = soup.select('div')
        for e in notes:
            if e.attrs['class'][0] == u'sectionHeading':
                self.notes.append('## ' + e.getText() + '\n')
            elif e.attrs['class'][0] == u'noteHeading':
                line = e.getText()
                line = line.replace(u'标注 (黄色) - ',u' ')
                line = line.replace(u'备注 - ', u' ')
                line = u'### ' + line + '\n'
                self.notes.append(line)
            elif e.attrs['class'][0] == u'noteText':
                self.notes.append(e.getText() + '\n')


    def readFile(self):
        file = open(self.uri,'r')
        content = file.read()
        file.close()
        return content

    def writeFile(self):
        if os._exists(self.uriMd):
            os.remove(self.uriMd)
        file = open(self.uriMd, 'w')
        for line in self.notes:
            file.write(line)
        file.close()

    def parseSingleNode(self, soup,style):
        elems = soup.select(style)
        return elems[0].getText()


if __name__ == '__main__':
    pdf = KindleNotes("/Users/hujiabao/books/technical/notebooks/精进：如何成为一个很厉害的人（知乎604939个赞同认证的惊喜之作！豆瓣9.4分高分推荐！）-笔记本.html")
    pdf.readNotes()
    pdf.writeFile()
    print('done')


