# -*- coding:utf-8 -*-

# 추웠던 순으로 정렬
class Weather:
    def __init__(self,line):
        line = line.replace("\n", "")
        line = line.split(",") 
        self.hour = int(line[0])
        self.temp = float(line[1])

    def printInfo(self):
        print(self.hour, ":", self.temp)

file = open("C:/KDY/example/kmaWeather.csv", "r", encoding="utf-8") 

weathers = []      
for line in file.readlines():
    weathers.append(Weather(line))

weathers.sort(key=lambda ww: ww.temp)

for i, w in enumerate(weathers):
    w.printInfo()
    
file.close()
