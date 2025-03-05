# -*- coding:utf-8 -*-

from datetime import datetime
from fileinput import lineno

file = open("C:/KDY/example/bus/getBus.csv", "r", encoding="utf-8") 
resultFile = open("C:/KDY/example/bus/busAnalyzeResult.txt", "w", encoding="utf-8")
passangerSum = {}
passangerCount = {}

for i, line in enumerate(file.readlines()):
    line = line.replace("\n", "")
    line = line.split(",")  
    date = datetime(int(line[0]), int(line[1]),int(line[2]))
    a = datetime.strftime(date, "%A")
    
    inPassanger = int(line[len(line)-2])
    
    if a in passangerCount:
        passangerSum[a] += inPassanger
        passangerCount[a] += 1
    else:
        passangerSum[a] = inPassanger
        passangerCount[a] = 1

for k, v in passangerSum.items():
    resultFile.write("%s 평균 승객 수 : %.1f\n" % (k, v / passangerCount[k]))

    