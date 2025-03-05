# -*- coding:utf-8 -*-

from random import randint

hand = [None, "가위", "바위", "보"]
userHand = None
def printRule():
    for i, h in enumerate(hand):
        if i > 0:
            print(i, ":", h)

def inputHand():
    global userHand             # 파이썬스럽게 근데 굳이?
    userHand = int(input("머 : "))
    if userHand > 3 or userHand < 1:
        inputHand()

def comHand():
    return randint(1 ,3)

def printHand(comHand):
    print("나 : ", hand[userHand])
    print("컴 : ", hand[comHand])

def judge(comHand):
    j = userHand - comHand
    if (j==0):
        print("무승부")
        return 0
    elif(j == -1 or j == 2):
        print("패")
        return 432342
    else:
        print("승")
        return 1
# --------------------------------------

printRule()
w = 0;
while True:
    inputHand()
    comHand = comHand()
    printHand(comHand)
    c = judge(comHand)
    if(c == 432342):
        break
    w += c
print(w, "연승")
