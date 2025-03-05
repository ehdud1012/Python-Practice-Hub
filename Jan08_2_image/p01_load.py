# -*- coding:utf-8 -*-

# 이미지/음악/동영상 ... -> 뭐든지 컴에는 숫자로
# 인코딩/디코딩만 할 줄 알면

# pip install opencv-python
import cv2
# 픽셀 하나가 0 ~ 255
a = cv2.imread("C:/KDY/source/1010.png", cv2.IMREAD_GRAYSCALE)
print(a)

# 픽셀 하나가 [255, 255, 0]
b = cv2.imread("C:/KDY/source/1010.png", cv2.IMREAD_COLOR)  # BGR
b = cv2.cvtColor(b, cv2.COLOR_BGR2RGB)                 # RGB로 바꾸고 싶으면
print(b)