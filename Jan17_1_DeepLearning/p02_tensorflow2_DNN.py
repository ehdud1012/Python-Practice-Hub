import tensorflow as tf
import numpy as np
import keras

# NN : 다차원, 다층 회귀분석
# tensorflow 1.x : 직접 다 구현 / 층도 다 만들고, 식도 다 썼음
# tensorflow 2.x : keras라는 라이브러리 흡수 -> 알아서 다 해줌
#   - np로
#   - 

xData = np.array([[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]])
yData = np.array([[1,0], [1,0], [0,1], [1,0], [0,1]])
label = ["액션", "조폭"] 

# 신경망 구성
model = tf.keras.models.Sequential(
    [   # 층
        tf.keras.layers.Flatten(input_shape=(2, 1)), # 입력 데이터를 1차원으로
        tf.keras.layers.Dense(100, activation="relu"), 
        tf.keras.layers.Dense(50, activation="relu"), 
        tf.keras.layers.Dense(30, activation="relu"), 
        tf.keras.layers.Dense(2, activation="softmax") 
    ]
)
o = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=o, loss="categorical_crossentropy")
# ----------------------------------------------------

# 학습 시작
model.fit(xData, yData, epochs=100)
# ----------------------------------------------------

# 예측
q = float(input("싸움 : "))
w = float(input("욕 : "))
newMovie = np.array([[q, w]])
result = model.predict(newMovie)
print(result)
print(label[result[0].argmax()])