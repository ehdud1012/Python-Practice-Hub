# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

file = open("C:/KDY/example/modquito.csv", "a", encoding="utf-8")

hc = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2016, 2025):
    for m in range(5, 11):
        for d in range(1, 32):
            t = "%d-%02d-%02d" % (y, m, d)
            hc.request("GET", "/575a4655496b636839386f58586542/xml/MosquitoStatus/1/1/" + t)
            rd = hc.getresponse().read()
            mosquitoData = fromstring(rd).find("row")
            if mosquitoData != None:
                file.write("%s" % (mosquitoData.find("MOSQUITO_DATE").text))
                file.write("%s" % mosquitoData.find("MOSQUITO_VALUE_WATER").text)
                file.write("%s" % mosquitoData.find("MOSQUITO_VALUE_HOUSE").text)
                file.write("%s" % mosquitoData.find("MOSQUITO_VALUE_PARK").text + '\n')
            print(t)

hc.close()
file.close()