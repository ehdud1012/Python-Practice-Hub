# -*- coding:utf-8 -*-

from json import loads
import pandas as pd
from http.client import HTTPConnection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb = hc.getresponse().read()
hc.close()

dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)

# 히스토그램
# sns.histplot(x="PM10", data=df, palette="coolwarm")

# 히스토그램 + 산점도 - 모든 케이스 전부 다
# sns.pairplot(data=df)

# 히스토그램인데 바이올린 모양
# sns.violinplot(x="PM10", data=df, palette="BuPu")
sns.violinplot(x="PM10", y="MSRRGN_NM", data=df, hue="MSRRGN_NM", palette="BuPu")
plt.show()

hc.close()