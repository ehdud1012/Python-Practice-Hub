# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# ---------------------------------------------------------------------------

resultFile = open("C:/KDY/example/kmaWeather.csv", "a", encoding="utf-8") 

hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")

resBody = hc.getresponse() .read()
datas = fromstring(resBody).iter("data") 

weathers = {}
for w in datas:
    h = int(w.find("hour").text)
    t = float(w.find("temp").text)
    wf = w.find("wfKor").text
    wd = w.find("wdKor").text
   
    resultFile.write("%d,%.2f,%s,%s\n" % (h, t, wf, wd))

hc.close()