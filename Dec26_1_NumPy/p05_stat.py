# -*- coding:utf-8 -*-
import numpy as np 

# 통계
a = np.random.randint(1, 11, [2, 3])
print(a)
print("----------------------------------------------")

b = np.sum(a)   # 모든 값 더하기
print(b)
c = np.mean(a)  # 평균
print(c)

d = a - c       # 편차 : 각 값에서 평균을 뺌 / 편차의 합은 0
d = d ** 2      # 음수를 없애려고 ^2 (제곱을 안해버리면 평균은 0이라서)
d = np.mean(d)  # = 분산
print(d)

# 분산     : 편차^2 의 평균 / 얼마나 평균에서 떨어져있나
e = np.var(a)
print(e)

f = np.sqrt(e)
print(f)
# 표준편차 : 분산의 제곱근 
#           원래의 값 단위로 돌아기기 위해 루트씌움 (분산은 제곱을 했기 떄문에 원래 단위와 안맞음)
g = np.std(a)
print(g)
print("----------------------------------------------")

h = np.max(a)   # 최댓값
print(h)
i = np.min(a)   # 최솟값
print(i)

# 통계함수들은 열/행별 계산이 가능
# j = np.max(a, axis=0)   # 열 별 최댓값
j = np.max(a, axis=1)   # 행 별 최댓값
print(j)

k = np.mean(a, axis=1)
print(k)
print("----------------------------------------------")
print(a)

# **중요 : 최종 결론 낼 때 주로 사용 / 얘도 axis 사용 가능
l = np.argmax(a)    # 제일 큰 값 있는 index 번호 (같은 숫자가 있으면 index 빠른걸로)
print(l)
m = np.argmin(a)    # 제일 작은 값 있는 index 번호
print(m)


