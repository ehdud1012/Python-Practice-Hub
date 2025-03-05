# -*- coding:utf-8 -*-
import pandas as pd
#1.x : append써서 Series도 추가, dict도 추가..
#2.x : 혼란스럽다고 append삭제, DF끼리 붙이기만 남겨둠
a = pd.DataFrame()
a["이름"] = ["새우깡", "양파링"]
a["가격"] = [1500, 4000]
print(a)
print('-----------------------------')
# pd.Series(list 같은) 추가
# append가 삭제 -> pd.concat
b = pd.Series(["빼빼로", 1000], index=["이름", "가격"])
b = pd.DataFrame([b])
a = pd.concat([a, b]) 
print(a)

print('-----------------------------')
# dict 추가

c = [{"이름" : "포카칩", "가격" : 5000}]
c = pd.DataFrame(c)
a = pd.concat([a, c], ignore_index=True)
print(a)

