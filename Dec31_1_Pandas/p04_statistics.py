# -*- coding:utf-8 -*-

import pandas as pd

ff = pd.read_csv("C:/KDY/example/lnps.csv", names=["이름", "품명", "가격", "종류", "지역구"])

# 최고가
print(ff["가격"].max())
print(ff[ff["가격"] == ff["가격"].max()])
print("---------------------")

# 최저가
print(ff["가격"].min())
print(ff[ff["가격"] == ff["가격"].min()])
print("---------------------")

# 평균
print(ff["가격"].mean())
print("---------------------")

# 중앙값
print(ff["가격"].median())
print("---------------------")

# 최빈값(제일 많이 나오는거)
print(ff["가격"].mode())
print("---------------------")

# 더하기
print(ff["가격"].sum())
print("---------------------")

# 개수
print(ff["가격"].count())
print("---------------------")

# 분산
print(ff["가격"].var())
print("---------------------")

# 표준편차
print(ff["가격"].std())
print("---------------------")

# 다
print(ff["가격"].describe())
print("---------------------")

# OracleDB에 있을 미세먼지 데이터를 불러다가 df로
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"
df = pd.read_sql(sql, con)
print(df.columns)

# pm10평균
print(df["SDD_PM10"].mean())
# pm25최소
print(df["SDD_PM25"].min())
# pm10 가장 높은 데이터
print(df[df["SDD_PM10"] == df["SDD_PM10"].max()])
# 다 통계
print(df["SDD_PM10"].describe())
con.close()
