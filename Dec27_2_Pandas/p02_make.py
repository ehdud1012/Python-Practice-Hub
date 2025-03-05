# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np 

# Python list
a = pd.DataFrame()
a["이름"] = ["새우깡", '감자깡', '양파깡']
a['가격'] = [4000, 2000, 3000]
print("-----------------------------------------")
# np.array
b = pd.DataFrame()
b['이름'] = np.array(['김', '도'])
b['나이'] = np.array([22,23])
print(b)
print("-----------------------------------------")
# 2차원 list/np.array
# c = [["김", 20], ["도", 21]]  이거나 아래나 똑같
c = np.array([["김", 20], ["도", 21]])
c = pd.DataFrame(c, columns=["이름", '나이'])  # 제목 달아주기
print(c)
print("-----------------------------------------")
# dict + list
d = {"이름" : ['김', '도'], '나이' : [12, 34]}
d = pd.DataFrame(d) # 딕션어리는 key값 이 있어서 제목 생략 가능
print(d)
print("-----------------------------------------")
# list + dict
e = [
    {"이름" : "김", '나이' : 21},
    {"이름" : "도", '나이' : 22}
]
e = pd.DataFrame(e)
print(e)