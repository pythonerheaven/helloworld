#!/usr/bin/python
#coding:utf-8

import bs4
import os
import sys

#python 2.7
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
    #pdf = KindleNotes("/Users/hujiabao/books/technical/notebooks/精进：如何成为一个很厉害的人（知乎604939个赞同认证的惊喜之作！豆瓣9.4分高分推荐！）-笔记本.html")
    #pdf = KindleNotes("/Users/hujiabao/books/technical/notebooks/中产阶级如何保护自己的财富（ 知名房地产投资者“水库论坛”版主“欧神”欧成效首部力作。思想自由、财务自由的标配读物。）-Notebook.html")
    #pdf = KindleNotes(
    #    "/Users/hujiabao/books/technical/notebooks/打造高效团队 (蓝狮子经理人)-Notebook.html")
    # pdf = KindleNotes(
    #        "/Users/hujiabao/books/technical/notebooks/自控力-Notebook.html")
    # pdf = KindleNotes(
    #        "/Users/hujiabao/books/technical/notebooks/习惯的力量（新版）-Notebook.html")
    # pdf = KindleNotes(
    #    "/Users/hujiabao/books/technical/notebooks/高效阅读-Notebook.html")

    # pdf = KindleNotes(
    #    "/Users/hujiabao/books/technical/notebooks/高效的秘密-Notebook.html")

    #pdf = KindleNotes(
    #    "/Users/hujiabao/books/technical/notebooks/深度工作（麻省理工博士教你保持专注的深度工作法，让你的忙碌真正转化为生产能力！）-Notebook.html")

    #pdf = KindleNotes(
    #    "/Users/hujiabao/books/technical/notebooks/极简思考：来自世界顶尖咨询公司的高效工作法-Notebook.html")

    #pdf = KindleNotes(
    #     "/Users/hujiabao/workspace_python/books/technical/notebooks/当机立断（教你如何通过数字、事实、逻辑快速做决定，完成工作任务，推动事业发展！）-Notebook.html")

    pdf = KindleNotes(
         "/Users/hujiabao/workspace_python/books/technical/notebooks/如何系统思考-笔记本.html")


    pdf.readNotes()
    pdf.writeFile()
    print('done')


