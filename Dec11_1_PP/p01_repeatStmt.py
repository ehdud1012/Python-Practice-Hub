# -*- coding:utf-8 -*-

# Python 
#    for-each / while 만 있음

# while

while True:
    x = int(input("x : "))
    if x % 2 ==0:
        break
    print(x)
    

# continue, break
for i in range(0, 3):
    for j in range(0,3):
        print(i, j)
        if(j == 1):
            break  # 누구의 브레이크인가 : j 
print("------------------------------")
# -> i를 깨려면
iEnd = False
for i in range(0, 3):
    for j in range(0,3):
        print(i, j)
        if(j == 1):
            iEnd = True 
            break
    if iEnd:
        break
print("------------------------------")