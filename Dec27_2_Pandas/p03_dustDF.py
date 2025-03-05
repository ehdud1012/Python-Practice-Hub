# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse() .read()
dustData = loads(resBody)["RealtimeCityAir"]["row"]  # list + dict

dustData = pd.DataFrame(dustData)
print(dustData)
hc.close()

# Pandas
#      MS Excel     = 태블로 = BImatrix = PowerBI ...
#   애초에 작업X  | 기본 .csv는 무료인데 웹데이터는 유료