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

# 관계를 보여주는 그래프

# 산점도 + 회귀선
#   회귀(Regression)
#       데이터들과의 오차를 최소화한 직선
# sns.lmplot(x="PM10", y="PM25", data=df)

# 히스토그램 + 산점도(기본)
# sns.jointplot(x="PM10", y="PM25", data=df)
# 히스토그램 + 회귀선
# sns.jointplot(x="PM10", y="PM25", data=df, kind="reg")
# 히스토그램 + 등고선
# sns.jointplot(x="PM10", y="PM25", data=df, kind="kde")
# 히스토그램 + 육각형
sns.jointplot(x="PM10", y="PM25", data=df, kind="hex")

plt.show()
hc.close()