# -*- coding:utf-8 -*-

# dict
a = {"키보드" : 10000, "마우스" :5000}
print(a.keys())
a['모니터'] = 100000  # 추가
a['마우스'] = 7000    # 수정 (키 값이 이미 있으면 수정, 없으면 추가)
print("마우스" in a)  # a라는 dict에 마우스
print(a)
print(type(a))
print(a['키보드'])
print("-----------------------------------------------")

# Python에만 있는 collection

# range : for? 느낌
# BD/AI : 더미데이터 생성
# 1~100까지 있는 list 생성
b = range(1, 5) # 1 ~ (5-1)까지
b = list(b)
# - ▽ 정리
b = list(range(1, 5))
b = list(range(1, 10, 2)) # 1~9까지 2씩
print(b)
print("-----------------------------------------------")

# tuple () 
c = (123,45,667,3,3)
print(c, type(c))
print(c[2])
# list랑 다른 점이..?
#   컬렉션 용도는 아니고, python 문법
#   1. 변수 여러개 한꺼번에 값 바꿀 때 
# x, y, z 값 바꾸기
x = 10
y = 20
z = 30
(x, y, z) = (y, z, x)
print(x, y, z)
#   2. 변수 여러개 한꺼번에 값 넣을 때 
(w, a, s) = (1, 4, 2)
print(w, a, s)
# tuple 쓸때 () 생략 가능 (변수 초기화할 때)
r, t = 45, 657
print(r, t)

y = 1, 3
print(y, type(y)) # y는 () 생략된 tuple

u, i = 1, 3
print(u, type(u)) # u는 1 (int)
print("-----------------------------------------------")
