# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("C:/KDY/book/자원2023/for AI/datingTestSet.txt", sep="\t", names=["비행기", "게임", "아이스크림", "인기도"])

# scikit-learn - np.array 대상
feature = df[["비행기", "게임", "아이스크림"]].to_numpy()
label = df["인기도"].to_numpy()

# 정규화 
#   각 항목의 값 차이로 인해 결론에 영향을 끼치는 퍼센트가 다를것
#   => 동등하게 하자
#   => 절댓값 사용 X, 비율로 바꾸기 (정규화)

#   각 항목의 최소값,최댓값을 0, 1로 두고 각각의 값을 비율로 변경
#   -> 모든 값을 0 ~ 1로 
mms = MinMaxScaler()
feature = mms.fit_transform(feature)  # 모든 값을 0 ~ 1로 

knc = KNeighborsClassifier(10)
knc.fit(feature, label)

a = float(input("비행기 : "))
b = float(input("게임 : "))
c = float(input("아이스크림 : "))

predictData = np.array([[a, b, c]])
predictData = mms.transform(predictData)
result = knc.predict(predictData) 
print(result[0])