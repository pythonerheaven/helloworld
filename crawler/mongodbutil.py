from pymongo import MongoClient

class Mongodbutil(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.client = MongoClient(ip,port)
        self.db = self.client.admin
        self.db.authenticate('root','experiment')
        self.fiv = self.db.fiv


    # item and items, all both ok
    def insertItems(self,items):
        self.fiv.insert(items)