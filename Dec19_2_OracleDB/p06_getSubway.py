# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# 지하철 승하차 정보 옛날 데이터가 다 있어서 바로 csv로
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/999/20240101/

file = open("C:/KDY/example/subway/getSubway.csv", "a", encoding="utf-8")

hc = HTTPConnection("openapi.seoul.go.kr:8088")

try :
    for y in range(2015, 2025):
        for m in range(1,13):
            for d in range(1,32):
                date = "%d/%d/%d%02d%02d/" % (1, 620, y, m, d)
                hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/" + date)
                resBody = hc.getresponse().read()
                subwayDatas = fromstring(resBody).iter("row") 
                for s in subwayDatas:
                    data = ("%d,%02d,%02d,%s,%s,%d,%d" 
                            % (y, m, d, s.find("SBWY_ROUT_LN_NM").text, s.find("SBWY_STNS_NM").text,
                                int(s.find("GTON_TNOPE").text), int(s.find("GTOFF_TNOPE").text)))
                    file.write(data + "\n")
                    print(y,m,d)
except:
    pass
file.close()
hc.close()