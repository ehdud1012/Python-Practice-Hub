# -*- coding:utf-8 -*-

# int a = 20; Java
# var a = 20; JS

# 자료형 신경 X 알아서 해줌
a = 20  # Object a = new Integer(20); 
print(a)

# 자료형 출력
print(type(a))
# 알 수 있는 것은?
# 1. int형이다 
# 2. int라는 객체이다 (Java의 Integer)
#       20이라는 숫자저장하는데 
#        Java   : 4바이트
#        python : 12바이트 (빅데이터...? 흠...)
# 3. 클래스명인데 소문자로 시작 

# a의 heap 주소값
print(id(a))

# Python : hybrid OOL
# 근데 기본형 없음 / 다 객체

a = "ㅋ" # a = new String("ㅋ"); 
print(a, type(a), id(a))  # 번지 값 변경 / 원래 heap 값 GC

#------------------------------------------------
b = 10
if b > 5:
    c = 20
    print(c)
print(c)
# 34번줄 실행되는 시점에 c가 있어서 오류 아님 ->  대화형이라 가능한 일

#------------------------------------------------
d = 10  # heap영역에 10이 저장됨 -> d에 10 대입
d = 20  # d에 20 대입

# 변수를 만든건지, 값을 바꾼건지 소스로 구분할 수 없음
#------------------------------------------------

a = 10 # Integer
print(a, type(a), id(a))

b = 231.213123 # Floate
print(b, type(b), id(b)) 

c = "c" # str  / char은 없음
print(c, type(c), id(c)) 

d = True # / False : bool
print(d, type(d), id(d))

e = None # null

