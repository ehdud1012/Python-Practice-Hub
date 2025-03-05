# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# 모기데이터 -> df
# 집, 물가, 공원 평균치
# 모기가 제일 심했던 날
# 물가의 값 없는 곳은 물가의 평균값 넣기

df = pd.read_csv("C:/KDY/example/mosquito2.csv", names=["날짜", "물가", "집", "공원"])
# 값이 다 있음
print(df[df["물가"].isnull()])
# 값이 다 있는데 n으로 되어있음
# print(df[df["물가"] == "n"])
# print(df["물가"].dtype) # 자료형이 object / 숫자 계산 X
# print(df["물가"].mean)

# 1. n -> 없애기
df["물가"] = df["물가"].replace("n", np.nan)
df["집"] = df["집"].replace("n", np.nan)
df["공원"] = df["공원"].replace("n", np.nan)

# 2. 필드 형변환
# ?? -> 숫자
df["물가"] = pd.to_numeric(df["물가"])
df["집"] = pd.to_numeric(df["집"])
df["공원"] = pd.to_numeric(df["공원"])

# 숫자 -> 글자               원하는 자료형
# df["물가"] = df["물가"].astype(str)

print(df["물가"].mean())
# 물가의 값 없는 곳은 물가의 평균값 넣기
df["물가"] = df["물가"].fillna(df["물가"].mean())
df["집"] = df["집"].fillna(df["집"].mean())
df["공원"] = df["공원"].fillna(df["공원"].mean())

df["평균"] = (df["물가"] + df["집"] + df["공원"]) / 3
print(df)

print(df[df["평균"] == df["평균"].max()])