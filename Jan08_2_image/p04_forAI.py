# -*- coding:utf-8 -*-
import cv2

# grayscale : x, y => 2차원
# color     : x, y, bgr => 3차원

# 인공신경망에 넣을려면 데이터 하나가 1차원이어야
a = cv2.imread("C:/KDY/source/greenBall.png", cv2.IMREAD_COLOR)
a = a.flatten()  # ?차원 -> 1차원으로 피기
print(a)

# tensorflow 2.x 에는 flatten기능이 자체적으로 있음
