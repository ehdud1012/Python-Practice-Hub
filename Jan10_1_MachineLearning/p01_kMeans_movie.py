# -*- coding:utf-8 -*-
from cProfile import label
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

# 분류 (classfication) 
#   - 지도 학습
#   - 학습 후 물어보면 예측해 답변
# 
# 클러스터링 (Clustering)
#   - 비지도 학습
#   - 데이터 주고 비슷한 것끼리 묶어봐 (그룹화)

# kMeans 알고리즘 - 클러스터링
#   - k개의 평균 / kNN 형제급
#   1) 데이터 그래프에 표시
#   2) 랜덤한 점 k개 그래프에 표시
#   3) 2)에서 찍은 점이랑 데이터들 각각 거리계산 (유클리드 계산)
#   4) 데이터 각각을 2)에서 찍은 점 중 가까운 쪽으로 그룹짓기 
#   5) 그룹 내에서 평균내서 다시 점 찍기
#   ...
#   더이상 그룹이 안바뀔 때까지 3 ~ 5 반복

df = pd.DataFrame()
df["싸움"] = [80, 95, 10, 90, 5]
df["욕"] = [20, 5, 90, 10, 95]

# 영화가 5개인데 그룹지어봐

data = df[['싸움', '욕']].to_numpy()
km = KMeans(3)
df["그룹"] = km.fit_predict(data)
print(df)

# Seaborn써서 그룹별 같은색
# sns.scatterplot(x="싸움", y="욕",data=df, hue="그룹", palette="Pastel1")
# plt.show()

# 입력받은 데이터는 어디 그룹에 속하나 예측
#   kMeans로 라벨링 + kNN으로 예측
a = float(input("싸움 : "))
b = float(input("욕 : "))
c = np.array([[a, b]]) 
label = df["그룹"].to_numpy()
knc = KNeighborsClassifier(3) 
knc.fit(data, label) 
print(knc.predict(c))