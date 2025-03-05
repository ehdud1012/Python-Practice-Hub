# -*- coding:utf-8 -*-
import numpy as np 

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("--------------------")
c = a + b   # NumPy라서 계산을 해버림
print(c)
print("--------------------") 
# list를 붙이고 싶다면?
# 1. 형식 그대로 붙이기
d = np.concatenate([a, b])
print(d)
# 2. 1차원으로 붙이기
e = np.append(a,b)
print(e)
print("--------------------") 

# 축 지정할 떄
# axis=0 : 열
# axis=0 : 행

# 행 방향으로 붙이기
# f = np.concatenate([a, b], axis=1) 
# 열 방향으로 붙이기 (기본값)
f = np.concatenate([a, b], axis=0) 
print(f)

# 행 방향으로 붙이기
# g = np.append(a, b, axis=0)
# 열 방향으로 붙이기
g = np.append(a, b, axis=1)
print(g)

print("--------------------") 

# 아무 기준 없이 2개로 나누기
h = np.array_split(a, 2)
print(h)

# 정확히, 똑같이 3개로 나누기
i = np.split(a, 3)
print(i)