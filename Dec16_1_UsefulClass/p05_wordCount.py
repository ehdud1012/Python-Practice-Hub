# -*- coding:utf-8 -*-
# kakaoTalkExample
file = open("C:/KDY/Kakaotalk_Chat/Talk_2024.12.16_20_03-1.txt", "r", encoding="utf-8") 
resultFile = open("C:/KDY/Kakaotalk_Chat/Kakaotalk_Chat_Result.txt", "a", encoding="utf-8") 

wc = {} 
for i, line in enumerate(file.readlines()):
    if (i > 4):
        line = line.replace("\n", "")
        # 대화에 enter가 있을 경우
        msg = None
        if ((not line.startswith("20")) and (line != "")):
            msg = line
        else:
            try:
                line = line.split(" : ")
                if len(line) > 1:
                    msg = ""
                    for ii, ll in enumerate(line):
                        if ii > 0:
                            msg += ll + " "
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            for word in msg:
                if (word in wc):
                    wc[word] += 1
                else:
                    wc[word] = 1

for k, v in wc.items():
    resultFile.write("%s\t%d\n" % (k, v))

resultFile.close()
file.close()

# 시각화
#   일단 엑셀로 
#   엑셀은 utf-8에 쥐약
#   파일 열지 말고 그냥 복붙