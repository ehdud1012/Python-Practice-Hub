# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv("C:/KDY/example/lnps.csv", names=["이름", "품명", "가격", "종류", "구"])
# 가격 비싼 순 정렬
df = df.sort_values(by="가격", ascending=False) 
# top 10
print(df.head(10))
print("------------------------------------------------------------------")
# 34902990보다 싼 것만
df = df[df["가격"] < 34902990]
# 평균가
print(df["가격"].mean())
print("------------------------------------------------------------------")
# 대형마트 평균가 vs 시장 평균가
print(df.groupby("종류")["가격"].mean())

# 구별 -> 종류별 (List형태로)
print(df.groupby(["구", "종류"])["가격"].mean())
print("------------------------------------------------------------------")

# OracleDB에 있는 미세먼지
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"
df2 = pd.read_sql(sql, con)
print(df2.columns)

df2["SDD_PM_SUM"] = df2["SDD_PM10"] + df2["SDD_PM25"]
print(df2["SDD_PM_SUM"])
# 구별 pm10+pm25평균
print(df2.groupby("SDD_LOC")["SDD_PM_SUM"].mean())
# 권역별 pm10+pm25평균
print(df2.groupby("SDD_RANGE")["SDD_PM_SUM"].mean())
# 권역별 -> 구별 pm10+pm25평균
print(df2.groupby("SDD_LOC", "SDD_RANGE")["SDD_PM_SUM"].mean())
con.close