# -*- coding:utf-8 -*-

# deprecated : 업그레이드 or 삭제하고 신제품을 만들 계획이 있음유예기간 
#               (다음버전에 없어질 수도 있음)
#                ==> 그래서 쓰지마셈
# Java   : java.util.Date
#          1996년에 만들어서 2000년대를 생각안함
#          -> 대부분의 기능 deprecated
#          SimpleDateFormat을 사용 
# Python : datetime 
#          2000년대를 생각하는 시점에 탄생

# 패키지가 없음
#     파일명         클래스명
from datetime import datetime
from time import strftime

#   클래스명.메소드명(...)
# today() : static 메소드
# 현재 시간 날짜
now = datetime.today() 
print(now)
print(now.year)
print(now.month)
print(now.day)

# 특정 시간 날짜
t = datetime(2024, 12, 20)
print(t)

s = input("날짜(yyyy/mm/dd) : ")
sa = s.split('/')
y = int(sa[0])
m = int(sa[1])
d = int(sa[2])
sDate = datetime(y,m,d) 
print(sDate)
# 과연 이게 편한가
# -> Java의 SimpleDateFormat 비슷한거 존재

# 패턴확인(Java != Python)
# print(help(strftime)) # time.py에 있는 strftime

# str -> datetime
t2 = datetime.strptime(s, '%Y/%m/%d')
print("t2 : ", t2)

# datetime -> str           요일
s2 = datetime.strftime(t2, "%A")
print("s2 : ", s2)
