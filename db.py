import os

import pandas as pd
import pymongo


class MongoDB:
    def __init__(self):
        self.host = 'localhost'
        self.port = 27017
        self.client = pymongo.MongoClient(self.host, self.port)
        return

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def create_db(self, db_name):
        return self.client[db_name]

    def cr_coll(self, db, collection_name):
        return db[collection_name]

    def ins_data(self, collection, data):
        return collection.insert_many(data)

    def exp_to_ex(self, collection):
        cursor = collection.find({})
        df = pd.DataFrame(list(cursor))
        file1 = input("Введите имя файла с расширением xlsx: ")
        df.to_excel(file1)


os.system('cls' if os.name == 'nt' else 'clear')
mongodb = MongoDB()
