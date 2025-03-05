# -*- coding:utf-8 -*-
from datetime import datetime
from matplotlib import cm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/subway/getSubway.csv", names=["년", "월", "일", "노선", "역", "탐", "내림"])
df["이용객수"] = df["탐"] + df["내림"]

# 피봇테이블 : 테이블을 요약해놓은 테이블
# 월별 이용객 수를 노선으로 찾게
pt = df.pivot_table(index="노선", columns="월", values="이용객수")
print(pt)

sns.heatmap(pt, cmap="BuPu")
plt.show()
