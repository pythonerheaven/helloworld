import os
import sys
import time
import re

from selenium import webdriver


def get_chapters_and_sections(chapterId, path):
    browser = webdriver.Firefox(executable_path='/Applications/geckodriver')
    browser.get(path)
    print(path)
    introduce = browser.find_element_by_class_name('components__text--1Y4j2').text
    print(introduce)
    title = browser.find_element_by_class_name('course__container-header--3ttvp').text
    print(title)
    ul = browser.find_elements_by_class_name('components__list--2f4Db')
    text = ul[0].text
    lines = text.split('\n')
    arr = doLines(lines)
    for a in arr:
        if len(a) == 0:
            arr.remove([])
    print(arr)
    browser.close()
    generate_chapters(chapterId, title, arr)


DELEY = 3
DELEY5 = 5

def generate_chapters(chapterId, title, arr):
    browser = webdriver.Firefox(executable_path='/Applications/geckodriver')
    browser.get('http://edu.ai2boss.com/admin')
    editor = browser.find_element_by_id('login_username')
    editor.send_keys('ai2boss@163.com')
    editor = browser.find_element_by_id('login_password')
    editor.send_keys('ai2boss')
    login = browser.find_element_by_class_name('js-btn-login')
    login.click()
    time.sleep(DELEY5)
    try:
        close = browser.find_element_by_class_name('close')
        close.click()
    except:
        time.sleep(DELEY5)
        close = browser.find_element_by_class_name('close')
        close.click()

    browser.get('http://edu.ai2boss.com/admin/course_set/normal/index')
    sm = browser.find_element_by_class_name('btn-sm')
    sm.click()

    browser.get('http://edu.ai2boss.com/course_set/create')
    editor = browser.find_element_by_id('course_title')
    editor.send_keys(title)
    time.sleep(DELEY)

    coursesetCreate = browser.find_element_by_id('courseset-create-btn')
    coursesetCreate.click()
    time.sleep(DELEY)

    # 7.3.0->8.3.0没有了
    #     close = browser.find_element_by_class_name('es-icon-close01')
    #     close.click()
    #     time.sleep(5)

    try:
        ccb = browser.find_element_by_xpath("//a[@href=\'/course_set/%d/manage/course/%d/info\']" % (chapterId, chapterId))
        ccb.click()
        time.sleep(DELEY5)
    except:
        ccb = browser.find_element_by_xpath(
            "//a[@href=\'/course_set/%d/manage/course/%d/info\']" % (chapterId, chapterId))
        ccb.click()
        time.sleep(DELEY5)

    close = browser.find_element_by_class_name('introjs-skipbutton')
    close.click()
    time.sleep(DELEY)

    ccb = browser.find_element_by_xpath("//a[@href=\'/course_set/%d/manage/course/%d/tasks\']" % (chapterId, chapterId))
    ccb.click()
    time.sleep(DELEY)

    for chapters in arr:
        # gen_chapter

        # ccb = browser.find_element_by_xpath("//button[@data-toggle=\'dropdown\']")
        ccb = browser.find_element_by_xpath("//div[@data-toggle=\'cd-dropdown\']/button")
        ccb.click()
        time.sleep(DELEY)

        # ccb = browser.find_element_by_xpath("//a[@data-url=\'/course/%d/manage/chapter/create\']" % (chapterId))
        ccb = browser.find_element_by_xpath("//a[@data-url=\'/course/%d/manage/chapter/manage\']" % (chapterId))
        ccb.click()
        time.sleep(DELEY)
        editor = browser.find_element_by_id('chapter-title-field')
        editor.send_keys(chapters[0])
        time.sleep(DELEY)
        ccb = browser.find_element_by_id('course-chapter-btn')
        ccb.click()
        time.sleep(DELEY)
        for index in range(1, len(chapters)):
            # gen_section
            # ccb = browser.find_element_by_xpath("//button[@data-toggle=\'dropdown\']")
            ccb = browser.find_element_by_xpath("//div[@data-toggle=\'cd-dropdown\']/button")
            ccb.click()
            time.sleep(DELEY)
            ccb = browser.find_element_by_xpath(
                "//a[@data-url=\'/course/%d/manage/chapter/manage?type=unit\']" % (chapterId))
            ccb.click()
            editor = browser.find_element_by_id('chapter-title-field')
            editor.send_keys(chapters[index])
            time.sleep(DELEY)
            ccb = browser.find_element_by_id('course-chapter-btn')
            ccb.click()
            time.sleep(DELEY)
    browser.close()

def readChapterId(path):
    with open(path,'r') as fp:
        content = fp.read()
        lines = content.split('\n')
        return lines[1][57:-4]


def doLines(lines):
    arr = []
    if len(lines) <= 0:
        return

    curChapterIndex = 0
    for line in lines:
        ci = chapterIndex(line)
        curChapterIndex = ci if ci > 0 else curChapterIndex


        if line == '宣传片':
            if len(arr) <= 0:
                arr.append([])
            arr[curChapterIndex].append(line)
        elif line.find('已学') >= 0:
            continue
        elif isSectionIndex(line) == True:
            continue
        else:
            if len(arr) <= curChapterIndex:
                arr.append([])
            if ci > 0:
                continue
            else:
                arr[curChapterIndex].append(line)

    return arr

def chapterIndex(line):
    #不是chapter,返回0
    pattern = re.compile(r"第 \d+ 讲")
    result = pattern.findall(line)
    if len(result) > 0:
        pattern = re.compile(r"\d+")
        result = pattern.findall(line)
        if len(result) > 0:
            return int(result[0])
    return 0

def isSectionIndex(line):
    pattern = re.compile(r"\d+.\d+")
    result = pattern.findall(line)
    if len(result) > 0:
        return True
    else:
        return False

def main():
    root = 'file:///Users/hujiabao/Downloads/courses/'
    path = '/Users/hujiabao/Downloads/courses/'

    chapterId = 72

    for folderName, subfolders, fileNames in os.walk(path):
        if folderName == path:
            for fileName in fileNames:
                if fileName.find('.DS_Store') >= 0:
                    continue
                get_chapters_and_sections(chapterId, root + fileName)
                chapterId += 1

if __name__ == "__main__":
    main()