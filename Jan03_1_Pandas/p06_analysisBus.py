# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/KDY/busResult2.txt", sep="\t", names=["요일", "평균"])
print(df)

df1 = df[df["요일"].str.endswith("합")]
df2 = df[df["요일"].str.endswith("갯수")]

df1 = df1.rename(columns={"평균":"합"})
df2 = df2.rename(columns={"평균":"갯수"})
df1["요일"] = df1["요일"].apply(lambda y:y.split("_")[0])
df2["요일"] = df2["요일"].apply(lambda y:y.split("_")[0])

df = pd.merge(df1, df2)
df["평균"] = df["합"] + df["갯수"]
print(df)