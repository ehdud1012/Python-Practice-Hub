# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/KDY/example/titanic.csv")

# 이름, 성별 빼고 나머지 다 삭제
df = df[["Name", "Sex"]]
print(df)
print("---------------------")

# male -> 남자 , female -> 여자
df["Sex"] = df["Sex"].replace(["male", "female"], ["남자", "여자"])
print(df)
print("---------------------")

# Mr. -> 미스터
def convertMr(t):
    return t.replace("Mr.", "미스터")
df["Name"] = df["Name"].apply(convertMr)
print(df)
print("---------------------")

# 성 빼고 이름만 남기기
#def removeFamilyName(n):
   #return n.split(", ")[0]
#df["Name"] = df["Name"].apply(removeFamilyName)
df["Name"] = df["Name"].apply(lambda n:n.split(", ")[0])
###############################
#def add(a,b):
    #return a + b
#c = add(10 + 20)

#c = (lambda a,b:a+b)(10 + 20)
print("---------------------")

df = pd.read_csv("C:/KMJ/CSV/titanic.csv")
df = df[["Survived", "Name", "Age"]]
df["Age"] = df["Age"].fillna(900)

def getDae(a):
    return "%d0대" % (a // 10)

df["대"] = df["Age"].apply(getDae)
df["대"] = df["대"].replace("900대", "미상")

# 22 -> 20대
# 35 -> 30eo
# 900 -> 900대
# NaN -> 미상
# 연령대별 산사람/죽은사람
print(df.groupby)