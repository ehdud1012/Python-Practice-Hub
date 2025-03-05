# -*- coding:utf-8 -*-
import numpy as np 
# SQL, 객체 list, pandas를 쓰지 왜 NumPy?
#   pandas, scikit-learn, tensorflow 등 후속 기술들이 사용
#       ex) tensorflow로 인공신경망 구성할 때 list 여러 개 필요
#           -> 일반 list보다는 NumPy가 편하니까

# tensorflow로 인공신경망 구성할 때 써먹을 거
a = np.zeros([3, 2])  # 값은 전부 0으로 3행 2열짜리 리스트 생성
print(a)
print(a.dtype)        # 기본 자료형 float 섬세한 데이터를 다루니까

# 만약 특정 자료형을 지정하고 싶다면?
a = np.zeros([3, 2], dtype=np.int64) 
print(a.dtype)        # 자료형 int

b = np.ones([3, 2])   # 값은 전부 1로 3행 2열짜리 리스트 생성
print(b)

c = np.empty([3, 2])  # 값은 대충하고 3행 2열짜리 리스트 생성
print(c)

d = np.arange(5)      # 0부터 4까지 
print(d)

d = np.arange(2, 5)   # 2부터 4까지 
print(d)

d = np.arange(1, 10, 2)   # 1부터 9까지 2씩
print(d)

e = np.random.rand(3, 2)  # 0.0 ~ 0.99999... 까지 3x2
print(e)

f = np.random.randn(3,2)  # 평균 0, 표준편차 1 인 3x2
print(f)

g = np.random.randint(1, 10, [3, 2])  # 1부터 9까지 3x2
print(g)