# -*- coding:utf-8 -*-

# Java : 통일된 입출력 시스템 (Stream 시리즈) 
#           -> 입출력은 어디다 하는지 소스 같게
#       System.in : 콘솔창 -> 프로그램 (InputStream)
#       Scanner : InputStream 쓰기 편하게
#       Scanner s = new Scanner(System.in);

# Python : 어디다 입출력하나에 따라 다 다름 (자유의 언어)

# 콘솔 입력
age = input("나이 :" );
print(age)
print(type(age), id(age))  # str

# 형 변환 인데... 주소값이 바뀌어...?  -> 형변환 X , 새로운 객체를 만들 뿐
# 글자 -> 숫자  
age = int(age)   # => 사실 생성자
print(type(age), id(age))

height = float(input("키 : "))
print(height, type(height), id(height)) 