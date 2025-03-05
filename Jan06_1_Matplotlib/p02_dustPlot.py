# -*- coding:utf-8 -*-

from oracledb import connect, init_oracle_client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
sql = "SELECT * FROM seoul_dust_data"

df = pd.read_sql(sql, con)
df = df[df["SDD_LOC"] == "종로구"]
df = df.sort_values(by="SDD_DATE")
df["SDD_DATE"] = df["SDD_DATE"] .apply(lambda d:"%d/%d %d시" % (d.month, d.day, d.hour))

xData = np.array(df["SDD_DATE"])
yData = df["SDD_PM10"].to_numpy()
yData2 = df["SDD_PM25"].to_numpy()

_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(xData, yData, "C9--*")
sub1Conf.set_xlabel("날씨")
sub1Conf.set_ylabel("농도")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(xData, yData2, "C6--*")
sub2Conf.set_ylabel("농도")
sub1Conf.legend(p1+p2, ["미세먼지", "초미세먼지"])
d = {"fontsize":20, "fontweight" : "bold", "color" : "#FF0000"}
plt.title("종로구 미세먼지", fontdict=d)
plt.show()

con.close()