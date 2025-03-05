# -*- coding:utf-8 -*-

# NumPy - 선수과정 (뒷 과정을 위한 발판)
# Pandas - Hadoop에서 나름

# 시각화
#   - 굳이? : excel,canvasjs, tableau같은 노코딩 툴 있음
#   - 과정에 있어서..
  
# matplotlib - Python 시각화 라이브러리
#   https://matplotlib.org/cheatsheets/
#   numpy array를 대상으로 그래프 그려줌
#   설치 - pip install matplotlib
#   import - import matplotlib.pyplot as plt
#   한글 사용 X (기본 폰트에 한글 없음)
#       1. C:\Windows\Fonts 가서 cmd
#       2. dir -> 정식 폰트 파일 명 확인
#       3. import (import matplotlib.font_manager as fm)
#       3. 폰트 설정
#           fontFile = "C:/Windows/Fonts/malgun.ttf" 
#           fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
#           plt.rc("font", family=fontName) 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName) # 기본폰트 전환
plt.rcParams["axes.unicode_minus"] = False # minus(-) 안깨지게

# plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())

yData = np.array([12, 23, 34, 5, 11])
# 일반 list -> 알아서 np.arrat로 변환해서 그래프
xData = [10, 20, 30, 40, 50]

# 여러가지 세팅
# plt.plot(yData) 
# 그래프 보여주기
# plt.show()

# 기본 꺾은선 그래프
# x, y
# plt.plot(xData, yData)
# plt.show()

# 축
# plt.plot(xData, yData)
# 축 이름 설정
# plt.xlabel("x축")
# plt.ylabel("y축")
# 축 값 설정 ([x최소, x최대, y최소, y최대])
# plt.axis([0, 300, -50 , 200])
# plt.show()

# 제목 (위치 조절 가능(L,R,C), 여러개 가능)
# 제목 CSS 하고 싶으면 -> dict로 / fontdict에 넣어주기
# d = {"fontsize":20, "fontweight" : "bold", "color" : "#FF0000"}
# plt.plot(xData, yData)
# plt.title("제목인데용", loc="left")
# plt.title("두번째제목인데용", loc="right", fontdict=d)
# plt.show()

# 선 (간단하게)    사이트보고 여러 기능 추가 가능
# https://matplotlib.org/cheatsheets/     
# plt.plot(xData, yData, "C9--*")
# plt.show()

# 선
# plt.plot(xData, yData, color="#453422", linestyle=":", marker="^", linewidth=5)
# plt.show()

# 그리드
# plt.plot(xData, yData)
# plt.grid(axis="y", color="red", linestyle="--")
# plt.grid(axis="x", color="blue", linestyle="-.")
# plt.show()


# 꺾은선 그래프 : xData가 변화할때 yData의 변화
#   xData가 변화할 수 있어야됨 -> xData가 숫자여야

# 눈금
# plt.plot(xData, yData)
# 실제 값은 10, 20,.. 이지만 보이는건 ↓
# plt.xticks(xData, ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"])

# yData = np.array([12, 23, 34, 5, 11])
# plt.yticks(yData, ["안","녕","하","세","용"])
# 규칙적으로 하고 싶었으면
# plt.yticks(np.arange(0, 21, 5), ["안","녕","하","세","용"])
#                             in/out/inout  
# plt.tick_params("y", direction="inout", length=20, pad=30)
# plt.tick_params("x", labelsize=20, labelcolor="#435322")
# plt.show()

# 선 여러개
# yData2 = [10, 34, 40, 32, 2]
# plt.plot(xData, yData, "C9--")
# plt.plot(xData, yData2, "C6--")
# plt.legend(["1", "2"])  # 뭐가 어떤건지 표시
# plt.show()

# y축 나눠서 선 여러 개
yData2 = [1000, 340, 400, 320, 2000]
_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(xData, yData, "C9--")
sub1Conf.set_xlabel("엑스")
sub1Conf.set_ylabel("와이")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(xData, yData2, "C6--")
sub2Conf.set_ylabel("와이2")
sub1Conf.legend(p1+p2, ["1","2"])
plt.show()