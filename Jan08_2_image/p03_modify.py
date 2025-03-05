# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt

# 편집
a = cv2.imread("C:/KDY/source/greenBall.png", cv2.IMREAD_GRAYSCALE)

# 인공신경망에 뭐든 학습 시킬려면 : 차원수가 다 같아야됨
# a = cv2.resize(a, dsize=(50,50))   # 50x50

# 원본 비율 따질려면
# a = cv2.resize(a, dsize=(0,0), fx=0.5, fy=0.5)   # x,y의 0.5배

# 자르기
a = a[0:15, 0:10]

plt.imshow(a, cmap="Greens")
plt.show()