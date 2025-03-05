# -*- coding:utf-8 -*-
import numpy as np 

# 수정

a = np.random.randint(1, 11, [10])
print(a)
print("-----------------------------------------")
# 수정?
a[0] = 100
a[1:3] = 200 
print(a)

# 새로운 수정 (조건, 바꿀 값, 대상) 
b = np.where(a % 2 == 1, 0, a)         # -> 조건 걸어서 바꾸기 가능
print(b)