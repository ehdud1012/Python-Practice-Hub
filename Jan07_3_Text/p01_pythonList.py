# -*- coding:utf-8 -*-
# 텍스트 데이터 분석 : 자연어 처리

a = ["ㄱ", "ㄴ", "ㄷ"]
b = ["ㄹ", "ㄱ", "ㅁ", "ㄴ"]
for bb in b:    # in의 정체 - for문 문법
    if bb in a: #  in의 정체 - a list속에 데이터 있나 체크
        print(bb)

print("--------------------------------------")
c = []

# b에 있는거 c에도 추가
# for bb in b:
#     c.append(bb)
# 파이썬에서 줄여서 사용 가능
c = [bb for bb in b]
print(c)

# d = []
# for bb in b:
#     if bb in a:
#         d.append(bb)

d = [bb for bb in b in bb in a]
print(d)
