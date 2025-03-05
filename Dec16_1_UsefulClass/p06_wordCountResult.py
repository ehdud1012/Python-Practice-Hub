# -*- coding:utf-8 -*-

# 분석 결과 파일 정리/시각화
#   엑셀
#   테블로/BImatrix/PowerBI
#   Python의 
#       정리   : NumPy/Pandas
#       시각화 : matplotlib/seaborn

# 일단 파이썬으로만 해보자 (객체지향 스타일로)
# 분석 결과 파일 열어서 출력

# ---------------------------------------------------------------------------
class Word:
    def __init__(self, line):
        line = line.replace("\n", "")
        line = line.split("\t")         # 내가 \t으로 구분해놨으니까
        self.word = line[0]
        self.count = int(line[1])

    def printInfo(self):
        print(self.word, ":", self.count)

# ---------------------------------------------------------------------------
resultFile = open("C:/KDY/Kakaotalk_Chat/Kakaotalk_Chat_Result.txt", "r", encoding="utf-8") 

# 빈 리스트 (Java의 ArrayList) - Word객체가 들어있는 list
words = []      
for line in resultFile.readlines():
    words.append(Word(line))

# 객체 list 정렬
#           정렬 기준 (여기다 람다함수 사용)
# ww에 뭐 넣으면 ww.word 리턴
# 넣지 않고 이대로 쓰면 ww자리에 list있는거 자동으로 넣어줌
# words.sort(key=lambda ww: ww.word) # 단어 가나다 순 정리
# words.sort(key=lambda ww: ww.count)  # 카운트 기준 오름차순 정렬 
words.sort(key=lambda ww: ww.count, reverse=True)  # 카운트 기준 내림차순 정렬 

for i, w in enumerate(words):
    w.printInfo()
    if i == 10:
      break  
resultFile.close()