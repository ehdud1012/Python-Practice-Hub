# -*- coding:utf-8 -*-
# 영어 소설책 사이트
# https://gutenberg.org/

# stopword (불용어) 거르기
# 별 의미 없는 단어 - a, the, ... 

# import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

sentence = "Here is Edward Bear, coming downstairs now, bump, bump, bump, on the back of his head, behind Christopher Robin. It is, as far as he knows, the only way of coming downstairs, but sometimes he feels that there really is another way, if only he could stop bumping for a moment and think of it. And then he feels that perhaps there isn't. Anyhow, here he is at the bottom, and ready to be introduced to you. Winnie-the-Pooh."
sw = stopwords.words("english") # 불용어들 list로
wt = word_tokenize(sentence)

for w in wt:
    w =  w.lower()
    if w not in sw:
        print(w)