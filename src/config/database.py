from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        # establish a connection we’ll use the MongoClient object.
        self._conn = MongoClient('mongodb://localhost:27017')
        self._db = self._conn["terranova"]


    def createCollection(self, name=""):
        return self._db[name]
