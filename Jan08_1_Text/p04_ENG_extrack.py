# -*- coding:utf-8 -*-

# 추출하기

from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

# 어간추출 - 영어 단어에서 어간 추출 (어형변화, 접사 다 제거한 어간)
ps = PorterStemmer()
data = "variable variation variety"   # 예시 X (어간이 안맞음)
wt = word_tokenize(data)
for w in wt:
    print(w, ps.stem(w))  # 추출

data = "play playing played plays"
wt = word_tokenize(data)
for w in wt:
    print(w, ps.stem(w)) 

print("-------------------------------")
# 표제어 추출 (동사원형)

# import nltk               # 추가설치
# nltk.download("omw-1.4")
# nltk.download("wordnet")
wnl = WordNetLemmatizer()

data = "am are is"
wt = word_tokenize(data)
for w in wt:
    print(w, wnl.lemmatize(w, wordnet.VERB)) # 동사원형 

data = "say said"
wt = word_tokenize(data)
for w in wt:
    print(w, wnl.lemmatize(w, wordnet.VERB))
print("-------------------------------")