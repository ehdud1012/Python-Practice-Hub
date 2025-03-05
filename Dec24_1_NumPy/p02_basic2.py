# -*- coding:utf-8 -*-
import numpy as np 

# 기본 list
a = [10,20]
b = [1,2]
c = a + b   # [10, 20, 1, 2] => append 붙여줌
print(c)
d = a * 3
print(d)    # [10,20,10,20,10,20] => 3번 반복 append
print("--------------------------------------------")

# NumPy사용 list
aa = np.array([10,20])
bb = np.array([1,2])
cc = aa + bb    # 모양이 같으면 같은 자리에 있는 것 끼리 계산 - 인덱스끼리 더하기
print(cc)
dd = aa * 3     # broadcasting : 모양이 다르면 차원수 높은쪽에 낮은쪽이 계산
print(dd)

print("--------------------------------------------")
name = np.array(["김","도","영"])
kor = np.array([10,20,30])
eng = np.array([40,50,60])
mat = np.array([70,80,90])

# 각 학생별 평균점수 내기
sum = kor + eng + mat
print(sum)
average = sum / 3
over40 = average > 40 
print(over40)
print(name[over40])     # masking : 조건에 맞는 것만

# ▽ 국어 점수가 20점 이상인 학생 : true 인것만 출력
print(name[kor >= 20])  # 조건식 가능


# 영어 점수가 40~70 사이인 학생 이름
#  기본 파이썬은 40 < eng < 70이 가능하지만 이 상황은 안됨
#  masking할때는 중간에 끊기면 안되기 떄문에 -> & 사용
print(name[(eng > 40) & (eng < 70)])