# -*- coding:utf-8 -*-
from oracledb import connect, init_oracle_client
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import seaborn as sns
from matplotlib import colormaps
from http.client import HTTPConnection
from json import loads

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

# 실시간 미세먼지를 df

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb = hc.getresponse().read()
hc.close()

dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
print(df)

# sns.barplot(data=df)
# x,y 지정
# sns.barplot(x="MSRSTE_NM", y="PM10", data=df, palette="Pastel1"
# 검은선 : 신뢰구간 95%
# 통계가 필요하면 통계내서 그림
# sns.barplot(x="MSRRGN_NM", y="PM10", data=df, palette="Pastel1")

# 검은선 : 표준편차
# sns.barplot(errorbar="sd", x="MSRRGN_NM", y="PM10", data=df, palette="Pastel1")
# plt.show()

# 갯수
# 권역별 데이터 몇개씩
# sns.countplot(x="MSRRGN_NM", data=df, palette="BuPu") 
# plt.show()

# 권역별 데이터 몇개씩, 상태별ㅀ 다른 색으로 표시
sns.countplot(x="MSRRGN_NM", data=df, hue="IDEX_NM", palette="winter") 
plt.show()

