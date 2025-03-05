# -*- coding:utf-8 -*-

# 단어 다시 뜯기

# NLTK (Natural Language Tookie) : 한글쪽은 약함
#   설치 - pip install nltk

# DLC : 기능은 추가로 다운 받아서 사용
#       처음 한번만 다운 받으면 됨
# import nltk
# nltk.download("punkt_tab") # 특수문자 관련 

from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "27일은 임시공휴일!! 하지만 못쉬어.."
# 특수 문자 / 단어 나누기
wt = word_tokenize(sentence)
print(wt)

# 문장 나누기
st = sent_tokenize(sentence)
print(st)