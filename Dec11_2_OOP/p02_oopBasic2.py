# -*- coding:utf-8 -*-

# OOP 할래 -> class 만들어
# 패키지 안할거임
 # Python는 대문자 안해도 되지만 자바했다 온거 티내기 가능
from turtle import back


class Dog:   
    # 접근제어자 X -> 캡슐화 X
    # static? -> 효율성 신경 안씀 => 없음
    name = None     # 외부에서 멤버 정의 되면
    age = None      # 이게 무슨 의미냐 (class 정의) -> 나중에는 멤버변수 잘 안씀

    def bark(self):         # 메소드는 첫번째 파라메터로 self 필수
        print("멍")

     # 메소드는 첫번째 파라메터로 self 안쓰면 : static 메소드
    def test():
        print("a")

    def barkRepeat(self, a):
        print("ㅁ멍" * a)

    # 파이썬은 자바의 thiis처럼 생략 불가능 무조건 self 붙여야함
    def printInfo(self): 
        print(self.name, self.age)

#----------------------------------
d = Dog()
print(d, type(d), id(d))

d.name = "딸기"
d.age = 3
d.weight = 3    # class외부에서 멤버 정의 가능
print(d.name, d.age, d.weight)

d.bark()        # 호출 때는 self는 없는셈 치고 / Java 스타일 호출
# 원래 메소드 호출
# Dog.bark(d)
Dog.test()  # 원래의 자바 문법
d.barkRepeat(3)
d.printInfo()