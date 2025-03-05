# -*- coding:utf-8 -*-

# 특수문자 뭐 있는지 확인

# unicode : 컴퓨터에 글자 표현하는 방식 중 하나
#   Unicode Transf Format - 8bit : uft-8

from sys import maxunicode
from unicodedata import category

print(maxunicode)       # unicode 전체 갯수
print(chr(99))          # unicode에서 99번 글자
print(category('a'))    # a는 뭐냐 (unicode category)

print("-------------------------------")

specials = []
for i in range(maxunicode):
    # print(chr(i))           # 전체 글자 다 찍기
    # print(category(chr(i)))   # 글자 category 다 찍기

    # 카테고리가 P로 시작하는 특수문자들
    if category(chr(i)).startswith("P"):
        specials.append(chr(i))

# ------------------------------------------------------------------

# sam01 특수문자 없애고 단어수 세기
f = open("C:/KDY/sam01.txt", "r", encoding="utf-8")
wordCount = {}
for line in f.readlines():
    for s in specials:
        line = line.replace(s, "")
    line = line.replace("\n", "").split(" ")
    for word in line:
        if (word in wordCount):
            wordCount[word] += 1
        else:
            wordCount[word] = 1
f.close()
for w, c in wordCount.items():
    print(w, c)