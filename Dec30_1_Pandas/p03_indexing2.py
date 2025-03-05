# -*- coding:utf-8 -*-

import pandas as pd

ff = pd.read_csv("C:/KMJ/subway.csv", names=["년", "월", "일", "노선", "역", "탐", "내림"])
print(ff.tail(3))

print(ff.head(1)[["년", "월", "일"]])

print(ff.iloc[100:111][["노선", "역"]])
# 노선번호로 찾을 수 있게
ff = ff.set_index(ff["노선"])
# 2호선 데이터만
print(ff.loc["2호선"])
# 1호선 데이터의 역이름, 탄사람수, 내린사람수
print(ff.loc["1호선"][["역", "탐", "내림"]])
# 탄 사람수가 50000이상인 데이터
print(ff[ff["탐"] >= 50000])
# 탄 사람수가 50이 안되는 데이터 날짜, 역
print(ff[ff["탐"] < 50][["년", "월", "일", "역"]])
# 종각역 데이터
print(ff[ff["역"] == "종각"])
# 역 이름에 입구가 들어가는 데이터
print(ff[ff["역"].str.contains("입구")])
#                    .startswith
#                    .endswith
# 역 이름이 서울로 시작하는 데이터의 노선
print(ff[ff["역"].str.startswith("서울")]["노선"])