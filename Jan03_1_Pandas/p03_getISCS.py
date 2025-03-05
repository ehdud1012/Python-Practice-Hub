# -*- coding:utf-8 -*-
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/IndividualServiceChargeService/1/100/

from http.client import HTTPConnection
from json import loads

f = open("C:/KDY/example/iscs.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for start in range(1, 6002, 1000):
    t = "%d/%d" % (start, start + 999)    
    hc.request("GET","/575a4655496b636839386f58586542/json/IndividualServiceChargeService/" + t, )
    rb = hc.getresponse().read()
    for i in loads(rb)["IndividualServiceChargeService"]["row"]:
        f.write("%s," % i["BSSH_NM"].replace(",", "."))
        f.write("%s," % i["INDUTY_DESC"].replace(",", "."))
        f.write("%s," % i["ADRES_CN2"].replace(",", "."))
        f.write("%s," % i["PRDLST_DESC"].replace(",", "."))
        f.write("%.0f\n" % i["PC"])
    print(t)
hc.close()