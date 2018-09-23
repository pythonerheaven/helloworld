import os
import sys
import shelve
import logging
import time

my_root = '/Users/hujiabao/workspace_bim'
for root, dirs, files in os.walk(my_root,True):
    for dir in dirs:
        path = os.path.join(root, dir)
        print(path)
        for root2,dirs2,files2 in os.walk(path,True):
            if '.git' in dirs2:
                os.chdir(path)
                print(os.getcwd())
                os.system('git checkout release')
                os.system('git pull')
                break
    break

