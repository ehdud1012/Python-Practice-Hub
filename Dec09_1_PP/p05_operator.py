# -*- coding:utf-8 -*-

x = int(input("x : "))
y = int(input("y : "))
print("----------------------")

a = x + y
b = x - y
c = x * y
d = x / y
e = x % y

print(a, b, c, d, e)
print("----------------------")
# Java   : ?? + String -> 됨    붙여서 String으로
# Python : ??  + str   -> 안됨  error
#          str  + str  -> 됨
# aa = x + "z"
# print(aa)
print("----------------------")
# Java   : ?? * String -> 안됨   error
# Python : ?? * str    -> 됨     글자 반복
cc = x * "z"
print(cc); 

print("----------------------")
# Java   : int / int = int (몫)
# Python : int / int = 자료형 알아서 (소수점까지)
dd = x / y
print(dd);
# 몫만 나오게 하고 싶으면
ddd = x // y
print(ddd);
print("----------------------")
# += -=  똑같음
# ++ --  없음
# Python : 사람친화적 -> 배우기 쉬움
#       대체 가능하면 없애버림 : 효율성 X (관심이 없음)
