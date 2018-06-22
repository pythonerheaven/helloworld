#!/usr/bin/python
#coding:utf-8

import bs4
import os
import sys

#python 2.7
#reload(sys)
#sys.setdefaultencoding('utf-8')

class GenerateReadme(object):
    def __init__(self,root):
        self.files = []
        self.root = root

    def get_files(self,root):
        for root, dirs, files in os.walk(root):
            print(root)  # 当前目录路径
            print(dirs)  # 当前路径下所有子目录
            print(files)  # 当前路径下所有非目录子文件

            gen_files =  []
            for file in files:
                if file.find('.ppt') > 0 :
                    gen_files.append(file)
            self.writeFile(root,gen_files)
            for dir in dirs:
                self.get_files(dir)



    def writeFile(self,root, gen_files):
        readme_file = root + "/readme.md"
        if os._exists(readme_file):
            os.remove(readme_file)
        file = open(readme_file, 'w')
        for f in gen_files:
            mid = root.replace(self.root,'')
            line = '* [{0}](../resources{1}/{2})\n'.format(f[0:f.find('.')],mid, f)
            file.write(line)
        file.close()



if __name__ == '__main__':
    '''
    每个目录下生成readme.md文件，内容如下：
    [PPT或PPTX后缀的文件名（不含后缀）](../resources/文件名)
    '''

    my_root = '/Users/hujiabao/Downloads/fangcloud/FangCloudV2/个人文件/考试资料/商务管理专业'
    gen_readme = GenerateReadme(my_root)

    gen_readme.get_files(my_root)

    print('done')


