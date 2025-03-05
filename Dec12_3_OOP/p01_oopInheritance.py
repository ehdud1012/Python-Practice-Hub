# -*- coding:utf-8 -*-

# 상속
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def printInfo(self):
        print(self.name)
        print(self.price)

# Java 
#   생성자 상속 X (어차피 상속 시켜줘도 멤버 변수 추가 시켜서 안쓸거잖앙 ㅜ)
#   => 알아서 생성해서 써

# product로부터 상속받는 pen
#   멤버변수  상속??
#   메소드    상속 O
#   생성자    상속 O
#       1) 보통 생성자에서 멤버변수 결정
#       2) 오버로딩 X -> 생성자를 자유롭게 못만듬 
#       3) 자유의 언어 

# 물려 받은 메소드 기능에 추가 
# overriding :  물려 받은 메소드 기능 재정의
class Pen(Product):
    # 펜을 생성할때 색도 넣고 싶음
    # 오버라이딩..? 파라메터 값을 추가했는데..?
    #   => 오버로딩과 오버라이딩 그 어딘가...? 
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

    # 오버라이딩
    def printInfo(self):
        super().printInfo()
        print(self.color)

# p = Pen()  생성자가 상속되었으니 기본 생성자 사용 불가
# p.name = "볼펜"     # 과연 멤버변수를 상속받은걸까
# p.price = 500       # 원래 멤버변수 추가 가능한뎅..
# p.color = "black"

p = Pen("볼펜", 500, "yellow")

p.printInfo()       # 이건 확실히 상속받네