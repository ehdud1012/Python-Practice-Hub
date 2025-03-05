# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# 정리 버전

hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")

resBody = hc.getresponse() .read()
datas = fromstring(resBody).iter("data") 
for w in datas:
    print(w.find("temp").text) 
    print(w.find("temp").text)

hc.close()