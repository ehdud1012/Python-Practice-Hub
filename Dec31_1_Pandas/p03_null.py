# -*- coding:utf-8 -*-

import pandas as pd

ff = pd.read_csv("C:/KMJ/lnps.csv", names=["이름", "품명", "가격", "종류", "지역구"])

# 값이 없나 확인
print(ff["품명"].isnull())
print("--------------------------")
print(ff[ff["품명"].isnull()])

# 없는 값 채우기
ff["품명"] = ff["품명"].fillna("모름")
print(ff[ff["품명"].isnull()])
print(ff[ff["품명"] == "모름"])

# 없애기
# pandas로 표현불가 -> numpy로
import numpy as np
ff["품명"] = ff["품명"].replace("모름", np.nan)
print(ff[ff["품명"].isnull()])