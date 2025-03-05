# -*- coding:utf-8 -*-

from sys import maxunicode
from unicodedata import category


f = open("C:/KDY/sam01.txt", "r", encoding="utf-8")

wordCount = {}
for line in f.readlines():
    line = line.replace("\n", "").split(" ")
    for word in line:
        if (word in wordCount):
            wordCount[word] += 1
        else:
            wordCount[word] = 1

f.close()
for w, c in wordCount.items():
    print(w, c)

# 이렇게 하면 특수 문자까지 포함해서 다 다른 단어로 도출