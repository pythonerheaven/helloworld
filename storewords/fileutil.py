import os
import sys
import shelve
import zipfile
import re
import traceback
import logging
from storewords import StoreWords
import time


from selenium import webdriver
browser = webdriver.Firefox(executable_path='/Applications/geckodriver')
browser.get('http://account.youdao.com/login?service=dict&back_url=http://dict.youdao.com/wordbook/wordlist%3Fkeyfrom%3Dlogin_from_dict2.index')
editor = browser.find_element_by_id('username')
editor.send_keys('hujb2033@163.com')
password = browser.find_element_by_id('password')
#password.send_keys('storewords')
password.send_keys('baojinta')
login = browser.find_element_by_class_name('login_btn')
login.click()



def strLen(str):
    if str.strip() == '':
        return 0
    else:
        return len(str)

#

# a = os.path.join('/Users/hujiabao/books/english/en/','words')
# print(a)
#
# print(os.getcwd())

# file = open('/Users/hujiabao/books/english/en/words/英汉互译.md')
# fileContent = file.read();
# # print (fileContent)
# file.close();

shelveFile = shelve.open("mydata")
cats = ['a','b']
shelveFile['cats'] = cats
shelveFile.close()

shelveFile = shelve.open('mydata')
fileContent = shelveFile['cats']
# print (fileContent)
shelveFile.close()

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
# DEBUG/INFO/WARNING/ERROR/CRITICAL
# basicConfig, provided the filename , save the log to file


path = '/Users/hujiabao/PycharmProjects/books/english/en/words/store/'
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is  ' + folderName)

    for subfolder in subfolders:
        print ('Subfolder of  ' + folderName + ': ' + subfolder)
    for filename  in filenames:
        print('File inside ' + folderName + ': ' + filename)
        file = open(folderName + filename)
        fileContent = file.read()
        # logging.info(fileContent)
        lines = fileContent.split('\n')
        logging.info(lines)
        for line in lines:
            # logging.debug(line)
            line.strip()
            line.strip('\'')
            line.strip('\"')
            if len(line) == 0:
                continue

            if strLen(line) < 12:
                addword = browser.find_element_by_id('addword')
                time.sleep(0.4)
                addword.click()
                time.sleep(0.4)
                word = browser.find_element_by_css_selector('#word')
                time.sleep(0.4)
                logging.info(line)
                word.send_keys(line)
                submit = browser.find_element_by_css_selector('#editwordform  form')
                time.sleep(4)
                submit.submit()
                time.sleep(0.5)
        file.close()

# try:
#     raise Exception('Symbol must be a single character string.')
# except Exception as err:
#     print('An exception happend:  ' + str(err) )
#     print traceback.format_exc()

browser.close()

assert( '1' == '1','aa' )
sys.exit(1)


# storeWords = StoreWords('/Users/hujiabao/books/english/en/words/')
# print(storeWords.folderPath)
