import tensorflow as tf
tf.compat.v1.disable_v2_behavior()

# input  layer (입력층) - 데이터 들어가는
# hidden layer (은닉층) - 중간 계산용
# output layer (출력층) - 결과 나오는

# ANN (Artificial Neural Network)
#   yData를 one-hot encoding으로 표현한 다차원 회귀분석
#   input  layer - 1개
#   output layer - 1개
#   => 식 하나
#   => 모든 문제가 식 하나로 해결이 되나..?
#   -> 정확도가 떨어짐
# ---------------------------------------------------------------
# 옛날에도  DNN이 하고 싶었는데, 컴 H/W가 부족해서 실현 불가능
#   => 지금은 컴이 좋아져서 실현가능하게 됨
# ---------------------------------------------------------------
# DNN (Deep Neural Network)
#   input  layer - 1개
#   hidden layer - n개 (n이 늘어날수록 컴이 고통 받음)
#   output layer - 1개
#   식 여러 개
#   -> 정확도 ↑

xData = [[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]]
yData = [[1,0], [1,0], [0,1], [1,0], [0,1]]
label = ["액션", "조폭"] 

x = tf.compat.v1.placeholder(tf.float64) 
y = tf.compat.v1.placeholder(tf.float64)

a1 = tf.Variable(tf.zeros([2, 100], dtype=tf.float64))
b1 = tf.Variable(tf.zeros([100], dtype=tf.float64))  
sik1 = tf.add(tf.matmul(x, a1), b1) 
sik1 = tf.nn.relu(sik1)

# 활성화 함수 - 특정 조건 맞는거는 안흐르는걸로 쳐서 다음 계산에서 빠지게
#   ex) 전기 흐름 묘사중
#       층, 차원수 ↑ -> 모든걸 다 계산하기에는 부담
#       => 특정 조건 맞는거는 안흐르는걸로 쳐서 다음 계산에서 빠지게
#   - relu    : 음수는 0으로
#   - softmax : 총 합을 1로  [1, 1, 3] -> [0.2, 0.2, 0.6]

a2 = tf.Variable(tf.zeros([100, 50], dtype=tf.float64))
b2 = tf.Variable(tf.zeros([50], dtype=tf.float64))  
sik2 = tf.add(tf.matmul(sik1, a2), b2) 
sik2 = tf.nn.relu(sik2)

a3 = tf.Variable(tf.zeros([50, 30], dtype=tf.float64))
b3 = tf.Variable(tf.zeros([30], dtype=tf.float64))  
sik3 = tf.add(tf.matmul(sik2, a3), b3) 
sik3 = tf.nn.relu(sik3)

a4 = tf.Variable(tf.zeros([30, 2], dtype=tf.float64))
b4 = tf.Variable(tf.zeros([2], dtype=tf.float64))  
sik4 = tf.add(tf.matmul(sik3, a4), b4) 

distance = tf.reduce_mean(tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik4))
o = tf.compat.v1.train.AdamOptimizer(learning_rate=0.1)  
goal = o.minimize(distance)

s = tf.compat.v1.Session()
s.run(tf.compat.v1.global_variables_initializer()) 

for i in range(8000):
    s.run(goal, feed_dict={x:xData, y:yData})
    print(s.run(distance, feed_dict={x:xData, y:yData}))
    print("-----")

q = float(input("싸움 : "))
w = float(input("욕 : "))
newMovie = [[q, w]]
result = s.run(tf.argmax(sik4, 1), {x:newMovie})
print(result)
print(label[result[0]])