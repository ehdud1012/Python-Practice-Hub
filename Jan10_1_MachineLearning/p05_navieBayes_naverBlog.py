# -*- coding:utf-8 -*-

from cProfile import label
from pymongo import MongoClient
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

con = MongoClient("192.168.0.55")
db = con.xxe

data = []
label = []
for n in db.food_naver_blog.find():
    data.append(n["title"] + " " + n["desc"])
    label.append(n["label"])
con.close()

cv = CountVectorizer()
cvResult = cv.fit_transform(data).toarray()

mnb = MultinomialNB()
mnb.fit(cvResult, label)

sentence = input("문장 : ")
sentenceCvResult = cv.transform([sentence]).toarray() 
print(sentenceCvResult)
result = mnb.predict(sentenceCvResult)[0]
print(result)