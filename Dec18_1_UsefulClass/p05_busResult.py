# -*- coding:utf-8 -*-

class Bus:
    def __init__(self,line):
        line = line.replace("\n", "").split(" : ") 
        self.a = line[0]
        self.average = float(line[1])

    def printInfo(self):
        print(self.a, ":", self.average)

file = open("C:/KDY/example/bus/busAnalyzeResult.txt", "r", encoding="utf-8") 

bus = []      
for line in file.readlines():
    bus.append(Bus(line))

bus.sort(key=lambda bb : bb.average, reverse=True)

for i, b in enumerate(bus):
    b.printInfo()
    
file.close()