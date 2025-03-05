# -*- coding:utf-8 -*-

# KoNLPy
#   Java를 쓰게 되어있음 -> 컴에 Java가 있어야함
#   Python에서 자바쓸 수 있도록 해주는 라이브러리 : jpype
#       설치 - pip install JPype1
#   설치 - pip install konlpy

from konlpy.tag import Okt

sentence = "27일은 임시공휴일!! 하지만 못쉬어.. "
sentence += "1월 12일은 도경수 생일~ 하지만 난 12일에 팝업을 가지 못해....ㅠ"

o = Okt()  # Open Korean Text분석기 (구 - 트위터 한글 형태소 분석기)

a = o.normalize(sentence)   # 정규화 (다듬기) 
print(a)

b = o.phrases(sentence)     # 어구 추출 (의미있는 단위로 나누기)
print(b)

c = o.morphs(sentence)      # 형태소 분석 (합성어 같은것도 나누기)
print(c)

d = o.morphs(sentence, stem=True)   # 형태소 분석 - 기본형
print(d)

e = o.pos(sentence)         # 형태소 분석 + 품사 -> (단어, 품사) tuple
for w, p in e:
    print(w, p)

f = o.pos(sentence, join=True)  # 형태소 분석 + 품사 -> 단어/품사 str
print(f)

g = o.pos(sentence, stem=True)  # 형태소 분석 + 품사 -> (단어, 품사) tuple - 기본형형태로
print(g)