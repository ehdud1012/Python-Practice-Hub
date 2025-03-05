# -*- coding:utf-8 -*-

# System.out.println("z");
from time import sleep


print("z")
print('zz')  #  "" / '' 구분 X

# System.out.print("z");
print("z", end="")  # 나중에 설명
print('zz') 

# System.out.printf("%d\n", 10);
# 따로 없음    ▽ 사용
# String s = String.fotmart("%d\n", 10);
s = "%d\n" % 10
print(s)
# --------------------- ▽ 정리
# System.out.println(String.fotmart("%d\n", 10));
print("%d\n" % 10)
print("%s, %02d, %.1f" % ("z", 1, 0.2345))

# %d / \t 시리즈는 그대로

# \r : carriage return 커서를 맨앞으로
# \n : new line 줄만 바꿈 

# \n 만 있어도 \r\n으로 처리

print("------------------------------")
print("이름 \t\t 김도영")
print("나이 \t\t 21")
print("생년월일 \t %d" % 20041012)

print("------------------------------")

sleep(3000)

# 실행파일

# Java : complie
#   .java -complie-> .class -압축-> .jar
#   .jar 주고 받음 : 소스 공개X, 기능만 사용

# Python : interpreter 
#   .py : 그냥 파일 찾아가서 열기
#   .py 주고 받음 : 소스 공개 / JS랑 다르게 포맷팅 이쁘게 되어있게 공개
