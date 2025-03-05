# -*- coding:utf-8 -*-

import pandas as pd

df1 = pd.read_csv("C:/KDY/example/titanic.csv")
df2 = pd.read_csv("C:/KDY/example/titanic.csv")

# 단순히 붙이기
df3 = pd.concat([df1, df2]) #df1 뒤에 df2 붙이기
print(df3)

df4 = pd.concat([df1, df2], axis=1) #df1 옆에 df2 붙이기
print(df4)

# join
snack = pd.DataFrame()
snack["이름"] = ["빼빼로", "새우깡"]
snack["가격"] = [2000, 3000]
snack["제조사"] = ["롯데", "농심"]

company = pd.DataFrame()
company["회사명"] = ["롯데", "농심"]
company["주소"] = ["서울", "인천"]

# 양쪽 다 제조사 필드 존재
#scDF = pd.merge(snack, company)
#print(scDF)

# 양쪽 다 존재하는 필드가 여러개라면 
#scDF = pd.merge(snack, company, on="제조사")
#print(scDF)

# 필드명 다르면
scDF = pd.merge(snack, company, left_on="제조사", right_on="회사명")
print(scDF)