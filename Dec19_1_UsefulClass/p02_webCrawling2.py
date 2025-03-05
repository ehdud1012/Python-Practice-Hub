# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from bs4 import BeautifulSoup

# https://news.daum.net/

hc = HTTPSConnection("news.daum.net")
hc.request("GET", "/")
resBody = hc.getresponse() .read()
newsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")

title = newsData.select(".content-article .tit_txt")
for i in title:
    print(i.text)

hc.close()