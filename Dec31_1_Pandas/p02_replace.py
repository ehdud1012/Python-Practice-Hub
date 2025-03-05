# -*- coding:utf-8 -*-

import pandas as pd

ff = pd.read_csv("C:/KMJ/lnps.csv", names=["이름", "품명", "가격", "종류", "지역구"])

# 대형마트 -> 마트
# 열 구분 없이
# ff = ff.replace("대형마트", "마트") 
# 특정 열만
ff["종류"] = ff["종류"].replace("대형마트", "마트")

# 한꺼번에
# 마트 -> mart, 전통시장 -> market
ff["종류"] = ff["종류"].replace(["마트", "전통시장"], ["mart", "market"])

# 마트 -> mart, 전통시장 -> market
ff["종류"] = ff["종류"].replace({"mart":"마트", "market":"시장"})

# 마트,시장 -> 상점
ff["종류"] = ff["종류"].replace(["마트", "시장"], '상점')

# 필드명 바꾸기(이름 -> 어디, 품명 -> 뭐)
ff = ff.rename(columns={"이름":"어디", "품명":'뭐'})
print(ff)