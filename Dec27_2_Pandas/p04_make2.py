# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np 
from oracledb import connect, init_oracle_client
# 확장자? (.xls, .csv, .txt, ...)는 허상 
#   Linux는 없음 
#   .xls : 그냥 이걸로 열먼 잘 열리겠네하는 짐작
#   .csv : 아 ,로 구분되어있네

# kaggle : DB/AI대회 (titanic / iris)

# titanic 
#   - 제목(첫줄)이 있는 .csv
# 제목이 있으면 바로 읽어오기 가능
# a = pd.read_csv("C:/KDY/titanic.csv")
# print(a)

print("-----------------------------------------")
# 첫줄부터 데이터인 csv
b = pd.read_csv("C:/KDY/example/dust/seoulDust.csv", names=["년", '월', '일','시','권역', '구', '미세', '초미세', '상태'])
print(b)

print("-----------------------------------------")
# txt \t으로 구분된 
#   확장자가 뭐든 다 이걸로 열기                        구분
c = pd.read_csv("C:/KDY/example/news/naverNews.txt", sep="\t", names=["제목", '내용'])
print(c)

print("-----------------------------------------")
# OracleDB - SQL
# 1. 어차피 데이터는 DB에 -> DB에서 데이터 가져와서 DF로 -> 분석
# 2. 어차피 데이터는 DB에 -> 분석을 DB SQL문으로 결과만 가져오기
init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

sql = "SELECT * FROM dec19_drink"
d = pd.read_sql(sql, con)
print(d)

con.close()