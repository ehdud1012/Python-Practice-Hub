# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np 

df = pd.read_csv("C:/KDY/example/bus/busResult.txt", sep="\t", names=["노선", "이용객수"])
df = df.sort_values(by="이용객수", ascending=False) 
# 2024년 이용객 수가 가장 많았던 노선 top 10
print(df.head(10))
print("---------------------------------------------------")
# 주로 타는 버스 정보
print(df[df["노선"].str.contains("7021")]) 

print("---------------------------------------------------")
# 주로타는 버스 정보가 평균보다 이용객스가 많은가
print(df[df["노선"].str.contains("7021")]["이용객수"] > df["이용객수"].mean()) 

print("---------------------------------------------------")
# 가장 이용객 수 가 적은 노선
print(df.tail(1))

