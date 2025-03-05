# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/KMJ/titanic.csv")
df = df.set_index(df["Name"])

#df = df.sort_index() # index기준 오름차순 정렬
df = df.sort_index(ascending=False)

# 행 방향 정렬
df = df.sort_index(axis=1)

# 특정 필드 기준 정렬
df = df.sort_values(by=["Pclass", "Age"], ascending=[False, True])
print(df[["Name", "Age"]])

# for문 써서
print(df.index) # 지정된 index들
for n in df.index:
    #print(n)
    print(df.loc[n])
    print("--------")