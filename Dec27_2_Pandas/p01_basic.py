# -*- coding:utf-8 -*-
import pandas as pd

# NumPy 
#   - 실제 사용 : np.array
#   - 기능 추가된 list
#   - OOP의 새대에 2차원 list? (NumPy가 좋은건 맞지만)
#   => 후속 기술을 위하여 = Pandas

# Pandas
#   - Python(Pan) Data AnalysiS library 
#   - 실제 사용 : pd.DataFrame
#   - 코딩으로 하는 엑셀 느낌, R
#   - 엑셀/SQL 두고 왜..
#   - 설치
#       pip install pandas
#   - import
#       import pandas as pd
#   - Pd가 지향하는거 : 원본 데이터에 영향 안가게
#   - 비정형 데이터의 느낌은 아님

# list스러운거
a = pd.Series([12,454,32,123])
print(a)    # dtype도 같이 출력
print(a[0])
print('-----------------------------')

# 엑셀스러운거
b = pd.DataFrame()
b["이름"] = ["새우깡", '감자깡', '양파깡']
b['가격'] = [4000, 2000, 3000]
print(b)

# 특정 필드만 가져오기 가능
print(b["이름"])

# Pd가 지향하는거 : 원본 데이터에 영향 안가게
# index : 데이터 찾는 기준
# 변수에 다시 담아주기
c = b.set_index(b['이름']) # 앞으로 데이터 찾을때 이름으로 찾겠다
print(c)

print(c.loc['새우깡']) # 세팅한 index로 찾기 
print(c.iloc[1])       # index 번호로 찾기 


