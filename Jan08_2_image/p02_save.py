# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt

a = cv2.imread("C:/KDY/source/greenBall.png", cv2.IMREAD_GRAYSCALE)
# print(a)

# plt.imshow(a)
# plt.show()

# 그림을 편집 한 다음에 저장
cv2.imwrite("C:/KDY/source/greenBall2.png", a)  # 색은 다 날라감