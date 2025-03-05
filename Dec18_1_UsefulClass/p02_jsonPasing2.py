# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

# REST API키 - e9f4bd4e350432ceafa6a59e824954d8
# 카카오 책 검색
# https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-book

searchWord = input("검색 : ")
searchWord = quote(searchWord) # 한글 인코딩
h = {"Authorization" : "KakaoAK e9f4bd4e350432ceafa6a59e824954d8"}
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", "/v3/search/book?query=" + searchWord, headers=h)

resBody = hc.getresponse() .read()
searchResult = loads(resBody)["documents"]

for v in searchResult:
    print("%s - %s원" % (v["title"], v["price"]))
hc.close()

