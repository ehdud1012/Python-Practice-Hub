# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/KDY/example/titanic.csv")
print(df)

# pandas의 모든 작업이 원본에 영향 안가게 되어있는데
# => 삭제가 의미 있나
df.sort_values(by="Name")

print(df)
print("--------")

# 열 삭제 : 나머지를 추출해도
df = df.drop("Survived", axis=1)
df = df.drop(["PassengerId", "Pclass"], axis=1)
print(df)
print("--------")

# 이름 , 나이 남기고 나머지 다 삭제 => 이름, 나이만 추출 
df = df[["Name", "Age"]]
print(df)
print("--------")
# 행 삭제 : 나머지를 추출해도
df = df.drop(0) # 0번 지우기x, index로 지우기
df = df.set_index(df["Name"])
df = df.drop("Dooley, Mr. Patrick")
print(df)

# 나이가 30살 미만 다 삭제 => 나이가 30살 이상만 추출
df = df[df["Age"] >= 30]
print(df) 
print("--------")

# OracleDB에 미세먼지 df
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"
df = pd.read_sql(sql, con)

# 권역, PM10, PM25 열 삭제
df = df[["SDD_RANGE", "SDD_PM10", "SDD_FIGURE"]]

# 상태가 없음인거 삭제
df = df[df["SDD_FIGURE"] != "없음"]
print(df)
con.close()
