# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/KDY/example/iscs.csv", names=["매장", "업종", "구", "주소", "상품", "가격"])

# 0원짜리는 삭제하고
df[df["가격"] != 0]
print(df)
print("------------")

# 업종별 평균가
print(df.groupby("업종")["가격"].mean())
print("------------")

# 상품별 평균가
print(df.groupby("상품")["가격"].mean())
print("------------")

# 없는 주소
df["주소"] = df["주소"].fillna("모름")
#df["구"] = df["주소"].apply(lambda a:a.split(" ")[1])

# 구별 평균가
print(df.groupby("구")["가격"].mean())
# 구별 -> 업종별 평균가
print(df.groupby(["구", "업종"])["가격"].mean())