# -*- coding:utf-8 -*-

import pandas as pd

ff = pd.read_csv("C:/KMJ/lnps.csv", names=["시장이름", "품명", "가격", "종류", "지역구"])

# 시장 이름으로 찾게 index지정
ff = ff.set_index(ff["시장이름"])

# 시장 이름 가나다순 정렬
ff = ff.sort_index()
print(ff)
print("--------------------------")

# 통인시장 데이터만
print(ff.loc["통인시장"])
print("--------------------------")

# 이름 없는 거 값 채우기
ff["시장이름"] = ff["시장이름"].fillna("몰라")

# 이름에 농협들어있는 데이터만
print(ff[ff["시장이름"].str.contains("농협")])
print("--------------------------")

# 품명 가나다 -> 비싼 순 정렬
ff = ff.sort_values(by=["품명", "가격"], ascending=[True, False])
print(ff)
print("--------------------------")

# 가격이 10000이상인 데이터의 품명, 가격
print(ff[ff["가격"] >= 10000][["품명", "가격"]])
print("--------------------------")

# 사과를 파는 시장이름
ff["품명"] = ff["품명"].fillna("몰라")
print(ff[ff["품명"].str.contains("사과")]["시장이름"])
#print(ff[ff["품명"] == "사과"]["시장이름"])
print("--------------------------")

# 종로구 데이터만 반복문으로 하나하나 출력
jongroFF = ff[ff["지역구"] == "종로구"]
for i, j in enumerate(jongroFF.index):
    print(jongroFF.iloc[i])
    print("--------------------------")