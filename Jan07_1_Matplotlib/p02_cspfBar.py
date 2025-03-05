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

plt.bar(xData, tagOn, width=0.3)
plt.bar(xData, freeTagOn, width=0.3, bottom=tagOn)
plt.bar(xData-0.3, tagOff, width=0.3, align="edge")
plt.bar(xData-0.3, freeTagOff, width=0.3, align="edge", bottom=tagOff)
plt.xticks(xData, route)
plt.show()