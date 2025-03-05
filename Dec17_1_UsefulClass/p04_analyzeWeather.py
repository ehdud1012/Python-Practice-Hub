# -*- coding:utf-8 -*-

class Weather:
    def __init__(self,line):
        line = line.replace("\n", "")
        line = line.split(",")         # 내가 \t으로 구분해놨으니까
        self.hour = int(line[0])
        self.temp = float(line[1])
        
file = open("C:/KDY/example/kmaWeather.csv", "r", encoding="utf-8") 
resultFile = open("C:/KDY/example/kmaWeatherResult.txt", "w", encoding="utf-8") 

# 배운거 다 써먹은 버전 (내가 쓴 버전)
# weathers = {}
# for line in file.readlines():
#     hour = Weather(line).hour
#     temp = Weather(line).temp
#     if (hour in weathers):
#         weathers[hour].append(temp)
#     else:
#         weathers[hour] = [temp]

# averageResult = {}
# for k, v in weathers.items():
#     temp = 0
#     for t in range(0, len(v)-1):
#         temp += v[t]
#     average = temp / len(v)
#     averageResult[k] = average

# for k,v in averageResult.items():
#     resultFile.write("%s\t%.1f\n" % (k, v))

# 강사님 버전
weatherSum = {}
weatherCount = {}

for line in file.readlines():
    hour = Weather(line).hour
    temp = Weather(line).temp
    if (hour in weatherCount):
        weatherSum[hour] += temp
        weatherCount[hour] += 1
    else:
        weatherSum[hour] = temp
        weatherCount[hour] = 1

for k, v in weatherSum.items():
    resultFile.write("%s\t%.1f\n" % (k, v / weatherCount[k]))
    
resultFile.close()
file.close()