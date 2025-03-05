# -*- coding:utf-8 -*-

from pymongo import MongoClient
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import seaborn as sns

# MongoDB에 있는 네이버 뉴스
# 정규화
# 
con = MongoClient("192.168.0.55")
db = con.xxe
o = Okt()
news = db.ai_naver_news.find()
word = {}
for n in news:
    line = n["n_title"] + " " + n["n_description"]
    line = o.normalize(line)
    for w, p in o.pos(line, stem=True):
        if p == "Verb":
            if w in word:
                word[w] += 1
            else:
                word[w] = 1
con.close()

df = []
for w, c in word.items():
    df.append({"단어" : w, "횟수": c})          

word = df["단어"].to_numpy()
c = df["횟수"].to_numpy()

sns.barplot(x="단어", y="횟수", data=df, palette="Pastel1")
plt.show()
