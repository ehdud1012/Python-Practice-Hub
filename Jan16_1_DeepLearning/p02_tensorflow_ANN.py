# -*- coding:utf-8 -*-
import tensorflow as tf
tf.compat.v1.disable_v2_behavior()

# 영화 정보 활용
# [[80, 20], 액션], [[95, 5], 액션], [[10, 90], 조폭], ...

# one-hot encoding : 목록 중에 하나만 1로
#                   => 전기 신호 흐름 묘사한 것
#   액션 = [1, 0]
#   조폭 = [0, 1]
#   => [[80, 20], [1, 0]], [[95, 5], [1, 0]], [[10, 90], [0, 1]], ...

# ANN (Artificial Neural Network)
#   yData를 one-hot encoding으로 표현한 다차원 회귀분석

xData = [[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]]
yData = [[1,0], [1,0], [0,1], [1,0], [0,1]]
label = ["액션", "조폭"] 


# y      = a*x             + b
# [1, 0] = [80, 20]*a      + b
# (1, 2) = (1, 2)  *a      + (1, 2)
# (1, 2) = (1, 2)  *(2, 2) + (1, 2)

# a/b의 모양 찾아야함 => 행렬을 이용하여
a = tf.Variable(tf.zeros([2, 2], dtype=tf.float64))  
b = tf.Variable(tf.zeros([2], dtype=tf.float64))  

x = tf.compat.v1.placeholder(tf.float64) 
y = tf.compat.v1.placeholder(tf.float64)

sik = tf.add(tf.matmul(x, a), b) 

# 다차원 계산할때 사용
distance = tf.reduce_mean(
    tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik)
)
o = tf.compat.v1.train.AdamOptimizer(learning_rate=0.1)  
goal = o.minimize(distance)

s = tf.compat.v1.Session()
s.run(tf.compat.v1.global_variables_initializer()) 

for i in range(8000):
    s.run(goal, feed_dict={x:xData, y:yData})
    # 값 확인용
    # print("y= x*", s.run(a), "+", s.run(b))
    print(s.run(distance, feed_dict={x:xData, y:yData}))
    print("-----")

q = float(input("싸움 : "))
w = float(input("욕 : "))
newMovie = [[q, w]]
# result = s.run(sik, {x:newMovie})
# tf.argmax() 
#   최댓값이 있는 index
#   axis=0 : 열방향
#   axis=1 : 행방향
result = s.run(tf.argmax(sik, 1), {x:newMovie})
print(result)
print(label[result[0]])