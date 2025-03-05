# -*- coding:utf-8 -*-

# MongoDB 접속
# mongosh 있는 곳(bin까지) 가서 cmd 
#   mongosh 주소
#   use DB명 (xxe)

# MongoDB
#   NoSQL
#       SQL X, JS로 제어 = Python과 문법 비슷
#       테이블 X, JS 배열 = Python의 list
#       레코드 X, JS 객체 = Python의 dict
#       뭔가를 정의 X, 자동 생성 -> 비정형 데이터

# Python + MongoDB 라이브러리 : pymongo.py
#   시작 cmd -> pip install pymongo

from pymongo import MongoClient

# 서버 연결 
con = MongoClient("192.168.0.55")
# db 연결 
db = con.xxe

# 입력 받기
name = input("이름 : ")
price = int(input("가격 : "))

# MongoDB의 레코드 : JS 객체 =  Python의 dict
snack = {"s_name" : name, "s_price" : price}

# insert
# MongoDB : JS로 제어 = Python과 문법 비슷
# pymongo.py : MongoDV제어 문법 그대로 사용 가능하게 해주는 라이브러리
r = db.dec23_snack.insert_one(snack)
# print(r)
if (r.acknowledged):
    print("성공")

# MongoDB 조회 : db.dec23_snack.find();
con.close()