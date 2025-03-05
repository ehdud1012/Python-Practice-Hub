# -*- coding:utf-8 -*-

# 소설 파일 읽어서, 불용어 빼고, 특수문자 빼고, 동사만(원형) 횟수
# 막대그래프

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tag import pos_tag


fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

f = open("C:/KDY/Sherlock_Book.txt", "r", encoding="utf-8")
sw = stopwords.words("english")
wnl = WordNetLemmatizer()

words = []
for line in f.readlines():
    line = line.replace("\n", "")
    wt = word_tokenize(line)
    for w in wt:
        w =  w.lower()
        if w not in sw:
            w, p = pos_tag([w])[0]
            if p.startswith("V"):
                w = wnl.lemmatize(w, wordnet.VERB)
                words.append(w)

bi = {}
for w in words:
    if w in bi:
        bi[w] += 1
    else:
        bi[w] = 1

df = []
for w, c in bi.items():
    df.append({"단어" : w, "횟수": c})

df = pd.DataFrame(df)
df = df.sort_values(by="횟수", ascending=False)

word = df["단어"].to_numpy()
c = df["횟수"].to_numpy()

sns.barplot(x="단어", y="횟수", data=df.head(20), palette="Pastel1")
plt.show()

f.close()