# -*- coding:utf-8 -*-
from cProfile import label
from time import process_time_ns
from unittest import result
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from matplotlib import colormaps
from sklearn.neighbors import KNeighborsClassifier
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/subway/getSubway.csv", names=["년", "월", "일", "호선", "역", "탐", "내림"])

# 역 별로 탄 사람, 내린사람 각각 평균
# 이용객 수 비슷한 역끼리 그룹화 (3개) 

df = df.groupby(["역"])[["탐", "내림"]].mean()
data = df[["탐", "내림"]].to_numpy()

# 그룹화
km = KMeans(3)
df["그룹"] = km.fit_predict(data)

# 1. 그래프
# sns.scatterplot(x="탐", y="내림",data=df, hue="그룹", palette="Pastel1")
# plt.show()

# print(df[df["탐"] == df["탐"].max()])

# 2. 역명 입력받아서 그 역과 이용객 수 비슷한 역 조회
station = input("역 : ")
print(df.loc[station])
print(df.loc[station]["그룹"])
print(df[df["그룹"] == df.loc[station]["그룹"]])