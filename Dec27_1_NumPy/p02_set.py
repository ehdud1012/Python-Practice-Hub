# -*- coding:utf-8 -*-
import numpy as np 

a = np.random.randint(1, 101, [10])

print(a[0])
print(a[2:5])       #2-4
print(a[3:9:2])     #3-8,2개씩
print(a[:9:2])      #0-8,2개씩
print(a[3::2])      # 3~끝, 2개씩
print(a[3:9:])      # 3~8, 1개씩
print(a[::2])       # 0~끝, 2개씩
print(a[::-1])      # 0~끝, 역순 

b = np.sort(a)      # 오름차순
print(b)

# 내림차순은 따로 없
c = np.sort(a)[::-1] # 내림차순 + 역순

print("-----------------------------------------")

# 이항 정렬
d = np.random.randint(1, 101, [3, 5])
print(d)
e = np.sort(d)  # 행별 정리
print(e)

f = np.sort(d, axis=1)  # 1이 기본값
f = np.sort(d, axis=0)  # 열별 정리
print(f)
print("-----------------------------------------")

g = np.sort(d, axis=0)[::-1] # 열별 내림차순 정렬
print(g)
h = np.sort(d)[::-1]    # 행별 내림차순 정렬..?
print(h)
print("-----------------------------------------")
# 제대로 행별 내림차순 정렬
i = []
for data in d:                      # 행별로 잘라서
    i.append((np.sort(data)[::-1])) # 역순으로 돌리고, i에 붙이기
i = np.array(i)                     # i NumPy로 만들기
print(i)