# -*- coding:utf-8 -*-
import numpy as np 
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

sql = "SELECT sdd_loc, avg(sdd_pm10 + sdd_pm25) FROM seoul_dust_data GROUP BY sdd_loc ORDER BY avg(sdd_pm10 + sdd_pm25) desc"
cur = con.cursor()
cur.execute(sql)

for sdd_loc, avg in cur:
    print(sdd_loc, avg)

cur.close()
con.close()