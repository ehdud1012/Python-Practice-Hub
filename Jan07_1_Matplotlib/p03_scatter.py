# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/subway/cspf.csv", names=["년", "월", "노선", "역", "찍고탄", "그냥탄", "찍고내린", "그냥내린"])

df = df.groupby("노선")[["찍고탄", "그냥탄", "찍고내린", "그냥내린"]].mean()
route = df.index.to_numpy()
tagOn = df["찍고탄"].to_numpy()
freeTagOn = df["그냥탄"].to_numpy()
tagOff = df["찍고내린"].to_numpy()
freeTagOff = df["그냥내린"].to_numpy()

xData = np.arange(len(route))

# 산점도
#   꺾은선 그래프인데 선 안이은거 XX
#   분포
#   x/y 관계
# plt.scatter(tagOn, tagOff)
# plt.scatter(tagOn, freeTagOn)             
freeTag = (freeTagOn + freeTagOff) / 1000
#                                           투명도  사이즈
plt.scatter(tagOn, tagOff, color="green", alpha=0.3, s=freeTag) 
# 많이 찍고 타면 많이 찍고 내린다 / 그냥 시리즈랑은 무관


plt.show()