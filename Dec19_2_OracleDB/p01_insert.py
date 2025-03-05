# -*- coding:utf-8 -*-

# DB 사용 흐름
# SQLPlus -> EclipseDTP (이클립스 내장 DB) spring까지 -> DBeaver

# JAVA + OracleDB : 내장x -> ojdbc8.jar 사용
# Python + OracleDB : 내장x 
#         -> cx_Oracle.py + instantclient 
#         -> oracledb.py (instantclient 내장 : 구버전 OracleDB지원 X)
#         => oracledb.py + instantclient 
#    설치 - cmd -> pip install oracledb


# instantclient 연결               
from oracledb import connect, init_oracle_client
# instantclient 폴더 경로
init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")

# oracledb 연결               
# SQLPlus로 접속할 때 주소 형태 ( sqlplus ehdud1012/1012@192.168.0.55:1521/xe )
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

# JDBC -> ConnectionPool -> MyBatis -> JPA
# JDBC 느낌으로 (sql 다 치기)

# insert
name = input("이름 : ")
price = int(input("가격 : "))

# 값 넣어서 완성된 버전으로  ( ;은 뺴고 )
sql = "INSERT INTO dec19_drink values('%s', %d)" % (name, price)

# 총괄매니저 객체 (java - PreparedStatement)
# 겸 DB 작업 결과
cur = con.cursor()

# 실행
cur.execute(sql)

if cur.rowcount == 1:
    print("등록 성공")
    # 서버에 반영 (MyBatis 느낌)
    con.commit()

cur.close()
con.close()