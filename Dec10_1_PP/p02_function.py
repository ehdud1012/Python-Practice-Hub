# -*- coding:utf-8 -*-

# 자바는 메소드 이기 때문에 접근제한자, static이란 개념이 있었지만
# 파이썬은 함수라서 X

# 자바처럼 main 메소드가 없고, interpreter 방식이라서
# -> 코드 정렬을 마음대로 해도 됨

# def 함수명(변수명, 변수명, ...):
#   코드 ...
#   return 값

def test():
    # : + 들여쓰기로 영역 구분
    # -> : 뒤에는 무조건 들여쓰기가 있어야됨
    # => 자리만 차지하게 하려면 pass
    pass

def printWeather():
    print("해")
    print("비")
printWeather()

print("-----------파라메터 값 있는 함수-------------")
def printSum(x, y):
    print("x + y =", x+y)
def printCha(x, y):
    print("x - y =", x-y)

def printGob(x=5, y=10):  # 기본 값 지정 가능 
    print("x * y =", x*y)

printSum(10,29)
printCha(y=10, x=29) # 값 지정 가능 
printGob(10, 20)
printGob(30)         # 기본 값 지정 가능 
printGob(y=20)

# def printGob(x, y, z): 
#     print("x * y * z =", x*y*z)
    
# 오버로딩
#   파라메터가 다르면 함수명 같아도 됨 
#   호출 때 구분 가능
#   일부러 함수명 같게 짓는 테크닉

# 파이썬
# 함수에 (기본값 시스템, 호출 때 파라메터 변수 지정), 자료형 자동 처리
#   => 오버로딩 불가 (구분이 안됨)
#   => 모든 함수명이 다 달라야 됨 (헉! 생성자 오버로딩이 안되네 ......)
#       -> 함수명이 길어짐
print("----------------도움말--------------------")
def helpTest(): 
    # 도움말 java /** 동일
    """
    aaaaaaa
    bbbbbbb
    """
    print("help")

help(helpTest)       # 도움말

print("----------------global--------------------")
x = 100
y = 100
def varTest():
    global y    # 지금부터 y라고 하는 거는 64번줄 y
    x = 50   # 63번줄 x랑 상관없음
    y = 50   # 64번줄 y
    print(x) 
    print(y) 
varTest()    
print(x)     # 100
print(y)     # 50
print("-----------------리턴--------------------")
def getSum(a,b):
    c = a + b
    return c
def getCha(a,b):
    c = a - b
    return c
# 함수 하나에 리턴 여러 개 X
# 컬렉션에 값 여러 개 담아서 컬렉션을 리턴 

# tuple 사용
def result(a, b):
    c = a - b
    d = a + b
    e = a * b
    f = a / b
    # tuple에 () 생략 가능하기에 리턴이 여러 개가 되는 것처럼 보임
    return d, c, e, f

print(getSum(5,3))

r = result(10,5)
print(r, type(r))
r1, r2, r3, r4 = result(10,3)
print(r1, type(r1))

# 합, 곱만 필요하면
r1, _, r3, _ = result(10,3)