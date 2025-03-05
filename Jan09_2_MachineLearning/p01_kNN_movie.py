# -*- coding:utf-8 -*-

# AI
#   잘 구별안하고 쓰긴 함
#   Machine Learning
#       - 문제 해결하는데 필요한 알고리즘을 사람이 지정하는 것
#       - AutoML이 나오면서 안맞기 시작
#       - 내가 만든 비만도 계산기, 가위바위보
#       - 머신러닝 알고리즘 대표적인 것 소개
#   Deep Learning
#       - 문제 해결하는데 필요한 알고리즘을 AI가 직접 찾게 하는 것
#       - 인공신경망
# ------------------------------------------------------------------------
# 지도학습
#   학습 데이터 + 기존 인간들이 내놓은 결론(라벨)
#           특성 feature       라벨
#       기온0도, 습도 20%  -> 히터 ON  
#       기온10도, 습도 50% -> 히터 OFF  
#       기온5도, 습도 30%  -> ?
#    -> 인간이 내놓은 결과를 사용해 예측해라
# 비지도학습 
#   학습 데이터만 줄테니 알아서 해라
#   -> 학생의 점수만 줄테니 알아서 3그룹으로 나눠라
# ------------------------------------------------------------------------
# scikit-learn : Python MachineLearning 라이브러리
#   설치 - pip install scikit-learn 

# kNN 알고리즘 (k-Nearest Neighbor) - 분류
#   인간은 비슷한 쪽으로 결론으로 냄 -> 수학적으로 표현
#   - 예측할 데이터와 기존 데이터간의 유크릴드 거리를 구해서 
#     가장 가까운 k개 뽑고 라벨 다수결로 결론

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

feature = np.array([[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]])
label = np.array(["액션", "액션", "조폭", "액션", "조폭"])

knc = KNeighborsClassifier(3)  # 가장 가까운 값 3개를 뽑
knc.fit(feature, label)        # 학습시키기

a = float(input("싸움 : "))
b = float(input("욕 : "))
z = np.array([[a, b]])  # 하나 말고도 여러개 물어볼 수 있음

result = knc.predict(z) # 예측시키기
print(result[0])