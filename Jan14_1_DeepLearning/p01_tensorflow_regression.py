# -*- coding:utf-8 -*-
import tensorflow as tf

#  [1, 10], [2, 20], [3, 30]   : y = 10x     -> [5, ?]
#  [1, 12], [2, 22], [3, 32]   : y = 10x + 2 -> [5, ?]
#  [1, 13], [2, 19], [3, 31.5] : y = ax + b  -> [5, ?]
#       -> 딱 떨어지는 a/b가 있을까?

# 회귀 - regression
#   - 주어진 값들 최대한 만족시킬 a/b
#       -> 회귀 방정식(y = ax + b)을 찾아서
#       -> 그걸로 예측하자
#   - 인공신경망 기본

tf.compat.v1.disable_v2_behavior()

# 0) 학습데이터 확보
xData = [1, 2, 3]
yData = [13, 19, 31.5]
# ---------------------------------------------------------
# 1) 인공신경망 구성
# 변수
#   y = ax+b 에서
#   - Variable    : a/b  -> AI가 찾아내야 할 값
#   - placeholder : x/y  -> 학습데이터 들어갈 자리

# 첫 값 지정 - 0 : 1차원, 자료형
a = tf.Variable(tf.zeros([1], dtype=tf.float64))  
# 첫 값 지정 - -1 ~ 1 사이 랜덤(정규분포를 따르는) : 1차원, 자료형
b = tf.Variable(tf.compat.v1.random_uniform([1], -1, 1, dtype=tf.float64)) 

x = tf.compat.v1.placeholder(tf.float64) # 자료형만
y = tf.compat.v1.placeholder(tf.float64)

sik = a*x + b                       # x, sik      x, y
# 처음 시작(ex) : sik = 0x + 0.43 -> [1, 0.43] : [1, 10]
#                                 -> 0.43과 10의 차이가 큼 -> a=0, b=0.43은 별로
# 바꿔서 다시 : ...
#   sik이랑 y가 차이가 별로 없을 때까지(그래프 상에서 거리 짧아질 때까지) 반복 ... 
#   -> 최적의 a/b를 찾아냄

# 차원수 줄이고, 평균 구하고, 거리 구하기
distance = tf.reduce_mean(tf.square(y - sik))

# HyperParameter : 사람이 지정해주는 값 
#   learning_rate가 클수록 값을 크게 바꿈
#     - 값이 크면 정답을 못찾을 수도 있음
#     - 값이 작으면 정답을 찾는데 시간이 오래 걸림

# a/b 바꿔가면서 반복 (최적의 a/b를 찾아줄 객체)
o = tf.compat.v1.train.AdamOptimizer(learning_rate=0.1)  
goal = o.minimize(distance) # distance 값 줄이는게 목표
# ---------------------------------------------------------
# 2) 학습데이터 넣어서 최적의 값 찾기
s = tf.compat.v1.Session()

# Variable 값 초기값 뽑기
s.run(tf.compat.v1.global_variables_initializer()) 

for i in range(10000):
    s.run(goal, feed_dict={x:xData, y:yData})
    # 값 확인용
    print("y= %fx + %f" % (s.run(a), s.run(b)))
    print(s.run(distance, feed_dict={x:xData, y:yData}))
    print("-----")
# ---------------------------------------------------------
# 3) 예측
xx = float(input("x : "))
result = s.run(sik, feed_dict={x:xx})
print(result)