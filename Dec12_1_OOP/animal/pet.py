# -*- coding:utf-8 -*-

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showInfo(self):
        print(self.name)
        print(self.age)

# 클래스 여러개 가능
class Cat:
    def __init__(self, name):
        self.name = name
    def showInfo(self):
        print(self.name)


# import 했을 떄는 실행 X , 여기서 실행했을 때만 뜨게
if __name__ == "__main__":   # 잘 안써서 그렇제 파이썬도 메인 있음
    print("zzz")
    
