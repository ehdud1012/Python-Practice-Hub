# -*- coding:utf-8 -*-

from pymongo import MongoClient


con = MongoClient("192.168.0.55")
db = con.xxe

file = open("C:/KDY/example/news/naverNews.txt", "a", encoding="utf-8") 

for n in db.ai_naver_news.find():
    file.write("%s\t" % n["n_title"])
    file.write("%s\n" % n["n_description"])

file.close()
con.close()

