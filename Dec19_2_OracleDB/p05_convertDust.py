# -*- coding:utf-8 -*-

from datetime import datetime
from time import strftime
from oracledb import connect, init_oracle_client

# 웹 실시간 데이터 -> DB (p03_getDust.py)
# DB -> csv (p05_convertDust.py)

# 굳이 DB로 되는데 왜 csv? -> 하둡이 DB 연동이 안됨(파일에 있는거만 할 줄 알아서)

file = open("C:/KDY/example/dust/seoulDust.csv", "w", encoding="utf-8") 
# 2024,12,19,10(시), 도심권, 중구, 10,20,보통

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

sql = "SELECT * FROM seoul_dust_data"
cur = con.cursor()
cur.execute(sql)
datas = ""
for date, loc, ran, pm10, pm25, figure in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H")
    data = "%s,%s,%s,%.0f,%.0f,%s\n" % (date, ran, loc, pm10, pm25, figure)
    datas = "%s%s" % (datas, data)

file.write(datas)

file.close()
cur.close()
con.close()