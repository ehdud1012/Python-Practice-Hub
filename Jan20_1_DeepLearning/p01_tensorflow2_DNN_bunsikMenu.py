import tensorflow as tf
import numpy as np
import keras
import cv2
import os

# 손글씨 인식
def getImg(folder, w, h):
    datas = []
    for f in os.listdir(folder): # 경로속에 있는 파일 명들
        data = cv2.imread(folder + "/" + f, cv2.IMREAD_GRAYSCALE)
        data = cv2.resize(data, (w, h))
        datas.append(data)
    return np.array(datas)

# 학습데이터
xData = getImg("C:/KDY/book/bunsikMenu", 100, 50)
print(xData)
label = ["떡볶이", "오뎅", "김밥", "튀김", "순대"]
yData = [0,0,0,0,0, 1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4]
yData = tf.one_hot(yData, 5) # 알아서 np로 바꿔주는 

# 신경망 구성
model = tf.keras.models.Sequential(
    [   # 층
        tf.keras.layers.Flatten(input_shape=(50, 100)), 
        tf.keras.layers.Dense(100, activation="relu"), 
        tf.keras.layers.Dense(100, activation="relu"), 
        tf.keras.layers.Dense(100, activation="relu"), 
        tf.keras.layers.Dense(5, activation="softmax") 
    ]
)
o = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=o, loss="categorical_crossentropy")
# ----------------------------------------------------

# 학습 시작
model.fit(xData, yData, epochs=100)

f = cv2.imread("C:/KDY/source/rightClick.png", cv2.IMREAD_GRAYSCALE)
f = cv2.resize(f, (100, 50))
f = np.array([f])
result = model.predict(f)
print(result)
print(label[result[0].argmax()])