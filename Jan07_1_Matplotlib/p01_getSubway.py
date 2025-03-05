# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from json import loads

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/5/201501/

file = open("C:/KDY/example/subway/cspf.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
try:
    for y in range(2015, 2025):
        for m in range(1, 13):
            date = "%d%02d/" % (y, m)
            hc.request("GET", "/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/1000/" + date)
            resBody = hc.getresponse() .read()
            subwayData = loads(resBody)
            if ("CardSubwayPayFree" in subwayData):
                subwayData = loads(resBody)["CardSubwayPayFree"]["row"]
                for station in subwayData:
                    routeName = station["SBWY_ROUT_LN_NM"]
                    stationName = station["STTN"]
                    tagOn = station["RMIO_GTON_NOPE"]
                    freeTagOn = station["FREECHRG_GTON_NOPE"]
                    tagOff = station["RMIO_GTOFF_NOPE"]
                    freeTagOff = station["FREECHRG_GTOFF_NOPE"]
                    data ="%d,%02d,%s,%s,%d,%d,%d,%d\n" % (y, m, routeName, stationName, tagOn, freeTagOn, tagOff, freeTagOff)
                    file.write(data)
            else:
                print("넘어감")
except:
    pass

# 622

