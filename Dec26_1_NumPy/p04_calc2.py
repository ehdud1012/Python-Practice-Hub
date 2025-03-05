# -*- coding:utf-8 -*-
import numpy as np 

# 일항 연산 - 소수점 계산
a = np.random.rand(2, 3)
print(a)
print("----------------------------------------------")
# 소수점 이하 올림
b = np.ceil(a)
print(b)
# 소수점 이하 버림
c = np.floor(a)
print(c)
# 소수점 이하 반올림
d = np.rint(a)
print(d)
# 자릿수 지정 반올림
e = np.round(a, 2)
print(e)
# 소수점 이하 셋째 자리에서 올림
f = np.ceil(a * 100) / 100
print("----------------------------------------------")
#                       값 없음      값 무한
b = np.array([45, 3554, np.nan, 567, np.inf, 5])

c = np.isnan(b)  # 값이 없는가 (t/f)
print(c)
d = np.isinf(b)  # 값이 무한대인가 (t/f)
print(d)
print("----------------------------------------------")

c = np.random.randint(-11, 11, [2, 3])
print(c)

# 절댓값
d = np.abs(c)
print(d)
# 제곱
e = np.square(c)
print(e)
# 루트 씌우기 (제곱근)
f = np.sqrt(c)
print(f)
print("----------------------------------------------")

