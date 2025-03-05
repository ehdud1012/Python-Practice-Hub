# -*- coding:utf-8 -*-
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
# 분류 : kNN
#   80, 20 -> 액션
#   10, 20, 맑음 -> 빨강 
# 만약 비정형 데이터(문장, 글) 이라면?

# navie bayes - 분류
#   자연어 처리쪽에 특화
#   전문적이지 않은 베이지안 정리
#   확률을 따져서 가장 높은 부분으로 판정

feature = ["너는 멍청해", "Java는 프로그래밍 언어다", "너는 착해", "Java는 어렵다", "오늘 날씨는 영하 10도야", "배고프다"]
label = ["욕", "강의", "칭찬", "개인의견", "정보", "개인감정"]

# 전처리
# BoW(Bag of Words) : 단어 수 세기
cv = CountVectorizer()
cvResult = cv.fit_transform(feature)
# print(cvResult)
print(cv.get_feature_names_out()) # 전체 단어들 확인
print(cv.vocabulary_)             # 단어 인덱스 번호 확인
cvResult = cvResult.toarray()     # 각 문장에서 단어가 있으면 1, 없으면 0
print(cvResult)                   

sentence = input("문장 : ")
sentenceCvResult = cv.transform([sentence]) # 모양 맞추기 list
sentenceCvResult = sentenceCvResult.toarray()
print(sentenceCvResult)

mnb = MultinomialNB()
mnb.fit(cvResult, label)
result = mnb.predict(sentenceCvResult)[0]
print(result)
