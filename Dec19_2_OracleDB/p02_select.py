# -*- coding:utf-8 -*-
         
from oracledb import connect, init_oracle_client

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

# select
sql = "SELECT * FROM dec19_drink"
cur = con.cursor()

# 실행 (insert와 동일)
cur.execute(sql)

# cur 자체가 실행 결과
# for d in cur:
#     print(d[0], d[1])  # tuple

# tuple 특성 사용
for n, p in cur:
    print(n, p)
cur.close()
con.close()