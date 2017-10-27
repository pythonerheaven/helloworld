try:
    from setuptools import  setup
except ImportError:
    from distutils.core import  setup

config = {
    'description':'StoreWords',
    'author':'allen.hu',
    'url': 'url',
    'download_url':'Where to download it',
    'author_email':'hujb2014@163.com',
    'version':'0.0.1',
    'install_requires':['nose'],
    'packages':['StoreWords'],
    'scripts':[],
    'name':'StoreWords'
}
