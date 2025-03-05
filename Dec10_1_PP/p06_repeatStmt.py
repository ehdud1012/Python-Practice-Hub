# -*- coding:utf-8 -*-

# 조건문 - 반복문
# Java 
#   반복 횟수   : 클래식 for
#   컬렉션 탐색 : for-each
#   반복 조건   : while / do-while

# Python 
#    for-each / while 만 있음

# 컬렉션 탐색 for-each
a = [234,543,67,8]
for v in a:
    print(v)
print("----------------------------------")

# 반복 횟수를 원하면.. (클래식 for)
b = [0,1,2,3]
for v in b:
    print(v)
# ----------------- range도 컬렉션
c = range(0,8) 
for v in c:
    print(v)
# ----------------- 결론
for v in range(0,8):
    print(v)
print("----------------------------------")
# jQuery에서 쓴 each : 클래식 + 신형 for
d = ['w', 'a', 's', 'd']
for i, v in enumerate(d): # tuple
    print(i, v)
print("----------------------------------")
# dict : 키-값 / 순서X
#       -> for문? (자바는 안되는데 파이썬은 가능)
e = {"탄":30, "단":25, "지":5}
for k, v in e.items():  # tuple
    print(k, v)
print("----------------------------------")

# 반복문 속에서 변수 생성 X 
#   -> 파이썬은 알아서 처리 / 효율성 신경 안써서 처리 안되도 상관 X
for i in range(0,3):
    f = input("입력 : ")
    print(f)