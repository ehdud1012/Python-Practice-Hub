# -*- coding:utf-8 -*-
import numpy as np 

# 이항 연산
a = np.random.randint(1, 11, [2, 3])
b = np.random.randint(1, 11, [2, 3])
print(a)
print(b)
print("----------------------------------------------")

# 항목 별 더하기 (연산자 다 가능)
c = a + b
print(c)
print("----------------------------------------------")
# 알아는 봐야해서 함수 사용
d = np.add(a, b)
print(d)
e = np.subtract(a, b)
print(e)
f = np.multiply(a, b)
print(f)
g = np.divide(a, b)
print(g)
h = np.mod(a, b) # 나눈 나머지
print(h)
i = np.power(a, b) # 제곱
print(i)
#  greater, greater_equal, less, less_equal, equal, not_equal 
j = np.less_equal(a, b) # a가 b보다 작거나 같은거
print(j)
print("----------------------------------------------")
k = np.maximum(a,b) # 둘 중에 큰 값으로 
print(k)
l = np.minimum(a,b) # 둘 중에 작은 값으로 
print(l)
print("----------------------------------------------")
# 평균이 30점 이상인 사람의 이름
name = np.array(["김","도","영"])
mid = np.array([10,20,40])
final = np.array([40,50,100])

r = np.greater_equal(np.divide(np.add(mid, final), 2), 30)
print(name[r])