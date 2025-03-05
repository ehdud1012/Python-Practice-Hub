# -*- coding:utf-8 -*-
from oracledb import connect, init_oracle_client
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import seaborn as sns
from matplotlib import colormaps

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

# Matplotlib : Python 시각화 라이브러리
#   Excel보다 나은점 ? - X
#               - np.array 대상 (주력은 Pandas DataFrame)
#               - 하나하나 다 코딩 (색깔 다 다르게 넣으려먼..ㅎ)

# Seaborn : Matplotlib를 편하게 쓰게 해주는 라이브러리
#   설치 - pip install seaborn
#   pd.DataFrame대상도 가능
#   자동으로 작업 해줌 (테마 기능)
#   부족한 부분은 Matplotlib 작업 (ex - plt.title)
# 
#    

# DB에 있는 미세먼지

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"
df = pd.read_sql(sql, con)
con.close()

# sns.lineplot(data=df, palette="rainbow")
# 알아서 그리는데 지정하고 싶으면
sns.lineplot(x="SDD_DATE", y="SDD_PM10", data=df, palette="BuPu")
print(colormaps)
plt.title("미세먼지")
plt.show()