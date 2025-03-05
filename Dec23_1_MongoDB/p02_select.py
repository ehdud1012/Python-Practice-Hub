# -*- coding:utf-8 -*-

from pymongo import MongoClient

con = MongoClient("192.168.0.55")
db = con.xxe

r = db.dec23_snack.find()
for s in r:
    # print(s) dict
    print(s["s_name"], s["s_price"])

con.close()