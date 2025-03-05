# -*- coding:utf-8 -*-

from gamePlayer import Enemy, User
class Referee:
    def __init__(self):
       self.hand = [None, "가위", "바위", "보"]
    def start(self):
      user = self.callBlueCorner()
      enemy = self.callRedCorner()
      self.printRule()
      while True:
         bluePaper = self.getBluePaper(user)
         redPaper = self.getRedPaper(enemy)
         self.printPaper(bluePaper, redPaper)
         result = self.judge(bluePaper, redPaper)
         if (result == -1):
            break
         user.win += result
      print(user.win, "연승") 

    def callBlueCorner(self):
       return User()
    def callRedCorner(self):
       return Enemy()
    
    def printRule(self):
        for i, h in enumerate(self.hand):
            if i > 0:
             print(i, ":", h)
    
    def getBluePaper(self, user):
       bluePaper = int(user.commit("머 : "))
       if bluePaper > 3 or bluePaper < 1:
          return self.getBluePaper(user)
       return bluePaper
        
    def getRedPaper(self, enemy):
       return enemy.submit()
    
    def printPaper(self, bluePaper, redPaper):
        print("나 : ", self.hand[bluePaper])
        print("컴 : ", self.hand[redPaper])

    def judge(self, bluePaper, redPaper):
        j = bluePaper - redPaper
        if (j==0):
            print("무승부")
            return 0
        elif(j == -1 or j == 2):
            print("패")
            return -1
        else:
            print("승")
            return 1

# --------------------------------------
if __name__ == "__main__":
   r = Referee()
   r.start()

