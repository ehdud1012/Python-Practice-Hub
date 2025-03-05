# -*- coding:utf-8 -*-

# 아무것도 없으면 기본적으로 class avengers(object):
class avengers():
    def __init__(self, name):
        self.name = name
    def attact(self):
        print("공격")
#----------------------------
class human:
    def __init__(self, addr):
        self.addr = addr
    def attact(self):
        print("밀치기")

    def eat(self):
        print("밥")
#----------------------------

# ironman is a human
# ironman is a avengers
# 다중 상속 : 부분의 OOL이 안됨
#           : 멤버 이름이 중복되면..? -> 그래서 안해주는 거임

#   Java    - 불가능 (interface로 대충 흉내)
#   Python  - 가능
#       1) 멤버이름 중복 문제
#               멤버 이름이 동일하면 먼저 쓴거(avengers)로 인식
#                   class ironman(avengers, human):
#                       pass
#                   i.attact()     # avengers의 attact
#       2) 생성자 상속 문제
#               생성자 상속 + 생성자에서 멤버변수 결정
#               => human에 있는 addr는 안받은거..? 
#                   i = ironman("ㅋㅋ")
#                   print(i.name)       # ㅋㅋ 출력
#                   print(i.addr)       # 없음
# 
#       => 혼돈 해결 : 의미가 있는가
class ironman(avengers, human):
    # 2) 오버로딩과 오버라이딩 그 어딘가
    def __init__(self, name, addr):
        super().__init__(name)
        human.__init__(self, addr)

    # 1) overriding => 의미 X
    def attact(self): 
        super().attact()  # avengers의 attact
        human(None).attact()  # human은 따로 설정 
        # => 이럴거면 상속 왜 하는가
#----------------------------
i = ironman("ㅋㅋ", "동탄")
print(i.name)
print(i.addr)
i.attact()
i.eat()
