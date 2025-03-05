# -*- coding:utf-8 -*-

s = "글자 관련"
print(s, type(s), id(s))  # str 객체

print(s.startswith("글자"))         # 글자로 시작하나
print(s.replace("글자", "문자열"))  # 글자 -> 문자열
print(len(s))                       # 총 글자수

print(s[1])                         # 2번째 글자
print(s.find("관련"))               # '관련'이 몇번째 인덱스에 있나 (없으면 -1이 나옴)
print(s.find("관련") != -1)         # '관련'이란 말이 있나 

# String s = String.fotmart("%d\n", 10);
s2 = "%d" % 10
print(s2)

# 이런식으로 문자열 붙이기 - XXX 
# heap영역에 새로 만들어져서 번지수 변경됨 그전 번지는 GC 
s3 = "aa";
s3 += "bb";
# Java 해결책 StringBuffer 사용
# Python : 메모리 효율성 신경 안씀 저대로 쓰면 됨

s4 = 'a,b,c'
# Java   - 정형 데이터   : split
#        - 비정형 데이터 : StringTokenizer
# Python - 무슨 데이터든 간에 split 사용
s4ar = s4.split(',')

# 웹 크롤링
# <div>
#       ㅋㅋ
# </div>
# =>  <div>\r\n\tㅋㅋ\r\n</div> 로 나올 것 

# 앞뒤로 필요없는 공백/문자 제거  
s5 ="   xx      "
print(s5.strip())
s6 = 'zzzzzzzzzzㅇㅇzzzzzzzzzz'
print(s6.strip('z'))

# Java
#   기본형 -> stack에 저장
#   기본형이 heap 에 데이터가 있어야 하는 경우
#       ->기본형에 해당하는 객체 : Wrapper Class
# Python
#   기본형이 없음
#   Python의 int = Java의 Integer