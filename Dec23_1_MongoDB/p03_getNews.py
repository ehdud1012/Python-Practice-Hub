# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote
from pymongo import MongoClient

# https://openapi.naver.com/v1/search/news.json

def clear(c):
    c = c.replace("amp;", "").replace("&quot;", "\"").replace("<b>", "").replace("</b>", "")
    return c

con = MongoClient("192.168.0.55")
db = con.xxe

searchWord = quote("ai")
h = {"X-Naver-Client-Id" : "J3ex8lwJZO0JU8nonIoa", "X-Naver-Client-Secret" : "oXpEo7AifR"}
hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.json?query=" + searchWord, headers=h)

resBody = hc.getresponse() .read()
searchResult = loads(resBody)

for n in searchResult["items"]:
    news = {"n_title" : clear(n["title"]), "n_description" : clear(n["description"])}
    r = db.ai_naver_news.insert_one(news)
    if (r.acknowledged):
        print("성공")

con.close()
hc.close()