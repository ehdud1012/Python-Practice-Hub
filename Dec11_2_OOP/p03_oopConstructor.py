# -*- coding:utf-8 -*-

# 대문자로 시작하든 말든 파이썬에선 논할 거리가 아님

class Snack:
    name = None
    def __init__(self):
        # 생성자
        print("생성자")

    def showInfo(self):
        print(self.name, self.price)

s = Snack()
s.name = "빼빼로"
s.price = 1700

s.showInfo()
#------------------------------ class 생성 여러 개 가능
class Menu:
    name = None  # 어차피 외부에서 정의되는데 무슨 의미가
    price = None   # -> 여기서 안쓰고 , 생성자에서 결정
    # 함수 기본값, 파라메터 지정 가능 -> 오버로딩 불가
    # -> 생성자는 하나만
    # 기본 생성자 포기
    # def __init__(self):
    #     pass

    # 오버로딩된 생성자
    # 멤버변수를 생성자에서 결정
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name)
        print(self.price)

    def __del__(self):
        print("소멸자")


m = Menu("야채김밥", 3000)
m.show()