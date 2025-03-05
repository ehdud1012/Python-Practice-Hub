from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

# 막대그래프 - 항목 간 절대적인 크기 비교
#               -> x축이 숫자일 필요는 없음
#   제목, 눈금, 그리드 ,... 꺾은선이랑 똑같음

# yData = [12, 23, 34, 5, 11]
# xData = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"]
# plt.bar(xData, yData)
# plt.show()

# ---------------기본 이런식으로 사용-----------------
yData = [12, 23, 34, 5, 11]
yData2 = [4, 56, 12, 1, 23]
xLabel = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"]
xData = np.arange(len(xLabel))
# plt.bar(xData, yData)
# plt.xticks(xData, xLabel)
# plt.show()
#                                    ↓ 이래서 x값에 숫자가 있어야함
# 디자인                 막대기색    막대두깨(x값)  막대기테두리색   테두리 두께(px)
# plt.bar(xData, yData, color="yellow", width=0.3, edgecolor="blue", linewidth=3)
# 막대기 색 다 다르게 하기
# colors = ["#549954", "#FF3242", "#547786", "#FFFF43", "#098182"]
# plt.bar(xData, yData, color=colors, width=0.3, edgecolor="blue", linewidth=3)
# plt.xticks(xData, xLabel)
# plt.show()

# 값 여러 개 (x값 하나당 y값 두개)
# 기능은 따로 없고 막대기 두께만큼 x값에서 빼서 조절
# plt.bar(xData, yData, width=0.3, align="edge")
# plt.bar(xData-0.3, yData2, width=0.3, align="edge")
# plt.xticks(xData, xLabel)
# plt.show()

# 값 여러 개 (누적 막대기) - 기능O
plt.bar(xData, yData)
plt.bar(xData, yData2, bottom=yData)
plt.xticks(xData, xLabel)
plt.show()