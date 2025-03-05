# -*- coding:utf-8 -*-

# J3ex8lwJZO0JU8nonIoa
# oXpEo7AifR

from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

class Search:
    def __init__(self, s):
        self.title = s.find("title").text
        title = title.replace("<b>", "").replace("</b>", "")
        self.price = int(s.find("lprice").text)

    def printInfo(self):
        print("%s\t%d원" % (self.title , self.price)) 
# -----------------------------------------------------

search = input("머 : ")
search = quote(search) # 한글 인코딩

# 요청 헤더 (dict로 표현)
h = {"X-Naver-Client-Id" : "J3ex8lwJZO0JU8nonIoa", 
     "X-Naver-Client-Secret" : "oXpEo7AifR"}

hc = HTTPSConnection("openapi.naver.com")               
hc.request("GET", "/v1/search/shop.xml?query=" + search, headers=h) # 헤더에 넣어주기

resBody = hc.getresponse() .read()
items = fromstring(resBody).iter("item") 

searchResults = []
for s in items:
    searchResults.append(Search(s))

searchResults.sort(key=lambda ww: ww.price)

for i, w in enumerate(searchResults):
    if i == 10:
      break  

hc.close()