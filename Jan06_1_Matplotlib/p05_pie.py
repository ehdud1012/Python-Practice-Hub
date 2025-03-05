from enum import auto
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/shResult.txt", sep="\t", names=["이름", "횟수"])

# 파이차트 : 점유율
#   큰 순서대로 정렬이 기본 -> 자동아님 
df = df.sort_values(by="횟수", ascending=False)

name = df["이름"].to_numpy()
count = df["횟수"].to_numpy()
d = {"width": 0.7, "edgecolor": "black", "linewidth":2}
e = [0,0,0.3]                             # 손권만 0.3만큼 밖으로, 시작 각도
plt.pie(count, labels=name, autopct="%.1f%%", explode=e, startangle=45
        , wedgeprops=d)
plt.show()