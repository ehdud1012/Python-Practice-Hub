# -*- coding:utf-8 -*-

# 파일 읽기

#                                    read 모드
file = open("C:/KDY/example/1216.txt", "r", encoding="utf-8") 

# 방법 1 : 전체 다 읽어서 str
#          - 나중에 빅데이터 사용하면 ram 폭발 (실전에서..)
# one = file.read()///
# print(one, type(one))
# 방법 2 : 다음 한 줄 한 줄 읽어서 str
# two = file.readline()
# print(type(two))
# print(two)

# 방법 3 : 전체 다 읽어서 \n 기준으로 나눠서(\n 남아있음)  -> list로 
# three = file.readlines()
# print(type(three))

# 최종
for line in file.readlines():
    line = line.replace("\n", "") # 남아있는 \n 처리
    print(line)
file.close()    # 파일 닫기 

# Python
# 분석 라이브러리 / AI 라이브러리 잘 되어 있음 
#   -> 효율성 X

# 빅데이터 (20TB) -> 하둡 -> 10MB ↓ -> 파이썬

# 중간에 하둡 : 서버급 컴 여러대 
