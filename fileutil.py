import os
import sys
import shelve
import zipfile
import re
import traceback
import logging
from storewords import StoreWords


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://163.com')


a = os.path.join('/Users/hujiabao/books/english/en/','words')
print a

print os.getcwd()

file = open('/Users/hujiabao/books/english/en/words/postgraduated2.md')
fileContent = file.read();
# print fileContent
file.close();

shelveFile = shelve.open("mydata")
cats = ['a','b']
shelveFile['cats'] = cats
shelveFile.close()

shelveFile = shelve.open('mydata')
fileContent = shelveFile['cats']
# print fileContent
shelveFile.close()

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
# DEBUG/INFO/WARNING/ERROR/CRITICAL
# basicConfig, provided the filename , save the log to file

for folderName, subfolders, filenames in os.walk('/Users/hujiabao/books/english/en/words/'):
    print('The current folder is  ' + folderName)
    for subfolder in subfolders:
        print ('Subfolder of  ' + folderName + ': ' + subfolder)
    for filename  in filenames:
        print('File inside ' + folderName + ': ' + filename)
        file = open(folderName + filename)
        fileContent = file.read()
        logging.info(fileContent)
        lines = fileContent.split('\n')
        logging.info(lines)
        for line in lines:
            logging.debug(line)
            line.strip()
            line.strip('\'')
            line.strip('\"')
        file.close()

# try:
#     raise Exception('Symbol must be a single character string.')
# except Exception as err:
#     print('An exception happend:  ' + str(err) )
#     print traceback.format_exc()

assert( '1' == '2','aa' )
# sys.exit(1)

storeWords = StoreWords('/Users/hujiabao/books/english/en/words/')
print storeWords.folderPath
