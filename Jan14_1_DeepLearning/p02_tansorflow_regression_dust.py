# -*- coding:utf-8 -*-
import tensorflow as tf
import pandas as pd
from oracledb import connect, init_oracle_client
tf.compat.v1.disable_v2_behavior()

init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 

sql = "SELECT * FROM seoul_dust_data"
df = pd.read_sql(sql, con)

pm10Data = df["SDD_PM10"]
pm25Data = df["SDD_PM25"]

a = tf.Variable(tf.zeros([1], dtype=tf.float64)) 
b = tf.Variable(tf.compat.v1.random_uniform([1], -1, 1, dtype=tf.float64)) 
x = tf.compat.v1.placeholder(tf.float64) 
y = tf.compat.v1.placeholder(tf.float64)
sik = a*x + b
distance = tf.reduce_mean(tf.square(y - sik))
o = tf.compat.v1.train.AdamOptimizer(learning_rate=0.1)  
goal = o.minimize(distance)

s = tf.compat.v1.Session()
s.run(tf.compat.v1.global_variables_initializer()) 

for i in range(10000):
    s.run(goal, feed_dict={x:pm10Data, y:pm25Data})
    # 값 확인용
    print("y= %fx + %f" % (s.run(a), s.run(b)))
    print(s.run(distance, feed_dict={x:pm10Data, y:pm25Data}))
    print("-----")

xx = float(input("x : "))
result = s.run(sik, feed_dict={x:xx})
print(result)