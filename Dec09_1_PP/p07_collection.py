# -*- coding:utf-8 -*-

# Java 
#   []      : 사이즈 고정
#   List    : 가변 사이즈 배열
#   Set     : 중복x, 순서?
#   Map     : 키-값 구조, 순서 X

# Python
# list : 가변 사이즈 배열 (주력) -> numpy(list 업그레이드 버전)
a = [123,435,546,4234,2342,657,78,546,214,2]
print(a, type(a))       #자바는 주소값뜨는걸 파이썬은 제대로 띄어줌
print(a[0])             # index는 0번부터

print(a[1:3])           # 1 ~ (3-1)까지
print(a[1:7:2])         # 1 ~ (7-1)까지 2칸씩
print(a[-1])            # 뒤에서 첫번째
a.append(9239)          # 뒤에 추가
print(a)
a.insert(2, 666)        # 2번 위치에 추가'
print(a)
a[2] = 777              # 3번자리 555로 바꾸기
del a[0]                # 1번 데이터 삭제
print(len(a))           # 총 몇개
a.reverse()             # 역순
print(a)
a.sort()                # 오름차순 정렬
print(a)
 # reverse에 값 지정하기 
a.sort(reverse=True)    # 내림차순 정렬
print(a)

s = "JS에서 문자열"
print(s)
print(s[0])
print(s[1:5:2])
print("-----------------------------------------------")
# set : 중복 X, 순서?
b = {23,435,546,4234,23}
print(b,   type(b))
# set -> list
b = list(b)
print(b, type(b))
print("-----------------------------------------------")
# dict(dictionary)  = Map : 키-값 구조, 순서 X
c = {"탄":30, "단":25, "지":5}
print(c, type(c))
print(c["단"])

# list + dict : JSON 형태

# 파이썬 빅데이터 분석?
# 1. 쉽다
# 2. 컬렉션 사용이 강력