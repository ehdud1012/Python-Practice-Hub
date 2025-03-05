# -*- coding:utf-8 -*-

import tensorflow as tf

# DeepLearning
#   인공신경망 구성 -> 학습
#    -> 최적의 알고리즘을 스스로 찾음
#    -> 그 알고리즘으로 예측

# tensorflow : 실무 
# pytorch    : 연구
#   -> pytorch가 대세
# CUDA : 기본 cpu에서 작동하는데 nvidia그래픽 카드에서 돌도록 세팅

# tensorflow
#   설치 - pip install tensorflow
#   - 최신 버전 tensorflow 2.x
#       인공신경망이 만드는 과정을 전혀 볼수가 없어서 설명 불가
#       => 수업은 1.x로 돌아가는 구조 확인 후 -> 2.x로

# tf 2.x기능 off
tf.compat.v1.disable_v2_behavior()
# ------------------------------------------------------------------------
# 1) 인공신경망 구성 (변수 만들고, 식 쓰고, ...) : 실제론 안됨
a = tf.constant(10)     # 변수(상수) 만들기 : 실제 값이 들어가지 않음
b = tf.constant(20)
c = tf.add(a, b)        # a + b : 실제 계산 안됨
print(c)
d = tf.constant("ㅎ") 
# ------------------------------------------------------------------------
# 2) 학습데이터 넣어서 최적의 알고리즘 찾기
s = tf.compat.v1.Session()  # 실행 세션 만들기
# aResult = s.run(a)        # 세션에서 실행 (이때 실제 값 들어감)
# print(aResult)
cResult = s.run(c)          # 연관된거 다 실행 (a, b)  : 식 쓰고 이것만
print(cResult)
dResult = s.run(d)
print(dResult.decode())     # 한글은 디코딩해야댐
# ------------------------------------------------------------------------

# 3) 찾아낸 알고리즘 예측 - 이번 예제는 아님