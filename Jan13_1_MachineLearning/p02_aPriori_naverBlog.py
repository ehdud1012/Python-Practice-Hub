# -*- coding:utf-8 -*-

# 네이버 블로그 불러서 정규화, 동사만 원형으로, 무슨 동사끼리 잘 나오나

from cProfile import label
from pymongo import MongoClient
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt
from apyori import apriori

con = MongoClient("192.168.0.55")
db = con.xxe
o = Okt() 

data = []
for n in db.food_naver_blog.find():
    words = []
    line = o.normalize(n["title"] + " " + n["desc"])
    for w, _ in o.pos(line, stem=True):
        words.append(w)
    data.append(words)
con.close()

result = list(apriori(data, min_support=0.5,min_confidence=0.5))
for r in result:
    for r2 in r.ordered_statistics:
        print("%s -> %s 확률 : %f" % 
              (list(r2.items_base), list(r2.items_add), r2.confidence))