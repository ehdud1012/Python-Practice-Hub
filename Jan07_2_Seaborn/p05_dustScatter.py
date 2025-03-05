# -*- coding:utf-8 -*-
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from oracledb import connect, init_oracle_client

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 


init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"
df = pd.read_sql(sql, con)
con.close()
print(df)
# PM10, PM25 관계
# PM10이 높으면 ㅖㅡ25도 높나
# 상태별로 색깔 다르게
sns.scatterplot(x="SDD_PM10", y="SDD_PM25", data=df, hue="SDD_FIGURE", palette="coolwarm")
plt.show()