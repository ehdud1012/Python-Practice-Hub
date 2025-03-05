# -*- coding:utf-8 -*-

from json import loads
import pandas as pd
from http.client import HTTPConnection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

# 실시간 미세먼지에서 권역, 구, pm10, pm25, idex_nm만 df로

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb = hc.getresponse().read()
hc.close()

dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)

xLabel = df["MSRSTE_NM"].to_numpy()
xData = np.arange(len(xLabel))
pm10Data = df["PM10"].to_numpy()
pm25Data = df["PM25"].to_numpy()

plt.bar(xData, pm10Data, color="#FFCFCF")
plt.bar(xData, pm25Data, bottom=pm10Data, color="#86A788")
plt.xticks(xData, xLabel)
plt.legend(["미세먼지", "초미세먼지"])
plt.title("실시간 미세먼지 데이터")

plt.show()

