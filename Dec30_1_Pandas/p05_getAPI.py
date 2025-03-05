# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from json import loads

f = open("C:/KDY/example/lnps.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for start in range(1, 596002, 1000):
    t = "%d/%d" % (start, start + 999)
    hc.request("GET", "/575a4655496b636839386f58586542/json/ListNecessariesPricesService/" + t)
    resBody = hc.getresponse().read()

    for v in loads(resBody)["ListNecessariesPricesService"]["row"]:
        f.write(v["M_NAME"].replace(",", ".") + ",")
        f.write(v["A_NAME"].replace(",", ".") + ",")
        f.write(v["A_PRICE"].replace(",", ".") + ",")
        f.write(v["M_TYPE_NAME"].replace(",", ".") + ",")
        f.write(v["M_GU_NAME"].replace(",", ".") + "\n")
    print(t)
hc.close()
f.close()