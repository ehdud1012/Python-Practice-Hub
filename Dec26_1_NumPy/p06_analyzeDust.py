# -*- coding:utf-8 -*-
import numpy as np 

# SQL로 하는게 맞지만

file = open("C:/KDY/example/dust/seoulDust.csv", "r", encoding="utf-8") 
dust = {}
locCount = {}
for line in file.readlines():
    line = line.replace("\n", "").split(",") 
    avg = int(line[6]) + int(line[7])
    if (line[5] in dust):
        dust[line[5]] += (avg / 2)
        locCount[line[5]] += 1
    else :
        dust[line[5]] = (avg / 2)
        locCount[line[5]] = 1
avgDust = []
locName = []
for k, v in dust.items():
    locName.append(k)
    avgDust.append(v / locCount[k])

avgDust = np.array(avgDust)
locName = np.array(locName)
totalAvg = np.mean(avgDust)
print("미세먼지가 가장 심한 구 : %s" % locName[np.argmax(avgDust)])
# print("미세먼지가 가장 덜한 구 : %s" % locName[np.argmin(avgDust)])
# 만약 같은 값이 있다면?
print("미세먼지가 가장 덜한 구 : %s" % locName[avgDust == np.min(avgDust)])

print("미세먼지가 가장 덜한 구 : %s" % locName[np.argmin(avgDust)])

print("서울 미세먼지 평균 : %.2f" % totalAvg)
print("미세먼지 평균보다 깨끗한 구 : %s" % locName[np.less_equal(avgDust, totalAvg)])

file.close()