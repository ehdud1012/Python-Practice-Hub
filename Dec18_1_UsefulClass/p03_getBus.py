# -*- coding:utf-8 -*-

# 서울 열린데이터 광장에서 버스 운행 정보 api
# 2024-01-01 ~ 2024-11-30
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/20240101/
# 39962

from http.client import HTTPConnection
from json import loads

file = open("C:/KDY/example/bus/getBus.csv", "a", encoding="utf-8")

hc = HTTPConnection("openapi.seoul.go.kr:8088")
    
try :
    for m in range(1,13):
        for d in range(1,32):
            for i in range(1, 42000, 1000):
                date = "%d/%d/2024%02d%02d/" % (i, i + 999, m, d)
                hc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/" + date)
                resBody = hc.getresponse().read()
                busData = loads(resBody)
                if ("CardBusStatisticsServiceNew" in busData):
                    busData = loads(resBody)["CardBusStatisticsServiceNew"]["row"]
                    for station in busData:
                        routeName = station["RTE_NM"]
                        stationName = station["SBWY_STNS_NM"]
                        inPassanger = station["GTON_TNOPE"]
                        outPassanger = station["GTOFF_TNOPE"]
                        data ="2024,%02d,%02d,%s,%s,%d,%d\n" % (m, d, routeName, stationName, inPassanger, outPassanger)
                        file.write(data)
                else:
                    print("넘어감")
except:
    pass

file.close()
hc.close()
