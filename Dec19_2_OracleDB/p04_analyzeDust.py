# -*- coding:utf-8 -*-

# NumPy/Pandas로 분석
# 1) DB에 10테라 있는데 가져와?
# 2) PC에서? 사양이..
# 3) Python으로?

# SQL로 분석            <- 이게 기술적으론 ↑ 
# 1) 10테라 안가져옴
# 2) DB서버에서 

# 일단 파이썬으로 봐
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

sql = "SELECT sdd_range, avg(sdd_pm10 + sdd_pm25) FROM seoul_dust_data GROUP BY sdd_range ORDER BY avg(sdd_pm10 + sdd_pm25) desc"
cur = con.cursor()
cur.execute(sql)

for sdd_range, avg in cur:
    print(sdd_range, avg)

cur.close()
con.close()