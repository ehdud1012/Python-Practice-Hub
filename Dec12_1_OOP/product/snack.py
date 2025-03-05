# -*- coding:utf-8 -*-

class Snack:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def showSnackInfo(self):
        print(self.name)
        print(self.price)