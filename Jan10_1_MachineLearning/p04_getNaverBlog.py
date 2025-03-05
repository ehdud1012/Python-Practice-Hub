# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote
from pymongo import MongoClient

# https://openapi.naver.com/v1/search/blog.json

def clear(c):
    c = c.replace("amp;", "").replace("&quot;", "\"").replace("<b>", "").replace("</b>", "")
    return c

con = MongoClient("192.168.0.55")
db = con.xxe

searchWord = quote("맛집")
h = {"X-Naver-Client-Id" : "J3ex8lwJZO0JU8nonIoa", "X-Naver-Client-Secret" : "oXpEo7AifR"}
hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/blog.json?query=" + searchWord, headers=h)

resBody = hc.getresponse() .read()
searchResult = loads(resBody)

for b in searchResult["items"]:
    print(clear(b["title"]))
    print(clear(b["description"]))
    what = input("광고/정상 : ")
    blog = {"title" : clear(b["title"]), "desc" : clear(b["description"]), "label" : what}
    r = db.food_naver_blog.insert_one(blog)
    if (r.acknowledged):
        print("성공")

con.close()
hc.close()