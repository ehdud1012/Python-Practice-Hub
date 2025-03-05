# -*- coding:utf-8 -*-

from http.client import HTTPConnection
from json import loads
from oracledb import connect, init_oracle_client

# 미세먼지
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/

# DB
init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

# http 통신
hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse() .read()
dustData = loads(resBody)["RealtimeCityAir"]["row"]

for d in dustData:
    figure = d["IDEX_NM"]
    if d["IDEX_NM"] == "":
        figure = "없음"

    sql = ("INSERT INTO seoul_dust_data values(sysdate, '%s', '%s', %.0f, %.0f, '%s')" 
           % (d["MSRSTE_NM"], d["MSRRGN_NM"], d["PM10"], d["PM25"], figure))
    cur = con.cursor()
    cur.execute(sql)

if cur.rowcount == 1:
    print("등록 성공")
    con.commit()

cur.close()
hc.close()
con.close()
