# -*- coding:utf-8 -*-

# Garbage Collection : 메모리 자동 관리

class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __del__(self):
        print("소멸자")

    def show(self):
        print(self.name)
        print(self.price)


m1 = Menu("야채김밥", 4000)
m1.show()
m2 = Menu("참치김밥", 4500)
m2.show()
m3 = m1
m3.show()

m1 = None
print("zzzz")
