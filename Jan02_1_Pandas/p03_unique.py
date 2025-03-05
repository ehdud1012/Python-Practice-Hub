# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/KDY/example/titanic.csv")
print(df.columns)

# 좌석 등급 별 산/죽은 사람 수 
print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())
# 좌석 등급 별 평균요금
print(df.groupby(["Pclass"])["Fare"].count())
# 성별별 산/죽은 사람 수 
print(df.groupby(["Sex", "Survived"])["PassengerId"].count())

print("-------------------------------------------------------")
# 객실 뭐뭐 있나 (중복 제거)
print(df["Cabin"].unique())

# 객실 몇종류 (중복 제거)
print(df["Cabin"].nunique())

# 객실별로 몇명
print(df["Cabin"].value_counts())

print("-------------------------------------------------------")
# 물가 csv
df2 = pd.read_csv("C:/KDY/example/lnps.csv", names=["이름", "품명", "가격", "종류", "구"])
# 시장/마트가 뭐뭐 있나
print(df2["이름"].unique())
# 시장/마트가 몇종류
print(df2["이름"].nunique())
# 구별로 데이터 갯수
print(df2["구"].value_counts())