import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        MONGO_DB_URL = "mongodb+srv://Paris:jay19920715@cluster0.ovtydoj.mongodb.net/?retryWrites=true&w=majority"

        
        self.client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=ca)   #os.getenv('MONGO_DB_URL')
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
