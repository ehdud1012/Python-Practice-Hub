# -*- coding:utf-8 -*-

import numpy as np 

# subway -> NumPy
# 역 별로 탄 사람 수, 내린 사람 수 다 더해서
# 내린 사람이 더 많은 역

# 직접 파싱한 subway 파일
file = open("C:/KDY/example/subway/getSubway.csv", "r", encoding="utf-8")
onPassanger = {}    
offPassanger = {}    
for line in file.readlines():
    line = line.replace("\n", "").split(",") 
    if (line[4] in onPassanger):
        onPassanger[line[4]] += int(line[5])
        offPassanger[line[4]] += int(line[6])
    else :
        onPassanger[line[4]] = int(line[5])
        offPassanger[line[4]] = int(line[6])

name, on, off = [], [], []
for k, v in onPassanger.items():
    name.append(k)
    on.append(v)
    off.append(offPassanger[k])

name = np.array(name)
on = np.array(on)
off = np.array(off)

print(name[on < off])
file.close()