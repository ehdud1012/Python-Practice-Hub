# -*- coding:utf-8 -*-
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/subway/getSubway.csv", names=["년", "월", "일", "호선", "역", "탐", "내림"])

df["이용객수"] = df["탐"] + df["내림"]

# 노선별 이용객 수 평균 막대그래프
# sns.barplot(x="호선", y="이용객수", data=df, hue="호선", palette="Pastel1")

def getYoil(d):
    d = "%d%02d%02d" % (d["년"], d["월"], d["일"])
    d = datetime.strptime(d, "%Y%m%d")
    return datetime.strftime(d, "%a")
df["요일"] = df.apply(getYoil, axis=1)

# 요일별 이용객 수 평균 막대그래프
# sns.barplot(x="요일", y="이용객수", data=df, hue="요일", palette="Pastel1")

# 노선별 이용객 수 평균 막대그래프 (요일별로 다른 색깔 표시)
sns.barplot(x="호선", y="이용객수", data=df, hue="요일", palette="Pastel1")

# 노선별 데이터 수 
sns.countplot(x="호선", data=df, hue="호선", palette="winter") 

# 요일별 데이터 수 (노선별로 다른 색깔 표시)
sns.countplot(x="요일", data=df, hue="호선", palette="winter") 

plt.show()