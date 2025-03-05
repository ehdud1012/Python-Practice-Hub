# -*- coding:utf-8 -*-

# Java : 통일된 입출력 시스템
#        -> InputStream / OutputStream
#       - 예외처리 필수
# Python : 장치마다 다 다름 
#           - 콘솔 출력 : print 
#           - 콘솔 입력 : input 

# 파일에 쓰기
t = input("머 : ")

# 파일 열기
#               파일 경로,                  모드 (r:read, w: write, a:append)
file = open("C:/KDY/example/1216.txt", "a", encoding="utf-8") 
#                                               인코딩 언어
file.write(t + "\n") # 파일에 쓰기
file.close()         # 파일 닫기