# -*- coding:utf-8 -*-
import numpy as np 

# 분석

# anaconda
#   Python + 분석/AI 라이브러리 다 설치된 가상환경
#   Jupyter Notebook이라는 툴
#       한줄 써서 결과보고 다음 줄 쓰고 ( = 대화형 처리, cmd인데 보기 편한 )
#       -> 분석툴처럼 쓰기에 편함
#   => 설치는 언제 경험하나 / 가상환경 ? / 우리는 AI-프로그램 개발이지 분석해서 보고서 쓰는게 아님 
# 
#  NumPy - 빅데이터 분석 라이브러리
#   설치 - cmd -> pip install numpy
#   import - 자동완성이면 너무 길어서 수동으로
#       import numpy as np 
#   - scikit-learn, tensorflow 등 후속기술들이 사용
#   - 기능 추가된 list
#   - slicing / broadcasting / masking

# 기본 list
#  OOL에서 2차원 list? => 그냥 객체 list 쓰지 (그냥 넘어가)
score = [[100,90,80], [70,60,50]]
print(score, type(score))
print(score[0])
print(score[0][1])
score[1][1] = 0
# score[1][0:3] = 0 는 안됨 한번에 하나만
print(score)

print("--------------------------------------------")

# NumPy사용 list
score2 = np.array(score) 
print(score2, type(score2)) # 가독성? 리스트마다 줄바꿈 / type - numpy.ndarray
print(score2[0])
print(score2[0][1]) # 기존 list스타일도 가능
print(score2[0, 1]) # NumPy 스타일 
score2[1, 1] = 99
score2[1, 0:3] = 0 # slicing - 한꺼번에 여러 개 처리
print(score2)
print(score2.shape) # 모양 - (몇행, 몇열)
print(score2.dtype) # 자료형
print(len(score2))  # 2차원이라 2개
print(score2.size)  # 총 갯수