# -*- coding:utf-8 -*-

from json import loads
import pandas as pd
from http.client import HTTPConnection

# 실시간 미세먼지에서 권역, 구, pm10, pm25, idex_nm만 df로

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb = hc.getresponse().read()
hc.close()

dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
df = df[["MSRRGN_NM", "MSRSTE_NM", "PM10", "PM25", "IDEX_NM"]]
df["PM_SUM"] = df["PM10"] + df["PM10"] # 열끼리 계산 가능
print(df)
print("----------------------")
# 구로 찾을 수 있게 index지정
df = df.set_index(df["MSRSTE_NM"])

# 종로그 데이터 확인
print(df.loc["종로구"])
print("----------------------")

# 미세먼지 합 심한 순으로 정렬
df = df.sort_values(by="PM_SUM", ascending=False)
print(df)
print("----------------------")

# 종로구 -> 학원
df["MSRSTE_NM"] = df["MSRSTE_NM"].replace("종로구", "학원")
print(df)
print("----------------------")

# 미세먼지 합이 평균보다 낮은 데이터의 구 확인
print(df[df["PM_SUM"] < df["PM_SUM"].mean()]["MSRSTE_NM"])
