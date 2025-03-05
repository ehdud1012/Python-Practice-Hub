# -*- coding:utf-8 -*-
import pandas as pd

a = pd.read_csv("C:/KDY/example/titanic.csv")
print(a)
print("-----------------------")
# a의 기본 정보
print(a.shape) # 몇행 몇열
print(a.columns) # 열 제목
print(a.head()) # 위에서 몇개
print(a.tail(7)) # 아래에서 7개

# 열 기준 조회
print(a["Name"])
print("-----------------------")
print(a.Name)  # 확인 필요
print("-----------------------")
print(a[["Name", "Age"]])

# 행 기준 조회
print(a.iloc[1]) # 1번 데이터
print(a.iloc[0:3]) # 0-2번 데이터
a = a.set_index(a["Name"]) # index 지정 : Name을 기준으로 찾겠다
print(a)
print(a.loc["Braund, Mr. Owen Harris"])  # index (Name)으로 찾기
print(a.loc["Braund, Mr. Owen Harris" : "Allen, Mr. William Henry"]) 
print("-----------------------")

# 행 + 열 기준 조회(데이터의 특정 필드만)
print(a.loc["Heikkinen, Miss. Laina"]["Age"])
print(a.loc["Heikkinen, Miss. Laina"][["Age", "Pclass"]])
print(a.loc["Heikkinen, Miss. Laina", "Age"])
print(a.loc["Heikkinen, Miss. Laina", ["Age", "Pclass"]])

#조건조회
print(a["Age"])
print(a["Age"] > 30) # 나이가 30초과 T/F
print(a[a["Age"] > 30]) # 나이가 30초과하는 사람

# 20대 : 20 <= 나이 < 30
print(a[(a["Age"] >= 20) & (a["Age"] < 30)])