# -*- coding:utf-8 -*-

# wordcloud
#   matplotlib 라이브러리
#   설치 - pip install wordcloud

from pymongo import MongoClient
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud

con = MongoClient("192.168.0.55")
db = con.xxe
o = Okt()
news = db.ai_naver_news.find()
words = ""
for n in news:
    line = n["n_title"] + " " + n["n_description"]
    line = o.normalize(line)
    for w, p in o.pos(line, stem=True):
        if p == "Verb":
            words += w + " "  # 단어 다 붙이기
con.close()

wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf").generate(words) 
# 많이 나온 동사는 크게 / 이미지를 그려줌
plt.imshow(wc)
plt.show()