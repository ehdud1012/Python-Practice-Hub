# -*- coding:utf-8 -*-

from math import pi


n = input("이름 : ")
h = float(input("키 : "))
a = int(input("나이 : "))
print("----------------------")
print("이름은 %s, 키는 %.1fcm, 나이는 %d살" % (n, h, a))

# 키가 150 이상
a = (h >= 150)
print(a)

# 이름이 홍길동
# 대부분의 PL에서 연산자 : stack
# Python에는 기본형 없, 객체 O
#   - 연산자가 stack 영역이면
#       -> 알아서 해줌
b = (n == '홍길동')
print(b)

print("----------------------")
# 나이가 2살 이상, 키 190 이상
# || : or, |
# && : and, &
c = (h >= 190 and a >= 2) # 항상 순서 생각
print(c)
print("----------------------")
# 나이 5살 이상 10살 이하
d = (a <= 10 and a >= 5)
d = (5 <= a <= 10) # 파이썬은 이게 가능
print(d)

print("----------------------")
# 나이가 20살 이상이면 어서오세요  아님 나가
# e = ( a >= 20 ) ? '어서오세여' : '나가' 삼항 연산자가 안댐 (대체 가능)

print("----------------------")
# 시프트 연산은 있음
print((1>>2))
