#  阅读笔记

 a.在python或python3 之后和.py文件这前加上-O开关，skip the assert clause
 b.最好使用Python 3.0版本
 c.from_moduel_name import function_name as mp


# Questions

1. python 在不同层级目录import 模块的方法(http://blog.csdn.net/hansel/article/details/8975663)
2. https://api.github.com/search/repositories?q=language:python&sort=starts
3. How to install talib
http://ta-lib.org/
所有程序 -> Mircosoft Visual Studio 2010 -> visual studio tools -> Visual Studio x64 win64 command prompt (2010)
在VS x64 win64命令行下，cd C:\ta-lib\c\make\cdr\win32\msvc 目录下，执行nmake
等执行完毕后，再运行pip install ta-lib， 这次终于成功了

  """
    南方东英杠反ETF策略
    详细参考 https://act.futunn.com/south-etf
    以及富途相应课程信息 https://live.futunn.com/course/1012
    """
=======
# Install packages

pip3 install send2trash requests beautifulsoup4 openpyxl  PyPDF2 selenium  python-docx   imapclient   pyzmail  twilio pillow  python3-xlib
pip3 install pyobjc-core pyobjc
pip3 install pyautogui
pip3 install requests
pip3 install beautifulsoup4
pip3 install pymongo
pip3 install APScheduler
pip3 install lxml
pip3 install urllib2
pip3 install futuquant --upgrade
pip3 install matplotlib 显示各种图表， http://matplotlib.org


# QA

```
SSL: CERTIFICATE_VERIFY_FAILED certificate verify failed(_ssl.c:749)

cd /Applications/Python 3.6 
./Install Certificates.command

https://blog.csdn.net/blueheart20/article/details/72824921

```